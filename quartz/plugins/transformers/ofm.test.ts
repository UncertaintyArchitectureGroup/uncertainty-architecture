import assert from "node:assert/strict"
import test from "node:test"
import type { Blockquote, Root } from "mdast"
import { ObsidianFlavoredMarkdown } from "./ofm"

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

test("callout classes remain a HAST class-name list", () => {
  const plugin = ObsidianFlavoredMarkdown(calloutOnlyOptions)
  const markdownPlugins = plugin.markdownPlugins?.({} as never) ?? []
  assert.equal(markdownPlugins.length, 1)

  const transformerFactory = markdownPlugins[0]
  assert.equal(typeof transformerFactory, "function")
  const transformer = (transformerFactory as () => (tree: Root, file: object) => void)()

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
})
