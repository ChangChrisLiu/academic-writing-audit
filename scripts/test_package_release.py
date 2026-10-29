import hashlib
import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location('package_release', Path(__file__).with_name('package_release.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PackageTests(unittest.TestCase):
    def test_reproducible_bytes_and_modes(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            entries = {'skills/demo/tool.py': (b'print(1)\n', 0o100755),
                       'skills/demo/data.bin': (bytes(range(256)), 0o100644)}
            module.write_zip(root / 'a.zip', entries)
            module.write_zip(root / 'b.zip', entries)
            self.assertEqual((root / 'a.zip').read_bytes(), (root / 'b.zip').read_bytes())
            with zipfile.ZipFile(root / 'a.zip') as archive:
                self.assertEqual(archive.read('skills/demo/data.bin'), bytes(range(256)))
                self.assertEqual(archive.getinfo('skills/demo/tool.py').external_attr >> 16, 0o100755)

    def test_package_committed_tree_and_refuse_overwrite_or_dirty_worktree(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder); root = base / 'repo'; root.mkdir()
            def git(*args):
                subprocess.run(['git', *args], cwd=root, check=True, capture_output=True)
            git('init')
            git('config', 'user.name', 'Fixture')
            git('config', 'user.email', 'fixture@example.invalid')
            (root / 'skills/demo/references').mkdir(parents=True)
            (root / 'skills/demo/SKILL.md').write_text('fixture')
            (root / 'skills/demo/references/local.md').write_text('bundled local rules')
            (root / 'assets').mkdir()
            for name in ['hero.jpg', 'social-card.jpg', 'workflow.jpg']:
                (root / 'assets' / name).write_bytes(b'fixture image bytes')
            git('add', '.'); git('commit', '-m', 'fixture')
            destination = base / 'release'
            record = module.package(root, destination, 'v0.1.0', validate=False)
            self.assertEqual(record['skills'], 1)
            self.assertEqual(len(record['assets']), 6)
            with zipfile.ZipFile(destination / 'academic-writing-skills-v0.1.0.zip') as archive:
                self.assertEqual(archive.read('skills/demo/references/local.md'), b'bundled local rules')
                self.assertNotIn('assets/hero.jpg', archive.namelist())
            for line in (destination / 'SHA256SUMS.txt').read_text().splitlines():
                digest, name = line.split('  ')
                self.assertEqual(digest, hashlib.sha256((destination / name).read_bytes()).hexdigest())
            before = (destination / 'SHA256SUMS.txt').read_bytes()
            with self.assertRaisesRegex(ValueError, 'already exists'):
                module.package(root, destination, 'v0.1.0', validate=False)
            self.assertEqual(before, (destination / 'SHA256SUMS.txt').read_bytes())
            (root / 'skills/demo/SKILL.md').write_text('uncommitted edit')
            with self.assertRaisesRegex(ValueError, 'clean checkout'):
                module.package(root, base / 'dirty-release', 'v0.1.1', validate=False)
            self.assertFalse((base / 'dirty-release').exists())

    def test_reject_symlinks_in_portable_zip(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaisesRegex(ValueError, 'Symlinks'):
                module.write_zip(Path(folder) / 'out.zip', {'link': (b'../outside', 0o120777)})


if __name__ == '__main__':
    unittest.main()
