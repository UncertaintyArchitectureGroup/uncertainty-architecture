from pathlib import Path
p = Path('content/research/notes/open-engineering-specification-article-draft.md')
text = p.read_text(encoding='utf-8')
old = 'Thinking Systems change this object by making one or more Consequential Runtime Responsibilities depend partly on probabilistic Model Judgment. The change can occur in the first model-enabled iteration; it does not require autonomous agents, dynamic orchestration, multiple models, memory, or a mature AI platform.\n\n'
if old not in text:
    anchor = 'A useful design-contract abstraction for explicitly encoded deterministic responsibility is:\n'
    if text.count(anchor) != 1:
        raise SystemExit(f'expected one section-2 anchor, got {text.count(anchor)}')
    text = text.replace(anchor, old + anchor, 1)
actual_stamp = '**STAMP** models hierarchical socio-technical control structures that can extend from software and operators through management and regulatory authority; **STPA** applies that systems-theoretic model to analyze unsafe control actions and causal scenarios.'
expected_stamp = '**STAMP already models hierarchical socio-technical control structures that can extend from software and operators through management and regulatory authority; STPA applies that systems-theoretic model to analyze unsafe control actions and causal scenarios.**'
if actual_stamp in text:
    text = text.replace(actual_stamp, expected_stamp, 1)
elif expected_stamp not in text:
    raise SystemExit('expected STAMP anchor not found')
p.write_text(text, encoding='utf-8')
