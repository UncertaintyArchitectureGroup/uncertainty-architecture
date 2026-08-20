#!/usr/bin/env node

import { execFile } from "node:child_process";
import { mkdir, readFile, realpath, readdir, rm, stat } from "node:fs/promises";
import path from "node:path";
import { promisify } from "node:util";
import { fileURLToPath } from "node:url";
import sharp from "sharp";
import {
  contentRoot,
  currentArticleSource,
  humanLicense,
  isInside,
  repoRoot,
  run,
  sha256,
} from "./publication-rendition.mjs";
import {
  assertSafeOutputPath,
  writeFileAtomically,
} from "./publication-path-safety.mjs";
import { canonicalFigure8Fingerprint } from "./publication-figure8-fingerprint.mjs";

const execFileAsync = promisify(execFile);
const pdfRoot = path.join(repoRoot, "dist", "pdf");
const commitShaPattern = /^[0-9a-f]{40}$/i;
const sha256Pattern = /^[0-9a-f]{64}$/i;
const datePattern = /^\d{4}-\d{2}-\d{2}$/;

function parseArgs(argv) {
  if (argv.length === 0 || argv.includes("--help") || argv.includes("-h"))
    return { help: true };
  const pdf = argv[0];
  let outputDir;
  let requireManifest = false;
  for (let i = 1; i < argv.length; i += 1) {
    if (argv[i] === "--output-dir") {
      outputDir = argv[++i];
      if (!outputDir) throw new Error("--output-dir requires a path");
    } else if (argv[i] === "--require-manifest") requireManifest = true;
    else throw new Error(`Unknown argument: ${argv[i]}`);
  }
  return { pdf, outputDir, requireManifest, help: false };
}

function usage() {
  console.log(
    "Usage: node quartz/scripts/verify-publication-pdf.mjs dist/pdf/file.pdf [--output-dir dist/pdf/visual/file] [--require-manifest]",
  );
}

function escapeXml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

function normalizeText(value) {
  return String(value ?? "")
    .replace(/\s+/g, " ")
    .trim();
}

function withoutWhitespace(value) {
  return String(value ?? "").replace(/\s+/g, "");
}

function isHttpUrl(value) {
  if (typeof value !== "string" || !value.trim()) return false;
  try {
    const url = new URL(value);
    return url.protocol === "http:" || url.protocol === "https:";
  } catch {
    return false;
  }
}

async function capture(command, args) {
  try {
    const { stdout, stderr } = await execFileAsync(command, args, {
      cwd: repoRoot,
      maxBuffer: 8 * 1024 * 1024,
    });
    return { stdout: stdout.trim(), stderr: stderr.trim() };
  } catch (error) {
    throw new Error(
      `PDF visual verification requires Poppler '${command}'. Install poppler-utils and retry. ${error.message}`,
    );
  }
}

export function verifyPageFurniture(text, expectedPages) {
  const pages = text.split("\f");
  const missingRunningFooterPages = [];
  const missingPageCounterPages = [];

  for (let index = 0; index < expectedPages; index += 1) {
    const pageNumber = index + 1;
    const page = pages[index] || "";
    if (!/Uncertainty Architecture\s*[·•]\s*Research Publication/i.test(page)) {
      missingRunningFooterPages.push(pageNumber);
    }
    if (
      !new RegExp(
        `Page\\s+${pageNumber}\\s*\\/\\s*${expectedPages}\\b`,
        "i",
      ).test(page)
    ) {
      missingPageCounterPages.push(pageNumber);
    }
  }

  const runningFooter = missingRunningFooterPages.length === 0;
  const allPageCounters = missingPageCounterPages.length === 0;
  return {
    running_footer: runningFooter,
    all_page_counters: allPageCounters,
    first_page_counter: !missingPageCounterPages.includes(1),
    last_page_counter: !missingPageCounterPages.includes(expectedPages),
    missing_running_footer_pages: missingRunningFooterPages,
    missing_page_counter_pages: missingPageCounterPages,
    valid: runningFooter && allPageCounters,
  };
}

