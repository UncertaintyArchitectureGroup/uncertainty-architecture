#!/usr/bin/env node

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
