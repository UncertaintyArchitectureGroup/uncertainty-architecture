import { test } from "node:test"
import assert from "node:assert/strict"
import { RepositoryControlMap } from "./controlMap"
import ControlMapLink from "../../components/ControlMapLink"
import type { BuildCtx } from "../../util/ctx"
import type { QuartzComponentProps } from "../../components/types"

test("temporary draft/PDF builds omit the map and its navigation entry", async () => {
  const previous = process.env.UA_INCLUDE_DRAFTS
  process.env.UA_INCLUDE_DRAFTS = "1"
  try {
    const emitted = []
    // No repository/build context is needed: the producer must not inspect the
    // temporary publication rendition, which is not canonical projection data.
    const result = await RepositoryControlMap().emit({} as BuildCtx, [], {
      css: [],
      js: [],
      additionalHead: [],
    })
    for await (const item of result) emitted.push(item)
    assert.deepEqual(emitted, [])
    assert.equal(ControlMapLink()({} as QuartzComponentProps), null)
  } finally {
    if (previous === undefined) delete process.env.UA_INCLUDE_DRAFTS
    else process.env.UA_INCLUDE_DRAFTS = previous
  }
})
