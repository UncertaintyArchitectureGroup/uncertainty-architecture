from pathlib import Path
p = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
s = p.read_text()
old = 'the Business-Authorization coverage rule for Project-only production reauthorization—including that coverage is an Organizationally owned envelope rather than a technical-architecture freeze—, Project-selected-design category-exit rule'
new = 'the Business-Authorization coverage rule for Project-only production reauthorization—including that coverage is an Organizationally owned envelope rather than a technical-architecture freeze—Project-selected-design category-exit rule'
if s.count(old) != 1:
    raise SystemExit(f'expected 1 punctuation target, found {s.count(old)}')
s = s.replace(old, new)
p.write_text(s)
