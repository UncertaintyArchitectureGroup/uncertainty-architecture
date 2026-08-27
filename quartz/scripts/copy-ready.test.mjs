import assert from "node:assert/strict";
import { mkdtemp, mkdir, rm, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";

import {
  appendHeadingLinkFallbacks,
  buildCopyReadyDocument,
  embedLocalImages,
} from "./render-copy-ready.mjs";

test("copy-ready embedding turns local images into self-contained data URIs", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ua-copy-ready-"));
  try {
    const articleDir = path.join(root, "renditions", "linkedin");
    const figureDir = path.join(root, "figures", "png");
    await mkdir(articleDir, { recursive: true });
    await mkdir(figureDir, { recursive: true });
    await writeFile(path.join(figureDir, "figure-1.png"), Buffer.from([137, 80, 78, 71]));
    const articlePath = path.join(articleDir, "article.html");
    const source = '<main><figure><img src="../../figures/png/figure-1.png" alt="Figure"/></figure></main>';
    const result = await embedLocalImages(source, articlePath, root);
    assert.equal(result.embedded, 1);
    assert.match(result.html, /src="data:image\/png;base64,/);
    assert.doesNotMatch(result.html, /\.\.\/\.\.\/figures/);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("copy-ready embedding rejects images outside the publication root", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ua-copy-ready-"));
  try {
    const articleDir = path.join(root, "renditions", "linkedin");
    await mkdir(articleDir, { recursive: true });
    const articlePath = path.join(articleDir, "article.html");
    await assert.rejects(
      () => embedLocalImages('<main><img src="../../../../escape.png"/></main>', articlePath, root),
      /escapes publication root/,
    );
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("copy-ready materializes URLs below every linked heading", () => {
  const source = '<main><h3><a href="https://www.iso.org/standard/79016.html">AI-based system (ISO/IEC TR 29119-11)</a></h3><p>Body</p><h3><a href="https://www.nist.gov/example">AI system (NIST AI RMF)</a></h3><h2>Unlinked heading</h2></main>';
  const result = appendHeadingLinkFallbacks(source);
  assert.equal(result.fallbacks, 2);
  assert.match(result.html, /heading-link-fallback[\s\S]*https:\/\/www\.iso\.org\/standard\/79016\.html/);
  assert.match(result.html, /heading-link-fallback[\s\S]*https:\/\/www\.nist\.gov\/example/);
  assert.doesNotMatch(result.html, /<h2>Unlinked heading<\/h2><p class="heading-link-fallback">/);
});

test("copy-ready document uses manual select-all copy and excludes helper furniture", () => {
  const source = `<!doctype html><html><head><style>body{}</style></head><body><main><h1>Article</h1><figure><img src="data:image/png;base64,AAAA"/><figcaption><strong>Upload file:</strong> figure.png</figcaption></figure><p class="provenance">Generated from source commit abc</p></main></body></html>`;
  const output = buildCopyReadyDocument(source);
  assert.match(output, /id="copy-surface"/);
  assert.doesNotMatch(output, /id="copy-article"/);
  assert.doesNotMatch(output, /id="select-article"/);
  assert.doesNotMatch(output, /ClipboardItem/);
  assert.doesNotMatch(output, /<script>/);
  assert.doesNotMatch(output, /Upload file:/);
  assert.doesNotMatch(output, /Generated from source commit/);
  assert.match(output, /data:image\/png;base64,AAAA/);
});
