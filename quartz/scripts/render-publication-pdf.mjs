#!/usr/bin/env node

import { mkdir, readFile, rename, rm, stat } from "node:fs/promises"
import path from "node:path"
import { fileURLToPath } from "node:url"
import {
  assertIndependentOutputTarget,
  assertSafeOutputPath,
  writeFileAtomically,
} from "./publication-path-safety.mjs"
import {
  buildPublicationRendition,
  currentArticleSource,
  defaultRepository,
  gitOutput,
  loadPublicationSource,
  normalizeDate,
  repoRoot,
  run,
  sha256,
  withTemporaryRendition,
} from "./publication-rendition.mjs"
import { determineSourceProvenance } from "./publication-provenance.mjs"

const defaultArticle = currentArticleSource
const defaultOutput = "dist/pdf/thinking-systems-when-the-controlled-object-changes.pdf"
const tocThresholdPages = 20
const outputRoot = path.join(repoRoot, "dist", "pdf")

function parseArgs(argv) {
  let source = defaultArticle
  let output = defaultOutput
  let splitDenseFigures = true
  let allowDirtyPreview = false
  for (let i = 0; i < argv.length; i += 1) {
    const value = argv[i]
    if (value === "--source") source = argv[++i]
    else if (value === "--output" || value === "-o") output = argv[++i]
    else if (value === "--no-split-dense") splitDenseFigures = false
    else if (value === "--allow-dirty-preview") allowDirtyPreview = true
    else if (value === "--help" || value === "-h") return { help: true }
    else if (!value.startsWith("-") && source === defaultArticle) source = value
    else throw new Error(`Unknown argument: ${value}`)
  }
  if (!source || !output) throw new Error("Source and output paths are required")
  return { source, output, splitDenseFigures, allowDirtyPreview, help: false }
}

function usage() {
  console.log(
    "Usage:\n  node quartz/scripts/render-publication-pdf.mjs [source.md] [--output dist/pdf/file.pdf] [--allow-dirty-preview]\n\nDefaults to the current Thinking Systems publication article. Publication provenance is strict by default: the source bytes must match the declared Git commit. Use --allow-dirty-preview only for explicitly non-versioned local previews.",
  )
}

export function countPdfPages(buffer) {
  const text = buffer.toString("latin1")
  const matches = text.match(/\/Type\s*\/Page\b/g)
  return matches?.length ?? 0
}

function manifestPathFor(pdfPath) {
  return pdfPath.replace(/\.pdf$/i, ".manifest.json")
}

async function renderWithGenericExporter(tempSourcePath, outputPath) {
  const relativeSource = path.relative(repoRoot, tempSourcePath).split(path.sep).join("/")
  const relativeOutput = path.relative(repoRoot, outputPath).split(path.sep).join("/")
  await run(
    process.execPath,
    [
      path.join(repoRoot, "quartz", "scripts", "export-pdf.mjs"),
      relativeSource,
      "--output",
      relativeOutput,
    ],
    { cwd: repoRoot },
  )
}

export { determineSourceProvenance }

export async function finalizePublicationPdf(preflightPath, outputPath, renameImpl = rename) {
  await renameImpl(preflightPath, outputPath)
}

