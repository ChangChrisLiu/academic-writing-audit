"""Behavioral checks for repository validation; fixtures never touch real evidence."""

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest import mock

import validate


class RepositoryValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("LICENSE", "Fixture license\n")
        self.skill = self.root / "skills/example"
        self.write("skills/example/SKILL.md", "---\nname: example\ndescription: Check a fictional example.\nlicense: MIT\n---\n# Example\n\n[Details](references/details.md#details)\n")
        self.write("skills/example/LICENSE", "Fixture license\n")
        self.write("skills/example/references/details.md", "# Details\n")
        self.write("skills/example/agents/openai.yaml", 'interface:\n  display_name: "Example"\n  short_description: "Check an example"\n  default_prompt: "Use $example on this passage."\n')
        self.git("init", "-q")
        self.git("config", "user.name", "Fixture")
        self.git("config", "user.email", "fixture@example.invalid")
        self.commit()

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def git(self, *args):
        return subprocess.check_output(["git", *args], cwd=self.root, text=True, stderr=subprocess.PIPE).strip()

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "Fixture")
        return self.git("rev-parse", "HEAD")

    def report(self, **kwargs):
        return validate.validate_repository(self.root, **kwargs)

    def assert_problem(self, fragment, **kwargs):
        self.assertTrue(any(fragment in error for error in self.report(**kwargs)["errors"]), self.report(**kwargs))

    def test_standalone_skill_and_heading_link_pass(self):
        self.assertEqual(self.report()["errors"], [])

    def test_missing_local_reference_fails(self):
        (self.skill / "references/details.md").unlink()
        self.assert_problem("Missing link")

    def test_missing_active_heading_fails(self):
        self.write("skills/example/references/details.md", "# Changed heading\n")
        self.assert_problem("Missing anchor")

    def test_links_in_code_fences_are_not_dependencies(self):
        self.write("README.md", "# Guide\n\n```md\n[Example](missing.md)\n```\n")
        self.assertEqual(self.report()["errors"], [])

    def test_reference_style_link_is_checked(self):
        self.write("README.md", "[Read][guide]\n\n[guide]: absent.md\n")
        self.assert_problem("Missing link")

    def test_cross_skill_dependency_fails_even_when_target_exists(self):
        self.write("skills/example/references/details.md", "# Details\n\n[Outside](../../../README.md)\n")
        self.write("README.md", "# Root\n")
        self.assert_problem("Standalone dependency")

    def test_missing_metadata_and_mismatched_license_fail(self):
        self.write("skills/example/agents/openai.yaml", 'interface:\n  display_name: "Example"\n')
        self.write("skills/example/LICENSE", "Different license\n")
        self.assert_problem("UI metadata")
        self.assert_problem("License mismatch")

    def test_unsupported_yaml_fails_explicitly(self):
        self.write("skills/example/SKILL.md", "---\nname: example\ndescription: >\n  A folded description.\nlicense: MIT\n---\n")
        self.assert_problem("simple scalar")

    def test_extra_discoverable_snapshot_fails(self):
        self.write("evals/archive/SKILL.md", "# Historical skill\n")
        self.assert_problem("Extra discoverable")

    def test_live_manifest_detects_corruption(self):
        self.write("evals/case/input.md", "before\n")
        self.write("evals/case/manifest.json", json.dumps({"files": {"evals/case/input.md": hashlib.sha256(b"before\n").hexdigest()}}))
        self.assertEqual(self.report()["errors"], [])
        self.write("evals/case/input.md", "after\n")
        self.assert_problem("Hash mismatch")

    def test_pinned_manifest_uses_historical_skill_bytes(self):
        data = (self.skill / "SKILL.md").read_bytes()
        commit = self.git("rev-parse", "HEAD")
        self.write("evals/case/manifest.json", json.dumps({"files": {}, "skill_versions": {"tested": {"directory": "skills/example", "git_commit": commit, "files": {"SKILL.md": hashlib.sha256(data).hexdigest()}}}}))
        with (self.skill / "SKILL.md").open("a") as stream:
            stream.write("\nAn active revision.\n")
        self.assertEqual(self.report()["errors"], [])

    def test_unavailable_history_is_not_reported_as_corruption(self):
        self.write("evals/case/manifest.json", json.dumps({"source_git_commit": "1" * 40, "files": {"skills/example/SKILL.md": "0" * 64}}))
        self.assert_problem("Git history unavailable")
        self.assertFalse(any("Hash mismatch" in error for error in self.report()["errors"]))

    def test_installed_directory_compares_complete_skill_bytes(self):
        installed = self.root / "installed"
        shutil.copytree(self.skill, installed / "example")
        self.assertEqual(self.report(installed_dir=installed)["errors"], [])
        (installed / "example/references/details.md").write_text("Changed\n")
        self.assert_problem("Installed mismatch", installed_dir=installed)

    def test_unlisted_archived_absolute_link_fails(self):
        self.write("evals/archive/answer.md", "[Result](/tmp/unrecorded-output.md)\n")
        self.assert_problem("Absolute local link")

    def test_exact_historical_compatibility_link_passes(self):
        page, target = "evals/archive/answer.md", "/synthetic/archived-output.md"
        digest = hashlib.sha256(target.encode()).hexdigest()
        self.write(page, f"[Output]({target})\n")
        with mock.patch.object(validate, "HISTORICAL_LINKS", {(page, digest)}):
            self.assertEqual(self.report()["errors"], [])
            self.write(page, "[Output](/synthetic/other-output.md)\n")
            self.assert_problem("Absolute local link")

    def test_shared_copy_drift_fails(self):
        self.write("shared/prose-policy.md", "Canonical\n")
        self.write("shared/manifest.json", json.dumps({"version": 1, "copies": [{"source": "shared/prose-policy.md", "targets": ["skills/example/references/prose-policy.md"]}]}))
        self.write("skills/example/references/prose-policy.md", "Outdated\n")
        self.assert_problem("Shared copy mismatch")

    def test_shared_copy_check_accepts_equal_bytes_without_writing(self):
        self.write("shared/prose-policy.md", "Canonical\n")
        self.write("shared/manifest.json", json.dumps({"version": 1, "copies": [{"source": "shared/prose-policy.md", "targets": ["skills/example/references/prose-policy.md"]}]}))
        target = self.write("skills/example/references/prose-policy.md", "Canonical\n")
        before = target.stat().st_mtime_ns
        self.assertEqual(self.report()["errors"], [])
        self.assertEqual(target.stat().st_mtime_ns, before)

    def test_shared_source_cannot_escape_repository(self):
        self.write("shared/manifest.json", json.dumps({"version": 1, "copies": [{"source": "../outside.md", "targets": ["skills/example/references/prose-policy.md"]}]}))
        self.assertTrue(self.report()["errors"])

    def test_shared_source_must_be_a_canonical_shared_file(self):
        self.write("shared/manifest.json", json.dumps({"version": 1, "copies": [{"source": "LICENSE", "targets": ["skills/example/LICENSE"]}]}))
        self.assert_problem("Source must be under shared/")

    def test_diff_whitespace_failure_is_reported(self):
        with (self.skill / "SKILL.md").open("a") as stream:
            stream.write("\nNew trailing space. \n")
        self.assert_problem("git diff --check")


if __name__ == "__main__":
    unittest.main()
