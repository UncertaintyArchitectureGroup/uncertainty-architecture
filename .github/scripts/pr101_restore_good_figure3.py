#!/usr/bin/env python3
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
FIG3='''flowchart LR
    subgraph A["Explicitly Authored Software"]
        direction TB
        A1["Situation and operating conditions"]
        A2["Explicitly authored consequential responsibilities"]
        A3["Consequential output, action, or downstream state"]
        A1 --> A2 --> A3
    end

    subgraph B["Motivating runtime-judgment class"]
        direction TB
        B1["Situation and operating conditions"]
        B2["Explicitly authored responsibilities before and between Judgment Nodes"]
        J1["One or more Judgment Nodes<br/>probabilistic Model Judgment"]
        B4["Explicitly authored responsibilities after Judgment Nodes"]
        B3["Consequential output, action, or downstream state"]
        B1 --> B2 --> J1 --> B4 --> B3
    end

    classDef judgment fill:#ffcdd2,stroke:#b71c1c,stroke-width:3px,color:#6a0000;
    class J1 judgment;'''

def replace_fig(path):
    p=ROOT/path
    t=p.read_text(encoding='utf-8')
    rx=re.compile(r'```mermaid\n(?P<body>(?:(?!```)[\s\S])*?)\n```\n\n(?P<cap>\*\*Figure 3 —[^\n]*controlled-object shift[^\n]*)')
    ms=list(rx.finditer(t))
    if len(ms)!=1: raise SystemExit(f'{path}: expected one Figure 3, got {len(ms)}')
    m=ms[0]
    p.write_text(t[:m.start('body')]+FIG3+t[m.end('body'):],encoding='utf-8')

for rel in ['content/research/notes/open-engineering-specification-article-draft.md','content/research/notes/thinking-systems-publication-draft.md']:
    replace_fig(rel)

bp=ROOT/'content/research/notes/open-engineering-specification-article-blueprint.md'
t=bp.read_text(encoding='utf-8')
start='Use two vertical top-to-bottom responsibility diagrams placed side by side.'
pos=t.find(start)
if pos<0: raise SystemExit('blueprint Figure 3 contract start not found')
end=t.find('\n\n```text',pos)
if end<0: raise SystemExit('blueprint Figure 3 contract end not found')
new=('Use two vertical top-to-bottom responsibility diagrams placed side by side. Restore the known-good Mermaid structure established in PR #56 (`7ef8859b`): top-level `flowchart LR`, followed by exactly two disconnected subgraphs in left-to-right source order. The left subgraph title is the short label `Explicitly Authored Software`; the right title is `Motivating runtime-judgment class`. Each subgraph declares `direction TB`. Keep explanatory detail in the caption rather than expanding the subgraph titles, because oversized group labels can change Mermaid bounding boxes and destabilize the side-by-side composition. The left column remains a three-block vertical chain: situation/conditions → explicitly authored consequential responsibilities → consequential output/action/state. The right column remains a five-block vertical chain: situation/conditions → explicitly authored responsibilities before/between Judgment Nodes → Judgment Node(s) → explicitly authored responsibilities after Judgment Nodes → consequential output/action/state. Do not add outer layout wrappers, cross-column edges, invisible alignment links, or Block Diagram syntax. CI must reject Figure 3 if it departs from this known-good structural contract.')
t=t[:pos]+new+t[end:]
bp.write_text(t,encoding='utf-8')

test=ROOT/'quartz/scripts/research-diagram-layout.test.mjs'
t=test.read_text(encoding='utf-8')
# replace f3 function wholesale
s=t.index('function f3(src){')
e=t.index('\nfunction ortho',s)
newf='function f3(src){const m=fig(src,3,"controlled-object shift");assert.match(m,/^flowchart LR/m);assert.match(m,/subgraph A\\["Explicitly Authored Software"\\][\\s\\S]*direction TB/);assert.match(m,/subgraph B\\["Motivating runtime-judgment class"\\][\\s\\S]*direction TB/);assert.ok(m.indexOf("subgraph A")<m.indexOf("subgraph B"));assert.match(m,/A1 --> A2 --> A3/);assert.match(m,/B1 --> B2 --> J1 --> B4 --> B3/);assert.doesNotMatch(m,/ROW3|^block$|columns 2|A[123]\\s*(?:---|-->|~~~).*B[1234J]|B[1234J]\\s*(?:---|-->|~~~).*A[123]/m);}'
t=t[:s]+newf+t[e:]
# replace blueprint assertions part
old_patterns=[
'assert.match(bp,/Mermaid Block Diagram syntax/);assert.match(bp,/top-level `block` with `columns 2`/);assert.match(bp,/composite blocks `L` and `R`/);assert.match(bp,/Both composite blocks must declare `columns 1`/);',
'assert.match(bp,/top-level `flowchart LR`/);assert.match(bp,/exactly two disconnected subgraphs/);assert.match(bp,/Each subgraph must declare `direction TB`/);'
]
for old in old_patterns:
    if old in t:
        t=t.replace(old,'assert.match(bp,/known-good Mermaid structure established in PR #56/);assert.match(bp,/top-level `flowchart LR`/);assert.match(bp,/exactly two disconnected subgraphs/);assert.match(bp,/Each subgraph declares `direction TB`/);',1)
        break
else:
    raise SystemExit('blueprint Figure 3 test assertions not found')
test.write_text(t,encoding='utf-8')
print('Restored known-good PR #56 Figure 3 structure with current semantics.')
