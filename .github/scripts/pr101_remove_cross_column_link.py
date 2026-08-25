#!/usr/bin/env python3
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
for rel in [
 'content/research/notes/open-engineering-specification-article-draft.md',
 'content/research/notes/thinking-systems-publication-draft.md',
]:
 p=ROOT/rel; t=p.read_text(encoding='utf-8')
 old='        A2 ~~~ J1\n'
 if t.count(old)!=1: raise SystemExit(f'{rel}: expected one cross-column alignment edge, got {t.count(old)}')
 p.write_text(t.replace(old,'',1),encoding='utf-8')

bp=ROOT/'content/research/notes/open-engineering-specification-article-blueprint.md'
t=bp.read_text(encoding='utf-8')
old='An invisible cross-column alignment edge may remain only as a secondary ordering aid. CI must reject Figure 3 when this structural layout contract disappears.'
new='Do not connect nodes across the two column subgraphs merely for alignment: Mermaid may then ignore the local `direction TB` of those subgraphs and re-layout their internal chains horizontally. The columns must remain disconnected at node level; the outer `ROW3` owns only their side-by-side placement. CI must reject Figure 3 when this structural layout contract disappears or a cross-column alignment edge is reintroduced.'
if t.count(old)!=1: raise SystemExit(f'blueprint alignment sentence count {t.count(old)}')
bp.write_text(t.replace(old,new,1),encoding='utf-8')

test=ROOT/'quartz/scripts/research-diagram-layout.test.mjs'
t=test.read_text(encoding='utf-8')
t=t.replace('assert.match(m,/A1 --> A2 --> A3/);assert.match(m,/B1 --> B2 --> J1 --> B4 --> B3/);assert.match(m,/A2 ~~~ J1/);','assert.match(m,/A1 --> A2 --> A3/);assert.match(m,/B1 --> B2 --> J1 --> B4 --> B3/);assert.doesNotMatch(m,/A2 ~~~ J1|A1 ~~~ B1|A3 ~~~ B3/);',1)
t=t.replace('assert.match(bp,/outer row subgraph `ROW3` with `direction LR`/);','assert.match(bp,/outer row subgraph `ROW3` with `direction LR`/);assert.match(bp,/columns must remain disconnected at node level/);',1)
test.write_text(t,encoding='utf-8')
print('Removed Figure 3 cross-column edge and guarded Mermaid subgraph direction.')
# trigger
