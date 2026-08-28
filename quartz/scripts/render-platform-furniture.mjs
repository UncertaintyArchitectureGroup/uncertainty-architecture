#!/usr/bin/env node

import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { repoRoot, sha256 } from "./publication-rendition.mjs";

const profilePath = path.join(
  repoRoot,
  "quartz",
  "publication",
  "thinking-systems.platforms.json",
);
const renditionRoot = path.join(
  repoRoot,
  "dist",
  "publication",
  "thinking-systems",
  "renditions",
);

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function platformUrl(item, platform) {
  return platform === "medium"
    ? item.medium_url || item.linkedin_url
    : item.linkedin_url || item.medium_url;
}

function platformProfileUrl(author, platform) {
  return platform === "medium" ? author.medium_profile : author.linkedin_profile;
}

function allArticlesUrl(research, platform) {
  return platform === "medium"
    ? research.medium_all_articles_url
    : research.linkedin_all_articles_url;
}

export function buildFurnitureMarkdown(profile, platform) {
  const author = profile.author_furniture;
  const research = profile.research_path;
  if (!author?.bio || !research?.items?.length) {
    throw new Error("Platform profile is missing author/research publication furniture");
  }
  const profileUrl = platformProfileUrl(author, platform);
  const allArticles = allArticlesUrl(research, platform);
  const lines = [
    `## ${author.heading}`,
    "",
    author.bio,
    "",
    `[${author.name} — ${platform === "medium" ? "Medium profile" : "LinkedIn profile"}](${profileUrl})`,
    "",
    `## ${research.heading}`,
    "",
    research.intro,
    "",
  ];
  for (const item of research.items) {
    const url = platformUrl(item, platform);
    lines.push(
      `### ${item.stage}`,
      "",
      `[${item.title}](${url})`,
      "",
      item.description,
      "",
    );
  }
  lines.push(`[Explore all articles by ${author.name}](${allArticles})`, "");
  return lines.join("\n");
}

export function buildFurnitureHtml(profile, platform) {
  const author = profile.author_furniture;
  const research = profile.research_path;
  if (!author?.bio || !research?.items?.length) {
    throw new Error("Platform profile is missing author/research publication furniture");
  }
  const profileUrl = platformProfileUrl(author, platform);
  const allArticles = allArticlesUrl(research, platform);
  const items = research.items
    .map((item) => {
      const url = platformUrl(item, platform);
      return `<h3>${escapeHtml(item.stage)}</h3><p><a href="${escapeHtml(url)}">${escapeHtml(item.title)}</a></p><p>${escapeHtml(item.description)}</p>`;
    })
    .join("");
  return `<section class="publication-furniture" data-platform="${platform}"><h2>${escapeHtml(author.heading)}</h2><p>${escapeHtml(author.bio)}</p><p><a href="${escapeHtml(profileUrl)}">${escapeHtml(author.name)} — ${platform === "medium" ? "Medium profile" : "LinkedIn profile"}</a></p><h2>${escapeHtml(research.heading)}</h2><p>${escapeHtml(research.intro)}</p>${items}<p><a href="${escapeHtml(allArticles)}">Explore all articles by ${escapeHtml(author.name)}</a></p></section>`;
}

export function buildFurnitureText(profile, platform) {
  const author = profile.author_furniture;
  const research = profile.research_path;
  if (!author?.bio || !research?.items?.length) {
    throw new Error("Platform profile is missing author/research publication furniture");
  }
  const profileUrl = platformProfileUrl(author, platform);
  const allArticles = allArticlesUrl(research, platform);
  const lines = [
    author.heading,
    "",
    author.bio,
    "",
    `${author.name} — ${platform === "medium" ? "Medium profile" : "LinkedIn profile"} (${profileUrl})`,
    "",
    research.heading,
    "",
    research.intro,
    "",
  ];
  for (const item of research.items) {
    const url = platformUrl(item, platform);
    lines.push(item.stage, "", `${item.title} (${url})`, "", item.description, "");
  }
  lines.push(`Explore all articles by ${author.name} (${allArticles})`, "");
  return lines.join("\n");
}

export function insertMarkdownFurniture(article, furniture) {
  if (article.includes("## About the author")) {
    throw new Error("Article already contains author furniture");
  }
  const marker = "\n## Resources\n";
  if (!article.includes(marker)) {
    throw new Error("Article Markdown is missing Resources boundary");
  }
  return article.replace(marker, `\n${furniture}\n${marker}`);
}

export function insertHtmlFurniture(article, furniture) {
  if (article.includes('class="publication-furniture"')) {
    throw new Error("Article already contains publication furniture");
  }
  const marker = "<h2>Resources</h2>";
  if (!article.includes(marker)) {
    throw new Error("Article HTML is missing Resources boundary");
  }
  return article.replace(marker, `${furniture}${marker}`);
}

export function insertTextFurniture(article, furniture) {
  if (article.includes("\nAbout the author\n")) {
    throw new Error("Article text already contains author furniture");
  }
  const marker = "\nResources\n";
  if (!article.includes(marker)) {
    throw new Error("Article text is missing Resources boundary");
  }
  return article.replace(marker, `\n${furniture}\n${marker}`);
}

async function renderPlatform(profile, platform) {
  const dir = path.join(renditionRoot, platform);
  const mdPath = path.join(dir, "article.md");
  const htmlPath = path.join(dir, "article.html");
  const textPath = path.join(dir, "article.txt");
  const md = await readFile(mdPath, "utf8");
  const html = await readFile(htmlPath, "utf8");
  const text = await readFile(textPath, "utf8");
  const nextMd = insertMarkdownFurniture(
    md,
    buildFurnitureMarkdown(profile, platform),
  );
  const nextHtml = insertHtmlFurniture(
    html,
    buildFurnitureHtml(profile, platform),
  );
  const nextText = insertTextFurniture(
    text,
    buildFurnitureText(profile, platform),
  );
  await writeFile(mdPath, nextMd, "utf8");
  await writeFile(htmlPath, nextHtml, "utf8");
  await writeFile(textPath, nextText, "utf8");
  return {
    [`${platform}/article.md`]: sha256(Buffer.from(nextMd)),
    [`${platform}/article.html`]: sha256(Buffer.from(nextHtml)),
    [`${platform}/article.txt`]: sha256(Buffer.from(nextText)),
  };
}

async function main() {
  const profileRaw = await readFile(profilePath, "utf8");
  const profile = JSON.parse(profileRaw);
  const linkedinOutputs = await renderPlatform(profile, "linkedin");
  const mediumOutputs = await renderPlatform(profile, "medium");

  const manifestPath = path.join(
    renditionRoot,
    "platform-renditions.manifest.json",
  );
  const manifest = JSON.parse(await readFile(manifestPath, "utf8"));
  manifest.publication_furniture = {
    author: profile.author_furniture.name,
    research_path_items: profile.research_path.items.length,
    platform_specific_navigation: true,
    included_in_research_pdf: false,
  };
  manifest.outputs = {
    ...manifest.outputs,
    ...linkedinOutputs,
    ...mediumOutputs,
  };
  await writeFile(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`, "utf8");

  console.log(
    "Platform author/research furniture added to LinkedIn and Medium MD/HTML/TXT renditions",
  );
}

const isEntryPoint =
  process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isEntryPoint) {
  main().catch((error) => {
    console.error(
      `Platform furniture failed: ${error instanceof Error ? error.message : String(error)}`,
    );
    process.exitCode = 1;
  });
}
