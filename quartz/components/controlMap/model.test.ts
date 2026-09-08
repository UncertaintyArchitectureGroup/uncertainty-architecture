import { test } from "node:test"
import assert from "node:assert/strict"
import {
  filterGraph,
  impactView,
  sourceURL,
  structuralWarnings,
  validateData,
  type MapData,
  type Filters,
  type MapEdge,
} from "./model"

const edge = (source: string, target: string, role = "control"): MapEdge => ({
  id: source + ":" + target,
  source,
  target,
  relation: role === "control" ? "SCOPED_BY" : "LINKS_TO",
  impact_role: role,
  impact_direction: role === "control" ? "both" : "none",
  edge_class: role === "control" ? "repository-control" : "navigation",
  provenance: { path: "AGENTS.md", kind: "scope", detail: "Fixture" },
})
function fixture(): MapData {
  const nodes = Array.from({ length: 12 }, (_, i) => ({
    id: "d" + i,
    path: `01-patterns/${i}.md`,
    title: `Document ${i}`,
    module: "patterns",
    family: "Document",
    projection_role: "maintained-conceptual-process-artifact",
  }))
  const hub = { id: "hub", path: "AGENTS.md", family: "AgentScope" }
  const edges = nodes.map((n) => edge(n.id, hub.id))
  edges.push(edge("d0", "d1", "navigation"))
  return {
    map_version: 1,
    source_state: { kind: "accepted", ref: "a".repeat(40) },
    projection: {
      schema_version: 2,
      view: "graph",
      source_identity: { digest: "b".repeat(64), input_count: 1 },
      producer: { producer_version: 6, interpretation_digest: "c".repeat(64) },
      graph: { nodes: [...nodes, hub], edges, signals: [] },
    },
    impact_by_path: {
      "01-patterns/0.md": {
        changed: ["d0"],
        impacted: [{ id: "hub" }],
        traversed_edges: [edges[0]],
      },
    },
    validation_by_path: {},
    live_overlay: { state: "unavailable", reason: "No overlay" },
  }
}
const filters: Filters = {
  lens: "explore",
  selected: "d0",
  global: false,
  depth: 2,
  module: "",
  family: "",
  status: "",
  relation: "",
  edgeClass: "",
  impactRole: "",
  boundary: "",
  extras: false,
  expandControls: false,
}

