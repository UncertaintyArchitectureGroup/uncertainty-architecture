import { createHash } from "node:crypto"
import { execFileSync } from "node:child_process"
import { access, mkdtemp, mkdir, readFile, writeFile } from "node:fs/promises"
import path from "node:path"
import { fileURLToPath, pathToFileURL } from "node:url"
import { parseDeck, createDeck, theme } from "./pmday-presentation.mjs"
import { assertSafeOutputPath, assertIndependentOutputTarget } from "./publication-path-safety.mjs"
import { finalizePublicationPair } from "./render-publication-pdf.mjs"

const root = path.resolve(fileURLToPath(new URL("../..", import.meta.url)))
const directory = "assets/presentations/pmday-2026"
const source = `${directory}/README.md`
const cover = `${directory}/artwork/ai-two-roles.png`
const fonts = `${directory}/artwork/roboto-fonts.zip`
const inputs = [
  source,
  cover,
  fonts,
  `${directory}/frozen-slides.json`,
  "quartz/scripts/pmday-presentation.mjs",
  "quartz/scripts/build-pmday-pptx.mjs",
  "quartz/scripts/validate-pmday-pptx.py",
  "quartz/scripts/pmday-fonts.py",
]
const sha = (bytes) => createHash("sha256").update(bytes).digest("hex")

export function runtimeEnvironment(env) {
  return {
    RUNTIME_NODE: env.CODEX_PRIMARY_RUNTIME_NODE,
    RUNTIME_NODE_MODULES: env.CODEX_PRIMARY_RUNTIME_NODE_MODULES,
    RUNTIME_PYTHON: env.CODEX_PRIMARY_RUNTIME_PYTHON,
    RUNTIME_BIN_DIR: path.join(env.CODEX_PRIMARY_RUNTIME_ROOT, "dependencies/bin/override"),
  }
}

export async function verifyPptxPair(pptx, manifest) {
  const record = JSON.parse(await readFile(manifest, "utf8"))
  if (record.pptx_sha256 !== sha(await readFile(pptx)))
    throw new Error("PPTX/manifest checksum mismatch")
  return record
}