export function findContentlessTextPages(text, expectedPages) {
  const rawPages = text.split("\f");
  const contentless = [];
  for (let index = 0; index < expectedPages; index += 1) {
    const page = rawPages[index] || "";
    const meaningful = page
      .split(/\r?\n/)
      .map((line) => line.trim())
      .filter(Boolean)
      .filter(
        (line) =>
          !/Uncertainty Architecture\s*[·•]\s*Research Publication/i.test(line),
      )
      .filter((line) => !/^(?:Page\s*)?\d+\s*\/\s*\d+$/i.test(line))
      .join(" ")
      .replace(/\s+/g, " ")
      .trim();
    if (meaningful.length < 8) contentless.push(index + 1);
  }
  return contentless;
}

function manifestPathFor(pdfPath) {
  return pdfPath.replace(/\.pdf$/i, ".manifest.json");
}

async function readPublicationManifest(pdfPath, requireManifest) {
  const manifestPath = manifestPathFor(pdfPath);
  try {
    const raw = await readFile(manifestPath, "utf8");
    return { present: true, path: manifestPath, manifest: JSON.parse(raw) };
  } catch (error) {
    if (error?.code === "ENOENT" && !requireManifest) {
      return { present: false, path: manifestPath, manifest: null };
    }
    if (error?.code === "ENOENT") {
      throw new Error(
        `Publication manifest is required but missing: ${path.relative(repoRoot, manifestPath)}`,
      );
    }
    if (error instanceof SyntaxError) {
      throw new Error(
        `Publication manifest is not valid JSON: ${error.message}`,
      );
    }
    throw error;
  }
}

function validateFigureList(value, label, errors) {
  if (!Array.isArray(value)) {
    errors.push(`${label} must be an array`);
    return;
  }
  for (const [index, figure] of value.entries()) {
    if (!figure || !Number.isInteger(figure.number) || figure.number <= 0) {
      errors.push(`${label}[${index}].number must be a positive integer`);
    }
    if (
      figure?.panel !== null &&
      figure?.panel !== "A" &&
      figure?.panel !== "B"
    ) {
      errors.push(`${label}[${index}].panel must be null, A, or B`);
    }
    if (!figure || typeof figure.title !== "string" || !figure.title.trim()) {
      errors.push(`${label}[${index}].title must be a non-empty string`);
    }
  }
}

