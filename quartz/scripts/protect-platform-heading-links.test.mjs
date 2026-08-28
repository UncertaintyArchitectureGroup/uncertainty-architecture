import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";

import {
  inspectMarkdownHeadingLinks,
  protectHtmlHeadingLinks,
  protectMarkdownHeadingLinks,
} from "./protect-platform-heading-links.mjs";
import { convertMarkdownTables } from "./render-platform-renditions.mjs";
import { currentArticleSource, repoRoot } from "./publication-rendition.mjs";

test("one linked Markdown heading receives one visible source line", () => {
  const result = protectMarkdownHeadingLinks(
    "### [AI-based system](https://example.com/iso)\n\nBody",
  );
  assert.equal(result.fallbackCount, 1);
  assert.match(result.markdown, /\*\*Source:\*\* <https:\/\/example\.com\/iso>/);
});

test("ordinary body hyperlink is not duplicated and heading without hyperlink is unchanged", () => {
  const source = "## Plain heading\n\nRead [the source](https://example.com/body).";
  const result = protectMarkdownHeadingLinks(source);
  assert.equal(result.fallbackCount, 0);
  assert.equal(result.markdown, source);
});

test("multiple linked headings and multiple links are deterministic and deduplicated", () => {
  const result = protectMarkdownHeadingLinks(
    "## [One](https://example.com/1)\n\n#### [A](https://example.com/a) and [B](https://example.com/b) and [A again](https://example.com/a)",
  );
  assert.equal(result.fallbackCount, 3);
  assert.match(result.markdown, /Source:\*\* <https:\/\/example\.com\/1>/);
  assert.match(result.markdown, /\*\*Sources:\*\* <https:\/\/example\.com\/a> · <https:\/\/example\.com\/b>/);
});

test("reference-style and Setext linked headings are protected structurally", () => {
  const source = "[Reference heading][src]\n========================\n\n[src]: https://example.com/reference";
  const result = protectMarkdownHeadingLinks(source);
  assert.equal(result.totalProtectedUrls, 1);
  assert.match(result.markdown, /\*\*Source:\*\* <https:\/\/example\.com\/reference>/);
  assert.equal(inspectMarkdownHeadingLinks(result.markdown)[0].protected, true);
});

test("fenced code that looks like a linked heading is not rewritten", () => {
  const source = "```markdown\n### [Not a heading](https://example.com/code)\n```";
  const result = protectMarkdownHeadingLinks(source);
  assert.equal(result.totalProtectedUrls, 0);
  assert.equal(result.markdown, source);
});

test("inline HTML anchor inside Markdown heading is protected", () => {
  const result = protectMarkdownHeadingLinks(
    "### <a href='https://example.com/html'>HTML-linked heading</a>",
  );
  assert.equal(result.totalProtectedUrls, 1);
  assert.match(result.markdown, /https:\/\/example\.com\/html/);
});

test("HTML protection mirrors the ordered Markdown URL inventory and ignores body links", () => {
  const html = protectHtmlHeadingLinks(
    '<h3><a href="https://example.com/a">A</a> and <a href="https://example.com/b">B</a></h3><p>Body <a href="https://example.com/body">link</a></p>',
  );
  assert.equal(html.totalProtectedUrls, 2);
  assert.match(html.html, /<strong>Sources:<\/strong>/);
  assert.equal((html.html.match(/https:\/\/example\.com\/body/g) || []).length, 1);
});

test("protection is idempotent while retaining the total linked-heading inventory", () => {
  const once = protectMarkdownHeadingLinks("### [A](https://example.com/a)\n\nBody");
  const twice = protectMarkdownHeadingLinks(once.markdown);
  assert.equal(twice.fallbackCount, 0);
  assert.equal(twice.totalProtectedUrls, 1);
  assert.equal(twice.markdown, once.markdown);

  const htmlOnce = protectHtmlHeadingLinks('<h3><a href="https://example.com/a">A</a></h3>');
  const htmlTwice = protectHtmlHeadingLinks(htmlOnce.html);
  assert.equal(htmlTwice.fallbackCount, 0);
  assert.equal(htmlTwice.totalProtectedUrls, 1);
  assert.equal(htmlTwice.html, htmlOnce.html);
});

test("current adapted article yields exactly the two reviewed linked headings after platform table expansion", async () => {
  const raw = await readFile(path.join(repoRoot, currentArticleSource), "utf8");
  const expanded = convertMarkdownTables(raw);
  const inventory = inspectMarkdownHeadingLinks(expanded);
  assert.deepEqual(inventory.map((entry) => entry.urls), [
    ["https://www.iso.org/standard/79016.html"],
    ["https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10"],
  ]);
});
