from pathlib import Path
p = Path('content/research/notes/open-engineering-specification-article-draft.md')
text = p.read_text(encoding='utf-8')
old = 'In a Thinking System, part of the mapping from situation to consequential behavior is instead completed during runtime through Model Judgment. Deterministic software may surround that judgment, but it no longer exhaustively specifies the consequential responsibility that depends on it.'
new = 'For the motivating runtime-judgment class developed in this paper, part of the mapping from situation to consequential behavior is instead completed during runtime through Model Judgment. Deterministic software may surround that judgment, but it no longer exhaustively specifies the consequential responsibility that depends on it. Whether the broader current Thinking-System definition should also include fixed learned probabilistic functions with a release-time-determined mapping remains under `TS-SCOPE-001`.'
if old in text:
    if text.count(old) != 1:
        raise SystemExit(f'ambiguous manuscript scope sentence: {text.count(old)} matches')
    text = text.replace(old, new, 1)
elif new not in text:
    raise SystemExit('expected manuscript scope sentence not found')
text = text.replace('The figure is descriptive of the category boundary, not a prescribed control architecture.', 'The figure is descriptive of the motivating class under the release-contract deduction, not a resolution of the broader category boundary or a prescribed control architecture.', 1)
p.write_text(text, encoding='utf-8')
print('final manuscript scope cleanup applied')
