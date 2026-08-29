#!/usr/bin/env node

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

function hasImmediateMarkdownFallback(tail, fallback) {
  return (
    tail === `\n\n${fallback}` ||
    tail.startsWith(`\n\n${fallback}\n`) ||
    tail === `\r\n\r\n${fallback}` ||
    tail.startsWith(`\r\n\r\n${fallback}\r\n`)
  );
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
    entries.push({
      depth: node.depth,
      urls,
      end,
      fallback,
      protected: hasImmediateMarkdownFallback(tail, fallback),
    });
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
