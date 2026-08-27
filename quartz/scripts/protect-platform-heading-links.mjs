#!/usr/bin/env node

import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { repoRoot, sha256 } from "./publication-rendition.mjs";

const renditionRoot = path.join(
  repoRoot,
  "dist",
  "publication",
  "thinking-systems",
  "renditions",
);

const markdownLinkPattern = /\[[^\]]+\]\((https?:\/\/[^)\s]+)(?:\s+"[^"]*")?\)/gi;
const htmlLinkPattern = /<a\s+[^>]*href="(https?:\/\/[^"]+)"[^>]*>[\s\S]*?<\/a>/gi;

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
  const links = urls.map((url) => `<${url}>`).join(" · ");
  return `**${sourceLabel(urls.length)}:** ${links}`;
}

function htmlFallback(urls) {
  const links = urls
    .map((url) => `<a href="${url}">${url}</a>`)
    .join(" · ");
  return `<p class="heading-link-fallback"><strong>${sourceLabel(urls.length)}:</strong> ${links}</p>`;
}

export function protectMarkdownHeadingLinks(markdown) {
  const lines = String(markdown).split(/\r?\n/);
  const output = [];
  let fallbackCount = 0;

  for (let index = 0; index < lines.length; index += 1) {
    const line = lines[index];
    output.push(line);
    if (!/^#{1,6}\s+\S/.test(line)) continue;

    const urls = unique([...line.matchAll(markdownLinkPattern)].map((match) => match[1]));
    if (urls.length === 0) continue;

    const fallback = markdownFallback(urls);
    const following = lines[index + 1] === "" ? lines[index + 2] : lines[index + 1];
    if (following === fallback) continue;

    output.push("", fallback);
    fallbackCount += urls.length;
  }

  return { markdown: output.join("\n"), fallbackCount };
}

export function protectHtmlHeadingLinks(html) {
  let fallbackCount = 0;
  const output = String(html).replace(
    /<(h[1-6])([^>]*)>([\s\S]*?)<\/\1>(?!<p class="heading-link-fallback">)/gi,
    (full, tag, attributes, inner) => {
      const urls = unique([...inner.matchAll(htmlLinkPattern)].map((match) => match[1]));
      if (urls.length === 0) return full;
      fallbackCount += urls.length;
      return `${full}${htmlFallback(urls)}`;
    },
  );
  return { html: output, fallbackCount };
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

  if (protectedMarkdown.fallbackCount !== protectedHtml.fallbackCount) {
    throw new Error(
      `${platform} Markdown/HTML heading-link protection diverged: ${protectedMarkdown.fallbackCount} vs ${protectedHtml.fallbackCount}`,
    );
  }

  await writeFile(markdownPath, protectedMarkdown.markdown, "utf8");
  await writeFile(htmlPath, protectedHtml.html, "utf8");

  return {
    count: protectedHtml.fallbackCount,
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
    applies_to: "h1-h6",
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
