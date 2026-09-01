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

function callout(value: string): Blockquote {
  return {
    type: "blockquote",
    children: [
      {
        type: "paragraph",
        children: [{ type: "text", value }],
      },
      {
        type: "paragraph",
        children: [{ type: "text", value: "Body" }],
      },
    ],
  }
}

test("callout classes remain HAST class-name lists", async () => {
  const directory = await mkdtemp(path.join(tmpdir(), "ua-ofm-test-"))
  const outfile = path.join(directory, "ofm.bundle.mjs")
  try {
    await build({
      entryPoints: [path.resolve("quartz/plugins/transformers/ofm.ts")],
      bundle: true,
      format: "esm",
      platform: "node",
      loader: { ".scss": "text" },
      plugins: [
        {
          name: "quartz-inline-script-stubs",
          setup(esbuild) {
            // Quartz imports *.inline.ts modules as source text in its production bundling path.
            // Stub only that boundary; bundle ordinary dependencies so the temp module is hermetic.
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

    const normal = callout("[!note] Regression")
    const collapsed = callout("[!warning]- Collapsed")
    const tree: Root = { type: "root", children: [normal, collapsed] }
    const file = { data: { slug: "index" } }

    for (const pluginEntry of markdownPlugins) {
      assert.equal(typeof pluginEntry, "function")
      const transformer = (pluginEntry as () => unknown)()
      if (typeof transformer === "function") {
        transformer(tree, file)
      }
    }

    assert.deepEqual(normal.data?.hProperties?.className, ["callout", "note"])
    assert.deepEqual(collapsed.data?.hProperties?.className, [
      "callout",
      "warning",
      "is-collapsible",
      "is-collapsed",
    ])
  } finally {
    await rm(directory, { recursive: true, force: true })
  }
})
