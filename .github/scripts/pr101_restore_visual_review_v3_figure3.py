#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

FIG3 = '''flowchart LR
    subgraph A["Explicitly Authored Software"]
        direction TB
        A1["Situation and operating conditions"]
        A2["Explicitly authored consequential<br/>responsibilities"]
        A3["Consequential output, action,<br/>or downstream state"]
        A1 --> A2 --> A3
    end

    subgraph B["Motivating runtime-judgment class"]
        direction TB
        B1["Situation and operating conditions"]
        B2["Explicitly authored responsibilities<br/>before, between, and after Judgment Nodes"]
        J1["One or more Judgment Nodes<br/>probabilistic Model Judgment"]
        B3["Consequential output, action,<br/>or downstream state"]
        B1 --> B2 --> B3
        B1 --> J1 --> B3
    end

    A2 ~~~ J1

    classDef judgment fill:#ffcdd2,stroke:#b71c1c,stroke-width:3px,color:#6a0000;
    class J1 judgment;'''


def replace_figure3(path: str):
    p = ROOT / path
    text = p.read_text(encoding="utf-8")
    rx = re.compile(
        r"```mermaid\n(?P<body>(?:(?!```)[\s\S])*?)\n```\n\n(?P<caption>\*\*Figure 3 —[^\n]*controlled-object shift[^\n]*)"
    )
    matches = list(rx.finditer(text))
    if len(matches) != 1:
        raise SystemExit(f"{path}: expected one Figure 3, got {len(matches)}")
    m = matches[0]
    p.write_text(text[:m.start("body")] + FIG3 + text[m.end("body"):], encoding="utf-8")


for rel in (
    "content/research/notes/open-engineering-specification-article-draft.md",
    "content/research/notes/thinking-systems-publication-draft.md",
):
    replace_figure3(rel)

# Blueprint: anchor Figure 3 to the source snapshot behind Visual Review v3.
bp = ROOT / "content/research/notes/open-engineering-specification-article-blueprint.md"
text = bp.read_text(encoding="utf-8")
start = "Use two vertical top-to-bottom responsibility diagrams placed side by side."
pos = text.find(start)
if pos < 0:
    # Current branch may already start with a previous Figure 3 layout contract.
    candidates = [
        "Use the Figure 3 Mermaid source topology from publication-review commit",
        "Use two vertical top-to-bottom responsibility diagrams placed side by side.",
    ]
    for candidate in candidates:
        pos = text.find(candidate)
        if pos >= 0:
            break
if pos < 0:
    raise SystemExit("blueprint Figure 3 contract start not found")
end = text.find("\n\n```text", pos)
if end < 0:
    raise SystemExit("blueprint Figure 3 contract end not found")
contract = (
    "Use the Figure 3 Mermaid source topology from publication-review commit `b6e309e3b0dabb1415f58d13a7e0a52181a37c61`, "
    "the source snapshot behind **Visual Review v3**. Preserve that topology rather than attempting new Mermaid layout strategies: "
    "top-level `flowchart LR`; two subgraphs; each declares `direction TB`; the left authored path is `A1 --> A2 --> A3`; "
    "the right side preserves the parallel authored and judgment paths `B1 --> B2 --> B3` and `B1 --> J1 --> B3`; and `A2 ~~~ J1` is retained as the historical alignment link. "
    "Only terminology labels may be updated to the current paper vocabulary (`Explicitly Authored Software` and `Motivating runtime-judgment class`) without changing this topology. "
    "For publication/PDF, `quartz/scripts/publication-figure3.mjs` is the reviewed deterministic rendition contract: it must continue to render two side-by-side panels with top-down internal flows, matching the geometry accepted in Visual Review v3. "
    "Do not replace this source with `ROW3`, Mermaid Block Diagram syntax, a five-node single-path rewrite, or another layout experiment without a new explicit visual review."
)
text = text[:pos] + contract + text[end:]
bp.write_text(text, encoding="utf-8")

