from pathlib import Path

p = Path('content/research/review-process.md')
text = p.read_text(encoding='utf-8')
replacements = {
    '## Active research item register': '## Research State Register',
    '- active research-register delta;': '- research-state-register delta;',
}
for old, new in replacements.items():
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'expected exactly one {old!r}, got {count}')
    text = text.replace(old, new, 1)
p.write_text(text, encoding='utf-8')
