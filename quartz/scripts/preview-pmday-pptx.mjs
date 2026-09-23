// Inspect the exported package through an independent application. Rendering is
// evidence for visual review, never a substitute for PowerPoint acceptance.
import { createHash } from "node:crypto"
import { execFileSync } from "node:child_process"
import { mkdtemp, readFile, readdir, writeFile } from "node:fs/promises"
import path from "node:path"
import { fileURLToPath, pathToFileURL } from "node:url"
import { assertSafeOutputPath } from "./publication-path-safety.mjs"

const root = path.resolve(fileURLToPath(new URL("../..", import.meta.url)))
const sha = (data) => createHash("sha256").update(data).digest("hex")

export function verifyPng(bytes) {
  const signature = Buffer.from("89504e470d0a1a0a", "hex")
  const ending = Buffer.from("0000000049454e44ae426082", "hex")
  if (
    bytes.length < 45 ||
    !bytes.subarray(0, 8).equals(signature) ||
    !bytes.subarray(-12).equals(ending)
  )
    throw new Error("Truncated or invalid rendered PNG")
}

export function verifyRenderedText(text) {
  // Regression for the narrow SDLC node whose final letter wrapped in export.
  if (!/\bIntegrate\b/.test(text))
    throw new Error("Rendered SDLC label Integrate is missing or split")
  for (const label of ["Button A", "Window B"])
    if (!text.includes(label))
      throw new Error(`Rendered requirements label ${label} is missing or split`)
}

export async function renderIndependentPreview(pptx, env = process.env) {
  // Reuse the publication boundary check for the source without creating parents.
  const source = path.resolve(root, pptx)
  await assertSafeOutputPath(root, root, source, { createParent: false })
  if (path.extname(source).toLowerCase() !== ".pptx") throw new Error("Expected a PPTX source")
  const directory = path.join(root, "dist/pptx")
  await assertSafeOutputPath(root, directory, path.join(directory, "preview-placeholder"))
  const stage = await mkdtemp(path.join(directory, "libreoffice-"))
  const snapshot = path.join(stage, "review.pptx")
  const bytes = await readFile(source)
  await writeFile(snapshot, bytes, { flag: "wx" })
  const run = (binary, args) =>
    execFileSync(binary, args, {
      timeout: 120000,
      encoding: "utf8",
      stdio: ["ignore", "pipe", "pipe"],
    })
  const soffice = env.UA_SOFFICE || "soffice"
  const pdftoppm = env.UA_PDFTOPPM || "pdftoppm"
  const python = env.UA_PDF_PYTHON || "python3"
  run(soffice, [
    `-env:UserInstallation=${pathToFileURL(path.join(stage, "profile")).href}`,
    "--headless",
    "--convert-to",
    "pdf",
    "--outdir",
    stage,
    snapshot,
  ])
  const pdf = path.join(stage, "review.pdf")
  await readFile(pdf)
  verifyRenderedText(
    run(python, [
      "-c",
      'import sys; from pypdf import PdfReader; print("\\n".join(page.extract_text() or "" for page in PdfReader(sys.argv[1]).pages))',
      pdf,
    ]),
  )
  run(pdftoppm, ["-scale-to", "1440", "-png", pdf, path.join(stage, "slide")])
  const pngs = (await readdir(stage)).filter((name) => /^slide-\d+\.png$/.test(name)).sort()
  for (const name of pngs) verifyPng(await readFile(path.join(stage, name)))
  if (pngs.length !== 15) throw new Error(`Expected 15 rendered pages, found ${pngs.length}`)
  if (sha(await readFile(snapshot)) !== sha(bytes) || sha(await readFile(source)) !== sha(bytes))
    throw new Error("PPTX changed during preview")
  const report = {
    pptx_sha256: sha(bytes),
    renderer: run(soffice, ["--version"]).trim(),
    pdf_sha256: sha(await readFile(pdf)),
    slides: await Promise.all(
      pngs.map(async (name) => ({ name, sha256: sha(await readFile(path.join(stage, name))) })),
    ),
    visual_review: "pending; inspect every PNG",
    powerpoint_acceptance: "not performed",
  }
  await writeFile(
    path.join(stage, "render-evidence.json"),
    JSON.stringify(report, null, 2) + "\n",
    { flag: "wx" },
  )
  return stage
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  if (process.argv.length > 3)
    throw new Error("Usage: npm run pptx:preview -- [repo-relative PPTX]")
  renderIndependentPreview(
    process.argv[2] || "assets/presentations/pmday-2026/ai-changes-both-sides.pptx",
  )
    .then(console.log)
    .catch((error) => {
      console.error(error.message)
      process.exitCode = 1
    })
}
