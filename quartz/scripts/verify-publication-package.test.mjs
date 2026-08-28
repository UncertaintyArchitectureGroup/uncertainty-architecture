import test from "node:test";
import assert from "node:assert/strict";

import {
  assertPlatformFigureInventory,
  countDataImages,
  remoteGithubImageSources,
} from "./verify-publication-package.mjs";

test("platform verifier requires nine figures with Figure 8A and 8B coupled", () => {
  const figures = Array.from({ length: 7 }, (_, index) => ({ number: index + 1, panel: null }));
  figures.push({ number: 8, panel: "A" }, { number: 8, panel: "B" });
  assert.doesNotThrow(() => assertPlatformFigureInventory({ figures }));
});

test("platform verifier rejects incomplete Figure 8 coupling", () => {
  const figures = Array.from({ length: 8 }, (_, index) => ({ number: index + 1, panel: null }));
  figures.push({ number: 8, panel: "A" });
  assert.throws(() => assertPlatformFigureInventory({ figures }), /Figure 8A and 8B/);
});

test("embedded image counter distinguishes data-URI payloads", () => {
  assert.equal(countDataImages('<img src="data:image/png;base64,a"><img src="https://example.com/x.png">'), 1);
});

test("remote image inventory recognizes immutable GitHub image sources", () => {
  const url = "https://raw.githubusercontent.com/UncertaintyArchitectureGroup/uncertainty-architecture/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/content/research/notes/thinking-systems-platform-assets/medium-hero.png";
  assert.deepEqual(remoteGithubImageSources(`<img src="${url}"><img src="https://example.com/x.png">`), [url]);
});
