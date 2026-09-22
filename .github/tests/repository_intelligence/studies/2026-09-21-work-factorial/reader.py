"""Logged fixture access for the authorized AGENTS-text/RI-operations experiment.

This is an experiment transport, not an OS sandbox or production retrieval API.
RI pages retain the unchanged pinned CLI stdout, without ranking or filtering.
"""
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE / 'source'
PAGE = 10000
MANIFEST = json.loads((BASE / 'source-manifest.json').read_text())
SOURCE = '989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3'
PROFILES = {'WF01': 'A', 'WF02': 'B', 'WF03': 'C', 'WF04': 'D', 'WF05': 'C', 'WF06': 'D', 'WF07': 'A', 'WF08': 'B', 'WF09': 'D', 'WF10': 'C', 'WF11': 'B', 'WF12': 'A', 'SMOKE_A': 'A', 'SMOKE_B': 'B', 'SMOKE_C': 'C', 'SMOKE_D': 'D'}
OPERATIONS = {'verify', 'context-for-task', 'find-owner', 'term-preflight',
              'artifact-preflight', 'validation-plan', 'impact-for-paths', 'stats'}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def permitted(path, guide, ri):
    try:
        rel = path.relative_to(ROOT).as_posix()
        path.resolve().relative_to(ROOT.resolve())
    except ValueError:
        return False
    if path.is_symlink() or (path.is_file() and rel not in MANIFEST) or path.name == 'AGENTS.md' and not guide:
        return False
    if rel.startswith('.github/tests/repository_intelligence/'):
        return False
    if rel.startswith('.github/scripts/') and 'repository_intelligence' in path.name:
        return False
    return ri or not rel.startswith('assets/repository-intelligence/')


def resolve(value, guide, ri):
    path = ROOT / value
    if Path(value).is_absolute() or '..' in Path(value).parts or not permitted(path, guide, ri):
        raise ValueError('Unavailable in this experimental condition')
    return path


def page(raw, offset, metadata):
    if offset < 0:
        raise ValueError('Negative offset')
    text = raw.decode('utf-8')
    fragment = text[offset:offset + PAGE]
    end = offset + len(fragment)
    return dict(metadata, content_sha256=digest(raw), total_utf8_bytes=len(raw),
                offset=offset, next_offset=end if end < len(text) else None,
                total_characters=len(text), text=fragment)


