#!/usr/bin/env python3
"""Read-only structural checks using Python's standard library.

The metadata reader accepts this repository's simple scalar YAML subset only;
it is not a general YAML parser. Markdown checks cover inline/reference links,
HTML src/href attributes, ATX heading anchors and explicit HTML IDs, not every
extension a Markdown renderer might support. Historical output anchors are not
reinterpreted. Git-resolved evidence requires the recorded commit objects.
"""

import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


# Exact captured output links, identified by digest to avoid copying old machine paths.
HISTORICAL_LINKS = {
    ('evals/manuscript-structure/regression/cases/mathematics/answer.md',
     'fbbf447ed7417758d2cb1e30031bd9cb6927cf2fddd1f22f2bd6079dfe07b3a0'),
    ('evals/reviewer-response-writing/transfer/results/revised/materials/answer.md',
     '0b2fa5d2dea672c8fa54e9ea4f411486251ea2984d266f1340229097f3094d59'),
    ('evals/reviewer-response-writing/transfer/results/revised/materials/answer.md',
     'dc9a5e2176d5c62705a42841b5afa2ddec853caf4c796684777ea754405370c4'),
}
IGNORED_PARTS = {".git", ".venv", ".local", "__pycache__"}


def scalar_mapping(text, indent=""):
    """Read the intentionally narrow string-mapping format used by our metadata."""
    result = {}
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(re.escape(indent) + r"([a-z_]+):\s*(.+?)\s*", line)
        if not match:
            raise ValueError("Expected simple scalar metadata; general YAML is unsupported")
        key, value = match.groups()
        if key in result:
            raise ValueError(f"Duplicate metadata key: {key}")
        if value.startswith('"'):
            value = json.loads(value)
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        elif (value[0] in "|>{[&*!" or ": " in value or " #" in value
              or value.lower() in {"null", "true", "false", "~"}):
            raise ValueError("Expected simple scalar metadata; quote strings or use a YAML parser")
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Empty or non-string metadata: {key}")
        result[key] = value
    return result


def without_fences(text):
    result, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence):
                fence = None
        elif match:
            fence = match[1]
        else:
            result.append(line)
    return "\n".join(result)