export async function verifyPublicationManifest(
  manifest,
  { pdfPath, pdfBuffer, expectedPages, sourceBuffer } = {},
) {
  const errors = [];
  const expectedPdfPath = path
    .relative(repoRoot, pdfPath)
    .split(path.sep)
    .join("/");

  if (manifest?.schema_version !== 2) errors.push("schema_version must be 2");
  if (manifest?.artifact !== "publication-pdf")
    errors.push("artifact must be publication-pdf");
  if (typeof manifest?.title !== "string" || !manifest.title.trim()) {
    errors.push("title must be a non-empty string");
  }
  if (!Array.isArray(manifest?.authors) || manifest.authors.length === 0) {
    errors.push("authors must contain at least one author");
  } else if (
    manifest.authors.some(
      (author) => typeof author !== "string" || !author.trim(),
    )
  ) {
    errors.push("authors must contain only non-empty strings");
  }
  if (
    typeof manifest?.source_path !== "string" ||
    !manifest.source_path.startsWith("content/") ||
    !manifest.source_path.endsWith(".md")
  ) {
    errors.push("source_path must identify Markdown under content/");
  }
  if (!commitShaPattern.test(manifest?.source_commit_sha || "")) {
    errors.push("source_commit_sha must be a full 40-character Git commit SHA");
  }
  if (
    manifest?.source_sha !== manifest?.source_commit_sha ||
    manifest?.source_commit !== manifest?.source_commit_sha
  ) {
    errors.push("source_sha and source_commit must match source_commit_sha");
  }
  if (!["committed", "dirty-preview"].includes(manifest?.source_state)) {
    errors.push("source_state must be committed or dirty-preview");
  }
  if (
    manifest?.source_git_blob_sha !== null &&
    !commitShaPattern.test(manifest?.source_git_blob_sha || "")
  ) {
    errors.push(
      "source_git_blob_sha must be null or a full 40-character Git blob SHA",
    );
  }
  if (!commitShaPattern.test(manifest?.source_working_blob_sha || "")) {
    errors.push(
      "source_working_blob_sha must be a full 40-character Git blob SHA",
    );
  }
  if (!sha256Pattern.test(manifest?.source_content_sha256 || "")) {
    errors.push("source_content_sha256 must be a SHA-256 digest");
  }
  if (
    manifest?.source_content_digest?.algorithm !== "sha256" ||
    manifest?.source_content_digest?.value !==
      manifest?.source_content_sha256 ||
    manifest?.source_sha256 !== manifest?.source_content_sha256
  ) {
    errors.push(
      "source_content_digest and source_sha256 must match source_content_sha256",
    );
  }
  if (manifest?.pdf_path !== expectedPdfPath) {
    errors.push(`pdf_path must equal ${expectedPdfPath}`);
  }
  const actualPdfSha256 = sha256(pdfBuffer);
  if (manifest?.pdf_sha256 !== actualPdfSha256) {
    errors.push("pdf_sha256 does not match the PDF bytes");
  }
  if (
    typeof manifest?.generated_at !== "string" ||
    Number.isNaN(Date.parse(manifest.generated_at))
  ) {
    errors.push("generated_at must be an ISO timestamp");
  }
  if (!datePattern.test(manifest?.generated_date || "")) {
    errors.push("generated_date must be YYYY-MM-DD");
  }
  if (
    typeof manifest?.generated_at === "string" &&
    datePattern.test(manifest?.generated_date || "") &&
    manifest.generated_at.slice(0, 10) !== manifest.generated_date
  ) {
    errors.push("generated_date must match generated_at");
  }
  if (
    manifest?.publication_date !== null &&
    !datePattern.test(manifest?.publication_date || "")
  ) {
    errors.push("publication_date must be null or YYYY-MM-DD");
  }
  if (!datePattern.test(manifest?.edition_date || "")) {
    errors.push("edition_date must be YYYY-MM-DD");
  }
  if (
    ![manifest?.status, manifest?.maturity].some(
      (value) => typeof value === "string" && value.trim(),
    )
  ) {
    errors.push("status or maturity must declare the publication state");
  }
  if (typeof manifest?.version !== "string" || !manifest.version.trim()) {
    errors.push("version must be a non-empty string");
  }
  if (humanLicense(manifest?.license) !== "CC BY 4.0") {
    errors.push("license must be CC BY 4.0");
  }
  for (const field of ["repository_url", "source_url"]) {
    if (!isHttpUrl(manifest?.[field]))
      errors.push(`${field} must be an HTTP(S) URL`);
  }
  if (
    commitShaPattern.test(manifest?.source_commit_sha || "") &&
    typeof manifest?.source_url === "string" &&
    !manifest.source_url.includes(manifest.source_commit_sha)
  ) {
    errors.push("source_url must include source_commit_sha");
  }
  if (manifest?.canonical_url !== null && !isHttpUrl(manifest?.canonical_url)) {
    errors.push("canonical_url must be null or an HTTP(S) URL");
  }
  for (const field of [
    "additional_publication_urls",
    "external_publication_urls",
  ]) {
    if (
      !Array.isArray(manifest?.[field]) ||
      manifest[field].some((value) => !isHttpUrl(value))
    ) {
      errors.push(`${field} must be an array of HTTP(S) URLs`);
    }
  }
  const expectedExternal = [
    ...new Set(
      [
        manifest?.canonical_url,
        ...(manifest?.additional_publication_urls || []),
      ].filter(Boolean),
    ),
  ];
  if (
    Array.isArray(manifest?.external_publication_urls) &&
    JSON.stringify(manifest.external_publication_urls) !==
      JSON.stringify(expectedExternal)
  ) {
    errors.push(
      "external_publication_urls must combine canonical_url and additional_publication_urls",
    );
  }
  if (
    !Number.isInteger(manifest?.page_count) ||
    manifest.page_count !== expectedPages
  ) {
    errors.push(`page_count must equal ${expectedPages}`);
  }
  if (manifest?.number_of_pages !== manifest?.page_count) {
    errors.push("number_of_pages must match page_count");
  }
  if (typeof manifest?.toc_included !== "boolean") {
    errors.push("toc_included must be boolean");
  }
  if (
    !Number.isInteger(manifest?.toc_threshold_pages) ||
    manifest.toc_threshold_pages <= 0
  ) {
    errors.push("toc_threshold_pages must be a positive integer");
  }
  if (
    Number.isInteger(manifest?.page_count) &&
    Number.isInteger(manifest?.toc_threshold_pages) &&
    manifest.page_count > manifest.toc_threshold_pages &&
    manifest.toc_included !== true
  ) {
    errors.push(
      "a publication over the TOC threshold must include clickable contents",
    );
  }
  if (!manifest?.figures || typeof manifest.figures !== "object") {
    errors.push("figures must contain canonical and rendered lists");
  } else {
    validateFigureList(manifest.figures.canonical, "figures.canonical", errors);
    validateFigureList(manifest.figures.rendered, "figures.rendered", errors);
  }
  if (
    JSON.stringify(manifest?.canonical_figures) !==
      JSON.stringify(manifest?.figures?.canonical) ||
    JSON.stringify(manifest?.rendition_figures) !==
      JSON.stringify(manifest?.figures?.rendered)
  ) {
    errors.push(
      "canonical_figures and rendition_figures must match the figures object",
    );
  }

  let actualSourceSha256 = null;
  if (
    typeof manifest?.source_path === "string" &&
    manifest.source_path.startsWith("content/")
  ) {
    try {
      let bytes = sourceBuffer;
      if (!bytes) {
        const candidate = path.resolve(repoRoot, manifest.source_path);
        const sourcePath = await realpath(candidate);
        if (!isInside(contentRoot, sourcePath)) {
          throw new Error("resolved source is outside content/");
        }
        bytes = await readFile(sourcePath);
      }
      actualSourceSha256 = sha256(bytes);
      if (manifest.source_content_sha256 !== actualSourceSha256) {
        errors.push(
          "source_content_sha256 does not match the canonical Markdown bytes",
        );
      }
    } catch (error) {
      errors.push(`unable to verify source content digest: ${error.message}`);
    }
  }

  return {
    valid: errors.length === 0,
    errors,
    schema_version: manifest?.schema_version ?? null,
    pdf_sha256: actualPdfSha256,
    source_content_sha256: actualSourceSha256,
    page_count: expectedPages,
  };
}

