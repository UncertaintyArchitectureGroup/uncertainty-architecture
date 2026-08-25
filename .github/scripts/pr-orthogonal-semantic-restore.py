#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUB = ROOT / "content/research/notes/thinking-systems-publication-draft.md"
MAN = ROOT / "content/research/notes/open-engineering-specification-article-draft.md"
FP = ROOT / "quartz/scripts/publication-figure8-fingerprint.mjs"
TEST = ROOT / "quartz/scripts/research-diagram-layout.test.mjs"

OLD = '''flowchart TB
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

NEW = '''flowchart TB
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
        subgraph F["Capability functions — how control becomes operational"]
            direction TB
            subgraph CAP_TOP[" "]
                direction LR
                A["Actuators and corrective action<br/>execute authorized change"]
                K["Constraints and realizations<br/>define and operationalize boundaries"]
            end
            subgraph CAP_BOTTOM[" "]
                direction LR
                S["Sensors and evidence<br/>observe behavior, conditions, and control state"]
                C["Controllers / decision functions<br/>interpret evidence and select bounded response"]
            end
        end
    end
    L -. "all four capability families may appear at every decision horizon" .- F
    classDef capability fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20;
    class A,K,S,C capability;
    style ROW_ORTHO fill:transparent,stroke:transparent
    style CAP_TOP fill:transparent,stroke:transparent
    style CAP_BOTTOM fill:transparent,stroke:transparent'''

for path in (PUB, MAN):
    text = path.read_text(encoding="utf-8")
    if text.count(OLD) != 1:
        raise SystemExit(f"{path}: expected exactly one simplified orthogonal model")
    path.write_text(text.replace(OLD, NEW, 1), encoding="utf-8")

# Recompute the publication Figure 8 semantic fingerprint after restoring the full decision model.
pub = PUB.read_text(encoding="utf-8")
block = re.compile(r"```mermaid\n(?P<body>(?:(?!```)[\s\S])*?)\n```\n\n(?P<caption>\*\*Figure 8 — Two orthogonal models\.[^\n]*)")
match = block.search(pub)
if not match:
    raise SystemExit("publication Figure 8 not found")
normalize = lambda v: "\n".join(line.rstrip() for line in v.replace("\r\n", "\n").strip().split("\n"))
fingerprint = hashlib.sha256(f"{normalize(match.group('body'))}\n\n{normalize(match.group('caption'))}".encode()).hexdigest()
fp = FP.read_text(encoding="utf-8")
fp, count = re.subn(r'canonicalFigure8Fingerprint = "[0-9a-f]{64}"', f'canonicalFigure8Fingerprint = "{fingerprint}"', fp, count=1)
if count != 1:
    raise SystemExit("Figure 8 fingerprint anchor missing")
FP.write_text(fp, encoding="utf-8")

# Strengthen the layout test with the material decision/authorization edges preserved from the prior figure.
test = TEST.read_text(encoding="utf-8")
anchor = 'assert.match(m,/subgraph CAP_BOTTOM\\[" "\\][\\s\\S]*direction LR/);assert.doesNotMatch(m,/classDef railpoint|\\bJ2\\b|\\bJ3\\b|\\bJ4\\b/);'
replacement = 'assert.match(m,/subgraph CAP_BOTTOM\\[" "\\][\\s\\S]*direction LR/);assert.match(m,/initial admissibility \\+ assessment eligibility/);assert.match(m,/specific Bounded Research Authorization/);assert.match(m,/Business Authorization or changed basis/);assert.match(m,/applicable Project Authorization scope \\/ set/);assert.match(m,/research-only and\\/or production-capable/);assert.match(m,/realization \\/ experiment evidence/);assert.match(m,/risk \\/ feasibility \\/ Model Judgment necessity/);assert.match(m,/Exogenous Organizational change/);assert.doesNotMatch(m,/classDef railpoint|\\bJ2\\b|\\bJ3\\b|\\bJ4\\b/);'
if test.count(anchor) != 1:
    raise SystemExit("layout test orthogonal anchor missing")
TEST.write_text(test.replace(anchor, replacement, 1), encoding="utf-8")

print(fingerprint)
