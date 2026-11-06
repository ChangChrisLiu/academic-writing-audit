"""Exercise the export checker at its normal CLI using a retained Scholar capture."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK = ROOT / 'skills/latex-bibliography-audit/scripts/check_scholar_exports.py'
SOURCE = ROOT / 'evals/scholar-export-only/verifier-a/export.bib'


class ScholarExportTest(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        folder = Path(temp.name)
        self.captures = folder / 'captures'
        self.captures.mkdir()
        self.work = folder / 'work.bib'
        self.raw = SOURCE.read_bytes()
        self.work.write_bytes(self.raw)
        self.index = self.captures / 'captures.json'
        self.capture = self.captures / 'original.bib'
        self.capture.write_bytes(self.raw)
        self.row = {'file': self.capture.name, 'sha256': sha256(self.raw).hexdigest(),
                    'captured_at': '2026-11-05T19:20-06:00',
                    'scholar_result': 'https://scholar.google.com/scholar?q=%22Random+Forests%22+%22Breiman%22+2001',
                    'version': 'Machine Learning journal article, 2001'}
        self.index.write_text(json.dumps([self.row]))

    def run_check(self, code, message, *files):
        paths = files or (self.work,)
        originals = [p.read_bytes() for p in paths]
        result = subprocess.run([sys.executable, str(CHECK), '--bib', *map(str, paths),
                                 '--exports', str(self.captures)], capture_output=True, text=True)
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        self.assertIn(message, result.stdout + result.stderr)
        self.assertEqual([p.read_bytes() for p in paths], originals)

    def test_exact_entry_and_surrounding_whitespace(self):
        self.work.write_bytes(b'\n\n' + self.raw + b'\n')
        self.run_check(0, 'exact entry match')

    def test_added_doi_and_rewritten_data_are_differences(self):
        changes = [(b'publisher={Springer}', b'publisher={Springer},\n  doi={10.1023/A:1010933404324}'),
                   (b'Random forests', b'Random Forests'), (b'year={2001}', b'year={2002}'),
                   (b'@article', b'@inproceedings'), (b'\n  title', b'\n title'),
                   (b'5--32', b'5-32')]
        for before, after in changes:
            with self.subTest(after=after):
                self.work.write_bytes(self.raw.replace(before, after))
                self.run_check(1, 'differs from export')

    def test_old_key_and_missing_coverage(self):
        self.work.write_bytes(self.raw.replace(b'breiman2001random', b'breiman2001'))
        self.run_check(1, 'no capture for working key')
        self.run_check(1, 'capture missing from working bibliography')

    def test_identical_text_without_capture_provenance(self):
        self.index.unlink()
        self.run_check(2, 'Comparison incomplete')

    def test_changed_or_untraceable_capture(self):
        self.capture.write_bytes(self.raw + b'\n')
        self.run_check(2, 'digest mismatch')
        self.capture.write_bytes(self.raw)
        self.index.write_text(json.dumps([{**self.row, 'scholar_result': 'https://publisher.example/record'}]))
        self.run_check(2, 'expected an observed Scholar')

    def test_colliding_export_keys(self):
        second = self.captures / 'different.bib'
        changed = self.raw.replace(b'year={2001}', b'year={2002}')
        second.write_bytes(changed)
        self.index.write_text(json.dumps([self.row, {**self.row, 'file': second.name,
                                                      'sha256': sha256(changed).hexdigest()}]))
        self.run_check(2, 'export-key collision')

    def test_duplicates_across_working_databases(self):
        second = self.work.with_name('appendix.bib')
        second.write_bytes(self.raw)
        self.run_check(1, 'duplicate working key', self.work, second)

    def test_self_comparison_and_unsupported_syntax_remain_unresolved(self):
        self.run_check(2, 'its own independent capture', self.capture)
        self.work.write_bytes(b'@string{j = "some journal"}\n' + self.raw)
        self.run_check(2, 'unsupported input')
        self.work.write_bytes(self.raw.rstrip()[:-1])
        self.run_check(2, 'incomplete braced entry')


if __name__ == '__main__':
    unittest.main()
