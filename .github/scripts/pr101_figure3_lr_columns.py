#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

FIG3 = '''flowchart LR
    subgraph A["Explicitly Authored Software — consequential mapping authored before release"]
        direction TB
        A1["Situation and operating conditions"]
        A2["Explicitly authored consequential<br/>responsibilities"]
        A3["Consequential output, action,<br/>or downstream state"]
        A1 --> A2 --> A3
    end
    subgraph B["Motivating runtime-judgment class — part of mapping completed at runtime"]
        direction TB
        B1["Situation and operating conditions"]
        B2["Explicitly authored responsibilities<br/>before and between Judgment Nodes"]
        J1["One or more Judgment Nodes<br/>probabilistic Model Judgment"]
        B4["Explicitly authored responsibilities<br/>after Judgment Nodes"]
        B3["Consequential output, action,<br/>or downstream state"]
        B1 --> B2 --> J1 --> B4 --> B3
    end
    classDef judgment fill:#ffcdd2,stroke:#b71c1c,stroke-width:3px,color:#6a0000;
    class J1 judgment;'''

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
old = ('Use two vertical top-to-bottom responsibility diagrams placed side by side. The comparison must read as two parallel columns, never as two diagrams stacked vertically and never as horizontal execution pipelines. Use an explicit transparent outer row subgraph `ROW3` with `direction LR`; place the explicitly authored and motivating-class columns inside it as separate subgraphs with `direction TB`. The left column must remain a three-block vertical chain: situation/conditions → explicitly authored consequential responsibilities → consequential output/action/state. The right column must remain a vertical chain: situation/conditions → explicitly authored responsibilities before/between Judgment Nodes → Judgment Node(s) → explicitly authored responsibilities after Judgment Nodes → consequential output/action/state. Do not connect nodes across the two column subgraphs merely for alignment: Mermaid may then ignore the local `direction TB` of those subgraphs and re-layout their internal chains horizontally. The columns must remain disconnected at node level; the outer `ROW3` owns only their side-by-side placement. CI must reject Figure 3 when this structural layout contract disappears or a cross-column alignment edge is reintroduced.')
new = ('Use two vertical top-to-bottom responsibility diagrams placed side by side. The comparison must read as two parallel columns, never as two diagrams stacked vertically and never as horizontal execution pipelines. Figure 3 must use top-level `flowchart LR` with exactly two disconnected subgraphs: the explicitly authored column first (left) and the motivating runtime-judgment column second (right). Each subgraph must declare `direction TB`. Do not wrap the columns in another layout subgraph and do not connect nodes across the two columns merely for alignment: either technique can cause GitHub Mermaid to override the intended local direction or stack the subgraphs vertically. The left column must remain a three-block vertical chain: situation/conditions → explicitly authored consequential responsibilities → consequential output/action/state. The right column must remain a vertical chain: situation/conditions → explicitly authored responsibilities before/between Judgment Nodes → Judgment Node(s) → explicitly authored responsibilities after Judgment Nodes → consequential output/action/state. CI must reject Figure 3 when the top-level `flowchart LR`, either local `direction TB`, the column order, or the disconnected-column contract disappears.')
if text.count(old) != 1:
    raise SystemExit(f'blueprint Figure 3 contract match count {text.count(old)}')
bp.write_text(text.replace(old, new, 1), encoding='utf-8')

test = ROOT / 'quartz/scripts/research-diagram-layout.test.mjs'
t = test.read_text(encoding='utf-8')
oldf = 'function f3(src){const m=fig(src,3,"controlled-object shift");assert.match(m,/^flowchart TB/m);assert.match(m,/subgraph ROW3\\[" "\\][\\s\\S]*direction LR/);assert.match(m,/subgraph A\\["Explicitly Authored Software[\\s\\S]*direction TB/);assert.match(m,/subgraph B\\["Motivating runtime-judgment class[\\s\\S]*direction TB/);assert.match(m,/A1 --> A2 --> A3/);assert.match(m,/B1 --> B2 --> J1 --> B4 --> B3/);assert.doesNotMatch(m,/A2 ~~~ J1|A1 ~~~ B1|A3 ~~~ B3/);}'
newf = 'function f3(src){const m=fig(src,3,"controlled-object shift");assert.match(m,/^flowchart LR/m);assert.doesNotMatch(m,/ROW3/);assert.match(m,/subgraph A\\["Explicitly Authored Software[\\s\\S]*direction TB/);assert.match(m,/subgraph B\\["Motivating runtime-judgment class[\\s\\S]*direction TB/);assert.ok(m.indexOf("subgraph A")<m.indexOf("subgraph B"));assert.match(m,/A1 --> A2 --> A3/);assert.match(m,/B1 --> B2 --> J1 --> B4 --> B3/);assert.doesNotMatch(m,/A[123]\\s*(?:---|-->|~~~).*B[1234J]|B[1234J]\\s*(?:---|-->|~~~).*A[123]/);}'
if oldf not in t:
    raise SystemExit('layout test Figure 3 function not found')
t = t.replace(oldf, newf, 1)
t = t.replace('assert.match(bp,/outer row subgraph `ROW3` with `direction LR`/);assert.match(bp,/columns must remain disconnected at node level/);', 'assert.match(bp,/top-level `flowchart LR`/);assert.match(bp,/exactly two disconnected subgraphs/);assert.match(bp,/Each subgraph must declare `direction TB`/);', 1)
test.write_text(t, encoding='utf-8')

print('Applied Figure 3 top-level LR / inner TB contract.')
