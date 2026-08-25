#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

IMAGE = '![Figure 3 — The controlled-object shift for the motivating class](../assets/thinking-systems-figure-3.svg)\n\n<!-- Figure 3 editable semantic source: ../assets/thinking-systems-figure-3.mmd -->'


def switch_md(rel: str):
    p = ROOT / rel
    text = p.read_text(encoding='utf-8')
    rx = re.compile(r'```mermaid\n(?:(?!```)[\s\S])*?\n```\n\n(?=\*\*Figure 3 —[^\n]*controlled-object shift)')
    matches = list(rx.finditer(text))
    if len(matches) != 1:
        raise SystemExit(f'{rel}: expected one Figure 3 Mermaid block, got {len(matches)}')
    text = rx.sub(IMAGE + '\n\n', text, count=1)
    p.write_text(text, encoding='utf-8')

for rel in (
    'content/research/notes/open-engineering-specification-article-draft.md',
    'content/research/notes/thinking-systems-publication-draft.md',
):
    switch_md(rel)

# Blueprint: visible rendition is now a committed SVG, with Mermaid kept as editable semantic source.
bp = ROOT / 'content/research/notes/open-engineering-specification-article-blueprint.md'
text = bp.read_text(encoding='utf-8')
start = text.find('Use the Figure 3 Mermaid source topology from publication-review commit')
if start < 0:
    raise SystemExit('Figure 3 blueprint contract start not found')
end = text.find('\n\n```text', start)
if end < 0:
    raise SystemExit('Figure 3 blueprint contract end not found')
contract = (
    'Figure 3 uses a **versioned deterministic SVG as the visible Markdown and publication rendition**: '
    '`content/research/assets/thinking-systems-figure-3.svg`. Both the long-form manuscript and the standalone publication adaptation must reference that same asset, so GitHub Markdown and the PDF cannot silently diverge in geometry. '
    'The editable semantic source remains `content/research/assets/thinking-systems-figure-3.mmd`, preserving the Figure 3 topology from publication-review commit `b6e309e3b0dabb1415f58d13a7e0a52181a37c61` / **Visual Review v3** with terminology updated to the current paper vocabulary. '
    'The SVG is the reviewed visual contract: Explicitly Authored Software is the left top-down panel; the motivating runtime-judgment class is the right top-down panel; the Judgment Node is highlighted only on the right. '
    '`quartz/scripts/publication-figure3.mjs` must preserve the same geometry when the PDF pipeline inlines the figure. Any semantic change requires updating the `.mmd`, SVG, renderer guard, and both paper references together; any geometry change requires explicit visual review. '
    'Do not return Figure 3 to inline Mermaid in the paper surfaces unless GitHub can be shown to preserve the reviewed side-by-side geometry reliably.'
)
text = text[:start] + contract + text[end:]
bp.write_text(text, encoding='utf-8')

