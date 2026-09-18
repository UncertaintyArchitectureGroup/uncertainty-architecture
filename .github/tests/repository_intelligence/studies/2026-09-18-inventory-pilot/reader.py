"""Bounded, logged ordinary-source reads for the local descriptive pilot."""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent / 'source'
BASE = ROOT.parent
run, operation, *args = sys.argv[1:]
if not re.fullmatch(r'(?:R0[1-8]|SMOKE)', run):
    raise SystemExit('Unknown run identifier')

def allowed(path):
    rel = path.relative_to(ROOT).as_posix()
    return not (path.is_symlink() or rel.startswith('assets/repository-intelligence/')
                or rel.startswith('.github/tests/repository_intelligence/')
                or rel.startswith('.github/scripts/repository_intelligence'))

def target(value):
    p = ROOT / value
    if Path(value).is_absolute() or '..' in Path(value).parts or not allowed(p):
        raise ValueError('Outside permitted source surface')
    return p

record = {'run': run, 'operation': operation, 'arguments': args}
try:
    if operation == 'read':
        p = target(args[0])
        offset = int(args[1]) if len(args) > 1 else 0
        limit = int(args[2]) if len(args) > 2 else 7500
        if offset < 0 or not 1 <= limit <= 7500:
            raise ValueError('Invalid read bounds')
        raw = p.read_bytes()
        source = raw.decode('utf-8')
        chunk = source[offset:offset + limit]
        end = offset + len(chunk)
        response = {'path': args[0], 'source_sha256': hashlib.sha256(raw).hexdigest(),
                    'offset': offset, 'next_offset': end if end < len(source) else None,
                    'total_characters': len(source), 'text': chunk}
    elif operation == 'list':
        prefix = args[0] if args else ''
        target(prefix)
        paths = sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
                       if p.is_file() and allowed(p) and p.relative_to(ROOT).as_posix().startswith(prefix))
        start = int(args[1]) if len(args) > 1 else 0
        if start < 0:
            raise ValueError('Invalid list offset')
        response = {'paths': paths[start:start + 60], 'total_paths': len(paths),
                    'next_index': start + 60 if start + 60 < len(paths) else None}
    elif operation == 'search':
        query = args[0]
        prefix = args[1] if len(args) > 1 else ''
        target(prefix)
        found = []
        pattern = re.compile(query, re.IGNORECASE)
        for p in sorted(ROOT.rglob('*')):
            if not p.is_file() or not allowed(p) or p.suffix not in {'.md', '.json', '.yml', '.yaml', '.py'}:
                continue
            rel = p.relative_to(ROOT).as_posix()
            if not rel.startswith(prefix):
                continue
            try:
                lines = p.read_text().splitlines()
            except (UnicodeError, OSError):
                continue
            for n, line in enumerate(lines, 1):
                if pattern.search(line):
                    found.append({'path': rel, 'line': n, 'text': line[:180]})
        response = {'matches': found[:24], 'total_matches': len(found),
                    'narrow_query_if_more': len(found) > 24}
    else:
        raise ValueError('Use read, list, or search')
except (ValueError, OSError, IndexError, re.error) as error:
    response = {'error': str(error)}
rendered = json.dumps(response, ensure_ascii=False)
record.update(response=response, response_utf8_bytes=len(rendered.encode('utf-8')) + 1)
with (BASE / 'runs' / (run + '-reads.jsonl')).open('a') as stream:
    stream.write(json.dumps(record, ensure_ascii=False) + '\n')
print(rendered)