test("collapsed controls cannot flood a local neighbourhood through a shared hub", () => {
  const view = filterGraph(fixture(), filters)
  assert.deepEqual(
    view.nodes.map((n) => n.id),
    ["d0", "d1"],
  )
  assert.equal(view.collapsed.length, 12)
  assert.equal(fixture().projection.graph.edges.length, 13)
  assert.equal(filterGraph(fixture(), { ...filters, expandControls: true }).nodes.length, 13)
})
test("impact consumes producer results and never propagates through a control hub", () => {
  const data = fixture()
  assert.deepEqual([...impactView(data, data.projection.graph.nodes[0]).nodes], ["d0", "hub"])
  assert.deepEqual(
    filterGraph(data, { ...filters, lens: "impact", global: true }).nodes.map((n) => n.id),
    ["d0", "hub"],
  )
})
test("filters and architecture navigation exclusion remain explicit", () => {
  assert.equal(filterGraph(fixture(), { ...filters, lens: "architecture" }).edges.length, 0)
  assert.equal(filterGraph(fixture(), { ...filters, family: "Term", global: true }).nodes.length, 0)
  assert.equal(
    filterGraph(fixture(), {
      ...filters,
      lens: "architecture",
      relation: "LINKS_TO",
    }).edges.length,
    1,
  )
})
test("local filters preserve matching neighbours when the focus is hidden", () => {
  const data = fixture()
  data.projection.graph.nodes.push({ id: "owner-role", family: "Responsibility" })
  data.projection.graph.edges.push({
    ...edge("d0", "owner-role", "ownership"),
    relation: "CANONICAL_FOR",
    edge_class: "semantic-evolution",
  })
  for (const lens of ["explore", "architecture"] as const) {
    const view = filterGraph(data, { ...filters, lens, family: "Responsibility", depth: 1 })
    assert.deepEqual(
      view.nodes.map((n) => n.id),
      ["owner-role"],
    )
    assert.deepEqual(view.edges, [])
  }
})
test("node filters retain two-hop matches through a hidden intermediate node", () => {
  const data = fixture()
  Object.assign(data.projection.graph.nodes[2], {
    module: "research",
    path: "content/research/result.md",
    status: "informative",
  })
  data.projection.graph.edges.push(edge("d1", "d2", "navigation"))
  for (const filter of [
    { module: "research" },
    { status: "informative" },
    { boundary: "research" },
  ]) {
    assert.deepEqual(
      filterGraph(data, { ...filters, ...filter }).nodes.map((n) => n.id),
      ["d2"],
    )
    assert.equal(filterGraph(data, { ...filters, ...filter, depth: 1 }).nodes.length, 0)
  }
  assert.equal(filterGraph(data, { ...filters, module: "absent" }).nodes.length, 0)
})
test("source links stay in the pinned repository even for hostile names", () => {
  assert.equal(sourceURL("../secret", "a".repeat(40)), null)
  assert.equal(sourceURL("/absolute", null), null)
  assert.equal(sourceURL("a\\b", null), null)
  const link = sourceURL("content/raw/A file #?.md", "a".repeat(40), "<script>")!
  assert.ok(link.includes("/" + "a".repeat(40) + "/content/raw/A%20file%20%23%3F.md#%3Cscript%3E"))
})
test("invalid or incomplete graph evidence fails visibly", () => {
  assert.equal(validateData(fixture()).map_version, 1)
  for (const mutation of [
    (d: MapData) => {
      d.projection.schema_version = 99
    },
    (d: MapData) => {
      d.source_state.ref = null
    },
    (d: MapData) => {
      d.projection.graph.nodes.pop()
    },
    (d: MapData) => {
      d.projection.graph.nodes.push(d.projection.graph.nodes[0])
    },
    (d: MapData) => {
      d.projection.graph.edges[0].impact_role = "invented"
    },
    (d: MapData) => {
      d.impact_by_path["01-patterns/0.md"].impacted.push({ id: "absent" })
    },
  ]) {
    const value = fixture()
    mutation(value)
    assert.throws(() => validateData(value))
  }
})
test("structural warnings do not become producer defects", () => {
  const data = fixture()
  assert.equal(structuralWarnings(data.projection.graph).length, 12)
  assert.equal(data.projection.graph.signals.length, 0)
  assert.match(structuralWarnings(data.projection.graph)[0].message, /not a defect/)
})

test("local views hide lateral clutter without losing global relationships", () => {
  const data = fixture()
  data.projection.graph.edges.push(edge("d0", "d2", "navigation"), edge("d1", "d2", "navigation"))
  assert.equal(filterGraph(data, { ...filters, depth: 1 }).edges.length, 2)
  assert.equal(filterGraph(data, { ...filters, global: true }).edges.length, 3)
})

test("responsibility boundary follows its declared owner", () => {
  const data = fixture()
  data.projection.graph.nodes.push({
    id: "responsibility:test",
    family: "Responsibility",
  })
  data.projection.graph.edges.push({
    ...edge("d0", "responsibility:test", "ownership"),
    relation: "CANONICAL_FOR",
    edge_class: "semantic-evolution",
    impact_direction: "none",
  })
  assert.ok(
    filterGraph(data, {
      ...filters,
      global: true,
      boundary: "framework",
    }).nodes.some((n) => n.id === "responsibility:test"),
  )
  assert.ok(
    !filterGraph(data, {
      ...filters,
      global: true,
      boundary: "repository",
    }).nodes.some((n) => n.id === "responsibility:test"),
  )
})
