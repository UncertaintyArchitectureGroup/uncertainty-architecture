#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

FIG3 = '''flowchart TB
    subgraph ROW3[" "]
        direction LR
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
        A2 ~~~ J1
    end
    classDef judgment fill:#ffcdd2,stroke:#b71c1c,stroke-width:3px,color:#6a0000;
    class J1 judgment;
    style ROW3 fill:transparent,stroke:transparent'''

ORTHO = '''flowchart TB
    subgraph ROW_ORTHO[" "]
        direction LR
        subgraph L["Decision ownership — where the decision belongs"]
            direction TB
            subgraph SPINE9[" "]
                direction TB
                O["Organization<br/>What may the organization assess, research, pursue, or continue?"]
                P["Project / Architecture<br/>Model-Judgment necessity · technical selection<br/>control feasibility · economics · viability"]
                CAT{"Selected technical design<br/>still a Thinking System?"}
                EXIT["Exit Thinking-System-specific lifecycle<br/>handoff to ordinary product/software governance"]
                D["Delivery<br/>Is this bounded realization complete and releasable<br/>for its authorized scope?"]
                R["Runtime<br/>Does active operation remain inside the authorized boundary?"]
                E["Delivery / Runtime reassessment evidence<br/>realization or operation evidence that challenges a decision basis"]
                X["Exogenous Organizational change<br/>authoritative or business basis"]

                O -->|initial admissibility + assessment eligibility<br/>authoritative / business basis| P
                P -->|technical design selected<br/>inside standing Organizational basis| CAT
                CAT -->|No| EXIT
                CAT -->|Yes| P
                P -->|reserved-boundary research request / viable production basis<br/>or changed Organizational premise / continuation decision| O
                O -->|specific Bounded Research Authorization<br/>Business Authorization or changed basis| P
                P -->|applicable Project Authorization scope / set<br/>research-only and/or production-capable where applicable| D
                D -->|approved realization + authorized exposure| R
                D -.->|realization / experiment evidence| E
                R -->|operation evidence| E
                X --> O
            end
            E -.->|implementation / realization / evidence issue| D
            E -.->|risk / feasibility / Model Judgment necessity<br/>capacity / economics invalidated or research answered| P
            style SPINE9 fill:transparent,stroke:transparent
        end
        subgraph F["Capability functions — one control architecture, not a sequence"]
            direction TB
            C["Controllers / decision functions<br/>interpret evidence and select bounded response"]
            S["Sensors and evidence<br/>observe behavior, conditions, and control state"]
            K["Constraints and realizations<br/>define and operationalize boundaries"]
            A["Actuators and corrective action<br/>execute authorized change"]
            C --- S --- K --- A
        end
    end
    L -. "all four capability families may appear at every decision horizon" .- F
    classDef capability fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20;
    class A,K,S,C capability;
    style ROW_ORTHO fill:transparent,stroke:transparent'''


def replace_figure(path: str, number: int, title_fragment: str, new_body: str):
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    rx = re.compile(r'```mermaid\n(?P<body>(?:(?!```)[\s\S])*?)\n```\n\n(?P<caption>\*\*Figure %d —[^\n]+)' % number)
    matches = [m for m in rx.finditer(text) if title_fragment in m.group('caption')]
    if len(matches) != 1:
        raise SystemExit(f'{path}: expected one Figure {number} {title_fragment!r}, got {len(matches)}')
    m = matches[0]
    text = text[:m.start('body')] + new_body + text[m.end('body'):]
    p.write_text(text, encoding='utf-8')

for path in [
    'content/research/notes/open-engineering-specification-article-draft.md',
    'content/research/notes/thinking-systems-publication-draft.md',
]:
    replace_figure(path, 3, 'controlled-object shift', FIG3)

replace_figure('content/research/notes/open-engineering-specification-article-draft.md', 9, 'Two orthogonal models', ORTHO)
replace_figure('content/research/notes/thinking-systems-publication-draft.md', 8, 'Two orthogonal models', ORTHO)

# Captions: vertical capability stack connected without arrows is architectural grouping, not sequence.
for path, fig in [
    ('content/research/notes/open-engineering-specification-article-draft.md', 'Figure 9'),
    ('content/research/notes/thinking-systems-publication-draft.md', 'Figure 8'),
]:
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    old = 'The green side is the capability anatomy. Its ordering is a reading aid, not an execution pipeline. There is no one-to-one mapping between horizons and capability families.'
    new = 'The green side is the capability anatomy. Controllers, Sensors, Constraints, and Actuators are stacked vertically and connected with non-directional lines to show that they belong to one control architecture; the vertical order is a reading aid, not an execution sequence. There is no one-to-one mapping between horizons and capability families.'
    if text.count(old) != 1:
        raise SystemExit(f'{path}: expected one capability caption sentence, got {text.count(old)}')
    p.write_text(text.replace(old, new, 1), encoding='utf-8')

