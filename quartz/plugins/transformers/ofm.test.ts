import assert from "node:assert/strict"
import { mkdtemp, rm } from "node:fs/promises"
import { tmpdir } from "node:os"
import path from "node:path"
import test from "node:test"
import { pathToFileURL } from "node:url"
import { build } from "esbuild"
import type { Blockquote, Root } from "mdast"

const calloutOnlyOptions = {
  comments: false,
  highlight: false,
  wikilinks: false,
  callouts: true,
  mermaid: false,
  parseTags: false,
  parseArrows: false,
  parseBlockReferences: false,
  enableInHtmlEmbed: false,
  enableYouTubeEmbed: false,
  enableVideoEmbed: false,
  enableCheckbox: false,
  disableBrokenWikilinks: false,
}

test("callout classes remain a HAST class-name list", async () => {
  const directory = await mkdtemp(path.join(tmpdir(), "ua-ofm-test-"))
  const outfile = path.join(directory, "ofm.bundle.mjs")
  try {
    await build({
      entryPoints: [path.resolve("quartz/plugins/transformers/ofm.ts")],
      bundle: true,
      format: "esm",
      platform: "node",
      packages: "external",
      loader: { ".scss": "text" },
      plugins: [
        {
          name: "quartz-inline-script-stubs",
          setup(esbuild) {
            // Quartz imports *.inline.ts modules as source text in its production bundling path.
            // Stub only that boundary so this test exercises the real OFM transformer.
            esbuild.onResolve({ filter: /\.inline$/ }, (args) => ({
              path: args.path,
              namespace: "quartz-inline-script",
            }))
            esbuild.onLoad({ filter: /.*/, namespace: "quartz-inline-script" }, () => ({
              contents: 'export default ""',
              loader: "js",
            }))
          },
        },
      ],
      outfile,
      logLevel: "silent",
    })

    const { ObsidianFlavoredMarkdown } = await import(pathToFileURL(outfile).href)
    const plugin = ObsidianFlavoredMarkdown(calloutOnlyOptions)
    const markdownPlugins = plugin.markdownPlugins?.({}) ?? []
    assert.equal(markdownPlugins.length, 1)

    const transformerFactory = markdownPlugins[0]
    assert.equal(typeof transformerFactory, "function")
    const transformer = transformerFactory()

    const blockquote: Blockquote = {
      type: "blockquote",
      children: [
        {
          type: "paragraph",
          children: [{ type: "text", value: "[!note] Regression" }],
        },
        {
          type: "paragraph",
          children: [{ type: "text", value: "Body" }],
        },
      ],
    }
    const tree: Root = { type: "root", children: [blockquote] }

    transformer(tree, { data: {} })

    assert.deepEqual(blockquote.data?.hProperties?.className, ["callout", "note"])
  } finally {
    await rm(directory, { recursive: true, force: true })
  }
})
