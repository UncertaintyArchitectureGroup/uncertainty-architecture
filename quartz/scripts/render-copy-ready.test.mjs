import assert from "node:assert/strict";
import { mkdtemp, mkdir, rm, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";

import {
  buildCopyReadyDocument,
  embedLocalImages,
} from "./render-copy-ready.mjs";

test("copy-ready HTML embeds local images as data URIs", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ua-copy-ready-"));
  try {
    const renditionDir = path.join(root, "renditions", "linkedin");
    const figureDir = path.join(root, "figures", "png");
    await mkdir(renditionDir, { recursive: true });
    await mkdir(figureDir, { recursive: true });
    const figurePath = path.join(figureDir, "figure-1.png");
    await writeFile(figurePath, Buffer.from([0x89, 0x50, 0x4e, 0x47]));
    const articlePath = path.join(renditionDir, "article.html");
    const source = '<main><img src="../../figures/png/figure-1.png" alt="Figure 1"/></main>';
    const result = await embedLocalImages(source, articlePath, root);
    assert.equal(result.embedded, 1);
    assert.match(result.html, /src="data:image\/png;base64,/);
    assert.doesNotMatch(result.html, /\.\.\/\.\.\/figures\/png/);
  } finally {
    await rm(root, { recursive: true, force: true });
  }
});

test("copy-ready document exposes automatic copy and persistent selection fallback", () => {
  const source = `<!doctype html><html><head><style>body{color:black}</style></head><body><main><h1>Thinking Systems</h1><figure><img src="data:image/png;base64,AAAA"/><figcaption><strong>Upload file:</strong> figure-1.png</figcaption></figure><p>Body</p><p class="provenance">Generated from source commit abc</p></main></body></html>`;
  const output = buildCopyReadyDocument(source, "linkedin");
  assert.match(output, /id="copy-surface"/);
  assert.match(output, /id="copy-article"/);
  assert.match(output, /id="select-article"/);
  assert.match(output, /navigator\.clipboard/);
  assert.match(output, /function selectArticle/);
  assert.match(output, /Article selected — tap Copy in the system menu/);
  assert.doesNotMatch(output, /document\.execCommand\('copy'\)/);
  assert.doesNotMatch(output, /selection\.removeAllRanges\(\);\s*status\.textContent='Copied'/);
  assert.doesNotMatch(output, /Upload file:/);
  assert.doesNotMatch(output, /class="provenance"/);
  assert.match(output, /data:image\/png;base64,AAAA/);
});

test("copy-ready document keeps toolbar outside copied article", () => {
  const source = '<!doctype html><html><head><style></style></head><body><main><p>Article</p></main></body></html>';
  const output = buildCopyReadyDocument(source, "medium");
  const toolbarIndex = output.indexOf("copy-ready-toolbar");
  const surfaceIndex = output.indexOf('id="copy-surface"');
  assert.ok(toolbarIndex >= 0 && surfaceIndex > toolbarIndex);
  assert.match(output, /Medium copy-ready article/);
  assert.match(output, /Select article/);
  assert.match(output, /On iPad or when browser clipboard access is blocked/);
});
