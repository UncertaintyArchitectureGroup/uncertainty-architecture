#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    text = read(path)
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected exactly one replacement target, found {count}")
    write(path, text.replace(old, new, 1))


# 1. Keep Figure 7 semantics unchanged but switch its publication source layout from
# a wide left-to-right graph to a portrait-friendly top-to-bottom graph. Both PDF
# and platform renderers consume the same canonical Mermaid and therefore inherit
# the readability improvement without introducing a second semantic representation.
replace_once(
    "content/research/notes/thinking-systems-publication-draft.md",
    '```mermaid\nflowchart LR\n    R["Authorized intent,<br/>Requirement, and assumptions"]\n',
    '```mermaid\nflowchart TB\n    R["Authorized intent,<br/>Requirement, and assumptions"]\n',
)

# 2. Replace the heading-link protector with a Markdown-AST implementation. It
# preserves original Markdown bytes except for inserted fallback lines and supports
# ATX/Setext headings, inline links, reference links, and inline HTML anchors while
# ignoring fenced code blocks structurally.
protect = r'''#!/usr/bin/env node

import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { unified } from "unified";
import remarkParse from "remark-parse";

import { repoRoot, sha256 } from "./publication-rendition.mjs";

const renditionRoot = path.join(
  repoRoot,
  "dist",
  "publication",
  "thinking-systems",
  "renditions",
);

function unique(values) {
  const seen = new Set();
  return values.filter((value) => {
    if (seen.has(value)) return false;
    seen.add(value);
    return true;
  });
}

function sourceLabel(count) {
  return count === 1 ? "Source" : "Sources";
}

function markdownFallback(urls) {
  return `**${sourceLabel(urls.length)}:** ${urls.map((url) => `<${url}>`).join(" · ")}`;
}

function htmlFallback(urls) {
  const links = urls
    .map((url) => `<a href="${url}">${url}</a>`)
    .join(" · ");
  return `<p class="heading-link-fallback"><strong>${sourceLabel(urls.length)}:</strong> ${links}</p>`;
}

function walk(node, visitor) {
  visitor(node);
  if (!Array.isArray(node?.children)) return;
  for (const child of node.children) walk(child, visitor);
}

function collectDefinitions(tree) {
  const definitions = new Map();
  walk(tree, (node) => {
    if (node?.type !== "definition") return;
    const identifier = String(node.identifier || "").toLowerCase();
    if (identifier && /^https?:\/\//i.test(String(node.url || ""))) {
      definitions.set(identifier, String(node.url));
    }
  });
  return definitions;
}

function htmlAnchorUrls(value) {
  const urls = [];
  const pattern = /<a\b[^>]*\bhref\s*=\s*(["'])(https?:\/\/.*?)\1[^>]*>/gi;
  for (const match of String(value || "").matchAll(pattern)) urls.push(match[2]);
  return urls;
}

function headingUrls(node, definitions) {
  const urls = [];
  walk(node, (child) => {
    if (child === node) return;
    if (child?.type === "link" && /^https?:\/\//i.test(String(child.url || ""))) {
      urls.push(String(child.url));
    } else if (child?.type === "linkReference") {
      const resolved = definitions.get(String(child.identifier || "").toLowerCase());
      if (resolved) urls.push(resolved);
    } else if (child?.type === "html") {
      urls.push(...htmlAnchorUrls(child.value));
    }
  });
  return unique(urls);
}

function parseMarkdown(markdown) {
  return unified().use(remarkParse).parse(String(markdown));
}

export function inspectMarkdownHeadingLinks(markdown) {
  const source = String(markdown);
  const tree = parseMarkdown(source);
  const definitions = collectDefinitions(tree);
  const entries = [];
  walk(tree, (node) => {
    if (node?.type !== "heading") return;
    const urls = headingUrls(node, definitions);
    if (urls.length === 0) return;
    const end = node.position?.end?.offset;
    if (!Number.isInteger(end)) {
      throw new Error("Linked Markdown heading is missing positional offsets");
    }
    const fallback = markdownFallback(urls);
    const tail = source.slice(end);
    const protectedAlready = new RegExp(
      `^\\r?\\n\\r?\\n${fallback.replace(/[.*+?^${}()|[\\]\\]/g, "\\$&")}(?:\\r?\\n|$)`,
    ).test(tail);
    entries.push({ depth: node.depth, urls, end, fallback, protected: protectedAlready });
  });
  return entries;
}

export function protectMarkdownHeadingLinks(markdown) {
  const source = String(markdown);
  const entries = inspectMarkdownHeadingLinks(source);
  const insertions = entries
    .filter((entry) => !entry.protected)
    .map((entry) => ({ offset: entry.end, text: `\n\n${entry.fallback}` }))
    .sort((left, right) => right.offset - left.offset);
  let output = source;
  for (const insertion of insertions) {
    output = `${output.slice(0, insertion.offset)}${insertion.text}${output.slice(insertion.offset)}`;
  }
  return {
    markdown: output,
    fallbackCount: entries
      .filter((entry) => !entry.protected)
      .reduce((sum, entry) => sum + entry.urls.length, 0),
    totalProtectedUrls: entries.reduce((sum, entry) => sum + entry.urls.length, 0),
  };
}

export function protectHtmlHeadingLinks(html) {
  let fallbackCount = 0;
  let protectedUrlCount = 0;
  const output = String(html).replace(
    /<(h[1-6])([^>]*)>([\s\S]*?)<\/\1>/gi,
    (full, tag, attributes, inner, offset, whole) => {
      const urls = unique(
        [...inner.matchAll(/<a\s+[^>]*href\s*=\s*(["'])(https?:\/\/.*?)\1[^>]*>[\s\S]*?<\/a>/gi)].map(
          (match) => match[2],
        ),
      );
      if (urls.length === 0) return full;
      protectedUrlCount += urls.length;
      const following = whole.slice(offset + full.length);
      if (/^\s*<p class="heading-link-fallback">/i.test(following)) return full;
      fallbackCount += urls.length;
      return `${full}${htmlFallback(urls)}`;
    },
  );
  return { html: output, fallbackCount, totalProtectedUrls: protectedUrlCount };
}

export function countProtectedHeadingLinks(html) {
  return (String(html).match(/class="heading-link-fallback"/g) || []).length;
}

async function protectPlatform(platform) {
  const directory = path.join(renditionRoot, platform);
  const markdownPath = path.join(directory, "article.md");
  const htmlPath = path.join(directory, "article.html");
  const markdown = await readFile(markdownPath, "utf8");
  const html = await readFile(htmlPath, "utf8");

  const protectedMarkdown = protectMarkdownHeadingLinks(markdown);
  const protectedHtml = protectHtmlHeadingLinks(html);

  if (protectedMarkdown.totalProtectedUrls !== protectedHtml.totalProtectedUrls) {
    throw new Error(
      `${platform} Markdown/HTML linked-heading URL inventory diverged: ${protectedMarkdown.totalProtectedUrls} vs ${protectedHtml.totalProtectedUrls}`,
    );
  }

  const markdownInventory = inspectMarkdownHeadingLinks(protectedMarkdown.markdown);
  if (markdownInventory.some((entry) => !entry.protected)) {
    throw new Error(`${platform} Markdown still contains an unprotected linked heading`);
  }

  await writeFile(markdownPath, protectedMarkdown.markdown, "utf8");
  await writeFile(htmlPath, protectedHtml.html, "utf8");

  return {
    count: protectedMarkdown.totalProtectedUrls,
    markdownSha256: sha256(Buffer.from(protectedMarkdown.markdown)),
    htmlSha256: sha256(Buffer.from(protectedHtml.html)),
  };
}

async function main() {
  const linkedin = await protectPlatform("linkedin");
  const medium = await protectPlatform("medium");
  if (linkedin.count !== medium.count) {
    throw new Error(
      `LinkedIn and Medium heading-link protection diverged: ${linkedin.count} vs ${medium.count}`,
    );
  }

  const manifestPath = path.join(renditionRoot, "platform-renditions.manifest.json");
  const manifest = JSON.parse(await readFile(manifestPath, "utf8"));
  manifest.heading_link_protection = {
    mechanism: "visible-source-line-after-linked-heading",
    parser: "remark-ast",
    applies_to: "markdown-heading-nodes-and-generated-h1-h6",
    body_links_duplicated: false,
    deterministic_multiple_links: true,
    linkedin_fallback_urls: linkedin.count,
    medium_fallback_urls: medium.count,
  };
  manifest.outputs["linkedin/article.md"] = linkedin.markdownSha256;
  manifest.outputs["linkedin/article.html"] = linkedin.htmlSha256;
  manifest.outputs["medium/article.md"] = medium.markdownSha256;
  manifest.outputs["medium/article.html"] = medium.htmlSha256;
  await writeFile(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`, "utf8");

  console.log(
    `Platform linked headings protected: ${linkedin.count} URL fallback(s) per platform`,
  );
}

const isEntryPoint =
  process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isEntryPoint) {
  main().catch((error) => {
    console.error(
      `Platform heading-link protection failed: ${error instanceof Error ? error.message : String(error)}`,
    );
    process.exitCode = 1;
  });
}
'''
write("quartz/scripts/protect-platform-heading-links.mjs", protect)

