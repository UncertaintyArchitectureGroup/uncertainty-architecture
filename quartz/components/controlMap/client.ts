import cytoscape from "cytoscape"
import {
  filterGraph,
  label,
  primaryNode,
  repositoryURL,
  selectedPaths,
  sourceURL,
  structuralWarnings,
  validateData,
  type Filters,
  type Lens,
  type MapData,
  type MapEdge,
} from "./model"

const element = <T extends HTMLElement = HTMLElement>(id: string) =>
  document.getElementById(id) as T
const make = <K extends keyof HTMLElementTagNameMap>(tag: K, text?: string) => {
  const node = document.createElement(tag)
  if (text !== undefined) node.textContent = text
  return node
}
const descriptions: Record<Lens, string> = {
  explore:
    "Browse the immediate neighbourhood of a document or term. Select any record to explore further.",
  architecture:
    "Inspect declared ownership, provenance and repository controls. Navigation links are hidden by default.",
  impact:
    "Review direct dependency and control relevance for the selected source. Shared controls do not propagate to sibling documents.",
  diagnostics:
    "Separate producer errors from explained structural warnings. Open the source before interpreting a signal.",
}
const colors: Record<string, string> = {
  Document: "#8ebed3",
  Term: "#c9e58d",
  Responsibility: "#d3a6dc",
  AgentScope: "#e7b888",
  PolicyOrValidator: "#e7b888",
  ResearchItem: "#83cdb6",
}

