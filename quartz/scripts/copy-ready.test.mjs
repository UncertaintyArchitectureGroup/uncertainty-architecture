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

test("linked heading receives a visible fallback while ordinary body links are untouched", () => {
  const source = '<main><h3><a href="https://www.iso.org/standard/79016.html">AI-based system (ISO/IEC TR 29119-11)</a></h3><p>See <a href="https://example.com/body">the body source</a>.</p><h2>Unlinked heading</h2></main>';
  const result = appendHeadingLinkFallbacks(source);
  assert.equal(result.fallbacks, 1);
  assert.match(
    result.html,
    /<h3><a href="https:\/\/www\.iso\.org\/standard\/79016\.html">AI-based system \(ISO\/IEC TR 29119-11\)<\/a><\/h3><p class="heading-link-fallback"><a href="https:\/\/www\.iso\.org\/standard\/79016\.html">https:\/\/www\.iso\.org\/standard\/79016\.html<\/a><\/p>/,
  );
  assert.equal((result.html.match(/https:\/\/example\.com\/body/g) || []).length, 1);
  assert.doesNotMatch(result.html, /<h2>Unlinked heading<\/h2><p class="heading-link-fallback">/);
});

test("multiple linked headings and multiple links in one heading preserve every distinct URL deterministically", () => {
  const source = '<main><h2><a href="https://example.com/a">A</a> and <a href="https://example.com/b">B</a> plus <a href="https://example.com/a">A again</a></h2><p>Body</p><h4><a href="https://example.com/c">C</a></h4></main>';
  const result = appendHeadingLinkFallbacks(source);
  assert.equal(result.fallbacks, 3);
  const aFallback = '<p class="heading-link-fallback"><a href="https://example.com/a">https://example.com/a</a></p>';
  const bFallback = '<p class="heading-link-fallback"><a href="https://example.com/b">https://example.com/b</a></p>';
  const cFallback = '<p class="heading-link-fallback"><a href="https://example.com/c">https://example.com/c</a></p>';
  assert.equal((result.html.match(/heading-link-fallback/g) || []).length, 3);
  assert.ok(result.html.indexOf(aFallback) < result.html.indexOf(bFallback));
  assert.ok(result.html.indexOf(bFallback) < result.html.indexOf(cFallback));
  assert.equal((result.html.match(/https:\/\/example\.com\/a<\/a><\/p>/g) || []).length, 1);
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
