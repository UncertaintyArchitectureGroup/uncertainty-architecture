import assert from "node:assert/strict";
import {
  mkdtemp,
  mkdir,
  rm,
  writeFile,
} from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";

import {
  appendHeadingLinkFallbacks,
  buildCopyReadyDocument,
  buildMediumUploadPlan,
  embedLocalImages,
} from "./render-copy-ready.mjs";

test("copy-ready HTML embeds local images as data URIs", async () => {
  const root = await mkdtemp(
    path.join(os.tmpdir(), "ua-copy-ready-"),
  );
  try {
    const renditionDir = path.join(
      root,
      "renditions",
      "linkedin",
    );
    const figureDir = path.join(
      root,
      "figures",
      "png",
    );
    await mkdir(renditionDir, { recursive: true });
    await mkdir(figureDir, { recursive: true });
    const figurePath = path.join(
      figureDir,
      "figure-1.png",
    );
    await writeFile(
      figurePath,
      Buffer.from([0x89, 0x50, 0x4e, 0x47]),
    );
    const articlePath = path.join(
      renditionDir,
      "article.html",
    );
    const source =
      '<main><img src="../../figures/png/figure-1.png" alt="Figure 1"/></main>';
    const result = await embedLocalImages(
      source,
      articlePath,
      root,
    );
    assert.equal(result.embedded, 1);
    assert.match(
      result.html,
      /src="data:image\/png;base64,/,
    );
    assert.doesNotMatch(
      result.html,
      /\.\.\/\.\.\/figures\/png/,
    );
  } finally {
    await rm(root, {
      recursive: true,
      force: true,
    });
  }
});

test("copy-ready heading links receive visible URL fallbacks", () => {
  const source =
    '<main><h3><a href="https://example.com/iso">AI-based system</a></h3><p>Body</p><h2>Plain heading</h2><h4><a href="https://example.com/a">A</a> and <a href="https://example.com/b">B</a></h4></main>';
  const result = appendHeadingLinkFallbacks(source);
  assert.equal(result.fallbacks, 3);
  assert.match(
    result.html,
    /<h3><a href="https:\/\/example\.com\/iso">AI-based system<\/a><\/h3><p class="heading-link-fallback"><a href="https:\/\/example\.com\/iso">https:\/\/example\.com\/iso<\/a><\/p>/,
  );
  assert.match(
    result.html,
    /https:\/\/example\.com\/a/,
  );
  assert.match(
    result.html,
    /https:\/\/example\.com\/b/,
  );
  assert.doesNotMatch(
    result.html,
    /<h2>Plain heading<\/h2><p class="heading-link-fallback">/,
  );
});

test("copy-ready document exposes one article-only copy surface", () => {
  const source =
    '<!doctype html><html><head><style>body{color:black}</style></head><body><main><h1>Thinking Systems</h1><figure><img src="data:image/png;base64,AAAA"/><figcaption><strong>Upload file:</strong> figure-1.png</figcaption></figure><p>Body</p><p class="provenance">Generated from source commit abc</p></main></body></html>';
  const output = buildCopyReadyDocument(source);
  assert.match(output, /id="copy-surface"/);
  assert.doesNotMatch(output, /id="copy-article"/);
  assert.doesNotMatch(output, /id="select-article"/);
  assert.doesNotMatch(
    output,
    /navigator\.clipboard/,
  );
  assert.doesNotMatch(output, /<script>/);
  assert.doesNotMatch(output, /Upload file:/);
  assert.doesNotMatch(
    output,
    /class="provenance"/,
  );
  assert.match(
    output,
    /data:image\/png;base64,AAAA/,
  );
});

test("copy-ready document keeps toolbar outside copied article by removing helper toolbar entirely", () => {
  const source =
    '<!doctype html><html><head><style></style></head><body><main><p>Article</p></main></body></html>';
  const output = buildCopyReadyDocument(source);
  assert.doesNotMatch(
    output,
    /copy-ready-toolbar/,
  );
  assert.doesNotMatch(output, /Copy article/);
  assert.doesNotMatch(output, /Select article/);
  assert.match(output, /id="copy-surface"/);
});

test("Medium upload plan is hero plus nine figures in deterministic order", () => {
  const figures = Array.from(
    { length: 7 },
    (_, index) => ({
      number: index + 1,
      panel: null,
      png_path: `dist/publication/thinking-systems/figures/png/figure-${index + 1}.png`,
    }),
  );
  figures.push(
    {
      number: 8,
      panel: "B",
      png_path:
        "dist/publication/thinking-systems/figures/png/figure-8b.png",
    },
    {
      number: 8,
      panel: "A",
      png_path:
        "dist/publication/thinking-systems/figures/png/figure-8a.png",
    },
  );
  const plan = buildMediumUploadPlan({
    figures,
  });
  assert.equal(plan.length, 10);
  assert.equal(
    plan[0].filename,
    "00-medium-hero.png",
  );
  assert.equal(
    plan[8].filename,
    "08-figure-08a.png",
  );
  assert.equal(
    plan[9].filename,
    "09-figure-08b.png",
  );
});