# Figure 3 caption wording no longer describes parallel right-hand paths.
for path in [
    'content/research/notes/open-engineering-specification-article-draft.md',
    'content/research/notes/thinking-systems-publication-draft.md',
]:
    p = ROOT / path
    text = p.read_text(encoding='utf-8')
    text = text.replace('The parallel paths are schematic responsibility relationships, not a prescribed execution topology.', 'The vertical paths are schematic responsibility relationships, not a prescribed execution topology.')
    p.write_text(text, encoding='utf-8')

# Blueprint owns the exact topology.
bp = ROOT / 'content/research/notes/open-engineering-specification-article-blueprint.md'
text = bp.read_text(encoding='utf-8')
old = '''Use two vertical top-to-bottom responsibility diagrams placed side by side. The comparison must read as two parallel columns, not as two horizontal execution pipelines and not as one mandatory topology. Do not rely on a top-level `flowchart LR` or an invisible alignment link alone. Use an explicit transparent outer row subgraph `ROW3` with `direction LR`; place the explicitly authored and motivating-class columns inside it as separate subgraphs with `direction TB`. An invisible cross-column alignment edge may remain only as a secondary ordering aid. CI must reject Figure 3 when this structural layout contract disappears.'''
new = '''Use two vertical top-to-bottom responsibility diagrams placed side by side. The comparison must read as two parallel columns, never as two diagrams stacked vertically and never as horizontal execution pipelines. Use an explicit transparent outer row subgraph `ROW3` with `direction LR`; place the explicitly authored and motivating-class columns inside it as separate subgraphs with `direction TB`. The left column must remain a three-block vertical chain: situation/conditions → explicitly authored consequential responsibilities → consequential output/action/state. The right column must remain a vertical chain: situation/conditions → explicitly authored responsibilities before/between Judgment Nodes → Judgment Node(s) → explicitly authored responsibilities after Judgment Nodes → consequential output/action/state. An invisible cross-column alignment edge may remain only as a secondary ordering aid. CI must reject Figure 3 when this structural layout contract disappears.'''
if text.count(old) != 1:
    raise SystemExit(f'blueprint: Figure 3 contract match count {text.count(old)}')
text = text.replace(old, new, 1)
old_block = '''Right — Thinking System — changed responsibility structure\nsituation and operating conditions\n├→ explicitly authored responsibilities before, between, and after Judgment Nodes\n└→ one or more Judgment Nodes using probabilistic Model Judgment\n   both responsibility paths converge on\n→ consequential output, action, or downstream state'''
new_block = '''Right — Thinking System — changed responsibility structure\nsituation and operating conditions\n→ explicitly authored responsibilities before and between Judgment Nodes\n→ one or more Judgment Nodes using probabilistic Model Judgment\n→ explicitly authored responsibilities after Judgment Nodes\n→ consequential output, action, or downstream state'''
if text.count(old_block) != 1:
    raise SystemExit(f'blueprint: Figure 3 text block match count {text.count(old_block)}')
text = text.replace(old_block, new_block, 1)
text = text.replace('The two right-hand paths are schematic responsibility relationships, not a prescribed execution topology.', 'The two vertical columns are schematic responsibility relationships, not prescribed execution topologies.', 1)
old = '''The two models must sit inside an explicit transparent `ROW_ORTHO` subgraph with `direction LR`; the capability side must use two horizontal rows (`CAP_TOP`, `CAP_BOTTOM`) rather than a railpoint chain. Ordering is a reading aid, not an execution pipeline or one-to-one mapping, and CI must reject loss of this layout structure.'''
new = '''The two models must sit inside an explicit transparent `ROW_ORTHO` subgraph with `direction LR`. The capability side must be one vertical `direction TB` stack ordered Controllers → Sensors → Constraints → Actuators. Adjacent capability-family blocks must be connected with plain non-directional Mermaid links (`---`), never arrows, to show that the four functions belong to one control architecture without implying execution order. The vertical ordering is a reading aid, not a pipeline or one-to-one mapping, and CI must reject loss of this layout structure or reintroduction of directional capability links.'''
if text.count(old) != 1:
    raise SystemExit(f'blueprint: orthogonal contract match count {text.count(old)}')
text = text.replace(old, new, 1)
bp.write_text(text, encoding='utf-8')

