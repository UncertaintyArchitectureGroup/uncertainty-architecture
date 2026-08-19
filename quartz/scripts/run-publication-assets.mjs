#!/usr/bin/env node

import path from "node:path"
import { fileURLToPath } from "node:url"
import { assertSafeOutputPath } from "./publication-path-safety.mjs"
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
  const requirements = [
    ["LinkedIn article", 42],
    ["social preview", 34],
    ["Medium hero", 34],
  ]
  for (const [label, maxChars] of requirements) {
    const lines = wrappedLineCount(title, maxChars)
    if (!Number.isFinite(lines) || lines > 3) {
      throw new Error(
        `${label} cover title cannot fit within three lines without truncation. Shorten the publication title or implement an explicit fit strategy.`,
      )
    }
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

  const childArgs = [
    path.join(repoRoot, "quartz", "scripts", "render-publication-assets.mjs"),
    args.source,
    "--output-root",
    args.outputRoot,
  ]
  if (args.allowDirtyPreview) childArgs.push("--allow-dirty-preview")
  await run(process.execPath, childArgs, { cwd: repoRoot })
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
