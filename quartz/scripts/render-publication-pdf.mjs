#!/usr/bin/env node

import { mkdtemp, readFile, rename, rm, stat } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  assertIndependentOutputTarget,
  assertSafeOutputPath,
  writeFileAtomically,
} from "./publication-path-safety.mjs";
import {
  buildPublicationRendition,
  currentArticleSource,
  defaultRepository,
  gitOutput,
  loadPublicationSource,
  normalizeAuthors,
  normalizeDate,
  repoRoot,
  run,
  sha256,
  withTemporaryRendition,
} from "./publication-rendition.mjs";
import { determineSourceProvenance } from "./publication-provenance.mjs";

const defaultArticle = currentArticleSource;
const defaultOutput =
  "dist/pdf/thinking-systems-when-the-controlled-object-changes.pdf";
const tocThresholdPages = 20;
const outputRoot = path.join(repoRoot, "dist", "pdf");

export function parseArgs(argv) {
  let source;
  let output;
  let splitDenseFigures = true;
  let allowDirtyPreview = false;

  for (let i = 0; i < argv.length; i += 1) {
    const value = argv[i];
    if (value === "--source") {
      source = argv[++i];
      if (!source) throw new Error("--source requires a path");
    } else if (value === "--output" || value === "-o") {
      output = argv[++i];
      if (!output) throw new Error(`${value} requires a path`);
    } else if (value === "--no-split-dense") splitDenseFigures = false;
    else if (value === "--allow-dirty-preview") allowDirtyPreview = true;
    else if (value === "--help" || value === "-h") return { help: true };
    else if (!value.startsWith("-") && !source) source = value;
    else throw new Error(`Unknown argument: ${value}`);
  }

  const selectedSource = source || defaultArticle;
  const selectedOutput =
    output || (selectedSource === defaultArticle ? defaultOutput : undefined);
  if (!selectedOutput) {
    throw new Error(
      "A custom publication source requires --output so it cannot overwrite the curated article PDF",
    );
  }

  return {
    source: selectedSource,
    output: selectedOutput,
    splitDenseFigures,
    allowDirtyPreview,
    help: false,
  };
}

function usage() {
  console.log(
    "Usage:\n  node quartz/scripts/render-publication-pdf.mjs [source.md] [--output dist/pdf/file.pdf] [--allow-dirty-preview]\n\nDefaults to the current Thinking Systems publication article. A custom source requires an explicit --output path. Publication provenance is strict by default: the source bytes must match the declared Git commit. Use --allow-dirty-preview only for explicitly non-versioned local previews.",
  );
}

export function countPdfPages(buffer) {
  const text = buffer.toString("latin1");
  const matches = text.match(/\/Type\s*\/Page\b/g);
  return matches?.length ?? 0;
}

function manifestPathFor(pdfPath) {
  return pdfPath.replace(/\.pdf$/i, ".manifest.json");
}

async function exists(candidate) {
  try {
    await stat(candidate);
    return true;
  } catch (error) {
    if (error?.code === "ENOENT") return false;
    throw error;
  }
}

async function renderWithGenericExporter(tempSourcePath, outputPath) {
  const relativeSource = path
    .relative(repoRoot, tempSourcePath)
    .split(path.sep)
    .join("/");
  const relativeOutput = path
    .relative(repoRoot, outputPath)
    .split(path.sep)
    .join("/");
  await run(
    process.execPath,
    [
      path.join(repoRoot, "quartz", "scripts", "export-pdf.mjs"),
      relativeSource,
      "--output",
      relativeOutput,
    ],
    { cwd: repoRoot },
  );
}

export { determineSourceProvenance };

export async function finalizePublicationPdf(
  preflightPath,
  outputPath,
  renameImpl = rename,
) {
  await renameImpl(preflightPath, outputPath);
}

export async function verifyPublicationPair(pdfPath, manifestPath) {
  const [pdfBuffer, manifestText] = await Promise.all([
    readFile(pdfPath),
    readFile(manifestPath, "utf8"),
  ]);
  let manifest;
  try {
    manifest = JSON.parse(manifestText);
  } catch (error) {
    throw new Error(`Publication manifest is not valid JSON: ${error.message}`);
  }
  const actual = sha256(pdfBuffer);
  if (manifest.pdf_sha256 !== actual) {
    throw new Error(
      `Publication PDF/manifest checksum mismatch: manifest ${manifest.pdf_sha256 || "missing"}, actual ${actual}`,
    );
  }
  return manifest;
}