# 3. Upgrade linked-heading tests to cover AST-only cases and semantic URL inventory.
protect_test = r'''import assert from "node:assert/strict";
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
'''
write("quartz/scripts/protect-platform-heading-links.test.mjs", protect_test)

# 4. Remove obsolete repository-contract marker spoofing from copy-ready renderer.
copy_ready_path = "quartz/scripts/render-copy-ready.mjs"
copy_ready = read(copy_ready_path)
legacy_comment = '''// Legacy repository-contract compatibility markers retained until the policy\n// contract is revised separately; generated HTML no longer exposes "Copy article"\n// controls and no longer relies on "best-effort-platform-dependent" clipboard APIs.\n'''
if legacy_comment not in copy_ready:
    raise RuntimeError("render-copy-ready.mjs: legacy marker comment not found")
write(copy_ready_path, copy_ready.replace(legacy_comment, ""))

# 5. Add a final package verifier. It runs after all post-processing and checks the
# exact generated package rather than only unit-level transformations.
verifier = r'''#!/usr/bin/env node

import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { inspectMarkdownHeadingLinks } from "./protect-platform-heading-links.mjs";
import { gitOutput, repoRoot, sha256 } from "./publication-rendition.mjs";

const publicationRoot = path.join(repoRoot, "dist", "publication", "thinking-systems");
const renditionRoot = path.join(publicationRoot, "renditions");
const pdfPath = path.join(repoRoot, "dist", "pdf", "thinking-systems-when-the-controlled-object-changes.pdf");
const pdfManifestPath = path.join(repoRoot, "dist", "pdf", "thinking-systems-when-the-controlled-object-changes.manifest.json");
const minimumPlatformLabelPx = 12;

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function digest(buffer) {
  return createHash("sha256").update(buffer).digest("hex");
}

export function assertPlatformFigureReadability(manifest, minimum = minimumPlatformLabelPx) {
  assert(Array.isArray(manifest?.figures) && manifest.figures.length === 9, "Expected nine platform figure renditions");
  for (const figure of manifest.figures) {
    const label = Number(figure.projected_desktop_minimum_label_px);
    assert(Number.isFinite(label), `Figure ${figure.number}${figure.panel || ""} has no measurable platform label size`);
    assert(label >= minimum, `Figure ${figure.number}${figure.panel || ""} projected desktop label ${label}px is below the ${minimum}px publication floor`);
  }
  const figure8 = manifest.figures.filter((figure) => figure.number === 8).map((figure) => figure.panel);
  assert(JSON.stringify(figure8) === JSON.stringify(["A", "B"]), "Figure 8A and 8B must travel together");
}

export function countDataImages(html) {
  return (String(html).match(/src="data:image\//g) || []).length;
}

function fallbackAnchorCount(html) {
  let count = 0;
  for (const match of String(html).matchAll(/<p class="heading-link-fallback">([\s\S]*?)<\/p>/gi)) {
    count += (match[1].match(/<a\b/gi) || []).length;
  }
  return count;
}

function assertNoCopyHelpers(html, platform) {
  assert(!/<script\b/i.test(html), `${platform} copy-ready HTML contains JavaScript`);
  assert(!/Copy article|Select article|navigator\.clipboard|ClipboardItem/i.test(html), `${platform} copy-ready HTML contains obsolete copy controls`);
  assert(!/Upload file:|class="provenance"/i.test(html), `${platform} copy-ready HTML leaked helper/provenance content`);
}

async function verifyOutputDigests(manifest) {
  for (const [relative, expected] of Object.entries(manifest.outputs || {})) {
    const bytes = await readFile(path.join(renditionRoot, relative));
    assert(sha256(bytes) === expected, `Platform output digest mismatch: ${relative}`);
  }
}

async function verifyPlatform(platform, manifest, expectedImages) {
  const directory = path.join(renditionRoot, platform);
  const [markdown, html, copyReady] = await Promise.all([
    readFile(path.join(directory, "article.md"), "utf8"),
    readFile(path.join(directory, "article.html"), "utf8"),
    readFile(path.join(directory, "copy-ready.html"), "utf8"),
  ]);
  const inventory = inspectMarkdownHeadingLinks(markdown);
  assert(inventory.every((entry) => entry.protected), `${platform} Markdown contains an unprotected linked heading`);
  const linkedUrls = inventory.reduce((sum, entry) => sum + entry.urls.length, 0);
  assert(linkedUrls === manifest.heading_link_protection?.[`${platform}_fallback_urls`], `${platform} heading-link manifest count diverged`);
  assert(fallbackAnchorCount(html) === linkedUrls, `${platform} article HTML heading fallback count diverged`);
  assert(fallbackAnchorCount(copyReady) === linkedUrls, `${platform} copy-ready heading fallback count diverged`);
  assert(countDataImages(copyReady) === expectedImages, `${platform} copy-ready embedded ${countDataImages(copyReady)} images; expected ${expectedImages}`);
  assertNoCopyHelpers(copyReady, platform);
  for (const marker of [
    "About the author",
    "Architecting Uncertainty: A Modern Guide to LLM-Based Software",
    "Uncertainty Architecture: A Modern Approach to Designing LLM Applications",
    "Uncertainty Architecture: Why AI Governance Is Actually Control Theory",
    "AI, the Externalization of Reasoning, and the Verification Crisis",
    "Reinventing Control Theory One Feature at a Time: The Fallacy of Agentic Loops",
    "Uncertainty Architecture: Beyond Embeddings — Neuro-Symbolic Verification of Semantic Drift in LLMs",
  ]) {
    assert(copyReady.includes(marker), `${platform} copy-ready HTML is missing publication furniture: ${marker}`);
  }
}

async function main() {
  const [platformManifest, assetManifest, pdfManifest, pdfBytes] = await Promise.all([
    readFile(path.join(renditionRoot, "platform-renditions.manifest.json"), "utf8").then(JSON.parse),
    readFile(path.join(publicationRoot, "assets.manifest.json"), "utf8").then(JSON.parse),
    readFile(pdfManifestPath, "utf8").then(JSON.parse),
    readFile(pdfPath),
  ]);

  const expectedCommit = process.env.UA_PDF_REPOSITORY_REF || process.env.GITHUB_SHA || (await gitOutput(["rev-parse", "HEAD"]));
  assert(platformManifest.publication_state === "candidate", "Platform package must remain candidate");
  assert(platformManifest.publication_ready === false, "Editable-source package must not self-certify publication readiness");
  assert(platformManifest.source_commit === expectedCommit, `Platform provenance ${platformManifest.source_commit} does not match ${expectedCommit}`);
  assert(pdfManifest.source_commit_sha === expectedCommit, `PDF provenance ${pdfManifest.source_commit_sha} does not match ${expectedCommit}`);
  assert(pdfManifest.pdf_sha256 === digest(pdfBytes), "PDF checksum does not match its manifest");
  assert(Number(pdfManifest.page_count) > 0, "PDF manifest has no page count");
  assertPlatformFigureReadability(assetManifest);
  await verifyOutputDigests(platformManifest);
  await verifyPlatform("linkedin", platformManifest, 9);
  await verifyPlatform("medium", platformManifest, 10);
  assert(platformManifest.publication_furniture?.research_path_items === 6, "Publication furniture must contain six research-path items");
  assert(platformManifest.copy_ready?.javascript_copy_controls === false, "Copy-ready contract must explicitly disable JavaScript controls");
  assert(platformManifest.figure_8_panels_must_travel_together === true, "Figure 8 coupling contract was lost");

  console.log(`Complete Thinking Systems publication package verified at ${expectedCommit}: candidate state, PDF, 9 platform figures, copy-ready HTML, linked-heading fallbacks, and publication furniture are coherent.`);
}

const isEntryPoint = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isEntryPoint) {
  main().catch((error) => {
    console.error(`Publication package verification failed: ${error instanceof Error ? error.message : String(error)}`);
    process.exitCode = 1;
  });
}
'''
write("quartz/scripts/verify-publication-package.mjs", verifier)

