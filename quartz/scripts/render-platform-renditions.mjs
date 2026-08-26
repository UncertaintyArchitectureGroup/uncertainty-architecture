#!/usr/bin/env node

import { mkdtemp, mkdir, readFile, rename, rm, stat } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import matter from "gray-matter";
import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkGfm from "remark-gfm";
import remarkRehype from "remark-rehype";
import rehypeRaw from "rehype-raw";
import { toHtml } from "hast-util-to-html";
import sharp from "sharp";
import {
  assertSafeOutputPath,
  writeFileAtomically,
} from "./publication-path-safety.mjs";
import { determineSourceProvenance } from "./publication-provenance.mjs";
import {
  currentArticleSource,
  defaultRepository,
  gitOutput,
  loadPublicationSource,
  repoRoot,
  sha256,
} from "./publication-rendition.mjs";
import { assertFigure8SemanticSource } from "./publication-figure8.mjs";
import { assertCanonicalFigure8Fingerprint } from "./publication-figure8-fingerprint.mjs";

const defaultProfile = "quartz/publication/thinking-systems.platforms.json";
const publicationRoot = path.join(repoRoot, "dist", "publication");

function parseArgs(argv) {
  let profile = defaultProfile;
  let allowDirtyPreview = false;
  for (let index = 0; index < argv.length; index += 1) {
    const value = argv[index];
    if (value === "--profile") profile = argv[++index];
    else if (value === "--allow-dirty-preview") allowDirtyPreview = true;
    else if (value === "--help" || value === "-h") return { help: true };
    else throw new Error(`Unknown argument: ${value}`);
  }
  return { profile, allowDirtyPreview, help: false };
}

function usage() {
  console.log(
    "Usage: node quartz/scripts/render-platform-renditions.mjs [--profile quartz/publication/file.json] [--allow-dirty-preview]",
  );
}

export function countCharacters(value) {
  return [...String(value ?? "")].length;
}

function parseTableRow(line) {
  return line
    .trim()
    .replace(/^\|/, "")
    .replace(/\|$/, "")
    .split("|")
    .map((cell) => cell.trim());
}

function isSeparatorRow(line) {
  const cells = parseTableRow(line);
  return cells.length > 0 && cells.every((cell) => /^:?-{3,}:?$/.test(cell));
}

export function convertMarkdownTables(markdown) {
  const lines = markdown.split(/\r?\n/);
  const output = [];
  let index = 0;
  while (index < lines.length) {
    if (
      lines[index]?.trim().startsWith("|") &&
      lines[index + 1]?.trim().startsWith("|") &&
      isSeparatorRow(lines[index + 1])
    ) {
      const headers = parseTableRow(lines[index]);
      index += 2;
      const rows = [];
      while (index < lines.length && lines[index].trim().startsWith("|")) {
        rows.push(parseTableRow(lines[index]));
        index += 1;
      }
      for (const row of rows) {
        output.push(`### ${row[0] || "Item"}`, "");
        for (let column = 1; column < headers.length; column += 1) {
          if (!row[column]) continue;
          output.push(`**${headers[column]}:** ${row[column]}`, "");
        }
      }
      continue;
    }
    output.push(lines[index]);
    index += 1;
  }
  return output.join("\n");
}

function encodeRepositoryPath(value) {
  return value.split("/").map(encodeURIComponent).join("/");
}

