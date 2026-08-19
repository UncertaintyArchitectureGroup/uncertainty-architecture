#!/usr/bin/env node

import { mkdtemp, readFile, rename, rm, stat } from "node:fs/promises"
import path from "node:path"
import { fileURLToPath } from "node:url"
import {
  assertSafeOutputPath,
  writeFileAtomically,
} from "./publication-path-safety.mjs"
import {
  currentArticleSource,
  loadPublicationSource,
  repoRoot,
  run,
} from "./publication-rendition.mjs"

const defaultSource = currentArticleSource
const defaultOutputRoot = "dist/publication/thinking-systems"
const publicationRoot = path.join(repoRoot, "dist", "publication")

function parseArgs(argv) {
  let source = defaultSource
  let outputRoot = defaultOutputRoot
  let allowDirtyPreview = false
  for (let i = 0; i < argv.length; i += 1) {
    const value = argv[i]
    if (value === "--source") source = argv[++i]
    else if (value === "--output-root") outputRoot = argv[++i]
    else if (value === "--allow-dirty-preview") allowDirtyPreview = true
    else if (value === "--help" || value === "-h") return { help: true }
    else if (!value.startsWith("-") && source === defaultSource) source = value
    else throw new Error(`Unknown argument: ${value}`)
  }
  return { source, outputRoot, allowDirtyPreview, help: false }
}

function wrappedLineCount(title, maxChars) {
  const words = String(title).trim().split(/\s+/).filter(Boolean)
  let lines = 0
  let current = ""
  for (const word of words) {
    if (word.length > maxChars) return Number.POSITIVE_INFINITY
    const candidate = current ? `${current} ${word}` : word
    if (candidate.length > maxChars && current) {
      lines += 1
      current = word
    } else {
      current = candidate
    }
  }
  if (current) lines += 1
  return lines
}

export function assertCoverTitleFits(title) {
  for (const [label, maxChars] of [
    ["LinkedIn article", 42],
    ["social preview", 34],
    ["Medium hero", 34],
  ]) {
    const lines = wrappedLineCount(title, maxChars)
    if (!Number.isFinite(lines) || lines > 3) {
      throw new Error(
        `${label} cover title cannot fit within three lines without truncation. Shorten the publication title or implement an explicit fit strategy.`,
      )
    }
  }
}

async function exists(candidate) {
  try {
    await stat(candidate)
    return true
  } catch (error) {
    if (error?.code === "ENOENT") return false
    throw error
  }
}