export function verifyTitlePage(text, manifest) {
  const firstPage = text.split("\f")[0] || "";
  const normalized = normalizeText(firstPage);
  const compact = withoutWhitespace(firstPage);
  const missing = [];
  const requiredText = [
    manifest.title,
    ...(manifest.authors || []),
    manifest.status,
    manifest.maturity,
    manifest.version,
    humanLicense(manifest.license),
    manifest.publication_date || manifest.edition_date,
  ].filter(Boolean);
  for (const value of requiredText) {
    if (!normalized.includes(normalizeText(value))) missing.push(String(value));
  }
  for (const value of [
    manifest.source_commit_sha,
    manifest.repository_url,
    manifest.canonical_url,
  ].filter(Boolean)) {
    if (!compact.includes(withoutWhitespace(value)))
      missing.push(String(value));
  }
  return {
    required_fields: requiredText,
    full_source_commit_sha: compact.includes(
      withoutWhitespace(manifest.source_commit_sha),
    ),
    missing,
    valid: missing.length === 0,
  };
}

export function verifyClickableContents(text, xml, manifest, expectedPages) {
  const threshold = manifest?.toc_threshold_pages ?? 20;
  const required = expectedPages > threshold;
  const included = manifest?.toc_included === true;
  const contentsPage = text.split("\f")[1] || "";
  const hasHeading = /\bContents\b/i.test(contentsPage);
  const internalLinks = (xml.match(/<a\s+href="[^"]*#\d+"/gi) || []).length;
  const valid =
    (!required || included) && (!included || (hasHeading && internalLinks > 0));
  return {
    required,
    included,
    heading_found: hasHeading,
    internal_link_count: internalLinks,
    valid,
  };
}

export function verifyFigure8PublicationRendition(text, manifest) {
  const required = manifest?.source_path === currentArticleSource;
  const split = manifest?.figure_8_split_for_readability === true;
  if (!required && !split) {
    return { required: false, split: false, skipped: true, valid: true };
  }

  const canonicalFigures =
    manifest?.figures?.canonical || manifest?.canonical_figures || [];
  const renderedFigures =
    manifest?.figures?.rendered || manifest?.rendition_figures || [];
  const canonicalEight = canonicalFigures.filter(
    (figure) => figure?.number === 8,
  );
  const renderedEight = renderedFigures.filter(
    (figure) => figure?.number === 8,
  );
  const panels = renderedEight.map((figure) => figure.panel).sort();
  const compactFigureText = (value) =>
    String(value ?? "")
      .replace(/[‐‑‒–—−]/g, "-")
      .replace(/\s+/g, "")
      .toLowerCase();
  const pages = text.split("\f");
  const compactPages = pages.map(compactFigureText);
  const pageAIndex = compactPages.findIndex((page) =>
    page.includes("figure8a-decision-ownershipmodel"),
  );
  const pageBIndex = compactPages.findIndex((page) =>
    page.includes("figure8b-capability-familyaxisandorthogonalityrelationship"),
  );
  const compactDocument = compactFigureText(text);
  const sharedCaption = compactDocument.includes(
    "together,figures8a-8bpreservecanonicalfigure8",
  );
  const unsplitCaption = /figure8-(?![ab])/i.test(compactDocument);
  const readability = manifest?.figure_8_readability;
  const readabilityChecks = Object.fromEntries(
    ["A", "B"].map((panel) => {
      const result = readability?.panels?.[panel];
      return [
        panel,
        Boolean(
          result &&
          result.effective_pdf_label_pt >= 5 &&
          result.pdf_hard_floor_met === true &&
          result.effective_pdf_label_pt >= 6 &&
          result.pdf_preferred_target_met === true &&
          result.effective_desktop_label_px >= 12 &&
          result.desktop_readable === true,
        ),
      ];
    }),
  );
  const checks = {
    split,
    canonical_single_figure:
      canonicalEight.length === 1 && canonicalEight[0].panel === null,
    rendered_panels:
      renderedEight.length === 2 && panels[0] === "A" && panels[1] === "B",
    fingerprint:
      manifest?.figure_8_source_fingerprint === canonicalFigure8Fingerprint,
    panel_a_present: pageAIndex >= 0,
    panel_b_present: pageBIndex >= 0,
    separate_pages:
      pageAIndex >= 0 && pageBIndex >= 0 && pageAIndex !== pageBIndex,
    shared_caption: sharedCaption,
    unsplit_caption_absent: !unsplitCaption,
    panel_a_readable: readabilityChecks.A,
    panel_b_readable: readabilityChecks.B,
  };
  return {
    required,
    split,
    panel_a_page: pageAIndex >= 0 ? pageAIndex + 1 : null,
    panel_b_page: pageBIndex >= 0 ? pageBIndex + 1 : null,
    checks,
    readability,
    valid: Object.values(checks).every(Boolean),
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) return usage();

  const pdfPath = path.resolve(repoRoot, args.pdf);
  if (path.extname(pdfPath).toLowerCase() !== ".pdf") {
    throw new Error(
      "Visual verification accepts only PDF files under dist/pdf/",
    );
  }
  await assertSafeOutputPath(repoRoot, pdfRoot, pdfPath, {
    createParent: false,
  });
  const pdfInfo = await stat(pdfPath);
  if (!pdfInfo.isFile() || pdfInfo.size < 1024)
    throw new Error("PDF is missing or too small to verify");
  const pdfBuffer = await readFile(pdfPath);

  const stem = path.basename(pdfPath, path.extname(pdfPath));
  const defaultOutput = path.join(pdfRoot, "visual", stem);
  const visualRoot = path.join(pdfRoot, "visual");
  const outputDir = path.resolve(repoRoot, args.outputDir || defaultOutput);
  await assertSafeOutputPath(repoRoot, visualRoot, outputDir);
  await rm(outputDir, { recursive: true, force: true });
  await mkdir(outputDir, { recursive: true });
  await assertSafeOutputPath(repoRoot, visualRoot, outputDir);

  const infoResult = await capture("pdfinfo", [pdfPath]);
  const pageCountMatch = /^Pages:\s+(\d+)$/m.exec(infoResult.stdout);
  const expectedPages = pageCountMatch ? Number(pageCountMatch[1]) : 0;
  if (expectedPages <= 0)
    throw new Error("pdfinfo could not determine a positive page count");

  const fontsResult = await capture("pdffonts", [pdfPath]);
  const textResult = await capture("pdftotext", ["-layout", pdfPath, "-"]);
  const pageFurniture = verifyPageFurniture(textResult.stdout, expectedPages);
  const contentlessTextPages = findContentlessTextPages(
    textResult.stdout,
    expectedPages,
  );
  if (!pageFurniture.valid) {
    throw new Error(
      `PDF page furniture is incomplete: ${JSON.stringify(pageFurniture)}. Expected running footer and counters from 1/${expectedPages} through ${expectedPages}/${expectedPages}.`,
    );
  }

  const manifestResult = await readPublicationManifest(
    pdfPath,
    args.requireManifest,
  );
  let manifestVerification = { present: false, valid: true };
  let titlePage = { valid: true, skipped: true };
  let contents = { valid: true, skipped: true };
  let figure8 = { valid: true, skipped: true };
  if (manifestResult.present) {
    manifestVerification = {
      present: true,
      path: path
        .relative(repoRoot, manifestResult.path)
        .split(path.sep)
        .join("/"),
      ...(await verifyPublicationManifest(manifestResult.manifest, {
        pdfPath,
        pdfBuffer,
        expectedPages,
      })),
    };
    if (!manifestVerification.valid) {
      throw new Error(
        `Publication manifest verification failed: ${manifestVerification.errors.join("; ")}`,
      );
    }
    titlePage = verifyTitlePage(textResult.stdout, manifestResult.manifest);
    if (!titlePage.valid) {
      throw new Error(
        `Publication title page is incomplete: ${titlePage.missing.join(", ")}`,
      );
    }
    let contentsXml = "";
    if (
      manifestResult.manifest.toc_included === true ||
      expectedPages > manifestResult.manifest.toc_threshold_pages
    ) {
      const contentsResult = await capture("pdftohtml", [
        "-xml",
        "-stdout",
        "-f",
        "2",
        "-l",
        "2",
        "-hidden",
        "-noframes",
        pdfPath,
      ]);
      contentsXml = contentsResult.stdout;
    }
    contents = verifyClickableContents(
      textResult.stdout,
      contentsXml,
      manifestResult.manifest,
      expectedPages,
    );
    if (!contents.valid) {
      throw new Error(
        `Publication contents verification failed: ${JSON.stringify(contents)}`,
      );
    }
    figure8 = verifyFigure8PublicationRendition(
      textResult.stdout,
      manifestResult.manifest,
    );
    if (!figure8.valid) {
      throw new Error(
        `Publication Figure 8 verification failed: ${JSON.stringify(figure8.checks)}`,
      );
    }
  }

  const prefix = path.join(outputDir, "page");
  await run("pdftoppm", ["-png", "-r", "110", pdfPath, prefix], {
    cwd: repoRoot,
  });

  const pages = (await readdir(outputDir))
    .filter((name) => /^page-\d+\.png$/.test(name))
    .sort((a, b) => Number(a.match(/\d+/)[0]) - Number(b.match(/\d+/)[0]));
  if (pages.length === 0)
    throw new Error("PDF visual verification produced no pages");
  if (pages.length !== expectedPages) {
    throw new Error(
      `Rasterized ${pages.length} pages but pdfinfo reports ${expectedPages}`,
    );
  }

  const thumbWidth = 320;
  const gap = 24;
  const columns = 4;
  const thumbnails = [];
  const blankPages = [];
  let thumbHeight = 0;
  for (let index = 0; index < pages.length; index += 1) {
    const pagePath = path.join(outputDir, pages[index]);
    const stats = await sharp(pagePath).stats();
    const rgb = stats.channels.slice(0, 3);
    const nearlyWhite = rgb.every(
      (channel) => channel.mean > 250 && channel.stdev < 3,
    );
    if (nearlyWhite) blankPages.push(index + 1);
    const buffer = await sharp(pagePath)
      .resize({ width: thumbWidth })
      .png()
      .toBuffer();
    const meta = await sharp(buffer).metadata();
    thumbHeight = Math.max(thumbHeight, meta.height || 0);
    thumbnails.push({
      buffer,
      page: index + 1,
      width: meta.width || thumbWidth,
      height: meta.height || 0,
    });
  }

  const rows = Math.ceil(thumbnails.length / columns);
  const cellHeight = thumbHeight + 46;
  const sheetWidth = columns * thumbWidth + (columns + 1) * gap;
  const sheetHeight = rows * cellHeight + (rows + 1) * gap;
  const composites = [];
  for (let index = 0; index < thumbnails.length; index += 1) {
    const row = Math.floor(index / columns);
    const column = index % columns;
    const left = gap + column * (thumbWidth + gap);
    const top = gap + row * (cellHeight + gap);
    composites.push({ input: thumbnails[index].buffer, left, top });
    const label = Buffer.from(
      `<svg xmlns="http://www.w3.org/2000/svg" width="${thumbWidth}" height="36"><text x="6" y="25" font-family="Arial, sans-serif" font-size="20" fill="#222">Page ${escapeXml(thumbnails[index].page)}</text></svg>`,
    );
    composites.push({ input: label, left, top: top + thumbHeight + 4 });
  }

  const sheetPath = path.join(outputDir, "contact-sheet.png");
  await sharp({
    create: {
      width: sheetWidth,
      height: sheetHeight,
      channels: 3,
      background: "#dddddd",
    },
  })
    .composite(composites)
    .png()
    .toFile(sheetPath);

  const report = {
    schema_version: 2,
    pdf: path.relative(repoRoot, pdfPath).split(path.sep).join("/"),
    pdf_bytes: pdfInfo.size,
    pages: pages.length,
    blank_pages: blankPages,
    contentless_text_pages: contentlessTextPages,
    page_furniture: pageFurniture,
    publication_manifest: manifestVerification,
    title_page: titlePage,
    clickable_contents: contents,
    figure_8: figure8,
    contact_sheet: path.relative(repoRoot, sheetPath).split(path.sep).join("/"),
    pdfinfo: infoResult.stdout,
    pdffonts: fontsResult.stdout,
    generated_at: new Date().toISOString(),
  };
  const reportPath = path.join(outputDir, "visual-verification.json");
  await writeFileAtomically(
    reportPath,
    `${JSON.stringify(report, null, 2)}\n`,
    {
      trustedRoot: repoRoot,
      allowedRoot: visualRoot,
    },
  );
  const invalidPages = [
    ...new Set([...blankPages, ...contentlessTextPages]),
  ].sort((a, b) => a - b);
  if (invalidPages.length > 0) {
    throw new Error(
      `Visual verification found contentless pages: ${invalidPages.join(", ")}`,
    );
  }
  console.log(
    `Visual verification ready: ${path.relative(repoRoot, sheetPath)} (${pages.length} pages; page furniture${manifestResult.present ? ", manifest, title page, and contents" : ""} verified)`,
  );
}

const isEntryPoint =
  process.argv[1] &&
  path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isEntryPoint) {
  main().catch((error) => {
    console.error(
      `PDF visual verification failed: ${error instanceof Error ? error.message : String(error)}`,
    );
    process.exitCode = 1;
  });
}
