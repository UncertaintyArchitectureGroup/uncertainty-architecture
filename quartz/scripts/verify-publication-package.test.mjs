import assert from "node:assert/strict";
import test from "node:test";

import {
  assertPlatformFigureReadability,
  countDataImages,
} from "./verify-publication-package.mjs";

function manifest(labels) {
  return {
    figures: labels.map((label, index) => ({
      number: index < 7 ? index + 1 : 8,
      panel: index === 7 ? "A" : index === 8 ? "B" : null,
      projected_desktop_minimum_label_px: label,
    })),
  };
}

test("package verifier rejects the previously accepted unreadable Figure 7 class", () => {
  const values = [16, 16, 16, 16, 16, 16, 6.96, 16, 16];
  assert.throws(() => assertPlatformFigureReadability(manifest(values)), /Figure 7 projected desktop label 6\.96px/);
});

test("package verifier accepts nine readable figures with Figure 8A and 8B coupled", () => {
  assert.doesNotThrow(() => assertPlatformFigureReadability(manifest([12, 13, 14, 15, 16, 17, 18, 19, 20])));
});

test("embedded image counter distinguishes LinkedIn and Medium copy-ready payloads", () => {
  const html = `<main>${'<img src="data:image/png;base64,AA"/>'.repeat(9)}</main>`;
  assert.equal(countDataImages(html), 9);
});