def main():
    run, operation, *args = sys.argv[1:]
    if run not in PROFILES:
        raise SystemExit('Unknown run')
    profile = PROFILES[run]
    guide, ri = profile in {'B', 'D'}, profile in {'C', 'D'}
    journal = BASE / 'runs' / (run + '-journal.jsonl')
    count = len(journal.read_text().splitlines()) if journal.exists() else 0
    record = {'run_id': run, 'operation': operation, 'arguments': args, 'source_commit': SOURCE}
    started = time.monotonic()
    try:
        if count >= 90:
            raise ValueError('Frozen limit of 90 reader/RI operations reached')
        if operation == 'start':
            if run.startswith('SMOKE'):
                raise ValueError('No participant message for smoke')
            response = page((BASE / 'messages' / (run + '.txt')).read_bytes(),
                            int(args[0]) if args else 0,
                            {'kind': 'starting_message', 'run_id': run})
        elif operation == 'read':
            path = resolve(args[0], guide, ri)
            response = page(path.read_bytes(), int(args[1]) if len(args) > 1 else 0,
                            {'kind': 'source', 'path': args[0]})
        elif operation == 'list':
            prefix = args[0] if args else ''
            resolve(prefix, guide, ri)
            paths = sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*')
                           if p.is_file() and permitted(p, guide, ri)
                           and p.relative_to(ROOT).as_posix().startswith(prefix))
            start = int(args[1]) if len(args) > 1 else 0
            if start < 0:
                raise ValueError('Negative index')
            response = {'paths': paths[start:start + 60], 'total_paths': len(paths),
                        'next_index': start + 60 if start + 60 < len(paths) else None}
        elif operation == 'search':
            pattern = re.compile(args[0], re.IGNORECASE)
            prefix = args[1] if len(args) > 1 else ''
            resolve(prefix, guide, ri)
            hits = []
            for path in sorted(ROOT.rglob('*')):
                if not path.is_file() or not permitted(path, guide, ri):
                    continue
                rel = path.relative_to(ROOT).as_posix()
                if not rel.startswith(prefix) or path.suffix not in {'.md', '.json', '.py', '.yml', '.yaml'}:
                    continue
                try:
                    lines = path.read_text().splitlines()
                except (OSError, UnicodeError):
                    continue
                for line, text in enumerate(lines, 1):
                    if pattern.search(text):
                        hits.append({'path': rel, 'line': line, 'text': text[:180]})
            response = {'matches': hits[:24], 'total_matches': len(hits), 'narrow_query_if_more': len(hits) > 24}
        elif operation == 'fixture':
            if args[0] != 'pr123':
                raise ValueError('Unknown fixture')
            response = page((BASE / 'fixtures/pr123.json').read_bytes(), int(args[1]) if len(args) > 1 else 0,
                            {'kind': 'task_fixture', 'fixture': 'pr123'})
        elif operation == 'ri':
            if not ri or not args or args[0] not in OPERATIONS:
                raise ValueError('RI operation unavailable')
            op = args[0]
            if op in {'verify', 'stats'} and len(args) != 1:
                raise ValueError('Unexpected arguments')
            if op not in {'verify', 'stats', 'impact-for-paths'} and len(args) != 2:
                raise ValueError('Provide one literal query argument')
            if op == 'impact-for-paths' and (len(args) < 2 or any(p.startswith('-') or '..' in Path(p).parts or Path(p).is_absolute() for p in args[1:])):
                raise ValueError('Provide repository-relative paths')
            command = [sys.executable, str(ROOT / '.github/scripts/repository_intelligence.py'), *args]
            result = subprocess.run(command, cwd=ROOT, capture_output=True, timeout=45, check=False)
            response_id = str(count + 1)
            cache = BASE / 'runs' / (run + '-ri-' + response_id + '.json')
            payload = {'command': args, 'exit_code': result.returncode, 'stdout': result.stdout.decode(),
                       'stderr': result.stderr.decode(), 'stdout_sha256': digest(result.stdout)}
            cache.write_text(json.dumps(payload, ensure_ascii=False) + '\n')
            record['ri_payload'] = payload
            response = page(result.stdout, 0, {'kind': 'ri_stdout', 'response_id': response_id,
                            'command': args, 'exit_code': result.returncode, 'stderr': payload['stderr']})
        elif operation == 'ri-more':
            if not ri or not re.fullmatch(r'[1-9][0-9]*', args[0]):
                raise ValueError('RI response unavailable')
            payload = json.loads((BASE / 'runs' / (run + '-ri-' + args[0] + '.json')).read_text())
            response = page(payload['stdout'].encode(), int(args[1]),
                            {'kind': 'ri_stdout', 'response_id': args[0], 'command': payload['command'],
                             'exit_code': payload['exit_code'], 'stderr': payload['stderr']})
        else:
            raise ValueError('Use start, read, list, search, fixture, ri or ri-more')
    except (ValueError, OSError, IndexError, UnicodeError, re.error, subprocess.TimeoutExpired) as error:
        response = {'error': str(error)}
    rendered = json.dumps(response, ensure_ascii=False) + '\n'
    record.update(response=response, response_utf8_bytes=len(rendered.encode()),
                  operation_elapsed_seconds=time.monotonic() - started)
    with journal.open('a') as stream:
        stream.write(json.dumps(record, ensure_ascii=False) + '\n')
    print(rendered, end='')


if __name__ == '__main__':
    main()
