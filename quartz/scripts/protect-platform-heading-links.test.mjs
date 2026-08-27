import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";

import {
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
  assert.match(
    result.markdown,
    /### \[AI-based system\]\(https:\/\/example\.com\/iso\)\n\n\*\*Source:\*\* <https:\/\/example\.com\/iso>/,
  );
});

test("ordinary body hyperlink is not duplicated", () => {
  const result = protectMarkdownHeadingLinks(
    "## Plain heading\n\nRead [the source](https://example.com/body).",
  );
  assert.equal(result.fallbackCount, 0);
  assert.doesNotMatch(result.markdown, /\*\*Source/);
});

test("heading without hyperlink is unchanged", () => {
  const source = "## Plain heading\n\nBody";
  const result = protectMarkdownHeadingLinks(source);
  assert.equal(result.fallbackCount, 0);
  assert.equal(result.markdown, source);
});

test("multiple linked headings each receive their own fallback", () => {
  const result = protectMarkdownHeadingLinks(
    "## [One](https://example.com/1)\n\nBody\n\n### [Two](https://example.com/2)",
  );
  assert.equal(result.fallbackCount, 2);
  assert.match(result.markdown, /Source:\*\* <https:\/\/example\.com\/1>/);
  assert.match(result.markdown, /Source:\*\* <https:\/\/example\.com\/2>/);
});

test("multiple links in one heading are deterministic and deduplicated", () => {
  const result = protectMarkdownHeadingLinks(
    "#### [A](https://example.com/a) and [B](https://example.com/b) and [A again](https://example.com/a)",
  );
  assert.equal(result.fallbackCount, 2);
  assert.match(
    result.markdown,
    /\*\*Sources:\*\* <https:\/\/example\.com\/a> · <https:\/\/example\.com\/b>/,
  );
});

test("HTML protection mirrors Markdown semantics", () => {
  const html = protectHtmlHeadingLinks(
    '<h3><a href="https://example.com/a">A</a> and <a href="https://example.com/b">B</a></h3><p>Body <a href="https://example.com/body">link</a></p>',
  );
  assert.equal(html.fallbackCount, 2);
  assert.match(html.html, /class="heading-link-fallback"/);
  assert.match(html.html, /<strong>Sources:<\/strong>/);
  assert.equal((html.html.match(/https:\/\/example\.com\/body/g) || []).length, 1);
});

test("protection is idempotent for already protected headings", () => {
  const once = protectMarkdownHeadingLinks(
    "### [A](https://example.com/a)\n\nBody",
  );
  const twice = protectMarkdownHeadingLinks(once.markdown);
  assert.equal(twice.fallbackCount, 0);
  assert.equal(twice.markdown, once.markdown);

  const htmlOnce = protectHtmlHeadingLinks(
    '<h3><a href="https://example.com/a">A</a></h3>',
  );
  const htmlTwice = protectHtmlHeadingLinks(htmlOnce.html);
  assert.equal(htmlTwice.fallbackCount, 0);
  assert.equal(htmlTwice.html, htmlOnce.html);
});

test("current adapted article yields exactly the two reviewed linked headings after platform table expansion", async () => {
  const raw = await readFile(path.join(repoRoot, currentArticleSource), "utf8");
  const expanded = convertMarkdownTables(raw);
  const linkedHeadings = expanded
    .split(/\r?\n/)
    .filter((line) => /^#{1,6}\s+.*\]\(https?:\/\//.test(line));

  assert.deepEqual(linkedHeadings, [
    "### **[AI-based system (ISO/IEC TR 29119-11)](https://www.iso.org/standard/79016.html)**",
    "### **[AI system (NIST AI RMF)](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10)**",
  ]);
});
