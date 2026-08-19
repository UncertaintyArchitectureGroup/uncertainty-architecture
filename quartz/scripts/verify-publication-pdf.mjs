#!/usr/bin/env node

import { execFile } from "node:child_process"
import { mkdir, readdir, rm, stat, writeFile } from "node:fs/promises"
import path from "node:path"
import { promisify } from "node:util"
import { fileURLToPath } from "node:url"
import sharp from "sharp"
import { repoRoot, run } from "./publication-rendition.mjs"
import { assertSafeOutputPath, writeFileAtomically } from "./publication-path-safety.mjs"

const execFileAsync = promisify(execFile)
const pdfRoot = path.join(repoRoot, "dist", "pdf")

function parseArgs(argv) {
  if (argv.length === 0 || argv.includes("--help") || argv.includes("-h")) return { help: true }
  const pdf = argv[0]
  let outputDir
  for (let i = 1; i < argv.length; i += 1) {
    if (argv[i] === "--output-dir") outputDir = argv[++i]
    else throw new Error(`Unknown argument: ${argv[i]}`)
  }
  return { pdf, outputDir, help: false }
}

function usage() {
  console.log(
    "Usage: node quartz/scripts/verify-publication-pdf.mjs dist/pdf/file.pdf [--output-dir dist/pdf/visual/file]",
  )
}

function escapeXml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
}

async function capture(command, args) {
  try {
    const { stdout, stderr } = await execFileAsync(command, args, {
      cwd: repoRoot,
      maxBuffer: 8 * 1024 * 1024,
    })
    return { stdout: stdout.trim(), stderr: stderr.trim() }
  } catch (error) {
    throw new Error(
      `PDF visual verification requires Poppler '${command}'. Install poppler-utils and retry. ${error.message}`,
    )
  }
}

export function verifyPageFurniture(text, expectedPages) {
  const runningFooter = /Uncertainty Architecture\s*[·•]\s*Research Publication/i.test(text)
  const firstPageCounter = new RegExp(`Page\\s+1\\s*\\/\\s*${expectedPages}\\b`, "i").test(text)
  const lastPageCounter = new RegExp(
    `Page\\s+${expectedPages}\\s*\\/\\s*${expectedPages}\\b`,
    "i",
  ).test(text)
  return {
    running_footer: runningFooter,
    first_page_counter: firstPageCounter,
    last_page_counter: lastPageCounter,
    valid: runningFooter && firstPageCounter && lastPageCounter,
  }
}

export function findContentlessTextPages(text, expectedPages) {
  const rawPages = text.split("\f")
  const contentless = []
  for (let index = 0; index < expectedPages; index += 1) {
    const page = rawPages[index] || ""
    const meaningful = page
      .split(/\r?\n/)
      .map((line) => line.trim())
      .filter(Boolean)
      .filter((line) => !/Uncertainty Architecture\s*[·•]\s*Research Publication/i.test(line))
      .filter((line) => !/^(?:Page\s*)?\d+\s*\/\s*\d+$/i.test(line))
      .join(" ")
      .replace(/\s+/g, " ")
      .trim()
    if (meaningful.length < 8) contentless.push(index + 1)
  }
  return contentless
}

