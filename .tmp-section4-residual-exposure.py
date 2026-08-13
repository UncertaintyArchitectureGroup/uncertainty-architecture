from pathlib import Path

draft = Path('content/research/notes/open-engineering-specification-article-draft.md')
text = draft.read_text()
old = '''    HUMAN["Human Authority · fallback<br/> containment · recovery"]
    ECON["Control economics and capacity<br/> latency · operating friction · dependencies"]
    DEC["Project decision<br/> authorize · narrow · research<br/> redesign · defer · No-Go"]
    RE["Delivery / Runtime invalidating evidence"]
    ORG --> NEED
    OUT --> NEED --> RISK --> K --> LOOP
    OUT -->|value hypothesis| DEC
    K -->|non-negotiable authorization boundary| DEC
    LOOP --> HUMAN --> DEC
    LOOP --> ECON --> DEC
'''
new = '''    HUMAN["Human Authority · fallback<br/> containment · recovery"]
    ECON["Control economics and capacity<br/> latency · operating friction · dependencies"]
    RES["Residual exposure + uncertainty<br/> after proposed control"]
    DEC["Project decision<br/> authorize · narrow · research<br/> redesign · defer · No-Go"]
    RE["Delivery / Runtime invalidating evidence"]
    ORG --> NEED
    OUT --> NEED --> RISK --> K --> LOOP
    OUT -->|value hypothesis| DEC
    K -->|non-negotiable authorization boundary| DEC
    LOOP --> HUMAN --> DEC
    LOOP --> ECON --> DEC
    LOOP --> RES --> DEC
'''
assert text.count(old) == 1, f'draft target count={text.count(old)}'
draft.write_text(text.replace(old, new, 1))

bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
text = bp.read_text()
old = '- Include the complete control perimeter in project viability rather than treating evaluation, Human Authority, fallback, observability, and control friction as post-launch overhead; keep attributable value visibly connected to the final Project decision rather than only to the AI-necessity check, and keep non-negotiable Project Constraint Architecture boundaries visibly connected to that decision rather than treating them as tradeable economics.'
new = '- Include the complete control perimeter in project viability rather than treating evaluation, Human Authority, fallback, observability, and control friction as post-launch overhead; keep attributable value, non-negotiable Project Constraint Architecture boundaries, and residual exposure / uncertainty after proposed control visibly connected to the final Project decision rather than collapsing them into tradeable economics.'
assert text.count(old) == 1, f'blueprint target count={text.count(old)}'
bp.write_text(text.replace(old, new, 1))