# Update permanent layout regression test contract.
t = ROOT / 'quartz/scripts/research-diagram-layout.test.mjs'
text = t.read_text(encoding='utf-8')
text = text.replace('assert.match(m,/A2 ~~~ J1/);', 'assert.match(m,/A1 --> A2 --> A3/);assert.match(m,/B1 --> B2 --> J1 --> B4 --> B3/);assert.match(m,/A2 ~~~ J1/);')
old = 'assert.match(m,/subgraph CAP_TOP\\[" "\\][\\s\\S]*direction LR/);assert.match(m,/subgraph CAP_BOTTOM\\[" "\\][\\s\\S]*direction LR/);'
new = 'assert.match(m,/subgraph F\\["Capability functions — one control architecture, not a sequence"\\][\\s\\S]*direction TB/);assert.match(m,/C\\["Controllers \/ decision functions[\\s\\S]*S\\["Sensors and evidence[\\s\\S]*K\\["Constraints and realizations[\\s\\S]*A\\["Actuators and corrective action/);assert.match(m,/C --- S --- K --- A/);assert.doesNotMatch(m,/C\s*-->|S\s*-->|K\s*-->/);'
if old not in text:
    raise SystemExit('layout test: old capability contract not found')
text = text.replace(old, new, 1)
text = text.replace('assert.doesNotMatch(m,/classDef railpoint|\\bJ2\\b|\\bJ3\\b|\\bJ4\\b/);', 'assert.doesNotMatch(m,/classDef railpoint|\\bJ2\\b|\\bJ3\\b|\\bJ4\\b|CAP_TOP|CAP_BOTTOM/);')
text = text.replace('assert.match(bp,/`ROW_ORTHO` subgraph with `direction LR`/);assert.match(bp,/two horizontal rows \\(`CAP_TOP`, `CAP_BOTTOM`\\)/);', 'assert.match(bp,/`ROW_ORTHO` subgraph with `direction LR`/);assert.match(bp,/Controllers → Sensors → Constraints → Actuators/);assert.match(bp,/plain non-directional Mermaid links \\(`---`\\)/);')
t.write_text(text, encoding='utf-8')

# Keep the publication Figure 8 static renderer aligned with the same vertical control-family contract.
p8 = ROOT / 'quartz/scripts/publication-figure8.mjs'
text = p8.read_text(encoding='utf-8')
start = text.index('function capabilityBox(y, title, subtitle) {')
end = text.index('\n\nexport function buildFigure8RenditionAssets()', start)
replacement = '''function capabilityBox(y, title, subtitle) {
  return `${box(175, y, 650, 105, { fill: "#e8f5e9", stroke: "#2e7d32" })}${textBlock(500, y + 34, [title], { size: 22, weight: 700, fill: "#1b5e20" })}${textBlock(500, y + 65, [subtitle], { size: 17, fill: "#2d5d39" })}`;
}

export function buildFigure8CapabilitySvg() {
  const connector = (y1, y2) => `<line x1="500" y1="${y1}" x2="500" y2="${y2}" stroke="#4f8a5b" stroke-width="3"/>`;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 870" style="width:100%;height:auto;max-width:none">
${textBlock(500, 45, ["Capability functions — one control architecture, not a sequence"], { size: 25, weight: 700, fill: "#1d4327" })}
${capabilityBox(105, "Controllers / decision functions", "interpret evidence and select bounded response")}
${connector(210, 250)}
${capabilityBox(250, "Sensors and evidence", "observe behavior, conditions, and control state")}
${connector(355, 395)}
${capabilityBox(395, "Constraints and realizations", "define and operationalize boundaries")}
${connector(500, 540)}
${capabilityBox(540, "Actuators and corrective action", "execute authorized change")}
${textBlock(500, 710, ["Non-directional lines show one control architecture; they do not encode execution order."], { size: 17, weight: 700, fill: "#1b5e20" })}
${textBlock(500, 750, ["All four capability families may appear at every decision horizon."], { size: 18, weight: 700, fill: "#1b5e20" })}
${textBlock(500, 790, ["Decision horizons answer where a decision is owned; capability families answer how control becomes operational."], { size: 16, fill: "#365f40" })}
${textBlock(500, 825, ["There is no one-to-one mapping. The vertical ordering is a reading aid, not an execution pipeline."], { size: 16, weight: 600, fill: "#365f40" })}
</svg>`;
}'''
text = text[:start] + replacement + text[end:]
# Semantic marker title tracks new wording.
text = text.replace('"Capability functions — how control becomes operational",', '"Capability functions — one control architecture, not a sequence",', 1)
p8.write_text(text, encoding='utf-8')

print('Applied PR #101 vertical diagram layout contract.')