export function rewriteRelativeLinks(
  markdown,
  sourceRelative,
  repository,
  sourceCommit,
) {
  const sourceDirectory = path.posix.dirname(sourceRelative);
  return markdown.replace(
    /\[([^\]]+)\]\(([^)\s]+)(?:\s+"[^"]*")?\)/g,
    (full, label, target) => {
      if (/^(?:https?:|mailto:|tel:|#)/i.test(target)) return full;
      const [pathname, fragment = ""] = target.split("#", 2);
      const resolved = path.posix.normalize(
        path.posix.join(sourceDirectory, pathname),
      );
      if (resolved.startsWith("../")) {
        throw new Error(
          `Platform rendition link escapes repository root: ${target}`,
        );
      }
      const suffix = fragment ? `#${encodeURIComponent(fragment)}` : "";
      return `[${label}](https://github.com/${repository}/blob/${encodeURIComponent(sourceCommit)}/${encodeRepositoryPath(resolved)}${suffix})`;
    },
  );
}

export function extractLaunchPost(raw) {
  const parsed = matter(raw);
  const match =
    /<!-- platform-copy:start -->\s*([\s\S]*?)\s*<!-- platform-copy:end -->/.exec(
      parsed.content,
    );
  if (!match)
    throw new Error(
      "LinkedIn launch-post source is missing platform-copy markers",
    );
  return match[1].trim();
}

export function stripCanonicalHeadingAndNote(content) {
  let value = content.replace(/^\uFEFF?[ \t\r\n]*#\s+[^\r\n]+\r?\n+/, "");
  value = value.replace(
    /^>\s+\*\*Publication note\.\*\*[^\n]*(?:\n>[^\n]*)*\n+/m,
    "",
  );
  value = value.replace(/\n## Continue the work\s*\n[\s\S]*$/, "\n");
  return value;
}

export function replaceMermaidWithFigureTokens(
  markdown,
  { verifyFigure8 = true } = {},
) {
  const seen = [];
  const pattern =
    /```mermaid\r?\n([\s\S]*?)\r?\n```\r?\n\r?\n(\*\*Figure\s+(\d+)\s+—[^\n]*)/g;
  const replaced = markdown.replace(
    pattern,
    (full, mermaid, caption, numberText) => {
      const number = Number(numberText);
      seen.push(number);
      if (number === 8) {
        assertFigure8SemanticSource(mermaid);
        if (verifyFigure8) assertCanonicalFigure8Fingerprint(mermaid, caption);
        return `@@UA_FIGURE_08A@@\n\n@@UA_FIGURE_08B@@\n\n${caption}`;
      }
      const id = String(number).padStart(2, "0");
      return `@@UA_FIGURE_${id}@@\n\n${caption}`;
    },
  );
  if (/```mermaid/.test(replaced)) {
    throw new Error(
      "A Mermaid block without a publication caption remains in the rendition",
    );
  }
  const expected = [1, 2, 3, 4, 5, 6, 7, 8];
  if (JSON.stringify(seen) !== JSON.stringify(expected)) {
    throw new Error(
      `Expected canonical Figures 1–8 in order; received ${seen.join(", ")}`,
    );
  }
  return replaced;
}

export function extractCanonicalFigure8Caption(markdown) {
  const match = /^(\*\*Figure 8 —[^\n]+)$/m.exec(markdown);
  if (!match) throw new Error("Canonical Figure 8 caption is missing");
  return match[1];
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function figureId(asset) {
  return `${String(asset.number).padStart(2, "0")}${String(asset.panel || "").toLowerCase()}`;
}

export function buildAssetMap(assetManifest) {
  return new Map(
    (assetManifest.figures || []).map((asset) => [figureId(asset), asset]),
  );
}

function figureImageRelativePath(asset) {
  const basename = path.posix.basename(asset.png_path);
  return `../../figures/png/${basename}`;
}

function buildFigureHtml(id, profile, assetMap) {
  const alt = profile.figures[id]?.alt;
  const asset = assetMap.get(id);
  if (!alt || !asset)
    throw new Error(`Missing figure metadata or asset for ${id}`);
  return `<figure class="platform-figure" data-figure-id="${id}"><img src="${figureImageRelativePath(asset)}" alt="${escapeHtml(alt)}"/><figcaption><strong>Upload file:</strong> ${escapeHtml(path.posix.basename(asset.png_path))}</figcaption></figure>`;
}

function buildFigureMarkdown(id, profile, assetMap) {
  const alt = profile.figures[id]?.alt;
  const asset = assetMap.get(id);
  if (!alt || !asset)
    throw new Error(`Missing figure metadata or asset for ${id}`);
  return `> **UPLOAD IMAGE:** \`${figureImageRelativePath(asset)}\`\n>\n> **Alt text:** ${alt}`;
}

async function markdownToHtml(markdown) {
  const mdast = unified().use(remarkParse).use(remarkGfm).parse(markdown);
  const hast = await unified()
    .use(remarkRehype, { allowDangerousHtml: true })
    .use(rehypeRaw)
    .run(mdast);
  return toHtml(hast, { allowDangerousHtml: true });
}

export function applyFigureHtmlMarkdown(markdown, profile, assetMap) {
  for (const id of ["01", "02", "03", "04", "05", "06", "07", "08a", "08b"]) {
    const token = `@@UA_FIGURE_${id.toUpperCase()}@@`;
    if (!markdown.includes(token))
      throw new Error(`Platform HTML source is missing figure token ${id}`);
    markdown = markdown.replace(token, buildFigureHtml(id, profile, assetMap));
  }
  return markdown;
}

function applyFigureMarkdown(markdown, profile, assetMap) {
  for (const id of ["01", "02", "03", "04", "05", "06", "07", "08a", "08b"]) {
    const token = `@@UA_FIGURE_${id.toUpperCase()}@@`;
    if (!markdown.includes(token))
      throw new Error(`Platform Markdown is missing figure token ${id}`);
    markdown = markdown.replace(
      token,
      buildFigureMarkdown(id, profile, assetMap),
    );
  }
  return markdown;
}

function decodeEntities(value) {
  return value
    .replaceAll("&amp;", "&")
    .replaceAll("&lt;", "<")
    .replaceAll("&gt;", ">")
    .replaceAll("&quot;", '"')
    .replaceAll("&#39;", "'")
    .replaceAll("&nbsp;", " ");
}

export function htmlToPlainText(html) {
  return decodeEntities(
    html
      .replace(
        /<figure[^>]*data-figure-id="([^"]+)"[^>]*>[\s\S]*?<\/figure>/g,
        "\n\n[UPLOAD IMAGE: figure-$1]\n\n",
      )
      .replace(/<a\s+href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/g, "$2 ($1)")
      .replace(/<li[^>]*>/g, "\n- ")
      .replace(
        /<\/(?:p|h1|h2|h3|h4|blockquote|li|ul|ol|section|div|figure)>/g,
        "\n\n",
      )
      .replace(/<br\s*\/?\s*>/g, "\n")
      .replace(/<[^>]+>/g, "")
      .replace(/[ \t]+\n/g, "\n")
      .replace(/\n{3,}/g, "\n\n")
      .trim(),
  );
}

export function standaloneHtml({
  title,
  subtitle,
  hero,
  body,
  sourceCommit,
  sourceState,
}) {
  const heroHtml = hero
    ? `<img class="platform-hero" src="../../${escapeHtml(hero)}" alt=""/>`
    : "";
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>${escapeHtml(title)}</title>
<style>
body{font-family:Arial,sans-serif;line-height:1.55;color:#202124;margin:0;background:#f3f4f5}main{max-width:820px;margin:0 auto;background:white;padding:48px 56px}h1{font-size:42px;line-height:1.12}h2{margin-top:2.2em}h3{margin-top:1.5em}main>blockquote:first-of-type{font-size:21px;color:#51606a}.platform-hero,.platform-figure img{display:block;max-width:100%;height:auto;margin:24px auto}.platform-figure{margin:36px 0}.platform-figure figcaption{font-size:13px;color:#667}blockquote{margin-left:0;border-left:4px solid #d3d8dc;padding-left:16px}.provenance{margin-top:48px;font-size:12px;color:#778}</style>
</head>
<body><main>${heroHtml}${body}<p class="provenance">Generated from source commit ${escapeHtml(sourceCommit)} · source state ${escapeHtml(sourceState)}</p></main></body>
</html>`;
}

function repositoryUrl(repository, sourceCommit, targetPath = "") {
  if (!targetPath) return `https://github.com/${repository}`;
  return `https://github.com/${repository}/blob/${encodeURIComponent(sourceCommit)}/${encodeRepositoryPath(targetPath)}`;
}

function buildResourceBlock(profile, sourceCommit) {
  const lines = ["## Resources", ""];
  for (const resource of profile.resources || []) {
    lines.push(
      `- [${resource.label}](${repositoryUrl(profile.repository, sourceCommit, resource.path)})`,
    );
  }
  return lines.join("\n");
}

export function buildPlatformMarkdown(base, platform, profile, sourceCommit) {
  return [
    `# ${platform.title}`,
    "",
    `> ${platform.subtitle}`,
    "",
    `> **Publication note.** ${platform.publication_note}`,
    "",
    base,
    "",
    buildResourceBlock(profile, sourceCommit),
    "",
  ].join("\n");
}

export function buildCandidatePublicationState(source, sourceCommit) {
  return {
    publication_state: "candidate",
    publication_ready: false,
    candidate_source_commit: sourceCommit,
    canonical_url: source.data.canonical_url || null,
    additional_publication_urls: Array.isArray(source.data.additional_publication_urls)
      ? source.data.additional_publication_urls
      : [],
  };
}

export function validateProfile(profile) {
  if (profile.schema_version !== 1)
    throw new Error("Unsupported platform-profile schema");
  if (profile.source !== currentArticleSource) {
    throw new Error(
      "Current profile must target the standalone Thinking Systems article",
    );
  }
  if (
    countCharacters(profile.linkedin.seo_title) >
    profile.linkedin.seo_title_max_characters
  ) {
    throw new Error("LinkedIn SEO title exceeds configured limit");
  }
  const descriptionLength = countCharacters(profile.linkedin.seo_description);
  if (
    descriptionLength < profile.linkedin.seo_description_min_characters ||
    descriptionLength > profile.linkedin.seo_description_max_characters
  ) {
    throw new Error("LinkedIn SEO description is outside the configured range");
  }
  for (const id of ["01", "02", "03", "04", "05", "06", "07", "08a", "08b"]) {
    if (!profile.figures[id]?.alt)
      throw new Error(`Missing alt text for figure ${id}`);
  }
  return profile;
}

async function assertFileDimensions(filePath, width, height, maxBytes = null) {
  const info = await stat(filePath);
  if (!info.isFile() || info.size === 0)
    throw new Error(`Missing generated image: ${filePath}`);
  if (maxBytes && info.size > maxBytes) {
    throw new Error(`Generated image exceeds platform byte limit: ${filePath}`);
  }
  const metadata = await sharp(filePath).metadata();
  if (metadata.width !== width || metadata.height !== height) {
    throw new Error(
      `${path.basename(filePath)} is ${metadata.width}×${metadata.height}; expected ${width}×${height}`,
    );
  }
}

export function verifyAssetManifest(manifest, profile, source) {
  if (manifest.artifact !== "publication-platform-assets") {
    throw new Error("Unexpected publication asset manifest type");
  }
  if (manifest.source_path !== profile.source) {
    throw new Error("Asset manifest source does not match platform profile");
  }
  if (manifest.source_content_sha256 !== sha256(Buffer.from(source.raw))) {
    throw new Error(
      "Asset manifest source digest does not match current article source",
    );
  }
  const assetMap = buildAssetMap(manifest);
  const expected = ["01", "02", "03", "04", "05", "06", "07", "08a", "08b"];
  for (const id of expected) {
    if (!assetMap.has(id))
      throw new Error(`Asset manifest is missing figure ${id}`);
    const asset = assetMap.get(id);
    if (asset.png_renderer !== "chromium") {
      throw new Error(`Figure ${id} is not rasterized by Chromium`);
    }
    if (asset.png_background !== "#ffffff" || asset.png_has_alpha !== false) {
      throw new Error(
        `Figure ${id} is not an opaque white-background upload PNG`,
      );
    }
  }
  const a = assetMap.get("08a");
  const b = assetMap.get("08b");
  if (
    !a.semantic_fingerprint ||
    a.semantic_fingerprint !== b.semantic_fingerprint
  ) {
    throw new Error(
      "Figure 8A/8B assets are not coupled to one semantic fingerprint",
    );
  }
  const heroMap = new Map(
    (manifest.heroes || []).map((hero) => [hero.key, hero]),
  );
  for (const key of [
    "linkedin_article_cover",
    "social_preview",
    "medium_hero",
  ]) {
    if (!heroMap.has(key)) throw new Error(`Asset manifest is missing ${key}`);
  }
  return { assetMap, heroMap };
}

async function finalizeDirectory(stagingRoot, destinationRoot) {
  await assertSafeOutputPath(repoRoot, publicationRoot, destinationRoot, {
    allowRoot: false,
    createParent: true,
  });
  const backupRoot = `${destinationRoot}.ua-backup-${process.pid}-${Date.now()}`;
  let previous = false;
  try {
    const existing = await stat(destinationRoot).catch((error) => {
      if (error?.code === "ENOENT") return null;
      throw error;
    });
    if (existing) {
      if (!existing.isDirectory())
        throw new Error("Existing rendition destination is not a directory");
      await rename(destinationRoot, backupRoot);
      previous = true;
    }
    await rename(stagingRoot, destinationRoot);
    if (previous) await rm(backupRoot, { recursive: true, force: true });
  } catch (error) {
    await rm(destinationRoot, { recursive: true, force: true }).catch(() => {});
    if (previous) await rename(backupRoot, destinationRoot).catch(() => {});
    throw error;
  }
}

function buildChecklist(
  platformName,
  profile,
  source,
  sourceCommit,
  publicationReady,
) {
  const platform = profile[platformName];
  const official = profile.official_sources;
  const lines = [
    `# ${platformName === "linkedin" ? "LinkedIn" : "Medium"} Publishing Checklist`,
    "",
    `- Source: \`${source.relative}\``,
    `- Source commit: \`${sourceCommit}\``,
    `- Package state: ${publicationReady ? "published edition" : "CANDIDATE — generated from the editable publication draft; publication itself comes before repository freeze"}`,
    "- Review `article.html` and the native platform preview before publishing.",
    "- Use `article.md` as the image-placement and alt-text guide.",
    "- Upload every image named by an `UPLOAD IMAGE` marker; do not paste Mermaid source.",
    "- Recheck links, captions, table conversion, and the Figure 8A/8B sequence.",
  ];
  if (platformName === "linkedin") {
    lines.push(
      "- Upload `../../cover-linkedin-article.png` as the article cover.",
      "- Apply `seo.json` in LinkedIn SEO settings.",
      "- Publish the native LinkedIn article first, copy its exact URL, and replace `{{LINKEDIN_ARTICLE_URL}}` in `launch-post.txt` before publishing the launch post.",
      "- Convert the names in `launch-post.txt` into actual LinkedIn mentions before publishing the launch post.",
      `- Keep the launch post at or below ${profile.linkedin.post_max_characters} characters after replacing the URL placeholder.`,
      "- Verify the generated labeled-section replacement for source tables.",
      "",
      `Official references: ${official.linkedin_article_limits} · ${official.linkedin_article_images} · ${official.linkedin_seo}`,
    );
  } else {
    lines.push(
      "- Upload `../../medium-hero.png` as the story hero.",
      "- After the first external publication establishes the principal canonical URL, use Medium import from that URL where appropriate or set the canonical URL manually.",
      "- Confirm each uploaded figure meets the 1,192 px minimum when full placement options are needed.",
      "",
      `Official references: ${official.medium_images} · ${official.medium_import} · ${official.medium_canonical}`,
    );
  }
  return `${lines.join("\n")}\n`;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) return usage();

  const profilePath = path.resolve(repoRoot, args.profile);
  const profileRaw = await readFile(profilePath, "utf8");
  const profile = validateProfile(JSON.parse(profileRaw));
  const source = await loadPublicationSource(profile.source);
  const sourceReference =
    process.env.UA_PDF_REPOSITORY_REF ||
    process.env.GITHUB_SHA ||
    (await gitOutput(["rev-parse", "HEAD"]));
  const provenance = await determineSourceProvenance(source, sourceReference, {
    allowDirtyPreview: args.allowDirtyPreview,
  });
  const sourceCommit = provenance.sourceCommit;
  profile.repository =
    process.env.GITHUB_REPOSITORY || profile.repository || defaultRepository;

  const outputRoot = path.resolve(repoRoot, profile.output_root);
  await assertSafeOutputPath(repoRoot, publicationRoot, outputRoot, {
    allowRoot: false,
  });
  const assetsManifestPath = path.join(outputRoot, "assets.manifest.json");
  const assetsManifestRaw = await readFile(assetsManifestPath, "utf8").catch(
    () => null,
  );
  if (!assetsManifestRaw) {
    throw new Error(
      "Publication assets are missing. Run npm run publication:assets first.",
    );
  }
  const assetsManifest = JSON.parse(assetsManifestRaw);
  const { assetMap } = verifyAssetManifest(assetsManifest, profile, source);

  await assertFileDimensions(
    path.join(outputRoot, profile.linkedin.cover.file),
    profile.linkedin.cover.width,
    profile.linkedin.cover.height,
    profile.linkedin.cover.max_bytes,
  );
  await assertFileDimensions(
    path.join(outputRoot, profile.linkedin.social_preview.file),
    profile.linkedin.social_preview.width,
    profile.linkedin.social_preview.height,
  );
  await assertFileDimensions(
    path.join(outputRoot, profile.medium.hero.file),
    profile.medium.hero.width,
    profile.medium.hero.height,
    profile.medium.image_max_bytes,
  );
  for (const asset of assetsManifest.figures || []) {
    const filePath = path.resolve(repoRoot, asset.png_path);
    const info = await stat(filePath);
    if (info.size > profile.medium.image_max_bytes) {
      throw new Error(`Figure exceeds Medium image limit: ${asset.png_path}`);
    }
    if (asset.png_width < profile.medium.image_min_width) {
      throw new Error(
        `Figure is too narrow for Medium full placement: ${asset.png_path}`,
      );
    }
  }

  let baseMarkdown = stripCanonicalHeadingAndNote(source.content);
  const figure8Caption = extractCanonicalFigure8Caption(baseMarkdown);
  baseMarkdown = replaceMermaidWithFigureTokens(baseMarkdown);
  baseMarkdown = convertMarkdownTables(baseMarkdown);
  baseMarkdown = rewriteRelativeLinks(
    baseMarkdown,
    source.relative,
    profile.repository,
    sourceCommit,
  );

  const launchPath = path.resolve(repoRoot, profile.launch_post_source);
  const launchRaw = await readFile(launchPath, "utf8");
  const launchPost = extractLaunchPost(launchRaw);
  if (!launchPost.includes("{{LINKEDIN_ARTICLE_URL}}")) {
    throw new Error(
      "LinkedIn launch post must contain {{LINKEDIN_ARTICLE_URL}} so the post can be bound to the exact native article after publication",
    );
  }
  const launchCharacters = countCharacters(launchPost);
  if (launchCharacters > profile.linkedin.post_max_characters) {
    throw new Error(
      `LinkedIn launch post is ${launchCharacters} characters; limit is ${profile.linkedin.post_max_characters}`,
    );
  }
  if (launchCharacters > profile.linkedin.post_target_max_characters) {
    throw new Error(
      `LinkedIn launch post exceeds the review target: ${launchCharacters} characters`,
    );
  }
  const launchReserve = profile.linkedin.post_url_mention_reserve_characters;
  if (!Number.isInteger(launchReserve) || launchReserve < 0) {
    throw new Error("LinkedIn URL/mention reserve must be a non-negative integer");
  }
  if (launchCharacters + launchReserve > profile.linkedin.post_max_characters) {
    throw new Error(
      `LinkedIn launch post leaves less than the configured ${launchReserve}-character URL/mention reserve`,
    );
  }

  const mediumBaseMarkdown = buildPlatformMarkdown(
    baseMarkdown,
    profile.medium,
    profile,
    sourceCommit,
  );
  const linkedinBaseMarkdown = buildPlatformMarkdown(
    baseMarkdown,
    profile.linkedin,
    profile,
    sourceCommit,
  );
  const mediumMarkdown = applyFigureMarkdown(
    mediumBaseMarkdown,
    profile,
    assetMap,
  );
  const linkedinMarkdown = applyFigureMarkdown(
    linkedinBaseMarkdown,
    profile,
    assetMap,
  );
  const mediumBody = await markdownToHtml(
    applyFigureHtmlMarkdown(mediumBaseMarkdown, profile, assetMap),
  );
  const linkedinBody = await markdownToHtml(
    applyFigureHtmlMarkdown(linkedinBaseMarkdown, profile, assetMap),
  );
  const mediumHtml = standaloneHtml({
    title: profile.medium.title,
    subtitle: profile.medium.subtitle,
    hero: profile.medium.hero.file,
    body: mediumBody,
    sourceCommit,
    sourceState: provenance.state,
  });
  const linkedinHtml = standaloneHtml({
    title: profile.linkedin.title,
    subtitle: profile.linkedin.subtitle,
    hero: null,
    body: linkedinBody,
    sourceCommit,
    sourceState: provenance.state,
  });
  const mediumText = htmlToPlainText(mediumBody);
  const linkedinText = htmlToPlainText(linkedinBody);
  const linkedinArticleCharacters = countCharacters(linkedinText);
  if (linkedinArticleCharacters > profile.linkedin.article_max_characters) {
    throw new Error(
      `LinkedIn article is ${linkedinArticleCharacters} characters; limit is ${profile.linkedin.article_max_characters}`,
    );
  }
  if (/<table\b/i.test(linkedinHtml) || /```mermaid/.test(linkedinMarkdown)) {
    throw new Error(
      "LinkedIn rendition still contains an unsupported table or Mermaid source",
    );
  }

  const publicationState = buildCandidatePublicationState(source, sourceCommit);
  const publicationReady = publicationState.publication_ready;
  const canonicalText = source.data.canonical_url
    ? `${source.data.canonical_url}\n`
    : `PENDING — publish the first external rendition, then immediately preserve the exact published edition under content/research/publications/ and record canonical_url before feedback-driven revision.\nCurrent versioned candidate source: ${repositoryUrl(profile.repository, sourceCommit, source.relative)}\n`;

  const stagingRoot = await mkdtemp(
    path.join(outputRoot, ".ua-platform-stage-"),
  );
  const renditionRoot = path.join(outputRoot, "renditions");
  try {
    const mediumDir = path.join(stagingRoot, "medium");
    const linkedinDir = path.join(stagingRoot, "linkedin");
    await mkdir(mediumDir, { recursive: true });
    await mkdir(linkedinDir, { recursive: true });

    const writes = [
      [path.join(mediumDir, "article.md"), `${mediumMarkdown}\n`],
      [path.join(mediumDir, "article.html"), `${mediumHtml}\n`],
      [path.join(mediumDir, "article.txt"), `${mediumText}\n`],
      [path.join(mediumDir, "canonical-url.txt"), canonicalText],
      [
        path.join(mediumDir, "publishing-checklist.md"),
        buildChecklist(
          "medium",
          profile,
          source,
          sourceCommit,
          publicationReady,
        ),
      ],
      [path.join(linkedinDir, "article.md"), `${linkedinMarkdown}\n`],
      [path.join(linkedinDir, "article.html"), `${linkedinHtml}\n`],
      [path.join(linkedinDir, "article.txt"), `${linkedinText}\n`],
      [path.join(linkedinDir, "launch-post.txt"), `${launchPost}\n`],
      [
        path.join(linkedinDir, "seo.json"),
        `${JSON.stringify(
          {
            title: profile.linkedin.seo_title,
            description: profile.linkedin.seo_description,
          },
          null,
          2,
        )}\n`,
      ],
      [
        path.join(linkedinDir, "publishing-checklist.md"),
        buildChecklist(
          "linkedin",
          profile,
          source,
          sourceCommit,
          publicationReady,
        ),
      ],
      [
        path.join(stagingRoot, "figure-08-shared-caption.md"),
        `${figure8Caption}\n`,
      ],
    ];

    const outputDigests = {};
    for (const [target, value] of writes) {
      await writeFileAtomically(target, value, {
        trustedRoot: repoRoot,
        allowedRoot: publicationRoot,
        forbiddenPaths: [source.absolute, launchPath],
      });
      outputDigests[
        path.relative(stagingRoot, target).split(path.sep).join("/")
      ] = sha256(Buffer.from(value));
    }

    const manifest = {
      schema_version: 1,
      artifact: "platform-renditions",
      publication_id: profile.publication_id,
      source_path: source.relative,
      source_commit: sourceCommit,
      source_state: provenance.state,
      source_git_blob_sha: provenance.committedBlob,
      source_working_blob_sha: provenance.workingBlob,
      source_sha256: sha256(Buffer.from(source.raw)),
      launch_post_sha256: sha256(Buffer.from(launchRaw)),
      platform_profile_sha256: sha256(Buffer.from(profileRaw)),
      assets_manifest_sha256: sha256(Buffer.from(assetsManifestRaw)),
      generated_at: new Date().toISOString(),
      publication_state: publicationState.publication_state,
      publication_ready: publicationReady,
      candidate_source_commit: publicationState.candidate_source_commit,
      canonical_url: publicationState.canonical_url,
      additional_publication_urls: publicationState.additional_publication_urls,
      launch_post_article_url_binding: "required-placeholder",
      linkedin_article_characters: linkedinArticleCharacters,
      linkedin_launch_post_characters: launchCharacters,
      linkedin_post_limit: profile.linkedin.post_max_characters,
      linkedin_post_url_mention_reserve_characters: launchReserve,
      linkedin_launch_post_reserved_total: launchCharacters + launchReserve,
      linkedin_article_limit: profile.linkedin.article_max_characters,
      figure_8_panels_must_travel_together: true,
      figure_8_semantic_fingerprint: assetMap.get("08a").semantic_fingerprint,
      outputs: outputDigests,
    };
    const manifestValue = `${JSON.stringify(manifest, null, 2)}\n`;
    await writeFileAtomically(
      path.join(stagingRoot, "platform-renditions.manifest.json"),
      manifestValue,
      {
        trustedRoot: repoRoot,
        allowedRoot: publicationRoot,
        forbiddenPaths: [source.absolute, launchPath],
      },
    );
    await finalizeDirectory(stagingRoot, renditionRoot);
  } finally {
    await rm(stagingRoot, { recursive: true, force: true });
  }

  console.log(
    `Platform renditions ready: ${path.relative(repoRoot, renditionRoot)}`,
  );
  console.log(
    `LinkedIn article: ${linkedinArticleCharacters}/${profile.linkedin.article_max_characters} characters`,
  );
  console.log(
    `LinkedIn launch post: ${launchCharacters}/${profile.linkedin.post_max_characters} characters (+${launchReserve} reserved for final URL/mentions)`,
  );
  if (!publicationReady) {
    console.log(
      "Publication readiness: candidate package; publish first, then freeze the exact external edition before feedback-driven revision",
    );
  }
}

const isEntryPoint =
  process.argv[1] &&
  path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isEntryPoint) {
  main().catch((error) => {
    console.error(
      `Platform rendition failed: ${error instanceof Error ? error.message : String(error)}`,
    );
    process.exitCode = 1;
  });
}
