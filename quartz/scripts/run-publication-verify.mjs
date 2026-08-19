#!/usr/bin/env node

import path from "node:path"
import { fileURLToPath } from "node:url"
import { assertSafeOutputPath } from "./publication-path-safety.mjs"
import { repoRoot, run } from "./publication-rendition.mjs"

function parseArgs(argv) {
  if (argv.length === 0 || argv.includes("--help") || argv.includes("-h")) {
    return { help: true }
  }
  const pdf = argv[0]
  let outputDir
  for (let i = 1; i < argv.length; i += 1) {
    if (argv[i] === "--output-dir") outputDir = argv[++i]
    else throw new Error(`Unknown argument: ${argv[i]}`)
  }
  return { pdf, outputDir, help: false }
}

async function main() {
  const args = parseArgs(process.argv.slice(2))
  if (args.help) {
    console.log("Usage: npm run pdf:verify -- dist/pdf/file.pdf [--output-dir dist/pdf/visual/file]")
    return
  }
  const pdfRoot = path.join(repoRoot, "dist", "pdf")
  const pdfPath = path.resolve(repoRoot, args.pdf)
  await assertSafeOutputPath(repoRoot, pdfRoot, pdfPath, { createParent: false })
  const visualRoot = path.join(pdfRoot, "visual")
  const stem = path.basename(pdfPath, path.extname(pdfPath))
  const outputDir = path.resolve(repoRoot, args.outputDir || path.join(visualRoot, stem))
  await assertSafeOutputPath(repoRoot, visualRoot, outputDir)
  await run(
    process.execPath,
    [path.join(repoRoot, "quartz", "scripts", "verify-publication-pdf.mjs"), ...process.argv.slice(2)],
    { cwd: repoRoot },
  )
}

const isEntryPoint =
  process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)
if (isEntryPoint) {
  main().catch((error) => {
    console.error(`PDF verification preflight failed: ${error.message}`)
    process.exitCode = 1
  })
}
