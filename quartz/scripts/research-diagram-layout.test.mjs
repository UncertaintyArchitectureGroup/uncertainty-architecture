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
  assert.equal(matches.length, 1, `expected one Figure ${n} Mermaid block`);
  return matches[0][1];
}

function normalizedLines(mermaid) {
  return mermaid
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
}

function subgraphBody(mermaid, id) {
  const lines = normalizedLines(mermaid);
  const start = lines.findIndex((line) => line.startsWith(`subgraph ${id}[`));
  assert.notEqual(start, -1, `missing subgraph ${id}`);

  let depth = 0;
  for (let i = start; i < lines.length; i += 1) {
    if (lines[i].startsWith("subgraph ")) depth += 1;
    if (lines[i] === "end") {
      depth -= 1;
      if (depth === 0) return lines.slice(start + 1, i);
    }
  }
  assert.fail(`unterminated subgraph ${id}`);
}

function assertDirection(mermaid, id, expected) {
  const body = subgraphBody(mermaid, id);
  assert.equal(
    body[0],
    `direction ${expected}`,
    `${id} must begin with direction ${expected}`,
  );
}

function assertFigure3Layout(mermaid) {
  const lines = normalizedLines(mermaid);
  assert.equal(lines[0], "flowchart TB", "Figure 3 outer flow must stay TB");
  assertDirection(mermaid, "ROW3", "LR");
  assertDirection(mermaid, "A", "TB");
  assertDirection(mermaid, "B", "TB");

  assert.ok(lines.includes("A1 --> A2 --> A3"), "left responsibility path changed");
  assert.ok(lines.includes("B1 --> B2 --> B3"), "right authored path changed");
  assert.ok(lines.includes("B1 --> J1 --> B3"), "right judgment path changed");
  assert.ok(
    lines.includes('A -. "responsibility-structure comparison" .- B'),
    "panels must be related at subgraph level",
  );
  assert.ok(
    lines.includes("style ROW3 fill:transparent,stroke:transparent"),
    "ROW3 must remain layout-only and transparent",
  );

  assert.doesNotMatch(mermaid, /~~~/, "Figure 3 must not use invisible alignment links");
  assert.doesNotMatch(mermaid, /^block$/m, "Figure 3 must not switch to block syntax");
  assert.doesNotMatch(mermaid, /columns\s+2/, "Figure 3 must not switch to block columns");
  assert.doesNotMatch(
    mermaid,
    /\bA\d+\s*(?:-->|---|-\.|~~~).*\b(?:B\d+|J\d+)\b|\b(?:B\d+|J\d+)\s*(?:-->|---|-\.|~~~).*\bA\d+\b/,
    "internal nodes from opposite panels must not be cross-linked",
  );
}

function assertOrthogonalLayout(mermaid) {
  const lines = normalizedLines(mermaid);
  assert.equal(lines[0], "flowchart TB", "orthogonal model outer flow must stay TB");
  assertDirection(mermaid, "ROW_ORTHO", "LR");
  assertDirection(mermaid, "L", "TB");
  assertDirection(mermaid, "F", "TB");

  assert.ok(
    lines.includes("C --- S --- K --- A"),
    "capability families must remain one non-directional vertical stack",
  );
  assert.ok(
    lines.includes('L -. "all four capability families may appear at every decision horizon" .- F'),
    "orthogonal panels must remain related at subgraph level",
  );
  assert.ok(
    lines.includes("style ROW_ORTHO fill:transparent,stroke:transparent"),
    "ROW_ORTHO must remain layout-only and transparent",
  );

  assert.doesNotMatch(mermaid, /C\s*-->|S\s*-->|K\s*-->/, "capability links must not imply execution order");
  assert.doesNotMatch(mermaid, /~~~/, "orthogonal model must not use invisible alignment links");
  assert.doesNotMatch(
    mermaid,
    /classDef railpoint|\bJ2\b|\bJ3\b|\bJ4\b|CAP_TOP|CAP_BOTTOM/,
    "retired layout rails must not return",
  );

  assert.match(mermaid, /initial admissibility \+ assessment eligibility/);
  assert.match(mermaid, /specific Bounded Research Authorization/);
  assert.match(mermaid, /Business Authorization or changed basis/);
  assert.match(mermaid, /applicable Project Authorization scope \/ set/);
  assert.match(mermaid, /research-only and\/or production-capable/);
  assert.match(mermaid, /realization \/ experiment evidence/);
  assert.match(mermaid, /risk \/ feasibility \/ Model Judgment necessity/);
  assert.match(mermaid, /Exogenous Organizational change/);
}

const publicationFigure3 = fig(pub, 3, "controlled-object shift");
const manuscriptFigure3 = fig(man, 3, "controlled-object shift");
const publicationOrthogonal = fig(pub, 8, "Two orthogonal models");
const manuscriptOrthogonal = fig(man, 9, "Two orthogonal models");

test("Figure 3 stays as two top-down panels in one LR row", () => {
  assertFigure3Layout(publicationFigure3);
  assertFigure3Layout(manuscriptFigure3);
  assert.equal(
    manuscriptFigure3,
    publicationFigure3,
    "Figure 3 Mermaid must stay synchronized across manuscript and publication",
  );
});

test("Figure 3 rejects known layout regressions", () => {
  assert.throws(
    () => assertFigure3Layout(publicationFigure3.replace("direction LR", "direction TB")),
    /ROW3 must begin with direction LR/,
  );
  assert.throws(
    () =>
      assertFigure3Layout(
        publicationFigure3.replace(
          'subgraph A["Explicitly Authored Software"]\n            direction TB',
          'subgraph A["Explicitly Authored Software"]\n            direction LR',
        ),
      ),
    /A must begin with direction TB/,
  );
  assert.throws(
    () =>
      assertFigure3Layout(
        publicationFigure3.replace(
          'A -. "responsibility-structure comparison" .- B',
          "A2 ~~~ J1",
        ),
      ),
    /panels must be related at subgraph level|invisible alignment links/,
  );
  assert.throws(
    () =>
      assertFigure3Layout(
        publicationFigure3.replace("B1 --> J1 --> B3", "B2 --> J1 --> B3"),
      ),
    /right judgment path changed/,
  );
});

test("orthogonal model stays as two side-by-side panels", () => {
  assertOrthogonalLayout(publicationOrthogonal);
  assertOrthogonalLayout(manuscriptOrthogonal);
  assert.equal(
    manuscriptOrthogonal,
    publicationOrthogonal,
    "orthogonal-model Mermaid must stay synchronized across manuscript and publication",
  );
});

test("orthogonal model rejects known layout regressions", () => {
  assert.throws(
    () => assertOrthogonalLayout(publicationOrthogonal.replace("direction LR", "direction TB")),
    /ROW_ORTHO must begin with direction LR/,
  );
  assert.throws(
    () => assertOrthogonalLayout(publicationOrthogonal.replace("C --- S --- K --- A", "C --> S --> K --> A")),
    /non-directional vertical stack|must not imply execution order/,
  );
  assert.throws(
    () =>
      assertOrthogonalLayout(
        publicationOrthogonal.replace(
          'L -. "all four capability families may appear at every decision horizon" .- F',
          "C ~~~ O",
        ),
      ),
    /orthogonal panels must remain related at subgraph level|invisible alignment links/,
  );
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
