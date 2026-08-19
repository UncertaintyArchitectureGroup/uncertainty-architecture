#!/usr/bin/env node

import { createReadStream } from "node:fs"
import { mkdir, mkdtemp, readFile, rm, stat, writeFile } from "node:fs/promises"
import http from "node:http"
import os from "node:os"
import path from "node:path"
import { fileURLToPath } from "node:url"
import { chromium } from "playwright"
import sharp from "sharp"
import {
  assertIndependentOutputTarget,
  assertSafeOutputPath,
  writeFileAtomically,
} from "./publication-path-safety.mjs"
import { determineSourceProvenance } from "./publication-provenance.mjs"
import {
  assertCurrentArticleFigure8Rendition,
  buildPublicationRendition,
  currentArticleSource,
  gitOutput,
  isInside,
  loadPublicationSource,
  normalizeAuthors,
  repoRoot,
  run,
  sha256,
  withTemporaryRendition,
} from "./publication-rendition.mjs"
import {
  buildFigure8CapabilitySvg,
  buildFigure8DecisionSvg,
} from "./publication-figure8.mjs"

const defaultSource = "content/research/notes/thinking-systems-publication-draft.md"
const defaultOutputRoot = "dist/publication/thinking-systems"
const publicationOutputRoot = path.join(repoRoot, "dist", "publication")

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

function usage() {
  console.log(
    "Usage: node quartz/scripts/render-publication-assets.mjs [source.md] [--output-root dist/publication/name] [--allow-dirty-preview]",
  )
}

function contentType(filePath) {
  const ext = path.extname(filePath).toLowerCase()
  return (
    {
      ".css": "text/css; charset=utf-8",
      ".html": "text/html; charset=utf-8",
      ".js": "text/javascript; charset=utf-8",
      ".json": "application/json; charset=utf-8",
      ".png": "image/png",
      ".svg": "image/svg+xml",
      ".woff": "font/woff",
      ".woff2": "font/woff2",
    }[ext] || "application/octet-stream"
  )
}

async function existingFile(candidate) {
  try {
    return (await stat(candidate)).isFile()
  } catch {
    return false
  }
}

async function startServer(root) {
  const server = http.createServer(async (request, response) => {
    try {
      const url = new URL(request.url || "/", "http://127.0.0.1")
      const decoded = decodeURIComponent(url.pathname).replace(/^\/+/, "")
      let candidate = path.resolve(root, decoded)
      if (!isInside(root, candidate)) throw new Error("outside publication root")

      try {
        const info = await stat(candidate)
        if (info.isDirectory()) candidate = path.join(candidate, "index.html")
      } catch {
        const html = `${candidate}.html`
        if (await existingFile(html)) candidate = html
      }

      if (!(await existingFile(candidate))) {
        response.writeHead(404)
        response.end("Not found")
        return
      }
      response.writeHead(200, { "content-type": contentType(candidate) })
      createReadStream(candidate).pipe(response)
    } catch (error) {
      response.writeHead(500)
      response.end(String(error))
    }
  })

  await new Promise((resolve, reject) => {
    server.once("error", reject)
    server.listen(0, "127.0.0.1", resolve)
  })
  const address = server.address()
  if (!address || typeof address === "string") throw new Error("Unable to determine asset server port")
  return {
    origin: `http://127.0.0.1:${address.port}`,
    close: () =>
      new Promise((resolve, reject) =>
        server.close((error) => (error ? reject(error) : resolve())),
      ),
  }
}

async function resolveBuiltPage(siteDir, sourcePath) {
  const index = JSON.parse(await readFile(path.join(siteDir, "static", "contentIndex.json"), "utf8"))
  const relative = path
    .relative(path.join(repoRoot, "content"), sourcePath)
    .split(path.sep)
    .join("/")
  const entry = Object.values(index).find((candidate) => candidate.filePath === relative)
  if (!entry?.slug) throw new Error(`Quartz did not index publication rendition ${relative}`)
  return entry.slug
}

function normalizeSvg(svg) {
  if (/xmlns=/.test(svg)) return svg
  return svg.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"')
}

function figureId(caption, fallback) {
  if (/Figure\s+8A\b/i.test(caption)) return "08a"
  if (/Figure\s+8B\b/i.test(caption)) return "08b"
  const match = /Figure\s+(\d+)/i.exec(caption)
  return match ? String(match[1]).padStart(2, "0") : String(fallback).padStart(2, "0")
}

