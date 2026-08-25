import assert from "node:assert/strict";
import test from "node:test";

import {
  assertFigure3SemanticSource,
  buildFigure3ControlledObjectSvg,
} from "./publication-figure3.mjs";
import {
  assertCurrentArticleFigure3Rendition,
  renderFigure3,
} from "./publication-rendition.mjs";

const canonicalFigure3 = `\`\`\`mermaid
flowchart TB
    subgraph ROW3[" "]
        direction LR
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
    end
    A -. "responsibility-structure comparison" .- B
    style ROW3 fill:transparent,stroke:transparent
\`\`\`

**Figure 3 — The controlled-object shift for the motivating class.** Canonical caption.`;

test("Figure 3 publication rendition is a side-by-side motivating-class comparison", () => {
  const result = renderFigure3(canonicalFigure3);
  assert.equal(result.rendered, true);
  assert.match(result.content, /data-ua-figure3-rendition="side-by-side"/);
  assert.match(result.content, /data-ua-flow="top-down"/);
  assert.match(result.content, /Explicitly Authored Software/);
  assert.match(result.content, /Motivating runtime-judgment class/);
  assert.match(result.content, /Consequential mapping authored before release/);
  assert.match(
    result.content,
    /Part of the consequential mapping completed at runtime/,
  );
  assert.doesNotMatch(result.content, /```mermaid/);
  assert.match(
    result.content,
    /<strong>Figure 3 — The controlled-object shift for the motivating class\.<\/strong>/,
  );
});

test("Figure 3 semantic guard remains coupled to the canonical Mermaid", () => {
  const mermaid = canonicalFigure3.match(/```mermaid\n([\s\S]*?)\n```/)[1];
  assert.doesNotThrow(() => assertFigure3SemanticSource(mermaid));
  const svg = buildFigure3ControlledObjectSvg();
  assert.match(svg, /Explicitly Authored Software/);
  assert.match(svg, /Motivating runtime-judgment class/);
  assert.throws(
    () =>
      assertFigure3SemanticSource(
        mermaid.replace("probabilistic Model Judgment", "removed"),
      ),
    /publication comparison requires review/,
  );
});

test("current article Figure 3 acceptance preserves one canonical and one rendered figure", () => {
  const rendition = {
    figure3Rendition: true,
    canonicalFigures: [
      { number: 3, panel: null, title: "The controlled-object shift" },
    ],
    renditionFigures: [
      { number: 3, panel: null, title: "The controlled-object shift" },
    ],
  };
  assert.doesNotThrow(() => assertCurrentArticleFigure3Rendition(rendition));
  assert.throws(
    () =>
      assertCurrentArticleFigure3Rendition({
        ...rendition,
        figure3Rendition: false,
      }),
    /side-by-side Figure 3 rendition/,
  );
});
