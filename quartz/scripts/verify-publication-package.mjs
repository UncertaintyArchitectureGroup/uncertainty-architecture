#!/usr/bin/env node

import { readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { inspectMarkdownHeadingLinks } from "./protect-platform-heading-links.mjs";
import { gitOutput, repoRoot, sha256 } from "./publication-rendition.mjs";

const publicationRoot = path.join(
  repoRoot,
  "dist",
  "publication",
  "thinking-systems",
);
const renditionRoot = path.join(publicationRoot, "renditions");

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

export function assertPlatformFigureInventory(manifest) {
  assert(
    Array.isArray(manifest?.figures) && manifest.figures.length === 9,
    "Expected nine platform figure renditions",
  );
  const figure8 = manifest.figures
    .filter((figure) => figure.number === 8)
    .map((figure) => figure.panel);
  assert(
    JSON.stringify(figure8) === JSON.stringify(["A", "B"]),
    "Figure 8A and Figure 8B must travel together",
  );
}

export function countDataImages(html) {
  return (String(html).match(/src="data:image\//g) || []).length;
}

export function extractEmbeddedDataImages(html) {
  const images = [];
  const pattern =
    /<img\b[^>]*\bsrc=(["'])data:([^;,"']+);base64,([^"']+)\1[^>]*>/gi;
  for (const match of String(html).matchAll(pattern)) {
    const bytes = Buffer.from(match[3], "base64");
    assert(bytes.length > 0, "Embedded preview image is empty");
    images.push({
      mimeType: match[2].toLowerCase(),
      bytes,
      sha256: sha256(bytes),
    });
  }
  return images;
}

export function assertMediumPreviewImageManifest(html, copyReady) {
  const listed = copyReady?.medium_upload_assets;
  const assets = Array.isArray(listed)
    ? listed.filter((asset) => asset.id !== "instructions")
    : [];
  const embedded = extractEmbeddedDataImages(html);
  assert(
    assets.length === 10,
    "Medium preview comparison requires ten ordered upload images",
  );
  assert(
    embedded.length === assets.length,
    `Medium preview contains ${embedded.length} embedded images; expected ${assets.length}`,
  );
  for (const [index, image] of embedded.entries()) {
    const asset = assets[index];
    assert(
      image.mimeType === "image/png",
      `Medium preview image ${index} is not PNG`,
    );
    assert(
      image.sha256 === asset.sha256,
      `Medium preview image ${index} does not match ${asset.path}`,
    );
  }
  return { embedded, assets };
}

export function assertMediumUploadManifest(copyReady) {
  assert(
    copyReady?.medium_manual_upload_required === true,
    "Medium manual upload must be required",
  );
  assert(
    copyReady?.medium_clipboard_images_supported === false,
    "Medium clipboard image transfer must not be claimed",
  );
  assert(
    copyReady?.medium_image_strategy === "embedded-data-uri-preview",
    "Medium copy-ready strategy must remain a self-contained visual preview",
  );
  assert(
    copyReady?.medium_upload_asset_count === 10,
    "Medium upload kit must contain hero plus nine figures",
  );
  assert(
    copyReady?.medium_upload_kit === "medium/upload/README.md",
    "Medium upload kit entrypoint is missing",
  );

  const assets = copyReady?.medium_upload_assets;
  assert(
    Array.isArray(assets) && assets.length === 11,
    "Medium upload manifest must contain ten images plus instructions",
  );
  const images = assets.filter((asset) => asset.id !== "instructions");
  assert(images.length === 10, "Medium upload manifest image count diverged");
  assert(
    images[0]?.path === "medium/upload/00-medium-hero.png",
    "Medium upload kit must start with the hero",
  );
  assert(
    images.every(
      (asset, index) =>
        asset.order === index &&
        asset.path.startsWith("medium/upload/") &&
        asset.path.endsWith(".png") &&
        /^[0-9a-f]{64}$/i.test(String(asset.sha256 || "")),
    ),
    "Medium upload image ordering or digest metadata is invalid",
  );
  assert(
    images[8]?.id === "08a" && images[9]?.id === "08b",
    "Medium upload kit must keep Figure 8A and Figure 8B together",
  );
  const instructions = assets.find((asset) => asset.id === "instructions");
  assert(
    instructions?.path === "medium/upload/README.md" &&
      /^[0-9a-f]{64}$/i.test(String(instructions.sha256 || "")),
    "Medium upload instructions metadata is invalid",
  );
}

function fallbackAnchorCount(html) {
  let count = 0;
  for (const match of String(html).matchAll(
    /<p class="heading-link-fallback">([\s\S]*?)<\/p>/gi,
  )) {
    count += (match[1].match(/<a\b/gi) || []).length;
  }
  return count;
}

function assertNoCopyHelpers(html, platform) {
  assert(!/<script\b/i.test(html), `${platform} copy-ready HTML contains JavaScript`);
  assert(
    !/Copy article|Select article|navigator\.clipboard|ClipboardItem/i.test(html),
    `${platform} copy-ready HTML contains obsolete copy controls`,
  );
  assert(
    !/Upload file:|class="provenance"/i.test(html),
    `${platform} copy-ready HTML leaked helper/provenance content`,
  );
}

async function verifyOutputDigests(manifest) {
  for (const [relative, expected] of Object.entries(manifest.outputs || {})) {
    const bytes = await readFile(path.join(renditionRoot, relative));
    assert(
      sha256(bytes) === expected,
      `Platform output digest mismatch: ${relative}`,
    );
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
  assert(
    inventory.every((entry) => entry.protected),
    `${platform} Markdown contains an unprotected linked heading`,
  );
  const linkedUrls = inventory.reduce(
    (sum, entry) => sum + entry.urls.length,
    0,
  );
  assert(
    linkedUrls ===
      manifest.heading_link_protection?.[`${platform}_fallback_urls`],
    `${platform} heading-link manifest count diverged`,
  );
  assert(
    fallbackAnchorCount(html) === linkedUrls,
    `${platform} article HTML heading fallback count diverged`,
  );
  assert(
    fallbackAnchorCount(copyReady) === linkedUrls,
    `${platform} copy-ready heading fallback count diverged`,
  );
  assert(
    countDataImages(copyReady) === expectedImages,
    `${platform} copy-ready embedded ${countDataImages(copyReady)} images; expected ${expectedImages}`,
  );
  assert(
    !/raw\.githubusercontent\.com/i.test(copyReady),
    `${platform} copy-ready unexpectedly depends on remote repository images`,
  );
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
    assert(
      copyReady.includes(marker),
      `${platform} copy-ready HTML is missing publication furniture: ${marker}`,
    );
  }

  if (platform === "linkedin") {
    assert(
      manifest.copy_ready?.linkedin_image_strategy === "embedded-data-uri",
      "LinkedIn image strategy diverged",
    );
  } else {
    assertMediumUploadManifest(manifest.copy_ready);
    const preview = assertMediumPreviewImageManifest(
      copyReady,
      manifest.copy_ready,
    );
    for (const [index, asset] of preview.assets.entries()) {
      const uploadBytes = await readFile(path.join(renditionRoot, asset.path));
      assert(
        uploadBytes.equals(preview.embedded[index].bytes),
        `Medium preview image ${index} is not byte-identical to ${asset.path}`,
      );
    }

    const [uploadReadme, checklist] = await Promise.all([
      readFile(path.join(directory, "upload", "README.md"), "utf8"),
      readFile(path.join(directory, "publishing-checklist.md"), "utf8"),
    ]);
    assert(
      uploadReadme.includes(
        "Medium preserves the pasted rich text but drops clipboard images",
      ),
      "Medium upload instructions do not record the observed platform limitation",
    );
    assert(
      uploadReadme.includes("Figure 8A") && uploadReadme.includes("Figure 8B"),
      "Medium upload instructions lost Figure 8 coupling",
    );
    assert(
      checklist.includes("copy-ready.html") &&
        checklist.includes("upload/README.md") &&
        checklist.includes("article.md"),
      "Medium publishing checklist is not bound to the copy-ready and ordered-upload path",
    );
    assert(
      !checklist.includes("../../medium-hero.png") &&
        !checklist.includes("Upload every image named by an `UPLOAD IMAGE` marker"),
      "Medium publishing checklist still exposes the obsolete generic image route",
    );
  }
}

async function main() {
  const [platformManifest, assetManifest] = await Promise.all([
    readFile(
      path.join(renditionRoot, "platform-renditions.manifest.json"),
      "utf8",
    ).then(JSON.parse),
    readFile(path.join(publicationRoot, "assets.manifest.json"), "utf8").then(
      JSON.parse,
    ),
  ]);

  const expectedCommit =
    process.env.UA_PDF_REPOSITORY_REF ||
    process.env.GITHUB_SHA ||
    (await gitOutput(["rev-parse", "HEAD"]));
  assert(
    platformManifest.publication_state === "candidate",
    "Platform package must remain candidate",
  );
  assert(
    platformManifest.publication_ready === false,
    "Editable-source package must not self-certify publication readiness",
  );
  assert(
    platformManifest.source_commit === expectedCommit,
    `Platform provenance ${platformManifest.source_commit} does not match ${expectedCommit}`,
  );
  assertPlatformFigureInventory(assetManifest);
  await verifyOutputDigests(platformManifest);
  await verifyPlatform("linkedin", platformManifest, 9);
  await verifyPlatform("medium", platformManifest, 10);
  assert(
    platformManifest.publication_furniture?.research_path_items === 6,
    "Publication furniture must contain six research-path items",
  );
  assert(
    platformManifest.copy_ready?.javascript_copy_controls === false,
    "Copy-ready contract must explicitly disable JavaScript controls",
  );
  assert(
    platformManifest.figure_8_panels_must_travel_together === true,
    "Figure 8 coupling contract was lost",
  );

  console.log(
    `Complete Thinking Systems platform package verified at ${expectedCommit}: candidate state, 9 platform figures, self-contained LinkedIn and Medium review pages, Medium ordered manual-upload kit, linked-heading fallbacks, and publication furniture are coherent.`,
  );
}

const isEntryPoint =
  process.argv[1] &&
  path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isEntryPoint) {
  main().catch((error) => {
    console.error(
      `Publication package verification failed: ${
        error instanceof Error ? error.message : String(error)
      }`,
    );
    process.exitCode = 1;
  });
}
