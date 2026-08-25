import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(fileURLToPath(new URL("../..", import.meta.url)));
const pub = readFileSync(
  path.join(root, "content/research/notes/thinking-systems-publication-draft.md"),
  "utf8",
);
const man = readFileSync(
  path.join(root, "content/research/notes/open-engineering-specification-article-draft.md"),
  "utf8",
);
const bp = readFileSync(
  path.join(root, "content/research/notes/open-engineering-specification-article-blueprint.md"),
  "utf8",
);

function fig(src, n, title = "") {
  const re = new RegExp(
    "```mermaid\\n((?:(?!```)[\\s\\S])*?)\\n```\\n\\n\\*\\*Figure " +
      n +
      " —([^\\n]+)",
    "g",
  );
  const matches = [...src.matchAll(re)].filter(
    (match) => !title || match[2].includes(title),
  );
  assert.equal(matches.length, 1);
  return matches[0][1];
}

function figure3(src) {
  const mermaid = fig(src, 3, "controlled-object shift");
  assert.match(mermaid, /^flowchart TB/m);
  assert.match(mermaid, /subgraph ROW3\[" "\][\s\S]*direction LR/);
  assert.match(
    mermaid,
    /subgraph A\["Explicitly Authored Software"\][\s\S]*direction TB/,
  );
  assert.match(
    mermaid,
    /subgraph B\["Motivating runtime-judgment class"\][\s\S]*direction TB/,
  );
  assert.match(mermaid, /A1 --> A2 --> A3/);
  assert.match(mermaid, /B1 --> B2 --> B3/);
  assert.match(mermaid, /B1 --> J1 --> B3/);
  assert.match(
    mermaid,
    /A -\. "responsibility-structure comparison" \.\- B/,
  );
  assert.match(mermaid, /style ROW3 fill:transparent,stroke:transparent/);
  assert.doesNotMatch(mermaid, /A2 ~~~ J1|^block$|columns 2/);
}

function orthogonal(src, n) {
  const mermaid = fig(src, n, "Two orthogonal models");
  assert.match(mermaid, /^flowchart TB/m);
  assert.match(mermaid, /subgraph ROW_ORTHO\[" "\][\s\S]*direction LR/);
  assert.match(mermaid, /subgraph L\["Decision ownership/);
  assert.match(mermaid, /subgraph F\["Capability functions/);
  assert.match(
    mermaid,
    /subgraph F\["Capability functions — one control architecture, not a sequence"\][\s\S]*direction TB/,
  );
  assert.match(
    mermaid,
    /C\["Controllers \/ decision functions[\s\S]*S\["Sensors and evidence[\s\S]*K\["Constraints and realizations[\s\S]*A\["Actuators and corrective action/,
  );
  assert.match(mermaid, /C --- S --- K --- A/);
  assert.doesNotMatch(mermaid, /C\s*-->|S\s*-->|K\s*-->/);
  assert.match(mermaid, /initial admissibility \+ assessment eligibility/);
  assert.match(mermaid, /specific Bounded Research Authorization/);
  assert.match(mermaid, /Business Authorization or changed basis/);
  assert.match(mermaid, /applicable Project Authorization scope \/ set/);
  assert.match(mermaid, /research-only and\/or production-capable/);
  assert.match(mermaid, /realization \/ experiment evidence/);
  assert.match(mermaid, /risk \/ feasibility \/ Model Judgment necessity/);
  assert.match(mermaid, /Exogenous Organizational change/);
  assert.doesNotMatch(
    mermaid,
    /classDef railpoint|\bJ2\b|\bJ3\b|\bJ4\b|CAP_TOP|CAP_BOTTOM/,
  );
}

test("Figure 3 stays as two top-down panels in one LR row", () => {
  figure3(pub);
  figure3(man);
});

test("orthogonal model stays as two side-by-side panels", () => {
  orthogonal(pub, 8);
  orthogonal(man, 9);
});

test("blueprint owns both structural layout contracts", () => {
  assert.match(bp, /same Mermaid panel-layout pattern already proven by Figure 8\/9/);
  assert.match(bp, /outer transparent `ROW3` subgraph with `direction LR`/);
  assert.match(bp, /`A -\. "responsibility-structure comparison" \.\- B`/);
  assert.match(bp, /Do \*\*not\*\* add alignment or comparison links between internal nodes/);
  assert.match(bp, /`ROW_ORTHO` subgraph with `direction LR`/);
  assert.match(bp, /Controllers → Sensors → Constraints → Actuators/);
  assert.match(bp, /plain non-directional Mermaid links \(`---`\)/);
});
