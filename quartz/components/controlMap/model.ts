/** Presentation only: impact results and source facts come from the shared producer. */
export interface MapNode {
  id: string
  family: string
  path?: string
  title?: string
  term?: string
  identity?: string
  anchor?: string
  module?: string
  status?: string
  artifact_type?: string
  projection_role?: string
  [key: string]: unknown
}
export interface MapEdge {
  id: string
  source: string
  target: string
  relation: string
  edge_class: string
  impact_role: string
  impact_direction: string
  provenance: { path: string; kind: string; detail: string }
}
export interface MapSignal {
  id: string
  class: string
  subjects: string[]
  severity: string
  disposition: string
  evidence: { path: string; detail: string }
}
export interface Graph {
  nodes: MapNode[]
  edges: MapEdge[]
  signals: MapSignal[]
}
export interface MapData {
  map_version: number
  source_state: { kind: "accepted" | "preview"; ref: string | null }
  projection: {
    schema_version: number
    view: string
    graph: Graph
    source_identity: { digest: string; input_count: number }
    producer: { producer_version: number; interpretation_digest: string }
  }
  impact_by_path: Record<
    string,
    {
      changed: string[]
      impacted: { id: string }[]
      traversed_edges: MapEdge[]
    }
  >
  validation_by_path: Record<
    string,
    {
      validators: string[]
      tests: string[]
      workflows: string[]
      companion_candidates: string[]
      instructions: { path: string }[]
    }
  >
  live_overlay: { state: string; reason: string }
}
export type Lens = "explore" | "architecture" | "impact" | "diagnostics"
export interface Filters {
  lens: Lens
  selected: string
  global: boolean
  depth: number
  module: string
  family: string
  status: string
  relation: string
  edgeClass: string
  impactRole: string
  boundary: string
  extras: boolean
  expandControls: boolean
}
export const repositoryURL =
  "https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture"
export const label = (node: MapNode) =>
  node.title || node.term || node.identity || node.path || node.id

export function sourceURL(path: string, ref: string | null, anchor?: string): string | null {
  // Always construct an HTTPS link to this repository; projected text is never a URL.
  if (
    !path ||
    /[\\\x00-\x1f]/.test(path) ||
    path.split("/").some((part) => !part || part === "." || part === "..")
  )
    return null
  const revision = ref && /^[a-f0-9]{40}$/.test(ref) ? ref : "main"
  return `${repositoryURL}/blob/${revision}/${path.split("/").map(encodeURIComponent).join("/")}${anchor ? "#" + encodeURIComponent(anchor) : ""}`
}