# Publication pipeline: locate the committed Markdown SVG reference and inline the reviewed deterministic SVG for PDF.
pr = ROOT / 'quartz/scripts/publication-rendition.mjs'
text = pr.read_text(encoding='utf-8')
s = text.index('export function locateCanonicalFigure3(content) {')
e = text.index('\nexport function assertCurrentArticleFigure3Rendition', s)
replacement = r'''export function locateCanonicalFigure3(content) {
  const pattern = /!\[Figure 3 — The controlled-object shift for the motivating class\]\(\.\.\/assets\/thinking-systems-figure-3\.svg\)\r?\n(?:\r?\n<!-- Figure 3 editable semantic source: \.\.\/assets\/thinking-systems-figure-3\.mmd -->)?\r?\n\r?\n(\*\*Figure 3 —[^\n]*)(?=\n\n|$)/;
  const match = pattern.exec(content);
  if (!match) return null;
  const captionStart = match.index + match[0].lastIndexOf(match[1]);
  return {
    start: match.index,
    end: captionStart + match[1].length,
    caption: match[1],
  };
}

export function renderFigure3(content) {
  const located = locateCanonicalFigure3(content);
  if (!located) return { content, rendered: false };
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
text = text[:s] + replacement + text[e:]
pr.write_text(text, encoding='utf-8')

# Permanent regression guard: papers reference one SVG; editable source remains pinned; Figure 8/9 guard is unchanged.
test = ROOT / 'quartz/scripts/research-diagram-layout.test.mjs'
test.write_text(r'''import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
const root=path.resolve(fileURLToPath(new URL("../..",import.meta.url)));
const pub=readFileSync(path.join(root,"content/research/notes/thinking-systems-publication-draft.md"),"utf8");
const man=readFileSync(path.join(root,"content/research/notes/open-engineering-specification-article-draft.md"),"utf8");
const bp=readFileSync(path.join(root,"content/research/notes/open-engineering-specification-article-blueprint.md"),"utf8");
const f3src=readFileSync(path.join(root,"content/research/assets/thinking-systems-figure-3.mmd"),"utf8");
const f3svg=readFileSync(path.join(root,"content/research/assets/thinking-systems-figure-3.svg"),"utf8");
function fig(src,n,title=""){const re=new RegExp("```mermaid\\n((?:(?!```)[\\s\\S])*?)\\n```\\n\\n\\*\\*Figure "+n+" —([^\\n]+)","g");const ms=[...src.matchAll(re)].filter(m=>!title||m[2].includes(title));assert.equal(ms.length,1);return ms[0][1];}
function visibleF3(src){assert.match(src,/!\[Figure 3 — The controlled-object shift for the motivating class\]\(\.\.\/assets\/thinking-systems-figure-3\.svg\)/);assert.match(src,/Figure 3 editable semantic source: \.\.\/assets\/thinking-systems-figure-3\.mmd/);assert.doesNotMatch(src,/```mermaid\n(?:(?!```)[\s\S])*?\n```\n\n\*\*Figure 3 —[^\n]*controlled-object shift/);}
function sourceF3(){assert.match(f3src,/^flowchart LR/m);assert.match(f3src,/subgraph A\["Explicitly Authored Software"\][\s\S]*direction TB/);assert.match(f3src,/subgraph B\["Motivating runtime-judgment class"\][\s\S]*direction TB/);assert.match(f3src,/A1 --> A2 --> A3/);assert.match(f3src,/B1 --> B2 --> B3/);assert.match(f3src,/B1 --> J1 --> B3/);assert.match(f3src,/A2 ~~~ J1/);assert.doesNotMatch(f3src,/ROW3|^block$|columns 2|B1 --> B2 --> J1/);assert.match(f3svg,/viewBox="0 0 1400 690"/);assert.match(f3svg,/Explicitly Authored Software/);assert.match(f3svg,/Motivating runtime-judgment class/);assert.match(f3svg,/x="24" y="62" width="660"/);assert.match(f3svg,/x="716" y="62" width="660"/);}
function ortho(src,n){const m=fig(src,n,"Two orthogonal models");assert.match(m,/^flowchart TB/m);assert.match(m,/subgraph ROW_ORTHO\[" "\][\s\S]*direction LR/);assert.match(m,/subgraph L\["Decision ownership/);assert.match(m,/subgraph F\["Capability functions/);assert.match(m,/subgraph F\["Capability functions — one control architecture, not a sequence"\][\s\S]*direction TB/);assert.match(m,/C\["Controllers \/ decision functions[\s\S]*S\["Sensors and evidence[\s\S]*K\["Constraints and realizations[\s\S]*A\["Actuators and corrective action/);assert.match(m,/C --- S --- K --- A/);assert.doesNotMatch(m,/C\s*-->|S\s*-->|K\s*-->/);assert.match(m,/initial admissibility \+ assessment eligibility/);assert.match(m,/specific Bounded Research Authorization/);assert.match(m,/Business Authorization or changed basis/);assert.match(m,/applicable Project Authorization scope \/ set/);assert.match(m,/research-only and\/or production-capable/);assert.match(m,/realization \/ experiment evidence/);assert.match(m,/risk \/ feasibility \/ Model Judgment necessity/);assert.match(m,/Exogenous Organizational change/);assert.doesNotMatch(m,/classDef railpoint|\bJ2\b|\bJ3\b|\bJ4\b|CAP_TOP|CAP_BOTTOM/);}
test("Figure 3 papers use one deterministic SVG rendition",()=>{visibleF3(pub);visibleF3(man);sourceF3();});
test("orthogonal model stays as two side-by-side panels",()=>{ortho(pub,8);ortho(man,9);});
test("blueprint owns the structural layout contract",()=>{assert.match(bp,/versioned deterministic SVG as the visible Markdown and publication rendition/);assert.match(bp,/thinking-systems-figure-3\.mmd/);assert.match(bp,/Visual Review v3/);assert.match(bp,/geometry change requires explicit visual review/);assert.match(bp,/`ROW_ORTHO` subgraph with `direction LR`/);assert.match(bp,/Controllers → Sensors → Constraints → Actuators/);assert.match(bp,/plain non-directional Mermaid links \(`---`\)/);});
''',encoding='utf-8')

# Publication Figure 3 tests: visible source is the Markdown SVG; semantic source is tested separately.
pft = ROOT / 'quartz/scripts/publication-figure3.test.mjs'
pft.write_text(r'''import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import { assertFigure3SemanticSource, buildFigure3ControlledObjectSvg } from "./publication-figure3.mjs";
import { assertCurrentArticleFigure3Rendition, renderFigure3 } from "./publication-rendition.mjs";
const root=path.resolve(fileURLToPath(new URL("../..",import.meta.url)));
const semanticSource=readFileSync(path.join(root,"content/research/assets/thinking-systems-figure-3.mmd"),"utf8");
const canonicalFigure3 = `![Figure 3 — The controlled-object shift for the motivating class](../assets/thinking-systems-figure-3.svg)\n\n<!-- Figure 3 editable semantic source: ../assets/thinking-systems-figure-3.mmd -->\n\n**Figure 3 — The controlled-object shift for the motivating class.** Canonical caption.`;
test("Figure 3 publication rendition is a side-by-side motivating-class comparison",()=>{const result=renderFigure3(canonicalFigure3);assert.equal(result.rendered,true);assert.match(result.content,/data-ua-figure3-rendition="side-by-side"/);assert.match(result.content,/data-ua-flow="top-down"/);assert.match(result.content,/Explicitly Authored Software/);assert.match(result.content,/Motivating runtime-judgment class/);assert.doesNotMatch(result.content,/thinking-systems-figure-3\.svg/);assert.match(result.content,/<strong>Figure 3 — The controlled-object shift for the motivating class\.<\/strong>/);});
test("Figure 3 semantic source and deterministic SVG stay coupled",()=>{assert.doesNotThrow(()=>assertFigure3SemanticSource(semanticSource));const svg=buildFigure3ControlledObjectSvg();assert.match(svg,/Explicitly Authored Software/);assert.match(svg,/Motivating runtime-judgment class/);assert.throws(()=>assertFigure3SemanticSource(semanticSource.replace("probabilistic Model Judgment","removed")),/publication comparison requires review/);});
test("current article Figure 3 acceptance preserves one canonical and one rendered figure",()=>{const rendition={figure3Rendition:true,canonicalFigures:[{number:3,panel:null,title:"The controlled-object shift"}],renditionFigures:[{number:3,panel:null,title:"The controlled-object shift"}]};assert.doesNotThrow(()=>assertCurrentArticleFigure3Rendition(rendition));assert.throws(()=>assertCurrentArticleFigure3Rendition({...rendition,figure3Rendition:false}),/side-by-side Figure 3 rendition/);});
''',encoding='utf-8')

print('Switched Figure 3 paper surfaces to deterministic SVG and synchronized publishing guards.')
