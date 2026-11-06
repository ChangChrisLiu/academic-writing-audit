#!/usr/bin/env python3
"""Read-only local comparison with separately captured Scholar export files."""
import argparse
from datetime import datetime
from hashlib import sha256
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit


HEADER = re.compile(rb'@([a-zA-Z]+)\s*\{\s*([^\s{},()"#%=]+)\s*,')
SCHOLAR_HOST = re.compile(r'scholar\.google\.(?:com|[a-z]{2}|(?:co|com)\.[a-z]{2})')
SPACE = re.compile(rb'\s*')


def entries(data, label):
    """Split ordinary braced records without regenerating or normalizing their bytes."""
    offset = 0
    while True:
        start = SPACE.match(data, offset).end()
        if start == len(data):
            return
        header = HEADER.match(data, start)
        if not header or header[1].lower() in {b'comment', b'preamble', b'string'}:
            raise ValueError(f'{label} at byte {start}: unsupported input requires manual inspection')
        depth = 1
        for end in range(header.end(), len(data)):
            char = data[end:end + 1]
            if char == b'{':
                depth += 1
            elif char == b'}':
                depth -= 1
            if depth == 0:
                offset = end + 1
                yield header[2].decode('utf-8'), data[start:offset]
                break
        else:
            raise ValueError(f'{label} at byte {start}: incomplete braced entry')


def load_captures(folder, working_files):
    rows = json.loads((folder / 'captures.json').read_text(encoding='utf-8'))
    if not isinstance(rows, list) or not rows:
        raise ValueError('A nonempty capture index is required')
    captures = {}
    names = set()
    folded_keys = set()
    for row in rows:
        name = row['file']
        if Path(name).name != name or not name.endswith('.bib') or name in names:
            raise ValueError(f'Invalid or repeated capture file: {name}')
        names.add(name)
        path = folder / name
        if any(path.samefile(work) for work in working_files):
            raise ValueError('A working file cannot serve as its own independent capture')
        url = urlsplit(row['scholar_result'])
        if url.scheme != 'https' or not SCHOLAR_HOST.fullmatch(url.hostname or ''):
            raise ValueError(f'{name}: expected an observed Scholar result or search URL')
        captured_at = datetime.fromisoformat(row['captured_at'].replace('Z', '+00:00'))
        if captured_at.tzinfo is None or not row['version'].strip():
            raise ValueError(f'{name}: capture time with timezone and intended version required')
        raw = path.read_bytes()
        if sha256(raw).hexdigest() != row['sha256']:
            raise ValueError(f'{name}: capture digest mismatch')
        records = list(entries(raw, name))
        if len(records) != 1:
            raise ValueError(f'{name}: expected a single captured entry')
        key, record = records[0]
        if key.casefold() in folded_keys:
            raise ValueError(f'{key}: export-key collision requires identity review')
        folded_keys.add(key.casefold())
        captures[key] = record
    if names != {p.name for p in folder.glob('*.bib')}:
        raise ValueError('Capture directory contains unindexed .bib files')
    return captures


def compare(working_files, captures):
    results = []
    seen = set()
    seen_folded = set()
    for path in working_files:
        for key, record in entries(path.read_bytes(), path.name):
            if key.casefold() in seen_folded:
                status = 'duplicate working key'
            elif key not in captures:
                status = 'no capture for working key'
            elif record != captures[key]:
                status = 'differs from export'
            else:
                status = 'exact entry match'
            results.append({'database': path.name, 'key': key, 'status': status})
            seen.add(key)
            seen_folded.add(key.casefold())
    results.extend({'key': key, 'status': 'capture missing from working bibliography'}
                   for key in sorted(captures.keys() - seen))
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--bib', nargs='+', required=True, type=Path)
    parser.add_argument('--exports', required=True, type=Path)
    args = parser.parse_args()
    try:
        captures = load_captures(args.exports, args.bib)
        results = compare(args.bib, captures)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print(f'Comparison incomplete: {exc}', file=sys.stderr)
        return 2
    print(json.dumps({'check': 'local entry equality only', 'entries': results}, indent=2))
    return int(any(r['status'] != 'exact entry match' for r in results))


if __name__ == '__main__':
    sys.exit(main())