async function main() {
  if (!process.env.CODEX_PRIMARY_RUNTIME_ROOT)
    throw new Error(
      "Codex primary runtime is required for authoring; use pptx:verify for portable CI",
    )
  Object.assign(process.env, runtimeEnvironment(process.env))
  const flags = process.argv.slice(2)
  if (flags.some((flag) => flag !== "--promote"))
    throw new Error("Usage: npm run pptx:pmday -- [--promote]")
  const modules = process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES
  const node = process.env.CODEX_PRIMARY_RUNTIME_NODE
  const python = process.env.CODEX_PRIMARY_RUNTIME_PYTHON
  const skill = process.env.UA_PRESENTATION_SKILL_DIR
  if (![modules, node, python, skill].every((v) => v && path.isAbsolute(v))) {
    throw new Error(
      "Authoring needs Codex primary runtime variables and UA_PRESENTATION_SKILL_DIR. CI can run npm run pptx:verify without this runtime.",
    )
  }
  for (const item of [
    modules,
    node,
    python,
    path.join(skill, "container_tools/artifact_tool_utils.mjs"),
  ])
    await access(item)
  const pkg = JSON.parse(
    await readFile(path.join(modules, "@oai/artifact-tool/package.json"), "utf8"),
  )
  if (pkg.version !== "2.8.59")
    throw new Error(`Unreviewed authoring runtime ${pkg.version}; expected 2.8.59`)
  const identity = Object.fromEntries(
    await Promise.all(
      inputs.map(async (name) => [name, sha(await readFile(path.join(root, name)))]),
    ),
  )
  const data = parseDeck(await readFile(path.join(root, source), "utf8"))
  const { Presentation, PresentationFile } = await import(
    pathToFileURL(path.join(modules, "@oai/artifact-tool/dist/artifact_tool.mjs")).href
  )
  const { finalizePresentation } = await import(
    pathToFileURL(path.join(skill, "container_tools/artifact_tool_utils.mjs")).href
  )
  const dist = path.join(root, "dist/pptx")
  await assertSafeOutputPath(root, dist, path.join(dist, "stage-placeholder"))
  const stage = await mkdtemp(path.join(dist, "pmday-"))
  const draft = path.join(stage, "candidate.pptx")
  const embedded = path.join(stage, "embedded.pptx")
  const checked = path.join(stage, "output", "ai-changes-both-sides.pptx")
  const manifest = path.join(stage, "output", "ai-changes-both-sides.manifest.json")
  await mkdir(path.dirname(checked), { recursive: true })
  const deck = createDeck(Presentation, data, { cover: await readFile(path.join(root, cover)) })
  await (await PresentationFile.exportPptx(deck)).save(draft)
  execFileSync(
    python,
    [path.join(root, "quartz/scripts/pmday-fonts.py"), draft, embedded, path.join(root, fonts)],
    { stdio: "inherit" },
  )
  await finalizePresentation({
    workspaceDir: root,
    candidatePath: embedded,
    finalPath: checked,
    explicitTotalSlideCount: 14,
    requiredNativeTableOwnerSlides: [11, 13],
    requiredNativeChartOwnerSlides: [],
    pythonExecutable: python,
    integrityValidatorPath: path.join(
      skill,
      "container_tools/inspect_presentation_package_integrity.py",
    ),
    layoutValidatorPath: path.join(
      skill,
      "container_tools/inspect_presentation_layout_geometry.py",
    ),
    layoutArgs: [
      "--expected-slide-size-emu",
      "12192000,6858000",
      "--validate-heading-fit",
      "--require-native-table-slide",
      "11",
      "--require-native-table-slide",
      "13",
    ],
    fontPolicy: { basis: "user_request", families: [theme.font] },
    verifyArtifactToolImport: true,
    receiptPath: path.join(stage, "validation.json"),
  })
  const record = {
    schema_version: 1,
    edition: "pmday-2026-review-candidate",
    source,
    inputs: identity,
    authoring_runtime: {
      package: "@oai/artifact-tool",
      version: pkg.version,
      bundle: process.env.CODEX_PRIMARY_RUNTIME_BUNDLE_VERSION || "unreported",
    },
    pptx_sha256: sha(await readFile(checked)),
    slide_count: 14,
    image_exceptions: [
      { slide: 1, asset: cover, purpose: "Requested conceptual cover illustration" },
    ],
    target_application: "Microsoft PowerPoint",
    visual_review: "required separately; structural validation is not visual acceptance",
  }
  // Refuse a mixed-source artifact if files changed during rendering.
  for (const name of inputs)
    if (identity[name] !== sha(await readFile(path.join(root, name))))
      throw new Error(`Source changed during generation: ${name}`)
  await writeFile(manifest, JSON.stringify(record, null, 2) + "\n", { flag: "wx" })
  execFileSync(
    python,
    [
      path.join(root, "quartz/scripts/validate-pmday-pptx.py"),
      "--pptx",
      checked,
      "--manifest",
      manifest,
    ],
    { stdio: "inherit" },
  )
  if (flags.includes("--promote")) {
    const allowed = path.join(root, directory)
    const output = path.join(allowed, path.basename(checked))
    const outputManifest = path.join(allowed, path.basename(manifest))
    for (const target of [output, outputManifest]) {
      await assertSafeOutputPath(root, allowed, target)
      await assertIndependentOutputTarget(
        target,
        inputs.map((name) => path.join(root, name)),
      )
    }
    // Reuse the established rollback-capable pair installer with PPTX-specific verification.
    await finalizePublicationPair(checked, manifest, output, outputManifest, {
      verifyImpl: verifyPptxPair,
    })
    console.log(output)
  } else console.log(checked)
}

if (process.argv[1] && pathToFileURL(path.resolve(process.argv[1])).href === import.meta.url) {
  main().catch((error) => {
    console.error(error.message)
    process.exitCode = 1
  })
}
