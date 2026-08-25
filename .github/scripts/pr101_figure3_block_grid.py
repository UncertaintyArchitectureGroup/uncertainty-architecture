#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

FIG3 = '''block
    columns 2
    H1["Explicitly Authored Software — consequential mapping authored before release"]
    H2["Motivating runtime-judgment class — part of mapping completed at runtime"]
    block:L
        columns 1
        A1["Situation and operating conditions"]
        A2["Explicitly authored consequential responsibilities"]
        A3["Consequential output, action, or downstream state"]
    end
    block:R
        columns 1
        B1["Situation and operating conditions"]
        B2["Explicitly authored responsibilities before and between Judgment Nodes"]
        J1["One or more Judgment Nodes — probabilistic Model Judgment"]
        B4["Explicitly authored responsibilities after Judgment Nodes"]
        B3["Consequential output, action, or downstream state"]
    end
    A1 --> A2 --> A3
    B1 --> B2 --> J1 --> B4 --> B3
    style H1 fill:#f7f9f8,stroke:#b7c2c7,color:#284b63
    style H2 fill:#f6fafb,stroke:#9fb5bf,color:#284b63
    style J1 fill:#ffcdd2,stroke:#b71c1c,stroke-width:3px,color:#6a0000'''

def replace_figure(path):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    rx = re.compile(r'```mermaid\n(?P<body>(?:(?!```)[\s\S])*?)\n```\n\n(?P<caption>\*\*Figure 3 —[^\n]*controlled-object shift[^\n]*)')
    matches = list(rx.finditer(text))
    if len(matches) != 1:
        raise SystemExit(f'{path}: expected one Figure 3, got {len(matches)}')
    m = matches[0]
    text = text[:m.start('body')] + FIG3 + text[m.end('body'):]
    p.write_text(text, encoding='utf-8')

for rel in [
    'content/research/notes/open-engineering-specification-article-draft.md',
    'content/research/notes/thinking-systems-publication-draft.md',
]:
    replace_figure(rel)

bp = ROOT / 'content/research/notes/open-engineering-specification-article-blueprint.md'
text = bp.read_text(encoding='utf-8')
old = ('Use two vertical top-to-bottom responsibility diagrams placed side by side. The comparison must read as two parallel columns, never as two diagrams stacked vertically and never as horizontal execution pipelines. Figure 3 must use top-level `flowchart LR` with exactly two disconnected subgraphs: the explicitly authored column first (left) and the motivating runtime-judgment column second (right). Each subgraph must declare `direction TB`. Do not wrap the columns in another layout subgraph and do not connect nodes across the two columns merely for alignment: either technique can cause GitHub Mermaid to override the intended local direction or stack the subgraphs vertically. The left column must remain a three-block vertical chain: situation/conditions → explicitly authored consequential responsibilities → consequential output/action/state. The right column must remain a vertical chain: situation/conditions → explicitly authored responsibilities before/between Judgment Nodes → Judgment Node(s) → explicitly authored responsibilities after Judgment Nodes → consequential output/action/state. CI must reject Figure 3 when the top-level `flowchart LR`, either local `direction TB`, the column order, or the disconnected-column contract disappears.')
new = ('Use two vertical top-to-bottom responsibility diagrams placed side by side. The comparison must read as two parallel columns, never as two diagrams stacked vertically and never as horizontal execution pipelines. Figure 3 must use Mermaid Block Diagram syntax rather than flowchart/subgraph auto-layout: top-level `block` with `columns 2`, followed by the left and right column headers, then exactly two composite blocks `L` and `R` occupying the second grid row. Both composite blocks must declare `columns 1`. The left composite block must remain a three-block vertical chain: situation/conditions → explicitly authored consequential responsibilities → consequential output/action/state. The right composite block must remain a five-block vertical chain: situation/conditions → explicitly authored responsibilities before/between Judgment Nodes → Judgment Node(s) → explicitly authored responsibilities after Judgment Nodes → consequential output/action/state. Do not add cross-column edges. This grid contract exists specifically to avoid GitHub Mermaid/Dagre reordering disconnected flowchart subgraphs. CI must reject Figure 3 when `block`, `columns 2`, either inner `columns 1`, the left/right header order, either vertical chain, or the disconnected-column contract disappears.')
if text.count(old) != 1:
    raise SystemExit(f'blueprint Figure 3 contract match count {text.count(old)}')
bp.write_text(text.replace(old, new, 1), encoding='utf-8')

test = ROOT / 'quartz/scripts/research-diagram-layout.test.mjs'
t = test.read_text(encoding='utf-8')
oldf = 'function f3(src){const m=fig(src,3,"controlled-object shift");assert.match(m,/^flowchart LR/m);assert.doesNotMatch(m,/ROW3/);assert.match(m,/subgraph A\\["Explicitly Authored Software[\\s\\S]*direction TB/);assert.match(m,/subgraph B\\["Motivating runtime-judgment class[\\s\\S]*direction TB/);assert.ok(m.indexOf("subgraph A")<m.indexOf("subgraph B"));assert.match(m,/A1 --> A2 --> A3/);assert.match(m,/B1 --> B2 --> J1 --> B4 --> B3/);assert.doesNotMatch(m,/A[123]\\s*(?:---|-->|~~~).*B[1234J]|B[1234J]\\s*(?:---|-->|~~~).*A[123]/);}'
newf = 'function f3(src){const m=fig(src,3,"controlled-object shift");assert.match(m,/^block$/m);assert.match(m,/^\\s*columns 2$/m);assert.ok(m.indexOf("H1[")<m.indexOf("H2[")&&m.indexOf("H2[")<m.indexOf("block:L")&&m.indexOf("block:L")<m.indexOf("block:R"));assert.match(m,/block:L[\\s\\S]*columns 1[\\s\\S]*A1\\[[\\s\\S]*A2\\[[\\s\\S]*A3\\[/);assert.match(m,/block:R[\\s\\S]*columns 1[\\s\\S]*B1\\[[\\s\\S]*B2\\[[\\s\\S]*J1\\[[\\s\\S]*B4\\[[\\s\\S]*B3\\[/);assert.match(m,/A1 --> A2 --> A3/);assert.match(m,/B1 --> B2 --> J1 --> B4 --> B3/);assert.doesNotMatch(m,/flowchart|subgraph|ROW3/);assert.doesNotMatch(m,/A[123]\\s*(?:---|-->|~~~).*B[1234J]|B[1234J]\\s*(?:---|-->|~~~).*A[123]/);}'
if oldf not in t:
    raise SystemExit('layout test Figure 3 function not found')
t = t.replace(oldf, newf, 1)
oldbp = 'assert.match(bp,/top-level `flowchart LR`/);assert.match(bp,/exactly two disconnected subgraphs/);assert.match(bp,/Each subgraph must declare `direction TB`/);'
newbp = 'assert.match(bp,/Mermaid Block Diagram syntax/);assert.match(bp,/top-level `block` with `columns 2`/);assert.match(bp,/composite blocks `L` and `R`/);assert.match(bp,/Both composite blocks must declare `columns 1`/);'
if oldbp not in t:
    raise SystemExit('layout test blueprint Figure 3 contract not found')
t = t.replace(oldbp, newbp, 1)
test.write_text(t, encoding='utf-8')

print('Applied deterministic two-column Mermaid block grid for Figure 3.')