export function validateData(value: unknown): MapData {
  const data = value as MapData
  if (
    data?.map_version !== 1 ||
    data.projection?.schema_version !== 2 ||
    data.projection.view !== "graph"
  )
    throw new Error("Unsupported map schema")
  if (
    !/^[a-f0-9]{64}$/.test(data.projection.source_identity?.digest) ||
    !["accepted", "preview"].includes(data.source_state?.kind)
  )
    throw new Error("Missing source identity")
  const ref = data.source_state.ref
  if (
    (ref !== null && !/^[a-f0-9]{40}$/.test(ref)) ||
    (data.source_state.kind === "accepted" && !ref)
  )
    throw new Error("Invalid source ref")
  const graph = data.projection.graph
  if (!Array.isArray(graph?.nodes) || !Array.isArray(graph.edges) || !Array.isArray(graph.signals))
    throw new Error("Incomplete graph")
  const nodeIds = new Set<string>(),
    edgeIds = new Set<string>()
  for (const node of graph.nodes) {
    if (
      typeof node.id !== "string" ||
      !node.id ||
      nodeIds.has(node.id) ||
      typeof node.family !== "string"
    )
      throw new Error("Invalid or duplicate node")
    for (const field of [
      "path",
      "title",
      "term",
      "identity",
      "anchor",
      "module",
      "status",
      "artifact_type",
    ]) {
      if (node[field] !== undefined && typeof node[field] !== "string")
        throw new Error("Invalid node field")
    }
    nodeIds.add(node.id)
  }
  for (const edge of graph.edges) {
    if (
      typeof edge.id !== "string" ||
      edgeIds.has(edge.id) ||
      !nodeIds.has(edge.source) ||
      !nodeIds.has(edge.target)
    )
      throw new Error("Invalid graph edge")
    if (
      !["source-to-target", "target-to-source", "both", "none"].includes(edge.impact_direction) ||
      !["dependency", "ownership", "provenance", "association", "navigation", "control"].includes(
        edge.impact_role,
      )
    )
      throw new Error("Unknown impact semantics")
    if (
      typeof edge.relation !== "string" ||
      typeof edge.edge_class !== "string" ||
      typeof edge.provenance?.path !== "string" ||
      typeof edge.provenance?.detail !== "string"
    )
      throw new Error("Missing edge evidence")
    edgeIds.add(edge.id)
  }
  if (
    !data.impact_by_path ||
    !data.validation_by_path ||
    data.live_overlay?.state !== "unavailable"
  )
    throw new Error("Missing map companion data")
  for (const item of Object.values(data.impact_by_path)) {
    if (
      !Array.isArray(item.changed) ||
      !Array.isArray(item.impacted) ||
      !Array.isArray(item.traversed_edges) ||
      item.impacted.some((n) => !nodeIds.has(n.id)) ||
      item.traversed_edges.some((e) => !edgeIds.has(e.id))
    )
      throw new Error("Incomplete impact evidence")
  }
  return data
}

export function primaryNode(node: MapNode): boolean {
  if (
    ["Term", "Responsibility", "ResearchItem", "AgentScope", "PolicyOrValidator"].includes(
      node.family,
    )
  )
    return true
  return (
    node.projection_role === "maintained-conceptual-process-artifact" ||
    node.projection_role === "repository-process-owner"
  )
}

export function selectedPaths(graph: Graph, selected: MapNode): string[] {
  if (selected.path) return [selected.path]
  // A responsibility resolves through explicit ownership, never graph centrality.
  const owners = new Set(
    graph.edges
      .filter((e) => e.target === selected.id && e.relation === "CANONICAL_FOR")
      .map((e) => e.source),
  )
  return graph.nodes.filter((n) => owners.has(n.id) && n.path).map((n) => n.path!)
}

export function nodeBoundaries(graph: Graph, node: MapNode): Set<string> {
  const paths = selectedPaths(graph, node)
  if (node.family === "ResearchItem") return new Set(["research"])
  return new Set(
    paths.map((path) =>
      path.startsWith("content/research/")
        ? "research"
        : /^(00-|01-|02-|03-|04-)/.test(path) || path === "SPECIFICATION.md"
          ? "framework"
          : "repository",
    ),
  )
}

export function impactView(
  data: MapData,
  selected: MapNode,
): { nodes: Set<string>; edges: Set<string> } {
  const nodes = new Set([selected.id]),
    edges = new Set<string>()
  for (const path of selectedPaths(data.projection.graph, selected)) {
    const result = data.impact_by_path[path]
    if (!result) continue
    result.changed.forEach((id) => nodes.add(id))
    result.impacted.forEach((item) => nodes.add(item.id))
    result.traversed_edges.forEach((edge) => edges.add(edge.id))
  }
  return { nodes, edges }
}