def heading_ids(text):
    text = without_fences(text)
    ids = set(re.findall(r"\b(?:id|name)=[\"']([^\"']+)[\"']", text))
    occurrences = {}
    for title in re.findall(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", text, re.M):
        title = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", title)
        title = re.sub(r"<[^>]*>", "", html.unescape(title))
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        occurrence = occurrences.get(slug, 0)
        occurrences[slug] = occurrence + 1
        ids.add(slug if not occurrence else f"{slug}-{occurrence}")
    return ids


def link_targets(text):
    text = without_fences(text)
    text = re.sub(r"(`+).*?\1", "", text)
    targets = re.findall(r"\]\((<[^>]+>|[^)]+)\)", text)
    targets += re.findall(r"^ {0,3}\[[^]]+\]:\s*(<[^>]+>|\S+)", text, re.M)
    targets += re.findall(r"(?:src|href)=[\"']([^\"']+)[\"']", text)
    for target in targets:
        target = target.strip()
        if target.startswith("<"):
            yield target[1:target.index(">")]
        else:
            yield re.split(r"\s+[\"']", target, maxsplit=1)[0]


def repository_path(root, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValueError(f"Invalid repository-relative path: {relative!r}")
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError(f"Repository path escape: {relative}")
    return path


def validate_repository(root, installed_dir=None):
    root = Path(root).resolve()
    installed_dir = Path(installed_dir).resolve() if installed_dir else None
    errors, warnings = [], []
    counts = {"skills": 0, "local_links": 0, "anchors": 0,
              "manifests": 0, "recorded_hashes": 0, "historical_links": 0,
              "shared_copies": 0}

    def files(pattern):
        return sorted(p for p in root.rglob(pattern)
                      if not (set(p.relative_to(root).parts) & IGNORED_PARTS)
                      and not (installed_dir and p.is_relative_to(installed_dir)))

    def git(*args):
        return subprocess.run(["git", *args], cwd=root, capture_output=True)

    def tree(path):
        return {str(p.relative_to(path)): p.read_bytes() for p in path.rglob("*")
                if p.is_file() and p.name != ".DS_Store"
                and not (set(p.relative_to(path).parts) & IGNORED_PARTS)}

    skill_dirs = sorted(p for p in (root / "skills").glob("*") if p.is_dir())
    counts["skills"] = len(skill_dirs)
    if not skill_dirs:
        errors.append("No installable skill directories found")
    for skill in skill_dirs:
        entry = skill / "SKILL.md"
        try:
            text = entry.read_text(encoding="utf-8")
            match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
            if not match:
                raise ValueError("Missing frontmatter")
            metadata = scalar_mapping(match[1])
            if metadata.get("name") != skill.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill.name) or len(skill.name) > 64:
                raise ValueError("Skill name must match its directory and the portable naming format")
            if not metadata.get("description") or len(metadata["description"]) > 1024:
                raise ValueError("Description must contain 1 to 1024 characters")
            if metadata.get("license") != "MIT":
                raise ValueError("Expected MIT license metadata")
        except (OSError, ValueError) as exc:
            errors.append(f"Frontmatter {entry.relative_to(root)}: {exc}")
        try:
            if (skill / "LICENSE").read_bytes() != (root / "LICENSE").read_bytes():
                errors.append(f"License mismatch: {skill.name}")
        except OSError as exc:
            errors.append(f"License {skill.name}: {exc}")
        try:
            ui = (skill / "agents/openai.yaml").read_text(encoding="utf-8")
            lines = ui.splitlines()
            if not lines or lines[0] != "interface:":
                raise ValueError("Expected interface mapping")
            metadata = scalar_mapping("\n".join(lines[1:]), "  ")
            if not all(metadata.get(key) for key in ("display_name", "short_description", "default_prompt")):
                raise ValueError("Missing display name, short description or default prompt")
        except (OSError, ValueError) as exc:
            errors.append(f"UI metadata {skill.name}: {exc}")
        if installed_dir and tree(skill) != tree(installed_dir / skill.name):
            errors.append(f"Installed mismatch: {skill.name}")
        for child in skill.rglob("*"):
            if child.is_symlink() and not child.resolve().is_relative_to(skill.resolve()):
                errors.append(f"Standalone dependency through symlink: {child.relative_to(root)}")

    expected_entries = {p / "SKILL.md" for p in skill_dirs}
    for entry in files("SKILL.md"):
        if entry not in expected_entries:
            errors.append(f"Extra discoverable skill entrypoint: {entry.relative_to(root)}")

    for page in files("*.md"):
        relative = page.relative_to(root).as_posix()
        try:
            text = page.read_text(encoding="utf-8")
            for target in link_targets(text):
                parsed = urlsplit(html.unescape(target))
                if parsed.scheme or target.startswith("//"):
                    continue
                path_text = unquote(parsed.path)
                if path_text.startswith("/"):
                    if (relative, hashlib.sha256(path_text.encode()).hexdigest()) in HISTORICAL_LINKS:
                        counts["historical_links"] += 1
                    else:
                        errors.append(f"Absolute local link: {relative} -> {path_text}")
                    continue
                if "{{" in path_text or "<" in path_text:
                    continue
                destination = (page.parent / path_text).resolve() if path_text else page.resolve()
                counts["local_links"] += 1
                if not destination.is_relative_to(root):
                    errors.append(f"Repository path escape in link: {relative} -> {target}")
                    continue
                if relative.startswith("skills/") and not destination.is_relative_to(root / "skills" / page.relative_to(root).parts[1]):
                    errors.append(f"Standalone dependency: {relative} -> {target}")
                if not destination.exists():
                    errors.append(f"Missing link: {relative} -> {target}")
                elif parsed.fragment and destination.suffix == ".md" and not relative.startswith("evals/"):
                    counts["anchors"] += 1
                    if unquote(parsed.fragment) not in heading_ids(destination.read_text(encoding="utf-8")):
                        errors.append(f"Missing anchor: {relative} -> {target}")
        except (OSError, ValueError) as exc:
            errors.append(f"Links {relative}: {exc}")

    unavailable_commits, available_commits = set(), set()
    for manifest in sorted((root / "evals").rglob("manifest.json")):
        counts["manifests"] += 1
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
            groups = [(data["files"], "", data.get("source_git_commit"))]
            groups += [(item["files"], item.get("directory", ""), item.get("git_commit"))
                       for item in data.get("skill_versions", {}).values()]
            for entries, base, commit in groups:
                for name, expected in entries.items():
                    if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-f]{64}", expected):
                        raise ValueError(f"Invalid SHA-256 digest for {name}")
                    path = repository_path(root, str(Path(base) / name))
                    relative = path.relative_to(root).as_posix()
                    if commit:
                        if commit in unavailable_commits:
                            continue
                        if commit not in available_commits:
                            if not re.fullmatch(r"[0-9a-f]{40}", commit) or git("cat-file", "-e", f"{commit}^{{commit}}").returncode:
                                unavailable_commits.add(commit)
                                errors.append(f"Git history unavailable: {commit} required by {manifest.relative_to(root)}; use a clone containing the recorded history")
                                continue
                            available_commits.add(commit)
                        result = git("show", f"{commit}:{relative}")
                        if result.returncode:
                            raise ValueError(f"Historical file missing: {relative} at {commit}")
                        content = result.stdout
                    else:
                        content = path.read_bytes()
                    counts["recorded_hashes"] += 1
                    if hashlib.sha256(content).hexdigest() != expected:
                        errors.append(f"Hash mismatch: {manifest.relative_to(root)} -> {relative} at {commit or 'working tree'}")
        except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
            errors.append(f"Manifest {manifest.relative_to(root)}: {exc}")

    shared_manifest = root / "shared/manifest.json"
    if shared_manifest.exists():
        try:
            from sync_shared import sync

            data = json.loads(shared_manifest.read_text(encoding="utf-8"))
            for name in sync(root, check=True):
                errors.append(f"Shared copy mismatch: {name}")
            counts["shared_copies"] = sum(len(item["targets"]) for item in data["copies"])
        except (ImportError, OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f"Shared manifest: {exc}")

    try:
        if git("rev-parse", "--is-inside-work-tree").returncode:
            errors.append("Git repository unavailable: diff checks and pinned evidence need a Git clone")
        else:
            for args in (("diff", "--check"), ("diff", "--cached", "--check")):
                result = git(*args)
                if result.returncode:
                    errors.append("git diff --check: " + (result.stdout + result.stderr).decode(errors="replace").strip())
    except OSError as exc:
        errors.append(f"Git unavailable: {exc}")
    return {"counts": counts, "errors": errors, "warnings": warnings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--installed-dir", type=Path, help="Optionally compare complete installed skill folders")
    args = parser.parse_args()
    report = validate_repository(Path(__file__).resolve().parents[1], args.installed_dir)
    print(json.dumps(report, indent=2))
    return bool(report["errors"])


if __name__ == "__main__":
    sys.exit(main())
