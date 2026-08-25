#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

FIG3 = '''```mermaid
flowchart TB
    subgraph ROW3[" "]
        direction LR
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
    end
    A -. "responsibility-structure comparison" .- B
    classDef judgment fill:#ffcdd2,stroke:#b71c1c,stroke-width:3px,color:#6a0000;
    class J1 judgment;
    style ROW3 fill:transparent,stroke:transparent
```'''

for rel in (
    'content/research/notes/open-engineering-specification-article-draft.md',
    'content/research/notes/thinking-systems-publication-draft.md',
):
    p = ROOT / rel
    text = p.read_text(encoding='utf-8')
    rx = re.compile(
        r'!\[Figure 3 — The controlled-object shift for the motivating class\]\(\.\.\/assets\/thinking-systems-figure-3\.svg\)\n\n'
        r'<!-- Figure 3 editable semantic source: \.\.\/assets\/thinking-systems-figure-3\.mmd -->'
    )
    if len(rx.findall(text)) != 1:
        raise SystemExit(f'{rel}: expected one SVG Figure 3 representation')
    p.write_text(rx.sub(FIG3, text, count=1), encoding='utf-8')

# Blueprint: use the same proven structural device as Figure 8.
bp = ROOT / 'content/research/notes/open-engineering-specification-article-blueprint.md'
text = bp.read_text(encoding='utf-8')
start = text.find('Figure 3 uses a **versioned deterministic SVG as the visible Markdown and publication rendition**')
if start < 0:
    # tolerate an earlier pre-SVG contract if a concurrent cleanup changed it
    for marker in (
        'Use the Figure 3 Mermaid source topology from publication-review commit',
        'Use two vertical top-to-bottom responsibility diagrams placed side by side.',
    ):
        start = text.find(marker)
        if start >= 0:
            break
if start < 0:
    raise SystemExit('Figure 3 blueprint contract start not found')
end = text.find('\n\n```text', start)
if end < 0:
    raise SystemExit('Figure 3 blueprint contract end not found')
contract = (
    'Figure 3 uses the **same Mermaid panel-layout pattern already proven by Figure 8/9** rather than relying on disconnected subgraphs or cross-links between internal nodes. '
    'The canonical paper source is inline Mermaid in both the long-form manuscript and standalone publication adaptation: top-level `flowchart TB`; an outer transparent `ROW3` subgraph with `direction LR`; inside it, left subgraph `A` (`Explicitly Authored Software`) and right subgraph `B` (`Motivating runtime-judgment class`), each with `direction TB`; and a non-semantic dashed relation between the **subgraphs themselves** (`A -. "responsibility-structure comparison" .- B`) to make the two panels participate in one LR row. '
    'The left internal responsibility chain is `A1 --> A2 --> A3`. The right side preserves parallel authored and judgment paths `B1 --> B2 --> B3` and `B1 --> J1 --> B3`. Do **not** add alignment or comparison links between internal nodes of the two panels (for example `A2 ~~~ J1`), because such links can override the local TB directions in GitHub Mermaid. '
    '`ROW3` is layout-only and visually transparent. The panel-to-panel dashed relation is a visual comparison relationship, not an execution or control edge. '
    'For PDF publication, `quartz/scripts/publication-figure3.mjs` remains the deterministic reviewed rendition contract and may replace this canonical Mermaid at export time, but Markdown must contain only the inline Mermaid representation, not an additional reader-facing SVG. '
    'Any future change to Figure 3 must preserve the two side-by-side panels and top-down internal flows or receive explicit visual review.'
)
bp.write_text(text[:start] + contract + text[end:], encoding='utf-8')

# Publication pipeline: recognize the canonical inline Mermaid again and use the deterministic renderer only for PDF.
pr = ROOT / 'quartz/scripts/publication-rendition.mjs'
text = pr.read_text(encoding='utf-8')
s = text.index('export function locateCanonicalFigure3(content) {')
e = text.index('\nexport function assertCurrentArticleFigure3Rendition', s)
replacement = r'''export function locateCanonicalFigure3(content) {
  const blockPattern = /```mermaid\r?\n([\s\S]*?)\r?\n```/g;
  let match;
  while ((match = blockPattern.exec(content)) !== null) {
    const mermaid = match[1];
    if (
      !mermaid.includes('subgraph ROW3[" "]') ||
      !mermaid.includes('subgraph A["Explicitly Authored Software"]') ||
      !mermaid.includes('subgraph B["Motivating runtime-judgment class"]')
    ) {
      continue;
    }
    const tail = content.slice(blockPattern.lastIndex);
    const captionMatch = /^\s*(\*\*Figure 3 —[^\n]*)(?=\n\n|$)/.exec(tail);
    if (!captionMatch) return null;
    const captionStart = blockPattern.lastIndex + captionMatch.index + captionMatch[0].indexOf(captionMatch[1]);
    return {
      start: match.index,
      end: captionStart + captionMatch[1].length,
      mermaid,
      caption: captionMatch[1],
    };
  }
  return null;
}

export function renderFigure3(content) {
  const located = locateCanonicalFigure3(content);
  if (!located) return { content, rendered: false };
  assertFigure3SemanticSource(located.mermaid);
  const svg = compactInlineSvg(buildFigure3ControlledObjectSvg());
  const caption = located.caption.replace(
    /^\*\*(Figure 3 — ?.*?\.)\*\*/,
    "<strong>$1</strong>",
  );
  const panel = `<section class="ua-pdf-static-figure ua-pdf-static-figure--3" data-ua-figure3-rendition="side-by-side">
${svg}
<p>${caption}</p>
</section>`;
  return {
    content: `${content.slice(0, located.start)}${panel}${content.slice(located.end)}`,
    rendered: true,
  };
}
'''
pr.write_text(text[:s] + replacement + text[e:], encoding='utf-8')

# Remove now-redundant workaround assets. publication-figure3.mjs is the PDF rendition source.
for rel in (
    'content/research/assets/thinking-systems-figure-3.svg',
    'content/research/assets/thinking-systems-figure-3.mmd',
):
    p = ROOT / rel
    if p.exists():
        p.unlink()

print('Figure 3 now uses the same outer-row/subgraph layout pattern as Figure 8; SVG workaround removed.')