async function main() {
  const args = parseArgs(process.argv.slice(2))
  if (args.help) return usage()

  const pdfPath = path.resolve(repoRoot, args.pdf)
  if (path.extname(pdfPath).toLowerCase() !== ".pdf") {
    throw new Error("Visual verification accepts only PDF files under dist/pdf/")
  }
  await assertSafeOutputPath(repoRoot, pdfRoot, pdfPath, { createParent: false })
  const pdfInfo = await stat(pdfPath)
  if (!pdfInfo.isFile() || pdfInfo.size < 1024) throw new Error("PDF is missing or too small to verify")

  const stem = path.basename(pdfPath, path.extname(pdfPath))
  const defaultOutput = path.join(pdfRoot, "visual", stem)
  const visualRoot = path.join(pdfRoot, "visual")
  const outputDir = path.resolve(repoRoot, args.outputDir || defaultOutput)
  await assertSafeOutputPath(repoRoot, visualRoot, outputDir)
  await rm(outputDir, { recursive: true, force: true })
  await mkdir(outputDir, { recursive: true })
  await assertSafeOutputPath(repoRoot, visualRoot, outputDir)

  const infoResult = await capture("pdfinfo", [pdfPath])
  const pageCountMatch = /^Pages:\s+(\d+)$/m.exec(infoResult.stdout)
  const expectedPages = pageCountMatch ? Number(pageCountMatch[1]) : 0
  if (expectedPages <= 0) throw new Error("pdfinfo could not determine a positive page count")

  const fontsResult = await capture("pdffonts", [pdfPath])
  const textResult = await capture("pdftotext", ["-layout", pdfPath, "-"])
  const pageFurniture = verifyPageFurniture(textResult.stdout, expectedPages)
  const contentlessTextPages = findContentlessTextPages(textResult.stdout, expectedPages)
  if (!pageFurniture.valid) {
    throw new Error(
      `PDF page furniture is incomplete: ${JSON.stringify(pageFurniture)}. Expected running footer and counters from 1/${expectedPages} through ${expectedPages}/${expectedPages}.`,
    )
  }

  const prefix = path.join(outputDir, "page")
  await run("pdftoppm", ["-png", "-r", "110", pdfPath, prefix], { cwd: repoRoot })

  const pages = (await readdir(outputDir))
    .filter((name) => /^page-\d+\.png$/.test(name))
    .sort((a, b) => Number(a.match(/\d+/)[0]) - Number(b.match(/\d+/)[0]))
  if (pages.length === 0) throw new Error("PDF visual verification produced no pages")
  if (pages.length !== expectedPages) {
    throw new Error(`Rasterized ${pages.length} pages but pdfinfo reports ${expectedPages}`)
  }

  const thumbWidth = 320
  const gap = 24
  const columns = 4
  const thumbnails = []
  const blankPages = []
  let thumbHeight = 0
  for (let index = 0; index < pages.length; index += 1) {
    const pagePath = path.join(outputDir, pages[index])
    const stats = await sharp(pagePath).stats()
    const rgb = stats.channels.slice(0, 3)
    const nearlyWhite = rgb.every((channel) => channel.mean > 250 && channel.stdev < 3)
    if (nearlyWhite) blankPages.push(index + 1)
    const buffer = await sharp(pagePath).resize({ width: thumbWidth }).png().toBuffer()
    const meta = await sharp(buffer).metadata()
    thumbHeight = Math.max(thumbHeight, meta.height || 0)
    thumbnails.push({
      buffer,
      page: index + 1,
      width: meta.width || thumbWidth,
      height: meta.height || 0,
    })
  }

  const rows = Math.ceil(thumbnails.length / columns)
  const cellHeight = thumbHeight + 46
  const sheetWidth = columns * thumbWidth + (columns + 1) * gap
  const sheetHeight = rows * cellHeight + (rows + 1) * gap
  const composites = []
  for (let index = 0; index < thumbnails.length; index += 1) {
    const row = Math.floor(index / columns)
    const column = index % columns
    const left = gap + column * (thumbWidth + gap)
    const top = gap + row * (cellHeight + gap)
    composites.push({ input: thumbnails[index].buffer, left, top })
    const label = Buffer.from(
      `<svg xmlns="http://www.w3.org/2000/svg" width="${thumbWidth}" height="36"><text x="6" y="25" font-family="Arial, sans-serif" font-size="20" fill="#222">Page ${escapeXml(thumbnails[index].page)}</text></svg>`,
    )
    composites.push({ input: label, left, top: top + thumbHeight + 4 })
  }

  const sheetPath = path.join(outputDir, "contact-sheet.png")
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
    .toFile(sheetPath)

  const report = {
    schema_version: 1,
    pdf: path.relative(repoRoot, pdfPath).split(path.sep).join("/"),
    pdf_bytes: pdfInfo.size,
    pages: pages.length,
    blank_pages: blankPages,
    contentless_text_pages: contentlessTextPages,
    page_furniture: pageFurniture,
    contact_sheet: path.relative(repoRoot, sheetPath).split(path.sep).join("/"),
    pdfinfo: infoResult.stdout,
    pdffonts: fontsResult.stdout,
    generated_at: new Date().toISOString(),
  }
  const reportPath = path.join(outputDir, "visual-verification.json")
  await writeFileAtomically(reportPath, `${JSON.stringify(report, null, 2)}\n`, {
    trustedRoot: repoRoot,
    allowedRoot: visualRoot,
  })
  const invalidPages = [...new Set([...blankPages, ...contentlessTextPages])].sort((a, b) => a - b)
  if (invalidPages.length > 0) {
    throw new Error(`Visual verification found contentless pages: ${invalidPages.join(", ")}`)
  }
  console.log(
    `Visual verification ready: ${path.relative(repoRoot, sheetPath)} (${pages.length} pages; page furniture verified)`,
  )
}

const isEntryPoint =
  process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)
if (isEntryPoint) {
  main().catch((error) => {
    console.error(`PDF visual verification failed: ${error instanceof Error ? error.message : String(error)}`)
    process.exitCode = 1
  })
}