async function renderSvgToPng(browser, svg, width, outputPath) {
  const page = await browser.newPage({ viewport: { width: width + 80, height: 1200 } })
  try {
    await page.setContent(
      `<!doctype html><html><body style="margin:0;background:white"><div id="root" style="width:${width}px;padding:24px;box-sizing:border-box">${svg}</div><style>#root svg{display:block;width:100%!important;height:auto!important}</style></body></html>`,
      { waitUntil: "load" },
    )
    const root = page.locator("#root")
    await root.screenshot({ path: outputPath, omitBackground: false })
    const metadata = await sharp(outputPath).metadata()
    if (metadata.width !== width) {
      throw new Error(`Rendered PNG ${path.basename(outputPath)} is ${metadata.width}px wide; expected ${width}px`)
    }
    return metadata
  } finally {
    await page.close()
  }
}

function escapeXml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
}

function wrapTitle(title, maxChars) {
  const words = title.split(/\s+/).filter(Boolean)
  const lines = []
  let current = ""
  for (const word of words) {
    if (word.length > maxChars) {
      throw new Error(`Cover title token '${word}' cannot fit within the supported line width`)
    }
    const candidate = current ? `${current} ${word}` : word
    if (candidate.length > maxChars && current) {
      lines.push(current)
      current = word
    } else {
      current = candidate
    }
  }
  if (current) lines.push(current)
  if (lines.length > 3) {
    throw new Error(`Cover title requires ${lines.length} lines; renderer supports at most 3 without truncation`)
  }
  return lines
}

