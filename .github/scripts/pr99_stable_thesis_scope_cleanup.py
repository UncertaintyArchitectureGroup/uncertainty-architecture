from pathlib import Path

p = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
text = p.read_text(encoding='utf-8')
old = 'The category names the changed engineering object; it does not certify that the object is adequately controlled. That changes the release contract: Delivery no longer releases only the implementation of a pre-authored consequential mapping, but also places into operation a judgment process that will complete part of that mapping at runtime.'
new = 'The category identifies the responsibility boundary under test; it does not certify that the object is adequately controlled. For the motivating runtime-judgment class covered by the release-contract deduction, that responsibility structure changes the release contract: Delivery no longer releases only the implementation of a pre-authored consequential mapping, but also places into operation a judgment process that will complete part of that mapping at runtime. Whether the same deduction extends to every system admitted by the broader current wording remains under `TS-SCOPE-001`.'
count = text.count(old)
if count != 1:
    raise SystemExit(f'expected exactly one stable-thesis match, got {count}')
p.write_text(text.replace(old, new, 1), encoding='utf-8')
