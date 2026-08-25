#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUB = ROOT / "content/research/notes/thinking-systems-publication-draft.md"
MAN = ROOT / "content/research/notes/open-engineering-specification-article-draft.md"
BP = ROOT / "content/research/notes/open-engineering-specification-article-blueprint.md"
FP = ROOT / "quartz/scripts/publication-figure8-fingerprint.mjs"
F3 = ROOT / "quartz/scripts/publication-figure3.mjs"
REN = ROOT / "quartz/scripts/publication-rendition.mjs"
F3TEST = ROOT / "quartz/scripts/publication-figure3.test.mjs"
LAYOUT_TEST = ROOT / "quartz/scripts/research-diagram-layout.test.mjs"

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
            B2["Explicitly authored responsibilities<br/>before, between, and after Judgment Nodes"]
            J1["One or more Judgment Nodes<br/>probabilistic Model Judgment"]
            B3["Consequential output, action,<br/>or downstream state"]
            B1 --> B2 --> B3
            B1 --> J1 --> B3
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
            X["Exogenous Organizational change"] --> O
            O["Organization<br/>assessment eligibility · authoritative / business basis"]
            O -->|initial assessment eligibility| P
            P["Project / Architecture<br/>technical selection · category · feasibility · economics"]
            P --> CAT{"Selected design still<br/>a Thinking System?"}
            CAT -->|No| EXIT["Exit Thinking-System-specific lifecycle"]
            CAT -->|Yes| PA["Applicable Project Authorization<br/>research-only and/or production-capable"]
            P -->|reserved-boundary research<br/>or changed basis| O
            PA --> D["Delivery<br/>realization + release decision"]
            D --> R["Runtime<br/>authorized operation"]
            D -->|realization evidence| E["Reassessment evidence"]
            R -->|operation evidence| E
            E -->|local realization / evidence basis| D
            E -->|technical / viability basis| P
            E -->|authority / business basis| O
        end
        subgraph F["Capability functions — how control becomes operational"]
            direction TB
            subgraph CAP_TOP[" "]
                direction LR
                A["Actuators<br/>execute authorized change"]
                K["Constraints and realizations<br/>define and operationalize boundaries"]
            end
            subgraph CAP_BOTTOM[" "]
                direction LR
                S["Sensors and evidence<br/>observe behavior, conditions, and control state"]
                C["Controllers / decision functions<br/>interpret evidence and select bounded response"]
            end
        end
    end
    L -. "orthogonal: all four capability families may appear at every decision horizon" .- F
    classDef capability fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20;
    class A,K,S,C capability;
    style ROW_ORTHO fill:transparent,stroke:transparent
    style CAP_TOP fill:transparent,stroke:transparent
    style CAP_BOTTOM fill:transparent,stroke:transparent'''

BLOCK = re.compile(r"```mermaid\n(?P<body>(?:(?!```)[\s\S])*?)\n```")

def find_figure(text: str, number: int, title: str = ""):
    found = []
    for m in BLOCK.finditer(text):
        tail = text[m.end():]
        cap = re.match(rf"\n\n(?P<caption>\*\*Figure {number} —[^\n]+)", tail)
        if cap and (not title or title in cap.group("caption")):
            found.append((m, cap.group("caption")))
    if len(found) != 1:
        raise SystemExit(f"expected one bounded Figure {number} block matching {title!r}; got {len(found)}")
    return found[0]

def replace_figure(path: Path, number: int, replacement: str, title: str = ""):
    text = path.read_text(encoding="utf-8")
    (m, _) = find_figure(text, number, title)
    path.write_text(text[:m.start("body")] + replacement + text[m.end("body"):], encoding="utf-8")

def replace_once(path: Path, old: str, new: str):
    text = path.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise SystemExit(f"{path}: expected one exact replacement anchor")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")

replace_figure(PUB, 3, FIG3, "controlled-object shift")
replace_figure(MAN, 3, FIG3, "controlled-object shift")
replace_figure(PUB, 8, ORTHO, "Two orthogonal models")
replace_figure(MAN, 9, ORTHO, "Two orthogonal models")

replace_once(BP,
"Because disconnected Mermaid subgraphs may otherwise stack vertically, use an invisible alignment link between the columns to force the side-by-side GitHub rendering.",
"Do not rely on a top-level `flowchart LR` or an invisible alignment link alone. Use an explicit transparent outer row subgraph `ROW3` with `direction LR`; place the explicitly authored and motivating-class columns inside it as separate subgraphs with `direction TB`. An invisible cross-column alignment edge may remain only as a secondary ordering aid. CI must reject Figure 3 when this structural layout contract disappears.")
replace_once(BP,
"Ordering is a reading aid, not an execution pipeline or one-to-one mapping.",
"The two models must sit inside an explicit transparent `ROW_ORTHO` subgraph with `direction LR`; the capability side must use two horizontal rows (`CAP_TOP`, `CAP_BOTTOM`) rather than a railpoint chain. Ordering is a reading aid, not an execution pipeline or one-to-one mapping, and CI must reject loss of this layout structure.")

replace_once(F3, '"Thinking System — changed responsibility structure",', '"Motivating class — changed responsibility structure",')
replace_once(F3, 'aria-label="Side-by-side top-down comparison of Linear Software and a Thinking System"', 'aria-label="Side-by-side top-down comparison of Explicitly Authored Software and the motivating runtime-judgment class"')
replace_once(F3, '["Linear Software"]', '["Explicitly Authored Software"]')
replace_once(F3, '["Thinking System"]', '["Motivating runtime-judgment class"]')
replace_once(F3, '["Model Judgment changes the responsibility structure at a bounded node;", "the surrounding system still contains explicitly authored responsibilities."]', '["Model Judgment leaves part of a consequential responsibility unresolved until operation;", "the surrounding system still contains explicitly authored responsibilities."]')
replace_once(REN, '!mermaid.includes("Thinking System — changed responsibility structure")', '!mermaid.includes("Motivating class — changed responsibility structure")')

s = F3TEST.read_text(encoding="utf-8")
for old,new in [
('subgraph B["Thinking System — changed responsibility structure"]','subgraph B["Motivating class — changed responsibility structure"]'),
('**Figure 3 — The controlled-object shift.** Canonical caption.','**Figure 3 — The controlled-object shift for the motivating class.** Canonical caption.'),
('side-by-side Linear Software comparison','side-by-side motivating-class comparison'),
('assert.match(result.content, /Linear Software/);','assert.match(result.content, /Explicitly Authored Software/);'),
('assert.match(result.content, /Thinking System/);','assert.match(result.content, /Motivating runtime-judgment class/);'),
('assert.match(svg, /Linear Software/);','assert.match(svg, /Explicitly Authored Software/);'),
('assert.match(svg, /Thinking System/);','assert.match(svg, /Motivating runtime-judgment class/);'),
('/<strong>Figure 3 — The controlled-object shift\\.<\\/strong>/','/<strong>Figure 3 — The controlled-object shift for the motivating class\\.<\\/strong>/')]:
    if old not in s: raise SystemExit(f"Figure3 test anchor missing: {old}")
    s=s.replace(old,new,1)
F3TEST.write_text(s, encoding="utf-8")

pub = PUB.read_text(encoding="utf-8")
m, caption = find_figure(pub, 8, "Two orthogonal models")
normalize=lambda v:"\n".join(line.rstrip() for line in v.replace("\r\n","\n").strip().split("\n"))
new_fp=hashlib.sha256(f"{normalize(m.group('body'))}\n\n{normalize(caption)}".encode()).hexdigest()
fp=FP.read_text(encoding="utf-8")
fp,n=re.subn(r'canonicalFigure8Fingerprint = "[0-9a-f]{64}"',f'canonicalFigure8Fingerprint = "{new_fp}"',fp,count=1)
if n!=1: raise SystemExit("Figure8 fingerprint anchor missing")
FP.write_text(fp,encoding="utf-8")

LAYOUT_TEST.write_text('''import assert from "node:assert/strict";\nimport { readFileSync } from "node:fs";\nimport path from "node:path";\nimport test from "node:test";\nimport { fileURLToPath } from "node:url";\nconst root=path.resolve(fileURLToPath(new URL("../..",import.meta.url)));\nconst pub=readFileSync(path.join(root,"content/research/notes/thinking-systems-publication-draft.md"),"utf8");\nconst man=readFileSync(path.join(root,"content/research/notes/open-engineering-specification-article-draft.md"),"utf8");\nconst bp=readFileSync(path.join(root,"content/research/notes/open-engineering-specification-article-blueprint.md"),"utf8");\nfunction fig(src,n,title=""){const re=new RegExp("```mermaid\\\\n((?:(?!```)[\\\\s\\\\S])*?)\\\\n```\\\\n\\\\n\\\\*\\\\*Figure "+n+" —([^\\\\n]+)","g");const ms=[...src.matchAll(re)].filter(m=>!title||m[2].includes(title));assert.equal(ms.length,1);return ms[0][1];}\nfunction f3(src){const m=fig(src,3,"controlled-object shift");assert.match(m,/^flowchart TB/m);assert.match(m,/subgraph ROW3\\[" "\\][\\s\\S]*direction LR/);assert.match(m,/subgraph A\\["Explicitly Authored Software[\\s\\S]*direction TB/);assert.match(m,/subgraph B\\["Motivating runtime-judgment class[\\s\\S]*direction TB/);assert.match(m,/A2 ~~~ J1/);}\nfunction ortho(src,n){const m=fig(src,n,"Two orthogonal models");assert.match(m,/^flowchart TB/m);assert.match(m,/subgraph ROW_ORTHO\\[" "\\][\\s\\S]*direction LR/);assert.match(m,/subgraph L\\["Decision ownership/);assert.match(m,/subgraph F\\["Capability functions/);assert.match(m,/subgraph CAP_TOP\\[" "\\][\\s\\S]*direction LR/);assert.match(m,/subgraph CAP_BOTTOM\\[" "\\][\\s\\S]*direction LR/);assert.doesNotMatch(m,/classDef railpoint|\\bJ2\\b|\\bJ3\\b|\\bJ4\\b/);}\ntest("Figure 3 stays as two top-down columns side by side",()=>{f3(pub);f3(man);});\ntest("orthogonal model stays as two side-by-side panels",()=>{ortho(pub,8);ortho(man,9);});\ntest("blueprint owns the structural layout contract",()=>{assert.match(bp,/outer row subgraph `ROW3` with `direction LR`/);assert.match(bp,/`ROW_ORTHO` subgraph with `direction LR`/);assert.match(bp,/two horizontal rows \\(`CAP_TOP`, `CAP_BOTTOM`\\)/);});\n''',encoding="utf-8")
print(new_fp)
