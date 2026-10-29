#!/usr/bin/env python3
"""Validate and package a clean committed checkout without publishing it."""

import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import stat
import subprocess
import sys
import zipfile


def write_zip(path, files):
    """Write reproducible ZIP entries and check every byte against its input."""
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, (data, mode) in sorted(files.items()):
            if stat.S_ISLNK(mode):
                raise ValueError(f'Symlinks are unsupported in portable bundles: {name}')
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = mode << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, data)
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise ValueError(f'Archive CRC check failed: {path.name}')
        actual = {x.filename: (archive.read(x), x.external_attr >> 16)
                  for x in archive.infolist()}
        if actual != files:
            raise ValueError(f'Archive content or mode mismatch: {path.name}')


def package(root, destination, tag, validate=True):
    if not re.fullmatch(r'v[0-9]+\.[0-9]+\.[0-9]+(?:[-.][A-Za-z0-9.-]+)?', tag):
        raise ValueError('Use a version tag such as v0.9.0')
    if destination.exists():
        raise ValueError('Output directory already exists; no files were overwritten')
    git = lambda *args: subprocess.check_output(['git', *args], cwd=root)
    if git('status', '--porcelain'):
        raise ValueError('Commit the intended files and use a clean checkout before packaging')
    if validate:
        subprocess.run([sys.executable, str(root / 'scripts/validate.py')],
                       cwd=root, check=True, stdout=sys.stderr)
    commit = git('rev-parse', 'HEAD').decode().strip()
    # Git's ZIP may omit regular-file mode bits; take modes from the tree itself.
    modes = {}
    for record in git('ls-tree', '-r', '-z', 'HEAD').split(b'\0'):
        if record:
            info, name = record.split(b'\t', 1)
            mode, kind, _ = info.decode().split()
            if kind != 'blob':
                raise ValueError('Submodules are unsupported in portable bundles')
            modes[name.decode()] = int(mode, 8)
    with zipfile.ZipFile(io.BytesIO(git('archive', '--format=zip', 'HEAD'))) as archive:
        files = {x.filename: (archive.read(x), modes[x.filename])
                 for x in archive.infolist() if not x.is_dir()}
    if set(files) != set(modes):
        raise ValueError('Git archive omits tracked files; check export-ignore attributes')
    skills = sorted(name.split('/')[1] for name in files
                    if re.fullmatch(r'skills/[^/]+/SKILL\.md', name))
    if not skills:
        raise ValueError('No installable skills found in committed tree')
    required_assets = ['hero.jpg', 'social-card.jpg', 'workflow.jpg']
    for name in required_assets:
        if 'assets/' + name not in files:
            raise ValueError(f'Missing committed release asset: {name}')
    if any(stat.S_ISLNK(mode) for _, mode in files.values()):
        raise ValueError('Resolve tracked symlinks before creating portable bundles')
    install = (
        f'Academic Writing Audit {tag}\n\n'
        f'This bundle contains {len(skills)} independently installable skills.\n'
        'Copy selected folders from skills/ to your agent client\'s skills directory.\n'
        'Keep each complete folder, including references, scripts where present, and LICENSE.\n'
        'Shared rules are already bundled locally; no other installed skill is required.\n'
        'Review existing installations before replacing them.\n'
        'Alternatively supply SKILL.md and its referenced files to an agent that reads Markdown.\n\n'
        'Source and documentation: https://github.com/ChangChrisLiu/academic-writing-audit\n'
        f'Source commit: {commit}\n'
    ).encode()
    destination.mkdir(parents=True, exist_ok=False)
    prefix = f'academic-writing-audit-{tag}/'
    write_zip(destination / f'academic-writing-audit-{tag}.zip',
              {prefix + name: value for name, value in files.items()})
    write_zip(destination / f'academic-writing-skills-{tag}.zip',
              {'INSTALL.txt': (install, 0o100644),
               **{name: value for name, value in files.items() if name.startswith('skills/')}})
    for name in required_assets:
        (destination / name).write_bytes(files['assets/' + name][0])
    checksums = ''.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.name + '\n'
                        for p in sorted(destination.iterdir()))
    (destination / 'SHA256SUMS.txt').write_text(checksums)
    return {
        'commit': commit, 'tag': tag, 'directory': str(destination.resolve()),
        'skills': len(skills), 'zip_source_match': True,
        'assets': {p.name: {'size': p.stat().st_size,
                          'digest': 'sha256:' + hashlib.sha256(p.read_bytes()).hexdigest()}
                   for p in sorted(destination.iterdir())},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tag', required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        record = package(root, args.output_dir.resolve(), args.tag)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f'Packaging failed: {exc}', file=sys.stderr)
        return 1
    print(json.dumps(record, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
