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
flowchart LR
    subgraph A["Primarily explicitly authored consequential behavior"]
        A1["Situation and operating conditions"]
        A2["Explicitly authored consequential responsibilities"]
        A3["Consequential output, action, or downstream state"]
        A1 --> A2 --> A3
    end
    subgraph B["Thinking System — changed responsibility structure"]
        B1["Situation and operating conditions"]
        B2["Explicitly authored responsibilities before, between, and after Judgment Nodes"]
        J1["One or more Judgment Nodes probabilistic Model Judgment"]
        B3["Consequential output, action, or downstream state"]
        B1 --> B2 --> B3
        B1 --> J1 --> B3
    end
\`\`\`

**Figure 3 — The controlled-object shift.** Canonical caption.`;

test("Figure 3 publication rendition is a side-by-side Linear Software comparison", () => {
  const result = renderFigure3(canonicalFigure3);
  assert.equal(result.rendered, true);
  assert.match(result.content, /data-ua-figure3-rendition="side-by-side"/);
  assert.match(result.content, /data-ua-flow="top-down"/);
  assert.match(result.content, /Linear Software/);
  assert.match(result.content, /Thinking System/);
  assert.match(result.content, /Consequential mapping authored before release/);
  assert.match(
    result.content,
    /Part of the consequential mapping completed at runtime/,
  );
  assert.match(result.content, /One or more/);
  assert.match(result.content, /Judgment Nodes/);
  assert.match(result.content, /before \/ between Judgment Nodes/);
  assert.match(result.content, /after Judgment Nodes/);
  assert.doesNotMatch(result.content, /```mermaid/);
  assert.match(
    result.content,
    /<strong>Figure 3 — The controlled-object shift\.<\/strong>/,
  );
  assert.doesNotMatch(result.content, /\*\*Figure 3/);
});

test("Figure 3 semantic guard rejects a materially incomplete source", () => {
  const svg = buildFigure3ControlledObjectSvg();
  assert.match(svg, /Linear Software/);
  assert.match(svg, /Thinking System/);
  assert.throws(
    () =>
      assertFigure3SemanticSource(
        canonicalFigure3.replace("probabilistic Model Judgment", "removed"),
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
