#!/usr/bin/env python3
"""Keep standalone skill resources equal to their maintained shared sources."""

import argparse
import json
from pathlib import Path
import sys


def local_path(root, relative):
    path = Path(relative)
    if path.is_absolute() or '..' in path.parts or not path.parts:
        raise ValueError(f'Expected a repository-relative path: {relative}')
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError(f'Path escapes the repository: {relative}')
    return root / path


def sync(root, check=False):
    """Return mismatched target names; in write mode update only declared copies."""
    manifest = json.loads((root / 'shared/manifest.json').read_text())
    if manifest.get('version') != 1:
        raise ValueError('Unsupported shared-file manifest version')
    jobs = []
    seen = set()
    for group in manifest['copies']:
        source = local_path(root, group['source'])
        if not group['source'].startswith('shared/'):
            raise ValueError(f'Source must be under shared/: {group["source"]}')
        data = source.read_bytes()
        for relative in group['targets']:
            target = local_path(root, relative)
            if not relative.startswith('skills/') or relative in seen:
                raise ValueError(f'Invalid or repeated skill target: {relative}')
            seen.add(relative)
            jobs.append((relative, target, data))
    mismatches = []
    for relative, target, data in jobs:
        if target.is_file() and target.read_bytes() == data:
            continue
        mismatches.append(relative)
        if not check:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    return mismatches


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Report drift without writing')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        mismatches = sync(args.root, check=args.check)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f'Shared resources: {exc}', file=sys.stderr)
        return 1
    label = 'Out of sync' if args.check else 'Updated'
    for path in mismatches:
        print(f'{label}: {path}')
    if not mismatches:
        print('Shared resources are synchronized.')
    return int(args.check and bool(mismatches))


if __name__ == '__main__':
    raise SystemExit(main())