function locateCanonicalFigure8Caption(content) {
  const blockPattern = /```mermaid\r?\n([\s\S]*?)\r?\n```/g
  let match
  while ((match = blockPattern.exec(content)) !== null) {
    const mermaid = match[1]
    if (
      !/\bsubgraph\s+L(?:\[|\s|$)/.test(mermaid) ||
      !/\bsubgraph\s+F(?:\[|\s|$)/.test(mermaid)
    ) {
      continue
    }
    const tail = content.slice(blockPattern.lastIndex)
    const captionMatch = /^\s*(?:<!--[\s\S]*?-->\s*)*(\*\*Figure 8 —[^\n]*)(?=\n\n|$)/.exec(tail)
    return captionMatch?.[1] ?? null
  }
  return null
}

export function buildFigure8CaptionDocument(canonicalCaption) {
  return [
    "# Figure 8 — Shared canonical caption",
    "",
    canonicalCaption.trim(),
    "",
    "> **Platform rendition rule.** Figure 8A and Figure 8B are two presentation panels of one logical Figure 8. Publish them together with this complete canonical caption; neither panel is a standalone replacement for the model.",
    "",
  ].join("\n")
}

function remapPath(value, stagingRelative, finalRelative) {
  if (typeof value !== "string") return value
  if (value === stagingRelative) return finalRelative
  if (value.startsWith(`${stagingRelative}/`)) {
    return `${finalRelative}${value.slice(stagingRelative.length)}`
  }
  return value
}

export function remapAssetManifestPaths(manifest, stagingRelative, finalRelative) {
  for (const figure of manifest.figures ?? []) {
    figure.svg = remapPath(figure.svg, stagingRelative, finalRelative)
    figure.png = remapPath(figure.png, stagingRelative, finalRelative)
  }
  for (const cover of Object.values(manifest.covers ?? {})) {
    cover.path = remapPath(cover.path, stagingRelative, finalRelative)
  }
  return manifest
}

async function validateStagedBundle(stagingRoot, manifest) {
  const required = [
    ...(manifest.figures ?? []).flatMap((figure) => [figure.svg, figure.png]),
    ...Object.values(manifest.covers ?? {}).map((cover) => cover.path),
  ]
  const stagingRelative = path.relative(repoRoot, stagingRoot).split(path.sep).join("/")
  for (const repositoryPath of required) {
    if (!repositoryPath?.startsWith(`${stagingRelative}/`)) {
      throw new Error(`Staged asset manifest points outside its build root: ${repositoryPath}`)
    }
    const absolute = path.join(repoRoot, ...repositoryPath.split("/"))
    const info = await stat(absolute)
    if (!info.isFile() || info.size === 0) {
      throw new Error(`Publication asset is missing or empty: ${repositoryPath}`)
    }
  }
}

export async function finalizePublicationDirectory(
  stagingRoot,
  outputRoot,
  { renameImpl = rename } = {},
) {
  const backupDirectory = await mkdtemp(
    path.join(path.dirname(outputRoot), ".ua-assets-backup-"),
  )
  const backupOutput = path.join(backupDirectory, path.basename(outputRoot))
  const hadOutput = await exists(outputRoot)
  let installed = false

  try {
    if (hadOutput) await renameImpl(outputRoot, backupOutput)
    await renameImpl(stagingRoot, outputRoot)
    installed = true
  } catch (error) {
    if (installed) await rm(outputRoot, { recursive: true, force: true })
    if (hadOutput && (await exists(backupOutput))) {
      await rename(backupOutput, outputRoot)
    }
    throw error
  } finally {
    await rm(backupDirectory, { recursive: true, force: true })
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2))
  if (args.help) {
    console.log(
      "Usage: npm run publication:assets -- [source.md] [--output-root dist/publication/name] [--allow-dirty-preview]",
    )
    return
  }

  const source = await loadPublicationSource(args.source)
  assertCoverTitleFits(source.data.title || "Untitled publication")
  const outputRoot = path.resolve(repoRoot, args.outputRoot)
  await assertSafeOutputPath(repoRoot, publicationRoot, outputRoot)

  const stagingRoot = await mkdtemp(path.join(publicationRoot, ".ua-assets-stage-"))
  try {
    const stagingRelative = path.relative(repoRoot, stagingRoot).split(path.sep).join("/")
    const childArgs = [
      path.join(repoRoot, "quartz", "scripts", "render-publication-assets.mjs"),
      "--source",
      args.source,
      "--output-root",
      stagingRelative,
    ]
    if (args.allowDirtyPreview) childArgs.push("--allow-dirty-preview")
    await run(process.execPath, childArgs, { cwd: repoRoot })

    const manifestPath = path.join(stagingRoot, "assets.manifest.json")
    const manifest = JSON.parse(await readFile(manifestPath, "utf8"))
    await validateStagedBundle(stagingRoot, manifest)

    const finalRelative = path.relative(repoRoot, outputRoot).split(path.sep).join("/")
    remapAssetManifestPaths(manifest, stagingRelative, finalRelative)

    const canonicalCaption = locateCanonicalFigure8Caption(source.content)
    if (source.relative === currentArticleSource && !canonicalCaption) {
      throw new Error(
        "Current publication assets require the complete canonical Figure 8 caption, but it was not recognized.",
      )
    }
    if (canonicalCaption) {
      const captionFile = "figure-08-shared-caption.md"
      const captionPath = path.join(stagingRoot, captionFile)
      await writeFileAtomically(
        captionPath,
        buildFigure8CaptionDocument(canonicalCaption),
        {
          trustedRoot: repoRoot,
          allowedRoot: publicationRoot,
          forbiddenPaths: [source.absolute],
        },
      )
      manifest.figure_8_canonical_caption = canonicalCaption
      manifest.figure_8_shared_caption_path = `${finalRelative}/${captionFile}`
      manifest.figure_8_panels_must_travel_together = true
    }

    await writeFileAtomically(
      manifestPath,
      `${JSON.stringify(manifest, null, 2)}\n`,
      {
        trustedRoot: repoRoot,
        allowedRoot: publicationRoot,
        forbiddenPaths: [source.absolute],
      },
    )
    await finalizePublicationDirectory(stagingRoot, outputRoot)
  } finally {
    await rm(stagingRoot, { recursive: true, force: true })
  }

  console.log(`Publication asset bundle ready: ${path.relative(repoRoot, outputRoot)}`)
}

const isEntryPoint =
  process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)
if (isEntryPoint) {
  main().catch((error) => {
    console.error(
      `Publication asset preflight failed: ${error instanceof Error ? error.message : String(error)}`,
    )
    process.exitCode = 1
  })
}
