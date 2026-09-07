import { execFileSync } from "node:child_process"
import { readFile } from "node:fs/promises"
import path from "node:path"
import { build } from "esbuild"
import { QuartzEmitterPlugin } from "../types"
import { FullSlug } from "../../util/path"
import { write } from "./helpers"
import { controlMapPage } from "../../components/controlMap/page"
import { validateData } from "../../components/controlMap/model"

export const RepositoryControlMap: QuartzEmitterPlugin = () => ({
  name: "RepositoryControlMap",
  async *emit(ctx) {
    // Quartz runs from the repository root. Keep Python arguments separate from
    // shell code, and bound output before parsing a complete materialization.
    const root = process.cwd()
    const args = [
      path.join(root, ".github/scripts/build_repository_control_map.py"),
      "--root",
      root,
    ]
    if (process.env.UA_MAP_ACCEPTED_REF)
      args.push("--accepted-ref", process.env.UA_MAP_ACCEPTED_REF)
    const json = execFileSync("python3", args, {
      encoding: "utf-8",
      maxBuffer: 8_000_000,
      timeout: 120_000,
    })
    validateData(JSON.parse(json))
    const bundle = await build({
      entryPoints: [path.join(root, "quartz/components/controlMap/client.ts")],
      bundle: true,
      minify: true,
      write: false,
      format: "esm",
      target: "es2020",
      legalComments: "eof",
    })
    const css = await readFile(path.join(root, "quartz/components/controlMap/style.css"), "utf-8")
    for (const [name, ext, content] of [
      ["index", ".html", controlMapPage],
      ["map", ".json", json],
      ["map", ".js", bundle.outputFiles[0].text],
      ["map", ".css", css],
    ] as const) {
      yield write({ ctx, slug: `control-map/${name}` as FullSlug, ext, content })
    }
  },
})
