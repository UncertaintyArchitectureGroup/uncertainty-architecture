#!/usr/bin/env node

import path from "node:path"
import { fileURLToPath } from "node:url"
import { assertSafeOutputPath } from "./publication-path-safety.mjs"
import { repoRoot, run } from "./publication-rendition.mjs"

function parseArgs(argv) {
  let source
  let output
  for (let i = 0; i < argv.length; i += 1) {
    const value = argv[i]
    if (value === "--output" || value === "-o") output = argv[++i]
    else if (value === "--help" || value === "-h") return { help: true }
    else if (value.startsWith("-")) throw new Error(`Unknown option: ${value}`)
    else if (!source) source = value
    else throw new Error(`Unexpected argument: ${value}`)
  }
  return { source, output, help: false }
}

async function main() {
  const args = parseArgs(process.argv.slice(2))
  if (args.help || !args.source) {
    console.log("Usage: npm run pdf -- <content/file.md> [--output dist/pdf/file.pdf]")
    if (!args.help) process.exitCode = 1
    return
  }
  const source = path.resolve(repoRoot, args.source)
  const output = args.output
    ? path.resolve(repoRoot, args.output)
    : path.join(
        repoRoot,
        "dist",
        "pdf",
        path.relative(path.join(repoRoot, "content"), source).replace(/\.md$/i, ".pdf"),
      )
  const outputRoot = path.join(repoRoot, "dist", "pdf")
  await assertSafeOutputPath(repoRoot, outputRoot, output)
  await run(
    process.execPath,
    [path.join(repoRoot, "quartz", "scripts", "export-pdf.mjs"), ...process.argv.slice(2)],
    { cwd: repoRoot },
  )
}

const isEntryPoint =
  process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)
if (isEntryPoint) {
  main().catch((error) => {
    console.error(`PDF export preflight failed: ${error.message}`)
    process.exitCode = 1
  })
}