export function filterGraph(
  data: MapData,
  filters: Filters,
): { nodes: MapNode[]; edges: MapEdge[]; collapsed: MapEdge[] } {
  const graph = data.projection.graph
  const selected = graph.nodes.find((n) => n.id === filters.selected)
  const impact = selected && filters.lens === "impact" ? impactView(data, selected) : undefined
  const allowed = (n: MapNode) =>
    (!filters.module || n.module === filters.module) &&
    (!filters.family || n.family === filters.family) &&
    (!filters.status || n.status === filters.status) &&
    (!filters.boundary || nodeBoundaries(graph, n).has(filters.boundary))
  let nodes = graph.nodes.filter((n) =>
    impact ? impact.nodes.has(n.id) : filters.extras || primaryNode(n) || n.id === filters.selected,
  )
  const allowedIds = new Set(nodes.filter(allowed).map((n) => n.id))
  let nodeIds = new Set(nodes.map((n) => n.id))
  let edges = graph.edges.filter(
    (e) =>
      nodeIds.has(e.source) &&
      nodeIds.has(e.target) &&
      (!impact || impact.edges.has(e.id)) &&
      (!filters.relation || e.relation === filters.relation) &&
      (!filters.edgeClass || e.edge_class === filters.edgeClass) &&
      (!filters.impactRole || e.impact_role === filters.impactRole) &&
      (filters.lens === "explore" ||
        filters.relation === "LINKS_TO" ||
        filters.edgeClass === "navigation" ||
        e.edge_class !== "navigation"),
  )
  const degrees = new Map<string, number>()
  for (const e of graph.edges.filter((e) => e.impact_role === "control")) {
    degrees.set(e.source, (degrees.get(e.source) || 0) + 1)
    degrees.set(e.target, (degrees.get(e.target) || 0) + 1)
  }
  const collapsed =
    !impact && !filters.expandControls
      ? edges.filter(
          (e) =>
            e.impact_role === "control" &&
            Math.max(degrees.get(e.source) || 0, degrees.get(e.target) || 0) > 8,
        )
      : []
  const collapsedIds = new Set(collapsed.map((e) => e.id))
  edges = edges.filter((e) => !collapsedIds.has(e.id))
  if (!impact && !filters.global) {
    // Neighbourhood exploration is navigation, not the impact algorithm.
    const reached = new Set([filters.selected])
    const distance = new Map([[filters.selected, 0]])
    for (let step = 0; step < filters.depth; step++) {
      const frontier = new Set(reached)
      for (const edge of edges) {
        if (frontier.has(edge.source) && !distance.has(edge.target)) {
          reached.add(edge.target)
          distance.set(edge.target, step + 1)
        }
        if (frontier.has(edge.target) && !distance.has(edge.source)) {
          reached.add(edge.source)
          distance.set(edge.source, step + 1)
        }
      }
    }
    nodes = nodes.filter((n) => reached.has(n.id))
    nodeIds = new Set(nodes.map((n) => n.id))
    // Suppress lateral links within one hop level on the local canvas. Their
    // full records remain in the inspector/global view, not silently discarded.
    edges = edges.filter(
      (e) =>
        nodeIds.has(e.source) &&
        nodeIds.has(e.target) &&
        Math.abs(distance.get(e.source)! - distance.get(e.target)!) === 1,
    )
  }
  // Node filters narrow the established neighbourhood, not the paths used to
  // discover it. A hidden focus or intermediate node must not erase matches.
  nodes = nodes.filter((n) => allowedIds.has(n.id))
  nodeIds = new Set(nodes.map((n) => n.id))
  edges = edges.filter((e) => nodeIds.has(e.source) && nodeIds.has(e.target))
  return {
    nodes,
    edges,
    collapsed: collapsed.filter((e) => allowedIds.has(e.source) && allowedIds.has(e.target)),
  }
}

export function structuralWarnings(graph: Graph): { node: MapNode; message: string }[] {
  const linked = new Set(
    graph.edges
      .filter((e) => e.edge_class === "semantic-evolution")
      .flatMap((e) => [e.source, e.target]),
  )
  return graph.nodes
    .filter((n) => n.family === "Document" && primaryNode(n) && !linked.has(n.id))
    .map((node) => ({
      node,
      message:
        "No explicit semantic or ownership links in this projection. Review if additional source relationships would help; this is not a defect.",
    }))
}