verifier_test = r'''import assert from "node:assert/strict";
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
'''
write("quartz/scripts/verify-publication-package.test.mjs", verifier_test)

# 6. Package scripts: restore readable JSON formatting and make the final verifier a
# first-class command rather than an implicit CI-only convention.
package_path = ROOT / "package.json"
package = json.loads(package_path.read_text(encoding="utf-8"))
scripts = package.setdefault("scripts", {})
scripts["publication:verify-package"] = "node quartz/scripts/verify-publication-package.mjs"
package_path.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 7. Correct the one misleading specific-item Medium link. Until that exact Medium
# edition URL is known, the furniture falls back to the exact LinkedIn article URL;
# the profile URL remains only the all-articles navigation target.
profile_path = ROOT / "quartz/publication/thinking-systems.platforms.json"
profile = json.loads(profile_path.read_text(encoding="utf-8"))
for item in profile["research_path"]["items"]:
    if item["stage"] == "Technical application" and item.get("medium_url") == profile["research_path"]["medium_all_articles_url"]:
        item.pop("medium_url", None)
profile_path.write_text(json.dumps(profile, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 8. Workflow: exact-head provenance everywhere, include the new verifier test, and
# verify the complete package after every post-processor before artifact upload.
workflow_path = ".github/workflows/export-platform-renditions.yml"
workflow = read(workflow_path)
workflow = workflow.replace(
    "      UA_PDF_REPOSITORY_REF: ${{ github.sha }}\n",
    "      UA_PDF_REPOSITORY_REF: ${{ github.event.pull_request.head.sha || github.sha }}\n",
)
workflow = workflow.replace(
    "          quartz/scripts/publication-assets.test.mjs\n",
    "          quartz/scripts/publication-assets.test.mjs\n          quartz/scripts/verify-publication-package.test.mjs\n",
)
workflow = workflow.replace(
    "      - name: Upload complete publication package\n",
    "      - name: Verify complete publication package\n        env:\n          UA_PDF_REPOSITORY_REF: ${{ github.event.pull_request.head.sha || github.sha }}\n        run: npm run publication:verify-package\n      - name: Upload complete publication package\n",
)
write(workflow_path, workflow)

# 9. Documentation: add the final verifier and make the all-figure readability gate
# explicit. Also describe heading protection as an upstream AST-based transform.
doc_path = "quartz/PLATFORM-RENDITIONS.md"
doc = read(doc_path)
doc = doc.replace(
    "npm run publication:copy-ready\n\n# or the complete platform sequence",
    "npm run publication:copy-ready\n\n# after the standalone PDF exists, verify the complete distribution package\nnpm run publication:verify-package\n\n# or generate the complete platform sequence",
)
doc = doc.replace(
    "→ self-contained copy-ready HTML\n→ one uploaded artifact",
    "→ self-contained copy-ready HTML\n→ final package verification (PDF, provenance, figures, furniture, fallbacks)\n→ one uploaded artifact",
)
doc = doc.replace(
    "The renderer consumes the current `publication:assets` manifest rather than inventing its own figure filenames.\n",
    "The renderer consumes the current `publication:assets` manifest rather than inventing its own figure filenames. The final package verifier rejects any platform figure whose projected minimum label falls below the 12 px no-zoom publication floor; this gate applies to Figures 1–7 as well as the Figure 8 panels.\n",
)
doc = doc.replace(
    "The same mechanism runs for LinkedIn and Medium and is generic for future articles rather than hard-coded to the current ISO/NIST examples.",
    "The same mechanism runs for LinkedIn and Medium. Markdown headings are identified through the Remark AST rather than line regexes, so ATX and Setext headings, inline links, reference links, and inline HTML anchors are handled without rewriting fenced-code examples; generated HTML receives the equivalent protection. The mechanism is generic for future articles rather than hard-coded to the current ISO/NIST examples.",
)
write(doc_path, doc)

note_path = "content/research/notes/thinking-systems-platform-renditions.md"
note = read(note_path)
note = note.replace(
    "The copy-ready renderer therefore scans all heading levels and, whenever an HTTP(S) hyperlink occurs inside a heading, emits the same URL as a separate visible linked line immediately below it.",
    "An upstream platform transform identifies Markdown heading nodes through the Remark AST and, whenever an HTTP(S) hyperlink occurs inside a heading, emits the same URL as a separate visible linked line immediately below it before normal HTML and copy-ready packaging. The copy-ready renderer preserves that protection rather than owning a second heading parser.",
)
note = note.replace(
    "The LinkedIn cover remains a separate platform upload.",
    "The complete-package verifier also enforces a 12 px projected no-zoom label floor across every generated platform figure before the artifact is accepted. The LinkedIn cover remains a separate platform upload.",
)
write(note_path, note)

# 10. Update the repository contract structurally. Remove obsolete clipboard-marker
# requirements, protect the actual five-stage pipeline and final verifier, and make
# exact-head provenance a protected workflow invariant.
contract_path = ROOT / ".github/policy/repository-contract-change-coupling.json"
contract = json.loads(contract_path.read_text(encoding="utf-8"))
required = contract.setdefault("required_paths", [])
required_map = {(item["path"], item["type"]) for item in required}
for path in [
    "quartz/scripts/protect-platform-heading-links.mjs",
    "quartz/scripts/protect-platform-heading-links.test.mjs",
    "quartz/scripts/render-platform-furniture.mjs",
    "quartz/scripts/platform-furniture.test.mjs",
    "quartz/scripts/copy-ready.test.mjs",
    "quartz/scripts/verify-publication-package.mjs",
    "quartz/scripts/verify-publication-package.test.mjs",
]:
    if (path, "file") not in required_map:
        required.append({"path": path, "type": "file"})

critical = contract.setdefault("critical_files", [])
by_path = {item["path"]: item for item in critical}

pkg = by_path["package.json"]["required_text"]
pkg[:] = [marker for marker in pkg if not marker.startswith('"publication:bundle"')]
for marker in [
    '"publication:platforms": "node quartz/scripts/render-platform-renditions.mjs"',
    '"publication:protect-links": "node quartz/scripts/protect-platform-heading-links.mjs"',
    '"publication:furniture": "node quartz/scripts/render-platform-furniture.mjs"',
    '"publication:copy-ready": "node quartz/scripts/render-copy-ready.mjs"',
    '"publication:verify-package": "node quartz/scripts/verify-publication-package.mjs"',
    '"publication:bundle": "npm run publication:assets && npm run publication:platforms && npm run publication:protect-links && npm run publication:furniture && npm run publication:copy-ready"',
]:
    if marker not in pkg:
        pkg.append(marker)

copy = by_path["quartz/scripts/render-copy-ready.mjs"]["required_text"]
copy[:] = [marker for marker in copy if marker not in {"Copy article", "best-effort-platform-dependent"}]
for marker in ["manual-select-all-copy", "javascript_copy_controls: false", "copy-ready.html"]:
    if marker not in copy:
        copy.append(marker)

workflow_markers = by_path[workflow_path]["required_text"]
workflow_markers[:] = [marker for marker in workflow_markers if marker != "UA_PDF_REPOSITORY_REF: ${{ github.sha }}"]
for marker in [
    "UA_PDF_REPOSITORY_REF: ${{ github.event.pull_request.head.sha || github.sha }}",
    "npm run publication:verify-package",
    "quartz/scripts/verify-publication-package.test.mjs",
    "dist/pdf/thinking-systems-when-the-controlled-object-changes.manifest.json",
]:
    if marker not in workflow_markers:
        workflow_markers.append(marker)

new_critical = {
    "quartz/scripts/protect-platform-heading-links.mjs": [
        "inspectMarkdownHeadingLinks",
        "remark-parse",
        "linkReference",
        "visible-source-line-after-linked-heading",
        "body_links_duplicated: false",
    ],
    "quartz/scripts/protect-platform-heading-links.test.mjs": [
        "reference-style and Setext linked headings are protected structurally",
        "fenced code that looks like a linked heading is not rewritten",
        "current adapted article yields exactly the two reviewed linked headings",
    ],
    "quartz/scripts/verify-publication-package.mjs": [
        "assertPlatformFigureReadability",
        "minimumPlatformLabelPx = 12",
        "publication_state === \"candidate\"",
        "publication_ready === false",
        "Figure 8A and 8B must travel together",
        "copy-ready HTML contains obsolete copy controls",
    ],
    "quartz/scripts/verify-publication-package.test.mjs": [
        "rejects the previously accepted unreadable Figure 7 class",
        "accepts nine readable figures with Figure 8A and 8B coupled",
    ],
}
for path, markers in new_critical.items():
    if path in by_path:
        by_path[path]["required_text"] = markers
    else:
        critical.append({"path": path, "required_text": markers})

contract_path.write_text(json.dumps(contract, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 11. Changelog/roadmap are already coupled to PR93. Add the substantive hardening
# note without changing framework/research authority.
changelog = read("CHANGELOG.md")
needle = "## Unreleased\n"
if needle in changelog and "all-figure platform readability" not in changelog:
    changelog = changelog.replace(
        needle,
        needle + "\n- Hardened the Thinking Systems publication package with AST-based linked-heading preservation, all-figure platform readability verification, exact-head package provenance checks, and end-to-end artifact verification.\n",
        1,
    )
write("CHANGELOG.md", changelog)

print("PR93 substantive fixup applied")
