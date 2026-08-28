#!/usr/bin/env node

import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { gitOutput, repoRoot, sha256 } from "./publication-rendition.mjs";

const publicationRoot = path.join(
  repoRoot,
  "dist",
  "publication",
  "thinking-systems",
);
const renditionRoot = path.join(publicationRoot, "renditions");
const mediumAssetRepoPath = "content/research/notes/thinking-systems-platform-assets";
const mediumAssetRoot = path.join(repoRoot, mediumAssetRepoPath);
const rawGithubBase =
  "https://raw.githubusercontent.com/UncertaintyArchitectureGroup/uncertainty-architecture";
const pngDataUriPrefix = "data:image/png;base64";

function isInside(root, candidate) {
  const relative = path.relative(root, candidate);
  return relative === "" || (!relative.startsWith("..") && !path.isAbsolute(relative));
}

function mimeTypeFor(filePath) {
  const extension = path.extname(filePath).toLowerCase();
  if (extension === ".png") return "image/png";
  if (extension === ".jpg" || extension === ".jpeg") return "image/jpeg";
  if (extension === ".webp") return "image/webp";
  throw new Error(`Unsupported copy-ready image type: ${extension || "none"}`);
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function encodedRepoPath(relativePath) {
  return relativePath.split("/").map(encodeURIComponent).join("/");
}

export async function embedLocalImages(html, articlePath, allowedRoot = publicationRoot) {
  const pattern = /<img\b([^>]*?)\bsrc="([^"]+)"([^>]*)>/gi;
  const matches = [...html.matchAll(pattern)];
  let output = html;
  let embedded = 0;

  for (const match of matches) {
    const [full, before, source, after] = match;
    if (/^(?:data:|https?:|mailto:|tel:|#)/i.test(source)) continue;

    const resolved = path.resolve(path.dirname(articlePath), source);
    if (!isInside(allowedRoot, resolved)) {
      throw new Error(`Copy-ready image escapes publication root: ${source}`);
    }
    const bytes = await readFile(resolved);
    if (bytes.length === 0) throw new Error(`Copy-ready image is empty: ${source}`);
    const mimeType = mimeTypeFor(resolved);
    const prefix = mimeType === "image/png" ? pngDataUriPrefix : `data:${mimeType};base64`;
    const dataUri = `${prefix},${bytes.toString("base64")}`;
    output = output.replace(full, `<img${before}src="${dataUri}"${after}>`);
    embedded += 1;
  }

  return { html: output, embedded };
}

export async function replaceMediumImagesWithRemoteSources(
  html,
  articlePath,
  assetCommit,
  allowedRoot = publicationRoot,
) {
  if (!/^[0-9a-f]{40}$/i.test(String(assetCommit))) {
    throw new Error(`Medium asset commit is not a full SHA: ${assetCommit}`);
  }

  const pattern = /<img\b([^>]*?)\bsrc="([^"]+)"([^>]*)>/gi;
  const matches = [...html.matchAll(pattern)];
  let output = html;
  let remote = 0;

  for (const match of matches) {
    const [full, before, source, after] = match;
    if (/^(?:data:|https?:|mailto:|tel:|#)/i.test(source)) continue;

    const resolved = path.resolve(path.dirname(articlePath), source);
    if (!isInside(allowedRoot, resolved)) {
      throw new Error(`Medium copy-ready image escapes publication root: ${source}`);
    }

    const generatedBytes = await readFile(resolved);
    const relative = path.relative(publicationRoot, resolved).split(path.sep).join("/");
    let assetRelative;
    if (relative === "medium-hero.png") {
      assetRelative = `${mediumAssetRepoPath}/medium-hero.png`;
    } else if (relative.startsWith("figures/png/")) {
      assetRelative = `${mediumAssetRepoPath}/figures/${path.posix.basename(relative)}`;
    } else {
      throw new Error(`Medium image has no materialized repository asset mapping: ${relative}`);
    }

    const committedBytes = await readFile(path.join(repoRoot, assetRelative));
    if (!generatedBytes.equals(committedBytes)) {
      throw new Error(
        `Materialized Medium asset is stale: ${assetRelative}. Regenerate platform assets before publishing.`,
      );
    }

    const remoteUrl = `${rawGithubBase}/${assetCommit}/${encodedRepoPath(assetRelative)}`;
    output = output.replace(full, `<img${before}src="${remoteUrl}"${after}>`);
    remote += 1;
  }

  return { html: output, remote };
}

export function appendHeadingLinkFallbacks(html) {
  const headingPattern = /<(h[1-6])([^>]*)>([\s\S]*?)<\/\1>/gi;
  let fallbacks = 0;
  const output = html.replace(
    headingPattern,
    (full, tag, attributes, inner, offset, whole) => {
      const links = [];
      const seen = new Set();
      const linkPattern = /<a\s+[^>]*href="([^"]+)"[^>]*>[\s\S]*?<\/a>/gi;
      for (const match of inner.matchAll(linkPattern)) {
        const target = match[1];
        if (!/^(?:https?:\/\/)/i.test(target) || seen.has(target)) continue;
        seen.add(target);
        links.push(target);
      }
      if (links.length === 0) return full;

      const following = whole.slice(offset + full.length);
      if (/^<p class="heading-link-fallback">/i.test(following)) {
        fallbacks += links.length;
        return full;
      }

      fallbacks += links.length;
      const visibleLinks = links
        .map(
          (target) =>
            `<p class="heading-link-fallback"><a href="${escapeHtml(target)}">${escapeHtml(target)}</a></p>`,
        )
        .join("");
      return `${full}${visibleLinks}`;
    },
  );
  return { html: output, fallbacks };
}

