#!/usr/bin/env node

import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { repoRoot } from "./publication-rendition.mjs";

const profilePath = path.join(repoRoot, "quartz", "publication", "thinking-systems.platforms.json");
const renditionRoot = path.join(repoRoot, "dist", "publication", "thinking-systems", "renditions");

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

export function buildFurnitureMarkdown(profile, platform) {
  const author = profile.author_furniture;
  const research = profile.research_path;
  if (!author?.bio || !research?.items?.length) {
    throw new Error("Platform profile is missing author/research publication furniture");
  }
  const profileUrl = platform === "medium" ? author.medium_profile : author.linkedin_profile;
  const allArticles = platform === "medium" ? research.medium_all_articles_url : research.linkedin_all_articles_url;
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
    lines.push(`### ${item.stage}`, "", `[${item.title}](${url})`, "", item.description, "");
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
  const profileUrl = platform === "medium" ? author.medium_profile : author.linkedin_profile;
  const allArticles = platform === "medium" ? research.medium_all_articles_url : research.linkedin_all_articles_url;
  const items = research.items.map((item) => {
    const url = platformUrl(item, platform);
    return `<h3>${escapeHtml(item.stage)}</h3><p><a href="${escapeHtml(url)}">${escapeHtml(item.title)}</a></p><p>${escapeHtml(item.description)}</p>`;
  }).join("");
  return `<section class="publication-furniture" data-platform="${platform}"><h2>${escapeHtml(author.heading)}</h2><p>${escapeHtml(author.bio)}</p><p><a href="${escapeHtml(profileUrl)}">${escapeHtml(author.name)} — ${platform === "medium" ? "Medium profile" : "LinkedIn profile"}</a></p><h2>${escapeHtml(research.heading)}</h2><p>${escapeHtml(research.intro)}</p>${items}<p><a href="${escapeHtml(allArticles)}">Explore all articles by ${escapeHtml(author.name)}</a></p></section>`;
}

export function insertMarkdownFurniture(article, furniture) {
  if (article.includes("## About the author")) throw new Error("Article already contains author furniture");
  const marker = "\n## Resources\n";
  if (!article.includes(marker)) throw new Error("Article Markdown is missing Resources boundary");
  return article.replace(marker, `\n${furniture}\n${marker}`);
}

export function insertHtmlFurniture(article, furniture) {
  if (article.includes('class="publication-furniture"')) throw new Error("Article already contains publication furniture");
  const marker = "<h2>Resources</h2>";
  if (!article.includes(marker)) throw new Error("Article HTML is missing Resources boundary");
  return article.replace(marker, `${furniture}${marker}`);
}

async function renderPlatform(profile, platform) {
  const dir = path.join(renditionRoot, platform);
  const mdPath = path.join(dir, "article.md");
  const htmlPath = path.join(dir, "article.html");
  const md = await readFile(mdPath, "utf8");
  const html = await readFile(htmlPath, "utf8");
  const nextMd = insertMarkdownFurniture(md, buildFurnitureMarkdown(profile, platform));
  const nextHtml = insertHtmlFurniture(html, buildFurnitureHtml(profile, platform));
  await writeFile(mdPath, nextMd, "utf8");
  await writeFile(htmlPath, nextHtml, "utf8");
}

async function main() {
  const profile = JSON.parse(await readFile(profilePath, "utf8"));
  await renderPlatform(profile, "linkedin");
  await renderPlatform(profile, "medium");
  console.log("Platform author/research furniture added to LinkedIn and Medium renditions");
}

const isEntryPoint = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isEntryPoint) {
  main().catch((error) => {
    console.error(`Platform furniture failed: ${error instanceof Error ? error.message : String(error)}`);
    process.exitCode = 1;
  });
}