export async function finalizePublicationPair(
  candidatePdf,
  candidateManifest,
  outputPdf,
  outputManifest,
  { renameImpl = rename, verifyImpl = verifyPublicationPair } = {},
) {
  await verifyImpl(candidatePdf, candidateManifest);

  const hadPdf = await exists(outputPdf);
  const hadManifest = await exists(outputManifest);
  if (hadPdf !== hadManifest) {
    throw new Error(
      "Existing publication bundle is incomplete; refusing to replace an orphaned PDF or manifest",
    );
  }
  if (hadPdf) {
    try {
      await verifyImpl(outputPdf, outputManifest);
    } catch (error) {
      throw new Error(
        `Existing publication bundle is invalid; refusing to replace it: ${error.message}`,
      );
    }
  }

  const recoveryDirectory = await mkdtemp(
    path.join(path.dirname(outputPdf), ".ua-publication-recovery-"),
  );
  const pdfBackup = path.join(recoveryDirectory, path.basename(outputPdf));
  const manifestBackup = path.join(
    recoveryDirectory,
    path.basename(outputManifest),
  );
  let installedPdf = false;
  let installedManifest = false;
  let completed = false;
  let rollbackComplete = false;

  try {
    if (hadPdf) await renameImpl(outputPdf, pdfBackup);
    if (hadManifest) await renameImpl(outputManifest, manifestBackup);
    await renameImpl(candidatePdf, outputPdf);
    installedPdf = true;
    await renameImpl(candidateManifest, outputManifest);
    installedManifest = true;
    await verifyImpl(outputPdf, outputManifest);
    completed = true;
  } catch (error) {
    const rollbackErrors = [];
    try {
      if (installedManifest) await rm(outputManifest, { force: true });
    } catch (rollbackError) {
      rollbackErrors.push(
        `remove installed manifest: ${rollbackError.message}`,
      );
    }
    try {
      if (installedPdf) await rm(outputPdf, { force: true });
    } catch (rollbackError) {
      rollbackErrors.push(`remove installed PDF: ${rollbackError.message}`);
    }
    try {
      if (hadManifest && (await exists(manifestBackup))) {
        await renameImpl(manifestBackup, outputManifest);
      }
    } catch (rollbackError) {
      rollbackErrors.push(`restore manifest: ${rollbackError.message}`);
    }
    try {
      if (hadPdf && (await exists(pdfBackup))) {
        await renameImpl(pdfBackup, outputPdf);
      }
    } catch (rollbackError) {
      rollbackErrors.push(`restore PDF: ${rollbackError.message}`);
    }

    rollbackComplete = rollbackErrors.length === 0;
    if (!rollbackComplete) {
      throw new Error(
        `${error.message}; rollback incomplete, recovery files retained at ${recoveryDirectory}: ${rollbackErrors.join("; ")}`,
      );
    }
    throw error;
  } finally {
    if (completed || rollbackComplete) {
      await rm(recoveryDirectory, { recursive: true, force: true });
    }
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) return usage();

  const source = await loadPublicationSource(args.source);
  const outputPath = path.resolve(repoRoot, args.output);
  const manifestPath = manifestPathFor(outputPath);
  if (path.extname(outputPath).toLowerCase() !== ".pdf") {
    throw new Error("Publication output must have a .pdf extension");
  }
  await assertSafeOutputPath(repoRoot, outputRoot, outputPath);
  await assertSafeOutputPath(repoRoot, outputRoot, manifestPath);
  await assertIndependentOutputTarget(outputPath, [source.absolute]);
  await assertIndependentOutputTarget(manifestPath, [source.absolute]);

  const sourceBefore = sha256(Buffer.from(source.raw));
  const declaredSourceReference =
    process.env.UA_PDF_REPOSITORY_REF ||
    process.env.GITHUB_SHA ||
    (await gitOutput(["rev-parse", "HEAD"]));
  const provenance = await determineSourceProvenance(
    source,
    declaredSourceReference,
    {
      allowDirtyPreview: args.allowDirtyPreview,
    },
  );
  const declaredSourceCommit = provenance.sourceCommit;
  const requireFigure8Split =
    source.relative === defaultArticle && args.splitDenseFigures;

  const buildDirectory = await mkdtemp(
    path.join(outputRoot, ".ua-publication-build-"),
  );
  const preflightPath = path.join(buildDirectory, "preflight.pdf");
  const finalCandidate = path.join(buildDirectory, "publication.pdf");
  const manifestCandidate = path.join(
    buildDirectory,
    "publication.manifest.json",
  );
  let selected;
  let pageCount = 0;
  let tocIncluded = false;

  try {
    const renditionOptions = {
      splitDenseFigures: args.splitDenseFigures,
      sourceCommit: declaredSourceCommit,
      provenance,
      requireFigure8Split,
    };
    const withoutToc = await buildPublicationRendition(source, {
      ...renditionOptions,
      includeToc: false,
    });
    selected = withoutToc;
    await withTemporaryRendition(
      source,
      withoutToc.rendered,
      async (tempSourcePath) => {
        await renderWithGenericExporter(tempSourcePath, preflightPath);
      },
    );
    pageCount = countPdfPages(await readFile(preflightPath));
    if (pageCount <= 0)
      throw new Error("Unable to determine publication PDF page count");

    if (pageCount > tocThresholdPages) {
      tocIncluded = true;
      selected = await buildPublicationRendition(source, {
        ...renditionOptions,
        includeToc: true,
      });
      await withTemporaryRendition(
        source,
        selected.rendered,
        async (tempSourcePath) => {
          await renderWithGenericExporter(tempSourcePath, finalCandidate);
        },
      );
    } else {
      await finalizePublicationPdf(preflightPath, finalCandidate);
    }

    const pdfBuffer = await readFile(finalCandidate);
    pageCount = countPdfPages(pdfBuffer);
    const sourceAfter = sha256(Buffer.from(await readFile(source.absolute)));
    if (sourceBefore !== sourceAfter) {
      throw new Error(
        "Canonical Markdown source changed during publication rendering",
      );
    }

    const repository = process.env.GITHUB_REPOSITORY || defaultRepository;
    const generatedAt = new Date().toISOString();
    const publicationDate = normalizeDate(source.data.publication_date);
    const editionDate =
      publicationDate ||
      normalizeDate(source.data.updated) ||
      normalizeDate(source.data.created) ||
      generatedAt.slice(0, 10);
    const version =
      source.data.edition ||
      source.data.version ||
      (source.data.draft === true ? "Draft" : "Unversioned");

    const repositoryUrl = `https://github.com/${repository}`;
    const sourceUrl = `${repositoryUrl}/blob/${encodeURIComponent(declaredSourceCommit)}/${source.relative
      .split("/")
      .map(encodeURIComponent)
      .join("/")}`;
    const canonicalUrl =
      typeof source.data.canonical_url === "string" &&
      source.data.canonical_url.trim()
        ? source.data.canonical_url.trim()
        : null;
    const additionalPublicationUrls = Array.isArray(
      source.data.additional_publication_urls,
    )
      ? source.data.additional_publication_urls
          .filter((value) => typeof value === "string" && value.trim())
          .map((value) => value.trim())
      : [];
    const externalPublicationUrls = [
      ...new Set([canonicalUrl, ...additionalPublicationUrls].filter(Boolean)),
    ];

    const manifest = {
      schema_version: 2,
      artifact: "publication-pdf",
      title: source.data.title || null,
      authors: selected.authors,
      source_path: source.relative,
      source_sha: declaredSourceCommit,
      source_commit: declaredSourceCommit,
      source_commit_sha: declaredSourceCommit,
      source_state: provenance.state,
      source_git_blob_sha: provenance.committedBlob,
      source_working_blob_sha: provenance.workingBlob,
      source_content_digest: {
        algorithm: "sha256",
        value: sourceBefore,
      },
      source_sha256: sourceBefore,
      source_content_sha256: sourceBefore,
      pdf_path: path.relative(repoRoot, outputPath).split(path.sep).join("/"),
      pdf_sha256: sha256(pdfBuffer),
      generated_at: generatedAt,
      generated_date: generatedAt.slice(0, 10),
      publication_date: publicationDate,
      edition_date: editionDate,
      version: String(version),
      status: source.data.status || null,
      maturity: source.data.maturity || null,
      draft: source.data.draft === true,
      license: source.data.license || "CC-BY-4.0",
      repository_url: repositoryUrl,
      source_url: sourceUrl,
      canonical_url: canonicalUrl,
      additional_publication_urls: additionalPublicationUrls,
      external_publication_urls: externalPublicationUrls,
      number_of_pages: pageCount,
      page_count: pageCount,
      toc_included: tocIncluded,
      toc_threshold_pages: tocThresholdPages,
      figures: {
        canonical: selected.canonicalFigures,
        rendered: selected.renditionFigures,
      },
      canonical_figures: selected.canonicalFigures,
      rendition_figures: selected.renditionFigures,
      figure_8_split_for_readability: selected.figure8Split,
      figure_8_source_fingerprint: selected.figure8Fingerprint,
      figure_8_readability: selected.figure8Readability,
    };

    await writeFileAtomically(
      manifestCandidate,
      `${JSON.stringify(manifest, null, 2)}\n`,
      {
        trustedRoot: repoRoot,
        allowedRoot: outputRoot,
        forbiddenPaths: [source.absolute],
      },
    );
    await finalizePublicationPair(
      finalCandidate,
      manifestCandidate,
      outputPath,
      manifestPath,
    );
  } finally {
    await rm(buildDirectory, { recursive: true, force: true });
  }

  const info = await stat(outputPath);
  console.log(
    `Publication PDF ready: ${path.relative(repoRoot, outputPath)} (${pageCount} pages, ${info.size} bytes; source ${provenance.state})`,
  );
  console.log(`Manifest: ${path.relative(repoRoot, manifestPath)}`);
  if (tocIncluded) {
    console.log(
      `Clickable contents added because the preflight PDF exceeded ${tocThresholdPages} pages.`,
    );
  }
}

const isEntryPoint =
  process.argv[1] &&
  path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isEntryPoint) {
  main().catch((error) => {
    console.error(
      `Publication PDF failed: ${error instanceof Error ? error.message : String(error)}`,
    );
    process.exitCode = 1;
  });
}
