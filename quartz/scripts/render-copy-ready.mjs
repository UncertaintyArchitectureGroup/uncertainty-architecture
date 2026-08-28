#!/usr/bin/env node

import { copyFile, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { repoRoot, sha256 } from "./publication-rendition.mjs";

const publicationRoot = path.join(
  repoRoot,
  "dist",
  "publication",
  "thinking-systems",
);
const renditionRoot = path.join(publicationRoot, "renditions");
const pngDataUriPrefix = "data:image/png;base64";

function isInside(root, candidate) {
  const relative = path.relative(root, candidate);
  return (
    relative === "" ||
    (!relative.startsWith("..") && !path.isAbsolute(relative))
  );
}

function mimeTypeFor(filePath) {
  const extension = path.extname(filePath).toLowerCase();
  if (extension === ".png") return "image/png";
  if (extension === ".jpg" || extension === ".jpeg") return "image/jpeg";
  if (extension === ".webp") return "image/webp";
  throw new Error(
    `Unsupported copy-ready image type: ${extension || "none"}`,
  );
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

export async function embedLocalImages(
  html,
  articlePath,
  allowedRoot = publicationRoot,
) {
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
    if (bytes.length === 0) {
      throw new Error(`Copy-ready image is empty: ${source}`);
    }
    const mimeType = mimeTypeFor(resolved);
    const prefix =
      mimeType === "image/png" ? pngDataUriPrefix : `data:${mimeType};base64`;
    const dataUri = `${prefix},${bytes.toString("base64")}`;
    output = output.replace(full, `<img${before}src="${dataUri}"${after}>`);
    embedded += 1;
  }

  return { html: output, embedded };
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
        if (!/^(?:https?:\/\/)/i.test(target) || seen.has(target)) {
          continue;
        }
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

function figureIdentity(asset) {
  return `${String(asset.number).padStart(2, "0")}${String(
    asset.panel || "",
  ).toLowerCase()}`;
}

export function buildMediumUploadPlan(assetManifest) {
  const figures = [...(assetManifest.figures || [])].sort((left, right) => {
    if (left.number !== right.number) return left.number - right.number;
    return String(left.panel || "").localeCompare(String(right.panel || ""));
  });
  if (figures.length !== 9) {
    throw new Error(
      `Medium upload kit requires nine article figures; received ${figures.length}`,
    );
  }

  const entries = [
    {
      order: 0,
      id: "hero",
      label: "Medium hero",
      source: path.join(publicationRoot, "medium-hero.png"),
      filename: "00-medium-hero.png",
    },
  ];

  figures.forEach((asset, index) => {
    const id = figureIdentity(asset);
    const panel = asset.panel ? String(asset.panel).toLowerCase() : "";
    entries.push({
      order: index + 1,
      id,
      label: `Figure ${asset.number}${asset.panel || ""}`,
      source: path.resolve(repoRoot, asset.png_path),
      filename: `${String(index + 1).padStart(2, "0")}-figure-${String(
        asset.number,
      ).padStart(2, "0")}${panel}.png`,
    });
  });

  return entries;
}

async function writeMediumUploadKit() {
  const assetManifestPath = path.join(publicationRoot, "assets.manifest.json");
  const assetManifest = JSON.parse(await readFile(assetManifestPath, "utf8"));
  const entries = buildMediumUploadPlan(assetManifest);
  const uploadRoot = path.join(renditionRoot, "medium", "upload");
  await rm(uploadRoot, { recursive: true, force: true });
  await mkdir(uploadRoot, { recursive: true });

  const outputs = [];
  for (const entry of entries) {
    if (!isInside(publicationRoot, entry.source)) {
      throw new Error(
        `Medium upload source escapes publication root: ${entry.source}`,
      );
    }
    const target = path.join(uploadRoot, entry.filename);
    await copyFile(entry.source, target);
    const bytes = await readFile(target);
    if (bytes.length === 0) {
      throw new Error(`Medium upload asset is empty: ${entry.filename}`);
    }
    outputs.push({
      order: entry.order,
      id: entry.id,
      label: entry.label,
      path: `medium/upload/${entry.filename}`,
      sha256: sha256(bytes),
    });
  }

  const readme = `# Medium image upload order

Practical iPad testing showed that Medium preserves the pasted rich text but drops clipboard images. The self-contained \`../copy-ready.html\` therefore remains the complete visual review and text-copy surface, while images must be uploaded separately.

1. Open \`../copy-ready.html\`, confirm that the hero and all nine figures are visible, then use **Select All → Copy → Paste** for the article text.
2. Use \`../article.md\` for the exact image positions and alt text.
3. Upload these files in order:

${outputs
  .map(
    (entry, index) =>
      `${index + 1}. **${entry.label}** — \`${path.posix.basename(entry.path)}\``,
  )
  .join("\n")}

Figure 8A and Figure 8B are two panels of one logical Figure 8. Both must be uploaded and kept with the shared Figure 8 caption.

These files are generated from the same reviewed platform assets as the article rendition. They are distribution assets, not an additional conceptual source.
`;
  const readmePath = path.join(uploadRoot, "README.md");
  await writeFile(readmePath, readme, "utf8");
  outputs.push({
    order: outputs.length,
    id: "instructions",
    label: "Medium upload instructions",
    path: "medium/upload/README.md",
    sha256: sha256(Buffer.from(readme)),
  });

  return { outputs, readme };
}

async function writeCopyReady(platformName) {
  const platformDir = path.join(renditionRoot, platformName);
  const articlePath = path.join(platformDir, "article.html");
  const source = await readFile(articlePath, "utf8");
  const embedded = await embedLocalImages(source, articlePath);
  const headingLinks = appendHeadingLinkFallbacks(embedded.html);
  const copyReady = buildCopyReadyDocument(headingLinks.html);
  const target = path.join(platformDir, "copy-ready.html");
  await writeFile(target, `${copyReady}\n`, "utf8");

  const expected = platformName === "medium" ? 10 : 9;
  if (embedded.embedded !== expected) {
    throw new Error(
      `${platformName} copy-ready HTML embedded ${embedded.embedded} images; expected ${expected}`,
    );
  }
  if ((copyReady.match(/src="data:image\//g) || []).length !== expected) {
    throw new Error(
      `${platformName} copy-ready HTML still has non-embedded article images`,
    );
  }
  if (/raw\.githubusercontent\.com/i.test(copyReady)) {
    throw new Error(
      `${platformName} copy-ready HTML unexpectedly depends on remote repository images`,
    );
  }

  return {
    target,
    embedded: embedded.embedded,
    headingLinkFallbacks: headingLinks.fallbacks,
    sha256: sha256(Buffer.from(`${copyReady}\n`)),
  };
}

async function main() {
  const medium = await writeCopyReady("medium");
  const linkedin = await writeCopyReady("linkedin");
  const mediumUpload = await writeMediumUploadKit();

  const readme = `# Copy-ready platform articles

Open the platform-specific \`copy-ready.html\` in a browser, use **Select All**, then **Copy**, and paste into the native editor. The pages intentionally have no JavaScript copy controls because local-file clipboard APIs are not reliable across iPadOS and other browsers.

Both pages are self-contained and display their article images through embedded data URIs.

- **LinkedIn:** the tested paste path preserves ${linkedin.embedded} embedded article figures. The native article cover remains a separate upload.
- **Medium:** the page displays the hero plus ${medium.embedded - 1} article figures, but practical iPad testing showed that Medium drops clipboard images while preserving the rich text. Copy the text, then upload the ten ordered PNG files from \`medium/upload/\` using \`medium/article.md\` as the exact placement and alt-text guide.
- Both renditions preserve heading-link fallback URLs immediately below linked headings.

This package is a distribution rendition only; canonical content remains the repository Markdown source.
`;
  const readmePath = path.join(renditionRoot, "copy-ready-readme.md");
  await writeFile(readmePath, readme, "utf8");

  const manifestPath = path.join(
    renditionRoot,
    "platform-renditions.manifest.json",
  );
  const manifest = JSON.parse(await readFile(manifestPath, "utf8"));
  manifest.copy_ready = {
    self_contained_html: true,
    clipboard_behavior: "manual-select-all-copy",
    javascript_copy_controls: false,
    heading_link_fallbacks: true,
    linkedin_heading_link_fallbacks: linkedin.headingLinkFallbacks,
    medium_heading_link_fallbacks: medium.headingLinkFallbacks,
    linkedin_article_images: linkedin.embedded,
    medium_article_images: medium.embedded,
    linkedin_image_strategy: "embedded-data-uri",
    medium_image_strategy: "embedded-data-uri-preview",
    medium_clipboard_images_supported: false,
    medium_manual_upload_required: true,
    medium_upload_asset_count: 10,
    medium_upload_kit: "medium/upload/README.md",
    medium_upload_assets: mediumUpload.outputs,
    linkedin_cover_separate: true,
    png_fallback_retained: true,
  };
  manifest.outputs["linkedin/copy-ready.html"] = linkedin.sha256;
  manifest.outputs["medium/copy-ready.html"] = medium.sha256;
  manifest.outputs["copy-ready-readme.md"] = sha256(Buffer.from(readme));
  for (const output of mediumUpload.outputs) {
    manifest.outputs[output.path] = output.sha256;
  }
  await writeFile(
    manifestPath,
    `${JSON.stringify(manifest, null, 2)}\n`,
    "utf8",
  );

  console.log(
    `Copy-ready LinkedIn HTML: ${path.relative(repoRoot, linkedin.target)} (${linkedin.embedded} embedded images, ${linkedin.headingLinkFallbacks} heading-link fallback URLs)`,
  );
  console.log(
    `Copy-ready Medium HTML: ${path.relative(repoRoot, medium.target)} (${medium.embedded} embedded review images, manual upload kit with ${mediumUpload.outputs.length - 1} PNGs, ${medium.headingLinkFallbacks} heading-link fallback URLs)`,
  );
}

const isEntryPoint =
  process.argv[1] &&
  path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isEntryPoint) {
  main().catch((error) => {
    console.error(
      `Copy-ready rendering failed: ${
        error instanceof Error ? error.message : String(error)
      }`,
    );
    process.exitCode = 1;
  });
}