async function main() {
  const args = parseArgs(process.argv.slice(2))
  if (args.help) return usage()

  const source = await loadPublicationSource(args.source)
  const outputPath = path.resolve(repoRoot, args.output)
  if (path.extname(outputPath).toLowerCase() !== ".pdf") {
    throw new Error("Publication output must have a .pdf extension")
  }
  await assertSafeOutputPath(repoRoot, outputRoot, outputPath)
  await assertIndependentOutputTarget(outputPath, [source.absolute])

  const sourceBefore = sha256(Buffer.from(source.raw))
  const declaredSourceCommit =
    process.env.UA_PDF_REPOSITORY_REF ||
    process.env.GITHUB_SHA ||
    (await gitOutput(["rev-parse", "HEAD"]))
  const provenance = await determineSourceProvenance(source, declaredSourceCommit, {
    allowDirtyPreview: args.allowDirtyPreview,
  })
  const requireFigure8Split =
    source.relative === defaultArticle && args.splitDenseFigures

  const preflightPath = path.join(
    path.dirname(outputPath),
    `.ua-preflight-${path.basename(outputPath)}`,
  )
  await assertSafeOutputPath(repoRoot, outputRoot, preflightPath)
  await rm(preflightPath, { force: true })

  const renditionOptions = {
    splitDenseFigures: args.splitDenseFigures,
    sourceCommit: declaredSourceCommit,
    provenance,
    requireFigure8Split,
  }
  const withoutToc = await buildPublicationRendition(source, {
    ...renditionOptions,
    includeToc: false,
  })
  let selected = withoutToc
  let pageCount = 0
  let tocIncluded = false

  await withTemporaryRendition(source, withoutToc.rendered, async (tempSourcePath) => {
    await renderWithGenericExporter(tempSourcePath, preflightPath)
  })
  const preflightBuffer = await readFile(preflightPath)
  pageCount = countPdfPages(preflightBuffer)
  if (pageCount <= 0) throw new Error("Unable to determine publication PDF page count")

  if (pageCount > tocThresholdPages) {
    tocIncluded = true
    selected = await buildPublicationRendition(source, {
      ...renditionOptions,
      includeToc: true,
    })
    await withTemporaryRendition(source, selected.rendered, async (tempSourcePath) => {
      await renderWithGenericExporter(tempSourcePath, outputPath)
    })
    await rm(preflightPath, { force: true })
    pageCount = countPdfPages(await readFile(outputPath))
  } else {
    await finalizePublicationPdf(preflightPath, outputPath)
  }

  const pdfBuffer = await readFile(outputPath)
  const repository = process.env.GITHUB_REPOSITORY || defaultRepository
  const sourceCommit = selected.sourceCommit || declaredSourceCommit
  if (sourceCommit !== declaredSourceCommit) {
    throw new Error(
      `Publication rendition source commit changed during rendering: ${declaredSourceCommit} -> ${sourceCommit}`,
    )
  }
  const generatedAt = new Date().toISOString()
  const publicationDate = normalizeDate(source.data.publication_date)
  const editionDate =
    publicationDate ||
    normalizeDate(source.data.updated) ||
    normalizeDate(source.data.created) ||
    generatedAt.slice(0, 10)
  const version =
    source.data.edition ||
    source.data.version ||
    (source.data.draft === true ? "Draft" : "Unversioned")

  const manifest = {
    schema_version: 1,
    artifact: "publication-pdf",
    title: source.data.title || null,
    source_path: source.relative,
    source_commit: sourceCommit,
    source_state: provenance.state,
    source_git_blob_sha: provenance.committedBlob,
    source_working_blob_sha: provenance.workingBlob,
    source_sha256: sourceBefore,
    pdf_path: path.relative(repoRoot, outputPath).split(path.sep).join("/"),
    pdf_sha256: sha256(pdfBuffer),
    generated_at: generatedAt,
    publication_date: publicationDate,
    edition_date: editionDate,
    version: String(version),
    status: source.data.status || null,
    maturity: source.data.maturity || null,
    draft: source.data.draft === true,
    license: source.data.license || "CC-BY-4.0",
    repository_url: `https://github.com/${repository}`,
    canonical_url: source.data.canonical_url || null,
    additional_publication_urls: Array.isArray(source.data.additional_publication_urls)
      ? source.data.additional_publication_urls
      : [],
    page_count: pageCount,
    toc_included: tocIncluded,
    canonical_figures: selected.canonicalFigures,
    rendition_figures: selected.renditionFigures,
    figure_8_split_for_readability: selected.figure8Split,
  }
  const manifestPath = manifestPathFor(outputPath)
  await writeFileAtomically(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`, {
    trustedRoot: repoRoot,
    allowedRoot: outputRoot,
    forbiddenPaths: [source.absolute],
  })

  const sourceAfter = sha256(Buffer.from(await readFile(source.absolute)))
  if (sourceBefore !== sourceAfter) {
    throw new Error("Canonical Markdown source changed during publication rendering")
  }

  const info = await stat(outputPath)
  console.log(
    `Publication PDF ready: ${path.relative(repoRoot, outputPath)} (${pageCount} pages, ${info.size} bytes; source ${provenance.state})`,
  )
  console.log(`Manifest: ${path.relative(repoRoot, manifestPath)}`)
  if (tocIncluded) {
    console.log(
      `Clickable contents added because the preflight PDF exceeded ${tocThresholdPages} pages.`,
    )
  }
}

const isEntryPoint =
  process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)
if (isEntryPoint) {
  main().catch((error) => {
    console.error(
      `Publication PDF failed: ${error instanceof Error ? error.message : String(error)}`,
    )
    process.exitCode = 1
  })
}