function start(data: MapData) {
  const graph = data.projection.graph
  const nodes = new Map(graph.nodes.map((n) => [n.id, n]))
  const edges = new Map(graph.edges.map((e) => [e.id, e]))
  const initial = new URL(location.href).searchParams.get("node")
  const defaultNode = "document:00-doctrine/control-loop-anatomy.md"
  const filters: Filters = {
    lens: "explore",
    selected:
      initial && nodes.has(initial)
        ? initial
        : nodes.has(defaultNode)
          ? defaultNode
          : graph.nodes[0]?.id || "",
    global: false,
    depth: 1,
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
  let selectedEdge: string | undefined
  const sourceRef = data.source_state.ref
  element("source-state").textContent =
    `${data.source_state.kind === "accepted" ? "Published snapshot" : "Build preview"} · ${sourceRef?.slice(0, 7) || "working tree — source links use main"}`
  element("counts").textContent =
    `${graph.nodes.length} records / ${graph.edges.length} relationships`
  element("identity").textContent =
    `Source digest: ${data.projection.source_identity.digest}. Producer ${data.projection.producer.producer_version}. Interpretation: ${data.projection.producer.interpretation_digest}. ${sourceRef ? "Source links are pinned to " + sourceRef + "." : "Working-tree facts may differ from linked main sources."}`

  // Canvas handles gestures; the parallel HTML lists provide keyboard selection.
  // Repository text is inserted with textContent, never interpreted as markup.
  const cy = cytoscape({
    container: element("graph"),
    elements: [],
    minZoom: 0.15,
    maxZoom: 3,
    wheelSensitivity: 0.25,
    boxSelectionEnabled: false,
    selectionType: "single",
    style: [
      {
        selector: "node",
        style: {
          label: "data(label)",
          "background-color": "data(color)",
          width: 20,
          height: 20,
          color: "#dbe7e6",
          "font-size": 18,
          "text-valign": "bottom",
          "text-margin-y": 7,
          "text-wrap": "ellipsis",
          "text-max-width": "150px",
          "border-width": 1,
          "border-color": "#263638",
        },
      },
      {
        selector: "node.focus",
        style: {
          width: 28,
          height: 28,
          "border-width": 3,
          "border-color": "#ffffff",
          "font-size": 20,
        },
      },
      {
        selector: "node:selected",
        style: { "border-width": 3, "border-color": "#ffffff" },
      },
      {
        selector: "edge",
        style: {
          width: 1.2,
          "line-color": "#536a70",
          "target-arrow-color": "#536a70",
          "source-arrow-color": "#536a70",
          "curve-style": "bezier",
          "target-arrow-shape": (edge) => edge.data("targetArrow"),
          "source-arrow-shape": (edge) => edge.data("sourceArrow"),
          "arrow-scale": 0.7,
        },
      },
      {
        selector: "edge.control",
        style: { "line-style": "dashed", "line-color": "#af8c69" },
      },
      {
        selector: "edge:selected",
        style: {
          width: 3,
          "line-color": "#c9e58d",
          "target-arrow-color": "#c9e58d",
          "source-arrow-color": "#c9e58d",
        },
      },
    ],
  })
  const resize = new ResizeObserver(() => cy.resize())
  resize.observe(element("graph"))
  window.addEventListener(
    "pagehide",
    () => {
      resize.disconnect()
      cy.destroy()
    },
    { once: true },
  )

  function addSource(container: HTMLElement, path: string, anchor?: string) {
    const url = sourceURL(path, sourceRef, anchor)
    if (!url) return
    const link = make("a", "Open source ↗")
    link.href = url
    link.className = "source-link"
    link.target = "_blank"
    link.rel = "noopener noreferrer"
    container.append(link)
  }
  function fieldList(container: HTMLElement, values: Record<string, unknown>) {
    const dl = make("dl")
    for (const [name, value] of Object.entries(values)) {
      if (value === undefined || value === "") continue
      dl.append(
        make("dt", name),
        make("dd", Array.isArray(value) ? value.join(", ") : String(value)),
      )
    }
    container.append(dl)
  }
  function edgeButton(edge: MapEdge) {
    const button = make(
      "button",
      `${label(nodes.get(edge.source)!)} → ${edge.relation} → ${label(nodes.get(edge.target)!)}`,
    )
    button.addEventListener("click", () => {
      selectedEdge = edge.id
      inspect()
      cy.$id(edge.id).select()
    })
    return button
  }
  function inspect() {
    const panel = element("inspector")
    panel.replaceChildren()
    const edge = selectedEdge ? edges.get(selectedEdge) : undefined
    if (edge) {
      panel.append(
        make("h2", edge.relation),
        make("p", "Declared relation direction and impact direction are separate."),
      )
      fieldList(panel, {
        From: label(nodes.get(edge.source)!),
        To: label(nodes.get(edge.target)!),
        Class: edge.edge_class,
        "Impact role": edge.impact_role,
        "Impact direction": edge.impact_direction,
        Evidence: edge.provenance.kind,
        Declaration: edge.provenance.detail,
      })
      addSource(panel, edge.provenance.path)
      for (const id of [edge.source, edge.target]) {
        const button = make("button", "Inspect " + label(nodes.get(id)!))
        button.addEventListener("click", () => selectNode(id))
        panel.append(button)
      }
      return
    }
    const node = nodes.get(filters.selected)
    if (!node) {
      panel.append(make("p", "No record selected."))
      return
    }
    panel.append(make("h2", label(node)))
    fieldList(panel, {
      Type: node.family,
      Path: node.path,
      Module: node.module,
      Status: node.status,
      Artifact: node.artifact_type,
      Role: node.projection_role,
      "Declared ownership": node.canonical_for,
      "Research state": node.research_state,
    })
    if (node.path) addSource(panel, node.path, node.anchor)
    const relations = graph.edges.filter((e) => e.source === node.id || e.target === node.id)
    // Show scope/control relations attached to any representation of this path.
    const representations = new Set(
      graph.nodes.filter((n) => node.path && n.path === node.path).map((n) => n.id),
    )
    const controls = graph.edges.filter(
      (e) =>
        e.impact_role === "control" &&
        (representations.has(e.source) || representations.has(e.target)),
    )
    const complete = [...new Map([...relations, ...controls].map((e) => [e.id, e])).values()]
    const details = make("details")
    details.open = true
    details.append(
      make("summary", `${complete.length} declared relationships · includes hidden links`),
    )
    const list = make("div")
    list.className = "relation-list"
    complete.forEach((e) => list.append(edgeButton(e)))
    details.append(list)
    panel.append(details)
    for (const path of selectedPaths(graph, node)) {
      const plan = data.validation_by_path[path]
      if (!plan) continue
      const guidance = make("details")
      guidance.append(make("summary", "Likely checks and companion sources"))
      const paths = [
        ...new Set([
          ...plan.validators,
          ...plan.tests,
          ...plan.workflows,
          ...plan.companion_candidates,
          ...plan.instructions.map((i) => i.path),
        ]),
      ]
      const ul = make("ul")
      for (const candidate of paths) {
        const li = make("li"),
          url = sourceURL(candidate, sourceRef)
        if (url) {
          const a = make("a", candidate)
          a.href = url
          a.target = "_blank"
          a.rel = "noopener noreferrer"
          li.append(a)
        } else li.textContent = candidate
        ul.append(li)
      }
      guidance.append(ul)
      panel.append(guidance)
    }
  }
  function diagnostics() {
    const panel = element("diagnostics")
    panel.replaceChildren(
      make("h2", "Diagnostics"),
      make("h3", `Producer signals · ${graph.signals.length}`),
    )
    if (!graph.signals.length)
      panel.append(
        make(
          "p",
          "No deterministic signals were reported by this projection. This is not a semantic review of the repository.",
        ),
      )
    for (const signal of graph.signals) {
      const row = make("div")
      row.className = "diagnostic"
      row.append(
        make("strong", `${signal.severity} · ${signal.class}`),
        make("p", signal.evidence.detail),
      )
      addSource(row, signal.evidence.path)
      for (const id of signal.subjects)
        if (nodes.has(id)) {
          const button = make("button", label(nodes.get(id)!))
          button.addEventListener("click", () => selectNode(id))
          row.append(button)
        }
      panel.append(row)
    }
    const warnings = structuralWarnings(graph)
    panel.append(make("h3", `Structural review signals · ${warnings.length}`))
    for (const warning of warnings) {
      const row = make("div")
      row.className = "diagnostic"
      const button = make("button", label(warning.node))
      button.addEventListener("click", () => selectNode(warning.node.id))
      row.append(button, make("p", warning.message))
      panel.append(row)
    }
    panel.append(
      make("h3", "Model-judgment candidates"),
      make(
        "p",
        "Not evaluated. This map does not infer contradictions, synonyms, or semantic authority.",
      ),
    )
  }
  function render() {
    const view = filterGraph(data, filters)
    cy.elements().remove()
    cy.add([
      ...view.nodes.map((n) => ({
        data: {
          id: n.id,
          label: label(n),
          color: colors[n.family] || "#8ebed3",
        },
        classes: n.id === filters.selected ? "focus" : "",
      })),
      ...view.edges.map((e) => ({
        data: {
          id: e.id,
          source: e.source,
          target: e.target,
          targetArrow: ["source-to-target", "both"].includes(e.impact_direction)
            ? "triangle"
            : "none",
          sourceArrow: ["target-to-source", "both"].includes(e.impact_direction)
            ? "triangle"
            : "none",
        },
        classes: e.impact_role === "control" ? "control" : "",
      })),
    ])
    const local = !filters.global || filters.lens === "impact"
    const neighbours = cy.$id(filters.selected).neighborhood().nodes()
    cy.layout(
      local
        ? {
            name: "concentric",
            animate: false,
            fit: true,
            padding: 45,
            minNodeSpacing: 40,
            avoidOverlap: true,
            concentric: (node) =>
              node.id() === filters.selected ? 3 : neighbours.has(node) ? 2 : 1,
            levelWidth: () => 1,
          }
        : {
            name: "cose",
            animate: false,
            randomize: true,
            fit: true,
            padding: 45,
            nodeRepulsion: () => 30000,
            idealEdgeLength: () => 130,
            numIter: 500,
          },
    ).run()
    element("visible-count").textContent =
      `${view.nodes.length} visible records · ${view.edges.length} links`
    element("view-note").textContent =
      filters.lens === "impact"
        ? "Arrows show impact direction. Direct results from the shared producer; filters may hide relevant records. Missing links do not prove absence of impact."
        : `${view.collapsed.length} control links collapsed. Local views show links between hop levels; the inspector preserves all relationships. Arrows show impact direction; relation direction is in the inspector.`
    const records = element("visible-records"),
      edgeList = element("visible-edges")
    records.replaceChildren()
    edgeList.replaceChildren()
    for (const node of [...view.nodes].sort((a, b) => label(a).localeCompare(label(b)))) {
      const button = make("button", label(node))
      button.addEventListener("click", () => selectNode(node.id))
      records.append(button)
    }
    for (const edge of view.edges) edgeList.append(edgeButton(edge))
    element("diagnostics").hidden = filters.lens !== "diagnostics"
    element("graph").hidden = filters.lens === "diagnostics"
    element("record-list").hidden = filters.lens === "diagnostics"
    if (filters.lens === "diagnostics") diagnostics()
    element("lens-description").textContent = descriptions[filters.lens]
    inspect()
    // Observable ready state is also used by the browser acceptance test.
    document.body.dataset.mapReady = "true"
  }
  function selectNode(id: string) {
    filters.selected = id
    selectedEdge = undefined
    const url = new URL(location.href)
    url.searchParams.set("node", id)
    history.replaceState(null, "", url)
    render()
  }
  cy.on("tap", "node", (event) => selectNode(event.target.id()))
  cy.on("tap", "edge", (event) => {
    selectedEdge = event.target.id()
    inspect()
  })
  element("fit").addEventListener("click", () => cy.fit(undefined, 45))
  element("zoom-in").addEventListener("click", () => cy.zoom(cy.zoom() * 1.25))
  element("zoom-out").addEventListener("click", () => cy.zoom(cy.zoom() / 1.25))
  const selects: [string, keyof Filters, string[]][] = [
    ["module", "module", graph.nodes.map((n) => n.module || "")],
    ["family", "family", graph.nodes.map((n) => n.family)],
    ["status", "status", graph.nodes.map((n) => n.status || "")],
    ["relation", "relation", graph.edges.map((e) => e.relation)],
    ["edge-class", "edgeClass", graph.edges.map((e) => e.edge_class)],
    ["impact-role", "impactRole", graph.edges.map((e) => e.impact_role)],
  ]
  for (const [id, key, values] of selects) {
    const select = element<HTMLSelectElement>(id)
    for (const value of [...new Set(values)].filter(Boolean).sort()) {
      const option = make("option", value)
      option.value = value
      select.append(option)
    }
    select.addEventListener("change", () => {
      Object.assign(filters, { [key]: select.value })
      render()
    })
  }
  element<HTMLSelectElement>("boundary").addEventListener("change", (event) => {
    filters.boundary = (event.target as HTMLSelectElement).value
    render()
  })
  for (const [id, key] of [
    ["global", "global"],
    ["extras", "extras"],
    ["controls", "expandControls"],
  ] as const) {
    element<HTMLInputElement>(id).addEventListener("change", (event) => {
      filters[key] = (event.target as HTMLInputElement).checked
      render()
    })
  }
  element<HTMLSelectElement>("depth").addEventListener("change", (event) => {
    filters.depth = Number((event.target as HTMLSelectElement).value)
    render()
  })
  element("reset-filters").addEventListener("click", () => {
    for (const [id, key] of selects) {
      Object.assign(filters, { [key]: "" })
      element<HTMLSelectElement>(id).value = ""
    }
    filters.boundary = ""
    element<HTMLSelectElement>("boundary").value = ""
    render()
  })
  for (const button of document.querySelectorAll<HTMLButtonElement>("[data-lens]")) {
    button.addEventListener("click", () => {
      filters.lens = button.dataset.lens as Lens
      for (const other of document.querySelectorAll("[data-lens]"))
        other.setAttribute("aria-pressed", String(other === button))
      for (const id of ["global", "depth", "extras", "controls"])
        element<HTMLInputElement>(id).disabled = filters.lens === "impact"
      render()
      cy.resize()
      cy.fit(undefined, 45)
    })
  }
  function search() {
    const query = element<HTMLInputElement>("search").value.toLocaleLowerCase().trim()
    const matches = graph.nodes.filter((n) =>
      query ? `${label(n)} ${n.path || ""}`.toLocaleLowerCase().includes(query) : primaryNode(n),
    )
    const results = element("search-results")
    results.replaceChildren()
    if (!matches.length)
      results.append(make("p", "No literal match. Try the repository’s English term or path."))
    for (const n of matches.slice(0, 30)) {
      const button = make("button", label(n))
      button.append(make("small", n.family))
      button.addEventListener("click", () => selectNode(n.id))
      results.append(button)
    }
    if (matches.length > 30)
      results.append(make("small", `${matches.length} matches. Refine the search to see more.`))
  }
  element("search").addEventListener("input", search)
  if (matchMedia("(max-width: 640px)").matches)
    element("map-controls").querySelector("details")!.open = false
  search()
  render()
}

async function load() {
  try {
    const response = await fetch("map.json", { credentials: "omit" })
    if (!response.ok) throw new Error(`Snapshot unavailable (${response.status})`)
    const text = await response.text()
    if (text.length > 8_000_000) throw new Error("Snapshot exceeds the supported client size")
    start(validateData(JSON.parse(text)))
  } catch (error) {
    element("source-state").textContent = "Map unavailable"
    const panel = element("load-error")
    panel.hidden = false
    panel.append(make("p", error instanceof Error ? error.message : "Invalid map data"))
    const link = make("a", "Read the current repository directly ↗")
    link.href = repositoryURL
    panel.append(link)
  }
}
void load()