export function buildCopyReadyDocument(html) {
  let value = html
    .replace(
      /<figcaption><strong>Upload file:<\/strong>[\s\S]*?<\/figcaption>/gi,
      "",
    )
    .replace(/<p class="provenance">[\s\S]*?<\/p>/gi, "")
    .replace("<main>", '<main id="copy-surface">');

  if (!value.includes('id="copy-surface"')) {
    throw new Error("Copy-ready source is missing the article <main> element");
  }

  value = value.replace(
    "</style>",
    ".heading-link-fallback{margin:.15em 0 1em;font-size:.92em;overflow-wrap:anywhere}.heading-link-fallback a{color:inherit;text-decoration:underline}\n</style>",
  );
  return value;
}

async function writeCopyReady(platformName) {
  const platformDir = path.join(renditionRoot, platformName);
  const articlePath = path.join(platformDir, "article.html");
  const source = await readFile(articlePath, "utf8");

  let prepared;
  let imageCount;
  let imageStrategy;
  let assetCommit = null;
  if (platformName === "medium") {
    assetCommit = await gitOutput([
      "log",
      "-1",
      "--format=%H",
      "--",
      mediumAssetRepoPath,
    ]);
    const remote = await replaceMediumImagesWithRemoteSources(source, articlePath, assetCommit);
    prepared = remote.html;
    imageCount = remote.remote;
    imageStrategy = "immutable-raw-github-url";
  } else {
    const embedded = await embedLocalImages(source, articlePath);
    prepared = embedded.html;
    imageCount = embedded.embedded;
    imageStrategy = "embedded-data-uri";
  }

  const headingLinks = appendHeadingLinkFallbacks(prepared);
  const copyReady = buildCopyReadyDocument(headingLinks.html);
  const target = path.join(platformDir, "copy-ready.html");
  await writeFile(target, `${copyReady}\n`, "utf8");

  const expected = platformName === "medium" ? 10 : 9;
  if (imageCount !== expected) {
    throw new Error(
      `${platformName} copy-ready HTML prepared ${imageCount} images; expected ${expected}`,
    );
  }
  if (platformName === "medium") {
    if ((copyReady.match(/src="data:image\//g) || []).length !== 0) {
      throw new Error("Medium copy-ready HTML must not contain data-URI images");
    }
    if ((copyReady.match(/src="https:\/\/raw\.githubusercontent\.com\//g) || []).length !== expected) {
      throw new Error("Medium copy-ready HTML does not contain the expected remote image sources");
    }
  } else if ((copyReady.match(/src="data:image\//g) || []).length !== expected) {
    throw new Error("LinkedIn copy-ready HTML still has non-embedded article images");
  }

  return {
    target,
    imageCount,
    imageStrategy,
    assetCommit,
    headingLinkFallbacks: headingLinks.fallbacks,
    sha256: sha256(Buffer.from(`${copyReady}\n`)),
  };
}

async function main() {
  const medium = await writeCopyReady("medium");
  const linkedin = await writeCopyReady("linkedin");

  const readme = `# Copy-ready platform articles\n\nOpen the platform-specific \`copy-ready.html\` in a browser, use **Select All**, then **Copy**, and paste into the native LinkedIn or Medium editor. The copy-ready page intentionally has no JavaScript copy controls because local-file clipboard APIs are not reliable across iPadOS and other browsers.\n\nThe two platforms need different image transport. LinkedIn keeps the nine article figures as embedded data URIs because that copy/paste path preserves them. Medium rejects or strips that representation in practice, so its copy-ready HTML uses ordinary HTTPS image URLs pinned to immutable repository assets at commit \`${medium.assetCommit}\`. Medium can then side-load those images when the rich HTML is pasted. The Medium hero and all nine article figures are materialized under \`${mediumAssetRepoPath}/\` and are byte-checked against the current generated assets before the copy-ready file is emitted.\n\n- LinkedIn: \`linkedin/copy-ready.html\` embeds ${linkedin.imageCount} article figures and preserves ${linkedin.headingLinkFallbacks} heading-link fallback URL(s). The LinkedIn cover remains a separate platform upload.\n- Medium: \`medium/copy-ready.html\` references the hero plus ${medium.imageCount - 1} article figures through immutable HTTPS URLs and preserves ${medium.headingLinkFallbacks} heading-link fallback URL(s).\n- The generated PNG files remain in the CI artifact as a manual-upload fallback if either platform changes its paste sanitizer.\n\nThis convenience artifact is a distribution rendition only; canonical content remains the repository Markdown source.\n`;
  const readmePath = path.join(renditionRoot, "copy-ready-readme.md");
  await writeFile(readmePath, readme, "utf8");

  const manifestPath = path.join(renditionRoot, "platform-renditions.manifest.json");
  const manifest = JSON.parse(await readFile(manifestPath, "utf8"));
  manifest.copy_ready = {
    clipboard_behavior: "manual-select-all-copy",
    javascript_copy_controls: false,
    heading_link_fallbacks: true,
    linkedin_heading_link_fallbacks: linkedin.headingLinkFallbacks,
    medium_heading_link_fallbacks: medium.headingLinkFallbacks,
    linkedin_article_images: linkedin.imageCount,
    medium_article_images: medium.imageCount,
    linkedin_image_strategy: linkedin.imageStrategy,
    medium_image_strategy: medium.imageStrategy,
    medium_asset_commit: medium.assetCommit,
    medium_asset_path: mediumAssetRepoPath,
    linkedin_cover_separate: true,
    png_fallback_retained: true,
  };
  manifest.outputs["linkedin/copy-ready.html"] = linkedin.sha256;
  manifest.outputs["medium/copy-ready.html"] = medium.sha256;
  manifest.outputs["copy-ready-readme.md"] = sha256(Buffer.from(readme));
  await writeFile(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`, "utf8");

  console.log(`Copy-ready LinkedIn HTML: ${path.relative(repoRoot, linkedin.target)} (${linkedin.imageCount} embedded images, ${linkedin.headingLinkFallbacks} heading-link fallback URLs)`);
  console.log(`Copy-ready Medium HTML: ${path.relative(repoRoot, medium.target)} (${medium.imageCount} immutable remote images pinned to ${medium.assetCommit}, ${medium.headingLinkFallbacks} heading-link fallback URLs)`);
}

const isEntryPoint =
  process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isEntryPoint) {
  main().catch((error) => {
    console.error(`Copy-ready rendering failed: ${error instanceof Error ? error.message : String(error)}`);
    process.exitCode = 1;
  });
}