# Permanent source/layout guard.
test = ROOT / "quartz/scripts/research-diagram-layout.test.mjs"
text = test.read_text(encoding="utf-8")
s = text.index("function f3(src){")
e = text.index("\nfunction ortho", s)
f3 = 'function f3(src){const m=fig(src,3,"controlled-object shift");assert.match(m,/^flowchart LR/m);assert.match(m,/subgraph A\\["Explicitly Authored Software"\\][\\s\\S]*direction TB/);assert.match(m,/subgraph B\\["Motivating runtime-judgment class"\\][\\s\\S]*direction TB/);assert.match(m,/A1 --> A2 --> A3/);assert.match(m,/B1 --> B2 --> B3/);assert.match(m,/B1 --> J1 --> B3/);assert.match(m,/A2 ~~~ J1/);assert.doesNotMatch(m,/ROW3|^block$|columns 2|B1 --> B2 --> J1/);}'
text = text[:s] + f3 + text[e:]
old = re.compile(r'test\("blueprint owns the structural layout contract",\(\)=>\{[^\n]*\}\);')
new = 'test("blueprint owns the structural layout contract",()=>{assert.match(bp,/publication-review commit `b6e309e3b0dabb1415f58d13a7e0a52181a37c61`/);assert.match(bp,/Visual Review v3/);assert.match(bp,/`A2 ~~~ J1`/);assert.match(bp,/reviewed deterministic rendition contract/);assert.match(bp,/`ROW_ORTHO` subgraph with `direction LR`/);assert.match(bp,/Controllers → Sensors → Constraints → Actuators/);assert.match(bp,/plain non-directional Mermaid links \\(`---`\\)/);});'
text, count = old.subn(new, text, count=1)
if count != 1:
    raise SystemExit("blueprint layout-test assertion not replaced")
test.write_text(text, encoding="utf-8")

# Align publication renderer semantic guard to the restored canonical source.
pf3 = ROOT / "quartz/scripts/publication-figure3.mjs"
text = pf3.read_text(encoding="utf-8")
markers_rx = re.compile(r'export const figure3SemanticMarkers = Object\.freeze\(\[[\s\S]*?\]\);')
markers = '''export const figure3SemanticMarkers = Object.freeze([
  "Explicitly Authored Software",
  "Motivating runtime-judgment class",
  "Situation and operating conditions",
  "Explicitly authored consequential",
  "before, between, and after Judgment Nodes",
  "One or more Judgment Nodes",
  "probabilistic Model Judgment",
  "Consequential output, action",
]);'''
text, count = markers_rx.subn(markers, text, count=1)
if count != 1:
    raise SystemExit("publication Figure 3 semantic markers not replaced")
pf3.write_text(text, encoding="utf-8")

# Keep the publication Figure 3 unit fixture on the same restored source topology.
pft = ROOT / "quartz/scripts/publication-figure3.test.mjs"
text = pft.read_text(encoding="utf-8")
fixture_rx = re.compile(r'const canonicalFigure3 = `\\`\\`\\`mermaid[\s\S]*?Canonical caption\.`;')
fixture = '''const canonicalFigure3 = `\\`\\`\\`mermaid
flowchart LR
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
        B2["Explicitly authored responsibilities before, between, and after Judgment Nodes"]
        J1["One or more Judgment Nodes probabilistic Model Judgment"]
        B3["Consequential output, action, or downstream state"]
        B1 --> B2 --> B3
        B1 --> J1 --> B3
    end
    A2 ~~~ J1
\\`\\`\\`

**Figure 3 — The controlled-object shift for the motivating class.** Canonical caption.`;'''
text, count = fixture_rx.subn(fixture, text, count=1)
if count != 1:
    raise SystemExit("publication Figure 3 unit fixture not replaced")
pft.write_text(text, encoding="utf-8")

print("Restored Figure 3 Mermaid topology from Visual Review v3 source snapshot and synchronized guards.")
