import assert from "node:assert/strict";
import { mkdtemp, mkdir, rm, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";

import {
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

test("copy-ready document exposes one-copy UI but excludes helper furniture from the copy surface", () => {
  const source = `<!doctype html><html><head><style>body{}</style></head><body><main><h1>Article</h1><figure><img src="data:image/png;base64,AAAA"/><figcaption><strong>Upload file:</strong> figure.png</figcaption></figure><p class="provenance">Generated from source commit abc</p></main></body></html>`;
  const output = buildCopyReadyDocument(source, "linkedin");
  assert.match(output, /id="copy-surface"/);
  assert.match(output, /id="copy-article"/);
  assert.match(output, /ClipboardItem/);
  assert.doesNotMatch(output, /Upload file:/);
  assert.doesNotMatch(output, /Generated from source commit/);
  assert.match(output, /data:image\/png;base64,AAAA/);
});