async function writeCover(pathname, width, height, title, byline, label) {
  const lines = wrapTitle(title, width >= 1900 ? 42 : 34)
  const titleSize = width >= 1900 ? 76 : 56
  const startY = Math.max(150, (height - lines.length * titleSize * 1.15) / 2)
  const tspans = lines
    .map(
      (line, index) =>
        `<tspan x="${Math.round(width * 0.08)}" dy="${index === 0 ? 0 : Math.round(titleSize * 1.15)}">${escapeXml(line)}</tspan>`,
    )
    .join("")
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}">
    <rect width="100%" height="100%" fill="#faf8f8"/>
    <rect x="0" y="0" width="${Math.round(width * 0.018)}" height="100%" fill="#284b63"/>
    <text x="${Math.round(width * 0.08)}" y="${Math.round(height * 0.16)}" font-family="Arial, sans-serif" font-size="${Math.round(titleSize * 0.34)}" font-weight="700" fill="#54736d" letter-spacing="2">${escapeXml(label.toUpperCase())}</text>
    <text x="${Math.round(width * 0.08)}" y="${Math.round(startY)}" font-family="Arial, sans-serif" font-size="${titleSize}" font-weight="700" fill="#1f1f1f">${tspans}</text>
    <text x="${Math.round(width * 0.08)}" y="${Math.round(height * 0.88)}" font-family="Arial, sans-serif" font-size="${Math.round(titleSize * 0.34)}" fill="#3f3f3f">${escapeXml(byline)}</text>
  </svg>`
  await sharp(Buffer.from(svg)).png().toFile(pathname)
  const metadata = await sharp(pathname).metadata()
  if (metadata.width !== width || metadata.height !== height) {
    throw new Error(`Cover ${path.basename(pathname)} did not render at ${width}×${height}`)
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2))
  if (args.help) return usage()

  const source = await loadPublicationSource(args.source)
  const declaredSourceCommit =
    process.env.UA_PDF_REPOSITORY_REF ||
    process.env.GITHUB_SHA ||
    (await gitOutput(["rev-parse", "HEAD"]))
  const provenance = await determineSourceProvenance(source, declaredSourceCommit, {
    allowDirtyPreview: args.allowDirtyPreview,
  })

  const outputRoot = path.resolve(repoRoot, args.outputRoot)
  if (!isInside(publicationOutputRoot, outputRoot) || outputRoot === publicationOutputRoot) {
    throw new Error("Publication assets must remain in a named directory under dist/publication/")
  }
  await assertSafeOutputPath(repoRoot, publicationOutputRoot, outputRoot)
  await rm(outputRoot, { recursive: true, force: true })
  const svgDir = path.join(outputRoot, "figures", "svg")
  const pngDir = path.join(outputRoot, "figures", "png")
  await mkdir(svgDir, { recursive: true })
  await mkdir(pngDir, { recursive: true })
  await assertSafeOutputPath(repoRoot, publicationOutputRoot, outputRoot)

  const rendition = await buildPublicationRendition(source, {
    includeToc: false,
    splitDenseFigures: true,
    sourceCommit: declaredSourceCommit,
    provenance,
    requireFigure8Split: source.relative === currentArticleSource,
  })
  if (source.relative === currentArticleSource) {
    assertCurrentArticleFigure8Rendition(rendition)
  }
  const tempRoot = await mkdtemp(path.join(os.tmpdir(), "ua-publication-assets-"))
  const siteDir = path.join(tempRoot, "site")
  let server
  let browser
  try {
    await withTemporaryRendition(source, rendition.rendered, async (tempSourcePath) => {
      await run(
        process.execPath,
        [path.join(repoRoot, "quartz", "bootstrap-cli.mjs"), "build", "--output", siteDir],
        {
          cwd: repoRoot,
          env: { ...process.env, UA_INCLUDE_DRAFTS: "1" },
        },
      )
      const slug = await resolveBuiltPage(siteDir, tempSourcePath)
      server = await startServer(siteDir)
      browser = await chromium.launch({
        headless: true,
        executablePath: process.env.CHROME_PATH || undefined,
      })
      const page = await browser.newPage({ viewport: { width: 1800, height: 1200 } })
      try {
        const url = `${server.origin}/${slug.split("/").map(encodeURIComponent).join("/")}`
        const response = await page.goto(url, { waitUntil: "networkidle" })
        if (!response?.ok()) throw new Error(`Publication asset page returned HTTP ${response?.status()}`)
        await page.waitForFunction(
          () =>
            Array.from(document.querySelectorAll("code.mermaid")).every(
              (node) => node.getAttribute("data-processed") === "true" && node.querySelector("svg"),
            ),
          undefined,
          { timeout: 30000 },
        )
        await page.evaluate(async () => {
          if (document.fonts) await document.fonts.ready
        })

        const figures = await page.evaluate(() =>
          Array.from(document.querySelectorAll("pre"))
            .filter((pre) => pre.querySelector(":scope > code.mermaid svg"))
            .map((pre, index) => {
              const svg = pre.querySelector(":scope > code.mermaid svg")
              const next = pre.nextElementSibling
              return {
                index: index + 1,
                svg: svg.outerHTML,
                caption: next?.tagName === "P" ? next.textContent.trim() : "",
              }
            }),
        )
        if (figures.length === 0) throw new Error("Publication rendition contains no Mermaid figures")

        const manifestFigures = []
        for (const figure of figures) {
          const id = figureId(figure.caption, figure.index)
          const normalized = normalizeSvg(figure.svg)
          const svgPath = path.join(svgDir, `figure-${id}.svg`)
          const pngPath = path.join(pngDir, `figure-${id}.png`)
          const width = id === "08a" ? 3200 : id === "08b" ? 2400 : 1800
          await writeFile(svgPath, normalized, "utf8")
          const metadata = await renderSvgToPng(browser, normalized, width, pngPath)
          manifestFigures.push({
            id,
            caption: figure.caption,
            svg: path.relative(repoRoot, svgPath).split(path.sep).join("/"),
            png: path.relative(repoRoot, pngPath).split(path.sep).join("/"),
            width: metadata.width,
            height: metadata.height,
          })
        }

        if (rendition.figure8Split) {
          const staticFigures = [
            {
              id: "08a",
              caption: "Figure 8A — Decision-ownership model.",
              svg: buildFigure8DecisionSvg(),
              width: 3200,
            },
            {
              id: "08b",
              caption: "Figure 8B — Capability-family axis and orthogonality relationship.",
              svg: buildFigure8CapabilitySvg(),
              width: 2400,
            },
          ]
          for (const figure of staticFigures) {
            const svgPath = path.join(svgDir, `figure-${figure.id}.svg`)
            const pngPath = path.join(pngDir, `figure-${figure.id}.png`)
            await writeFile(svgPath, figure.svg, "utf8")
            const metadata = await renderSvgToPng(browser, figure.svg, figure.width, pngPath)
            manifestFigures.push({
              id: figure.id,
              caption: figure.caption,
              svg: path.relative(repoRoot, svgPath).split(path.sep).join("/"),
              png: path.relative(repoRoot, pngPath).split(path.sep).join("/"),
              width: metadata.width,
              height: metadata.height,
            })
          }
        }

        const ids = manifestFigures.map((figure) => figure.id)
        const duplicates = [...new Set(ids.filter((id, index) => ids.indexOf(id) !== index))]
        if (duplicates.length > 0) {
          throw new Error(`Publication asset figure IDs must be unique; duplicates: ${duplicates.join(", ")}`)
        }
        if (source.relative === currentArticleSource) {
          const count8A = ids.filter((id) => id === "08a").length
          const count8B = ids.filter((id) => id === "08b").length
          const count8 = ids.filter((id) => id === "08").length
          if (count8A !== 1 || count8B !== 1 || count8 !== 0) {
            throw new Error(`Current article assets require exactly one Figure 8A and one Figure 8B and no unsplit Figure 8; received 8A=${count8A}, 8B=${count8B}, unsplit=${count8}`)
          }
        }

        const title = source.data.title || "Untitled publication"
        wrapTitle(title, 42)
        wrapTitle(title, 34)
        const authors = normalizeAuthors(source.data.authors ?? source.data.author)
        const byline =
          authors.length > 0
            ? `${authors.join(", ")} · Uncertainty Architecture`
            : "Uncertainty Architecture"
        await writeCover(
          path.join(outputRoot, "cover-linkedin-article.png"),
          2000,
          600,
          title,
          byline,
          "LinkedIn article",
        )
        await writeCover(
          path.join(outputRoot, "social-preview.png"),
          1200,
          627,
          title,
          byline,
          "Thinking Systems",
        )
        await writeCover(
          path.join(outputRoot, "medium-hero.png"),
          1600,
          900,
          title,
          byline,
          "Medium",
        )

        const assetManifest = {
          schema_version: 1,
          artifact: "publication-assets",
          source_path: source.relative,
          source_commit: rendition.sourceCommit,
          source_state: provenance.state,
          source_git_blob_sha: provenance.committedBlob,
          source_working_blob_sha: provenance.workingBlob,
          source_sha256: sha256(Buffer.from(source.raw)),
          generated_at: new Date().toISOString(),
          canonical_url: source.data.canonical_url || null,
          additional_publication_urls: Array.isArray(source.data.additional_publication_urls)
            ? source.data.additional_publication_urls
            : [],
          figure_8_split_for_readability: rendition.figure8Split,
          figures: manifestFigures,
          covers: {
            linkedin_article: {
              path: path.relative(repoRoot, path.join(outputRoot, "cover-linkedin-article.png")).split(path.sep).join("/"),
              width: 2000,
              height: 600,
            },
            social_preview: {
              path: path.relative(repoRoot, path.join(outputRoot, "social-preview.png")).split(path.sep).join("/"),
              width: 1200,
              height: 627,
            },
            medium_hero: {
              path: path.relative(repoRoot, path.join(outputRoot, "medium-hero.png")).split(path.sep).join("/"),
              width: 1600,
              height: 900,
            },
          },
        }
        const manifestPath = path.join(outputRoot, "assets.manifest.json")
        await assertSafeOutputPath(repoRoot, publicationOutputRoot, manifestPath)
        await assertIndependentOutputTarget(manifestPath, [source.absolute])
        await writeFileAtomically(
          manifestPath,
          `${JSON.stringify(assetManifest, null, 2)}\n`,
          {
            trustedRoot: repoRoot,
            allowedRoot: publicationOutputRoot,
            forbiddenPaths: [source.absolute],
          },
        )
      } finally {
        await page.close()
      }
    })
  } finally {
    if (browser) await browser.close()
    if (server) await server.close()
    await rm(tempRoot, { recursive: true, force: true })
  }

  console.log(`Publication assets ready: ${path.relative(repoRoot, outputRoot)}`)
}

const isEntryPoint =
  process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)
if (isEntryPoint) {
  main().catch((error) => {
    console.error(
      `Publication asset rendering failed: ${error instanceof Error ? error.message : String(error)}`,
    )
    process.exitCode = 1
  })
}
