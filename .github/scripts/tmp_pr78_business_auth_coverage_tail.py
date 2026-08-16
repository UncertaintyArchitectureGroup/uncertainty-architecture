from pathlib import Path
p = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
s = p.read_text()
old = '   ├→ still production-viable inside standing Organizational basis → production Project Reauthorization'
new = '   ├→ still production-viable inside standing Organizational basis and covered by the applicable existing Organizational Business Authorization → production Project Reauthorization'
if s.count(old) != 1:
    raise SystemExit(f'expected 1 stale production reauthorization route, found {s.count(old)}')
s = s.replace(old, new)
if old in s or new not in s:
    raise SystemExit('production reauthorization route guard failed')
p.write_text(s)
