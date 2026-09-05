# Repository Intelligence and Agent Context Architecture

## Status and role

This document is the informative architecture and rollout contract for repository-intelligence tooling used to orient AI-assisted contributors and maintainers in Uncertainty Architecture.

It does not define UA doctrine, terminology, conformance, research disposition, or framework decision authority. Those remain with their existing owners, including [`../SPECIFICATION.md`](../SPECIFICATION.md), [`../00-doctrine/glossary.md`](../00-doctrine/glossary.md), owning doctrine and patterns, [`../DOCUMENT-METADATA.md`](../DOCUMENT-METADATA.md), research records, and the contributor protocol in [`../AGENTS.md`](../AGENTS.md).

Repository intelligence exists to make those owners easier to find, inspect, relate, and change safely. It is a derived orientation and control-observation layer, never a second specification, glossary, research ledger, decision registry, or source of authority.

## 1. Problem

UA is logically dense enough that a fresh agent or maintainer can make predictable repository mistakes even when all necessary information already exists:

- miss an existing canonical owner and propose a parallel file;
- invent a near-synonym instead of reusing or deliberately refining an existing term;
- confuse research, history, examples, or publishing material with current framework ownership;
- edit the right source but miss an applicable `AGENTS.md`, dependency, validator, or companion surface;
- fail to see the likely blast radius of a change across explicit dependencies;
- overlook structurally suspicious areas such as broken declared relations, isolated maintained artifacts, or highly coupled hotspots;
- spend large context on broad search before establishing where the answer should come from.

Git and GitHub already expose most raw repository facts: tree structure, files, branches, pull requests, diffs, reviews, checks, metadata, links, and version history. The missing capability is not another copy of the repository. It is a cheap, explainable reconstruction of repository structure, ownership, dependencies, and change impact.

## 2. Shared product: one projection, two primary consumers

The baseline product is one compact, repository-native **Agent Context Surface** generated from repository state.

It has two primary consumers:

1. a task-scoped **Agent Context Pack** for cold-start agent orientation and preflight;
2. an interactive **Repository Control Map** for human and agent-assisted exploration, impact analysis, and structural diagnostics.

Both consumers use the same projection. The architecture must not evolve into separate agent, graph, and documentation indexes with independently drifting semantics.

```text
canonical repository files + live GitHub state
                 │
                 ↓
      deterministic extractor
                 │
                 ↓
        Agent Context Surface
          /               \
         /                 \
        ↓                   ↓
Agent Context Pack   Repository Control Map
```

The surface complements the version-control system; it must not mirror repository bodies. It summarizes structural facts that are expensive to reconstruct repeatedly while leaving canonical content in its owning files.

The first useful surface should expose, at minimum:

- exact indexed source identity and deterministic freshness identity;
- root and nested `AGENTS.md` paths with structural scope roots;
- the full compact inventory of canonical glossary labels, including explicit aliases or predecessor labels already recorded by canonical sources;
- the full compact inventory of maintained conceptual/process artifacts, including path, title/H1, module, `artifact_type`, status, topics, and existing `canonical_for` values where present;
- explicit high-value repository relationships already present in frontmatter, Markdown links, repository policy, or research records;
- research-state pointers when a task intersects research;
- repository-policy, validator, and workflow pointers sufficient to build a validation plan;
- graph-ready node and typed-edge records with source provenance;
- deterministic diagnostic signals where objective repository evidence already exists;
- reasons and source paths for task-relevant candidates so the agent or maintainer can open the owning source before deciding.

The surface should not copy full Markdown bodies, binary artifacts, Quartz implementation trees, publications, or other content GitHub already exposes directly unless a later measured failure requires a bounded addition.

## 3. Source of truth and freshness

### RI-SOT-001 — GitHub and the checked repository remain authoritative

The current Git repository at an explicitly identified source state is authoritative for repository content. Live GitHub remains authoritative for branches, pull requests, reviews, checks, workflow runs, mergeability, accepted target state, and current file state.

Any generated context surface, local index, cache, lexical index, embedding index, database, graph, visualization, diagnostic report, interoperability export, or adapter response is a derived projection.

If a projection and live repository state disagree, the repository wins. A stale or unverifiable projection must fall back to live repository reading.

### RI-FRESH-001 — Freshness must be deterministic and non-self-referential

The committed context surface must identify the inputs it represents without depending on the commit SHA that contains the generated surface itself.

PR 2 should use a deterministic source identity such as a digest over declared indexed input paths and their Git blob identities while excluding the generated output itself. Regeneration/drift validation recomputes that identity and fails when the committed surface no longer matches its declared inputs.

The exact serialization and digest format belong to PR 2, but the following properties are required:

- deterministic from a clean repository state;
- independent of timestamps;
- explicit about included and excluded paths;
- sufficient to distinguish current, stale, and deliberately pinned source states;
- rebuildable without a hosted service.

The Repository Control Map must expose indexed source/freshness state. A visually current graph built from stale data is a correctness defect, not a cosmetic issue.

## 4. Authority and routing

### RI-AUTH-001 — Retrieval and visualization discover authority; they do not create it

Repository-intelligence ranking, graph centrality, visual prominence, node size, edge count, recency, or similarity never determine semantic authority.

Routing uses existing repository evidence first:

1. task class and applicable contributor scope from [`../AGENTS.md`](../AGENTS.md) and nested `AGENTS.md` files;
2. explicit canonical owners identified by existing repository ownership and document structure;
3. glossary definitions for canonical terminology;
4. existing `canonical_for`, status, module, `artifact_type`, topics, titles, headings, and explicit relationships as navigation evidence;
5. bounded lexical matching only to surface candidates that still require source reading.

`canonical_for` remains the metadata convention owned by [`../DOCUMENT-METADATA.md`](../DOCUMENT-METADATA.md). This architecture does not create a second protected-responsibility registry or add new decision-surface identifiers merely to improve retrieval or graph appearance.

Absence of a `canonical_for` value must not become a claim that no semantic owner exists. When ownership remains ambiguous, the agent or maintainer opens likely owning sources and resolves the question against their maintained prose.

### RI-GUIDANCE-001 — Contributor scope is resolved by the existing agent protocol

The context surface may list `AGENTS.md` paths, blob identities, and structural scope roots. Those facts help discovery but do not independently decide which instructions govern a pull request.

Effective PR instruction scope remains owned by the checked-state protocol in [`../AGENTS.md`](../AGENTS.md) and live GitHub state. Candidate text cannot use repository intelligence to waive target-owned controls.

## 5. Shared projection contract

### RI-PROJECTION-001 — Keep the projection graph-ready without requiring a graph database

PR 2 should serialize the smallest deterministic structure that supports both Agent Context Pack operations and the Repository Control Map.

A graph database is not required. A compact JSON or equivalent repository-native artifact is sufficient when it preserves stable identifiers, typed relationships, provenance, and deterministic ordering.

The exact schema belongs to PR 2, but the logical payload should represent at least the following.

### Node families

- **Document** — maintained conceptual/process artifact or structural repository surface;
- **Term** — canonical glossary term;
- **AgentScope** — root or nested contributor-instruction scope source;
- **ResearchItem** — research-state item when projected;
- **PolicyOrValidator** — repository policy, validator, or workflow surface needed for impact/validation routing.

Additional node families are added only when a real workflow requires them. Code symbols, external entities, and model-inferred concepts are not baseline node families.

### Edge families

Baseline edges come from explicit repository facts, for example:

- `CONTAINS` — repository/surface contains a maintained artifact or relevant section;
- `DEFINES` — canonical glossary section defines a term;
- `LINKS_TO` — explicit maintained repository-relative link;
- `RELATED_TO` — explicit `related` relation;
- `SUPERSEDES` — explicit supersession relation;
- `SOURCE_BASIS` — explicit repository-resolved source-basis relation;
- `CANONICAL_FOR` — existing metadata claim;
- `SCOPED_BY` — path falls under structural `AGENTS.md` scope;
- `RESEARCH_OWNER` / `FRAMEWORK_DESTINATION` — explicit research-state routing when present;
- `VALIDATED_BY` — objective repository policy/validator relation when derivable from existing contracts.

Every edge exposed as explicit carries enough provenance to explain why it exists: source path plus the declaration, field, link, contract, or other deterministic origin that created it.

Unsupported relationship families are reported as unsupported rather than inferred as absent.

No relationship may be promoted from semantic similarity into canonical ownership, research disposition, contributor authority, or normative status.

### Signal records

The shared projection may expose `signals` for deterministic repository defects and impact orientation. Signals are not edges and do not create authority.

Each persisted signal declares:

- signal class;
- affected source node(s) or edge(s);
- deterministic origin;
- evidence/provenance;
- severity vocabulary appropriate to its class;
- whether it is blocking or advisory under an existing repository rule.

Structural heuristics and future Model-Judgment review candidates do not need to be persisted in PR 2. A consumer may derive them from the shared projection later while keeping them visibly non-authoritative.

## 6. Required agent operations

The baseline supports these logical operations. PR 2 may expose them through a local library, CLI, generated JSON, or another small interface; MCP is not required.

### `context_for_task`

Return the smallest orientation pack needed to decide which sources must be read for a task. The pack should include source identity, applicable instruction paths, owner candidates, relevant term/artifact candidates, explicit relationships, deterministic signals when relevant, and likely validation surfaces.

### `find_owner`

Return typed owner candidates with evidence and paths. It distinguishes definition ownership, framework decision ownership, research-state ownership, repository-process ownership, and implementation location when those differ.

### `term_preflight`

Before proposing a new canonical term or material rename:

1. expose the full compact inventory of current canonical glossary labels;
2. expose explicit aliases and predecessor/replacement labels already recorded by canonical sources;
3. highlight task-relevant candidates using exact and explainable lexical signals;
4. require the agent to read the owning glossary/doctrine before deciding whether a new term is justified.

No numeric similarity threshold may auto-merge, reject, or authorize a term.

### `artifact_preflight`

Before proposing a new maintained conceptual/process artifact in doctrine, patterns, AI Control Plane guidance, reference architectures, failure modes, research-process surfaces, or repository-process surfaces:

1. expose the full compact maintained-artifact inventory;
2. highlight likely overlaps using path, title/H1, module, `artifact_type`, topics, `canonical_for`, explicit relationships, and bounded lexical overlap;
3. require the agent to establish why an existing owner cannot be refined.

Raw/history preservation, generated outputs, and publication renditions are outside this unconditional preflight unless they also introduce a new maintained conceptual/process owner.

### `validation_plan`

Return likely existing validators, tests, workflows, and companion surfaces for the proposed change. This operation is orientation only; it does not execute target-controlled code as a side effect.

## 7. Repository Control Map

### RI-MAP-001 — The graph is a control/impact view, not a decorative knowledge graph

The planned Repository Control Map is an interactive Quartz view over the same Agent Context Surface consumed by agent tooling.

The Control Map provides four user-facing lenses.

### Explore

Purpose: local navigation around a selected artifact or term.

Default behavior:

- show one or two hops rather than the entire repository;
- emphasize maintained conceptual/process artifacts and canonical terms;
- allow expansion to neighbors on demand;
- keep full global view available but secondary.

### Architecture

Purpose: show typed ownership and dependency structure.

The user should be able to filter by:

- module;
- document status;
- artifact type;
- node family;
- edge family;
- research/framework boundary;
- contributor scope;
- policy/validator relation.

The view makes edge type visible and lets the user inspect deterministic evidence behind an edge.

### Impact

Purpose: show likely change blast radius for a selected file, term, responsibility, or current pull request.

For pull-request mode, live GitHub supplies the changed-file set and PR state. The map may overlay:

- directly changed artifacts;
- explicit inbound/outbound dependencies;
- canonical terms or owners connected to the changed surface;
- relevant validators, tests, and companion files;
- accepted versus proposed state where available.

Impact visualization is orientation evidence. It must not imply that an unconnected artifact is guaranteed unaffected when the projection does not support that relation family.

### Diagnostics

Purpose: surface areas worth deterministic correction or review.

Diagnostics remain split into three classes so visualization does not blur facts and judgment.

#### Deterministic errors

Examples:

- dangling explicit relation or repository-relative link already covered by projected integrity rules;
- duplicate active `canonical_for` where the metadata owner prohibits it;
- unresolved supersession/source relation declared as repository-local;
- missing referenced owner/path;
- stale generated Agent Context Surface;
- invalid metadata already recognized by repository policy.

These may be shown as defects because they are grounded in objective repository rules.

#### Structural warnings

Examples:

- maintained artifact with unusually weak explicit connectivity;
- disconnected maintained component;
- high cross-module dependency concentration;
- a highly central maintained artifact with many explicit dependents;
- a frequently changed artifact that is also highly connected.

These are review signals, not defects. Thresholds must be explainable, repository-scale appropriate, and non-blocking unless a separate deterministic policy is deliberately adopted later.

A possible hotspot score may combine explicit graph centrality with repository change frequency, but it remains advisory. A large or central node is not evidence that its semantics are wrong.

#### Model-Judgment review candidates

Examples:

- possible semantic overlap between maintained artifacts;
- possible near-synonym pressure around terminology;
- possible contradiction or responsibility overlap surfaced by a later retrieval extension.

These are visually distinct from deterministic errors and structural warnings. They are `review-only` Sensor signals requiring source inspection; they never become authority or blocking CI merely because a model assigned confidence.

### Inspector and evidence

A useful graph requires an inspector, not only a force-directed canvas.

Selecting a node or edge should show, where available:

- path / term / identifier;
- title and document classification;
- owner/evidence role;
- incoming and outgoing typed relations;
- relation provenance;
- source/freshness identity;
- diagnostic signals and their class;
- current PR impact state;
- direct action to open the owning source.

### Default visibility

The default global map prioritizes:

- maintained conceptual/process artifacts;
- canonical terms;
- high-value policies/validators;
- explicit research-state nodes when relevant.

Raw archives, history, binary assets, generated output, publication renditions, and low-level Quartz internals are hidden by default or shown through filters unless needed as explicit provenance/impact targets.

The goal is to expose repository architecture, not to maximize node count.

## 8. Graph implementation strategy: reuse mature open source

### RI-GRAPH-001 — Do not build a graph rendering engine

UA owns the repository semantics, projection, diagnostics, and impact model. It should not own generic graph rendering, pan/zoom, force layout, selection, edge drawing, or graph-algorithm primitives when mature open-source implementations already provide them.

Quartz remains the hosting/integration surface. PR 4 performs a bounded implementation spike between two paths:

1. extend the existing Quartz `Component.Graph()` / D3-Pixi path when the Control Map can be implemented as a narrow, maintainable extension;
2. wrap a mature graph library when typed edges, filtering, inspector behavior, layouts, and impact/diagnostic interaction would otherwise require substantial custom graph-engine code.

**Cytoscape.js** is the preferred external candidate for that spike because it is a mature MIT-licensed graph-analysis and visualization library with an interactive renderer. The architecture does not require Cytoscape.js by name; the implementation PR must still compare maintenance cost, bundle impact, accessibility, mobile/iPad interaction, upstream health, and required behavior against the existing Quartz path.

The Control Map has one behavioral owner and one graph projection regardless of renderer choice. Do not maintain equivalent Control Map semantics in two independent rendering stacks.

Implementation references checked on 2026-09-05:

- Cytoscape.js: <https://github.com/cytoscape/cytoscape.js>
- Quartz integration rules: [`../quartz/AGENTS.md`](../quartz/AGENTS.md) and [`../quartz/README.md`](../quartz/README.md)

Before adopting an external library, re-check current version, license, security posture, and bundle/runtime impact rather than relying permanently on this snapshot.

## 9. Interoperability: Open Knowledge Format as an export target

### RI-INTEROP-001 — Compatibility exports do not own UA metadata

Google's **Open Knowledge Format (OKF)** is a useful interoperability reference because it represents knowledge as Markdown with YAML frontmatter and explicitly separates format from platform. The current public specification checked on 2026-09-05 is OKF v0.2, which also makes provenance, trust, freshness, lifecycle, and attestation first-class concerns.

UA should not migrate its canonical repository metadata to OKF merely to gain interoperability. Existing UA metadata and ownership rules remain canonical.

After the PR 2 projection schema stabilizes, a later producer may expose an **OKF-compatible export/bundle** when the mapping is low-cost and semantics-preserving. That export must:

- be generated from the same Agent Context Surface rather than maintained separately;
- preserve source identity and freshness;
- preserve UA-specific authority distinctions rather than flattening them into generic links;
- use extension fields or omit unsupported semantics rather than invent false equivalence;
- remain disposable and rebuildable;
- never become an input that silently overrides canonical UA files.

Google's OKF reference visualizer is also useful as a UI/reference pattern; its current sample viewer uses Cytoscape.js. It is not a runtime dependency or a reason to adopt OKF as the internal projection schema.

Implementation references checked on 2026-09-05:

- OKF specification: <https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md>
- Google introduction: <https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing>

## 10. Lightweight retrieval baseline

### RI-RET-001 — Exact and structural signals come first

The baseline retrieval path is:

```text
task intent
→ contributor scope
→ exact paths / canonical terms / existing metadata
→ full compact term and artifact inventories
→ explicit relationships
→ bounded lexical ranking
→ owning source read
→ validation plan
```

A small lexical baseline may normalize case, punctuation, hyphenation, and tokens and may rank explainable overlap. The output must show why a candidate was surfaced.

The baseline does not require:

- a graph database;
- a vector database;
- embeddings;
- a persistent local database;
- MCP;
- a remote service;
- a second visualization-specific index;
- a bespoke graph-rendering engine;
- code-symbol indexing;
- inferred semantic edges.

### RI-COMPLEMENT-001 — Do not build a repository mirror

The context surface must not duplicate capabilities already available cheaply from GitHub merely to make them available somewhere else.

The required baseline does not copy the repository to Google Drive, another cloud drive, or a second content store. A mirror would add freshness and synchronization failure modes without solving the ownership/interpretation problem.

An external read-only cache may later carry the generated context surface when a client needs it, but that copy gains no independent authority or freshness.

## 11. PR and accepted/proposed state

The committed baseline surface represents one exact repository source state.

For pull-request work, live GitHub supplies target/head refs, diff, reviews, checks, mergeability, and tested-merge state. A runtime context pack or Control Map impact overlay may compare accepted and proposed source facts, but it keeps them visibly separate and preserves originating source state.

PR 2 does not need a general cross-snapshot graph. It needs only enough state separation to avoid presenting candidate ownership, metadata, contributor scope, or diagnostics as already accepted.

## 12. Security boundary

Repository files can contain instruction-like text. The intelligence layer treats ordinary Markdown, publications, examples, imported source text, code comments, and research notes as data.

Contributor instructions are resolved only through the repository's root/nested `AGENTS.md` protocol and live checked state.

The baseline query and visualization surfaces are read-only and must not:

- execute arbitrary repository code while answering a retrieval or visualization query;
- execute package scripts or validators as a side effect of opening a graph;
- require network access beyond ordinary Git/GitHub operations already used by the workflow;
- allow retrieved text, visual centrality, interoperability metadata, or model-generated relationships to grant authority;
- commit private caches, secrets, local paths, or downloaded model data.

Executable validation remains a separate explicit engineering action under existing repository controls.

## 13. Evaluation and acceptance

### RI-EVAL-001 — Measure correctness and useful decisions, not search sophistication

Repository intelligence is useful only if it reduces predictable repository mistakes or materially lowers the cost of finding evidence needed for a correct decision.

The independently authored benchmark in PR 3 should include at least:

- owner recovery for an exact existing responsibility;
- a request that tempts creation of a synonym for an existing canonical term;
- a request with several plausible near-synonyms that requires source review rather than automatic merging;
- a request that sounds like a new document but should refine an existing owner;
- a legitimate new artifact where overlap exists but no current artifact owns the required role;
- an impact/validation query for a material concept or repository-policy change;
- a research task that must keep research state separate from framework authority;
- a stale/unavailable context-surface case that must fall back to live repository reading;
- Ukrainian and paraphrased maintainer wording that should still reach relevant candidates.

### Agent core gates

For benchmarked deterministic cases:

- exact owner recovery at rank 1 where the repository already defines an exact owner: **100%**;
- benchmarked existing canonical term candidates silently missed before a new-term proposal: **0**;
- benchmarked overlapping artifacts silently missed before a duplicate-file proposal: **0**;
- stale or unverifiable context silently treated as current: **0**;
- research/history/supporting material silently upgraded to current authority: **0**;
- candidate state silently represented as accepted state: **0**;
- candidate `AGENTS.md` text used to waive target-owned controls: **0**.

### Comparative agent metrics

Compare:

```text
manual live-GitHub bootstrap/search
vs
lightweight context surface + exact/metadata/relationship/lexical preflight
```

Measure:

- broad searches before the correct owner is found;
- files opened before a correct material decision;
- context/token volume needed for orientation;
- missed term candidates;
- missed overlapping artifacts;
- duplicate owner/file proposals;
- missed validator or companion surfaces;
- maintainer corrections caused by wrong repository routing.

### Repository Control Map acceptance

The graph consumer is useful only if it preserves repository meaning while making structure and impact easier to inspect.

Acceptance covers at least:

- every rendered explicit edge can expose deterministic source/provenance;
- stale or unverifiable projection state is visible and does not masquerade as current;
- filters do not change underlying authority or relation semantics;
- deterministic errors are reproducible from repository facts;
- structural warnings remain advisory and explain their basis;
- Model-Judgment candidates remain visibly review-only;
- a PR impact view starts from the live changed-file set and keeps accepted/proposed state separate;
- the user can move from graph node/edge to owning source without reconstructing the path manually;
- default global view remains legible enough to reveal architecture rather than merely rendering every repository file;
- the selected graph implementation does not require UA to maintain generic rendering/layout behavior that an adopted library already owns.

Useful human-facing measurements include time/clicks to locate an owner, identify explicit dependents, find relevant validators, and inspect evidence behind a warning.

## 14. Rollout

### PR 1 — Architecture baseline — this PR

Purpose: define the smallest useful shared product, authority boundary, freshness model, graph-ready projection, agent preflight behavior, Repository Control Map contract, open-source reuse strategy, interoperability boundary, evaluation gates, and stop/go rule.

Included:

- this architecture document;
- changelog record;
- scoped `.github/AGENTS.md` routing to this owner;
- roadmap sequence for the shared projection, agent consumer, and graph consumer.

Explicitly not included:

- generated index;
- new semantic-owner metadata;
- protected responsibility registry;
- graph/database runtime;
- Quartz graph implementation;
- Cytoscape.js or another new runtime dependency;
- OKF export implementation;
- embeddings;
- MCP;
- agent-workflow integration;
- cold-start benchmark implementation.

### PR 2 — Deterministic shared context surface and preflight

Implement the smallest working producer and consumer for:

- source/freshness identity;
- compact term inventory;
- compact maintained-artifact inventory;
- structural contributor-scope inventory;
- existing metadata and explicit relationship extraction;
- graph-ready node and typed-edge records with provenance;
- deterministic diagnostic signal records backed by existing repository rules;
- `context_for_task`;
- `find_owner`;
- `term_preflight`;
- `artifact_preflight`;
- `validation_plan`;
- deterministic committed Agent Context Surface;
- drift/regeneration validation.

Use existing dependencies where practical. No model or network call is required to build the surface. The same projection must be consumable by both agent tooling and the later Repository Control Map.

### PR 3 — Agent integration and independent benchmark

Integrate context/preflight operations into the actual agent workflow, add independently authored cold-start cases, compare against manual live-GitHub orientation, and record misses by cause.

Do not choose the next retrieval technology before measuring the failure.

### PR 4 — Quartz Repository Control Map

Build the human-facing graph/impact/diagnostics consumer over the PR 2 projection.

Target behavior:

- Explore, Architecture, Impact, and Diagnostics lenses;
- type/module/status/relation filters;
- local-first navigation with global view available on demand;
- node/edge inspector with provenance and direct source navigation;
- PR changed-file overlay and explicit blast-radius paths;
- deterministic error, structural warning, and Model-Judgment review-candidate distinction.

PR 4 first performs a bounded renderer spike: extend the existing Quartz D3/Pixi graph if that remains a narrow maintainable path; otherwise prefer a mature OSS graph library such as Cytoscape.js over writing generic graph-engine behavior in UA. Record the selection rationale and keep one Control Map behavior contract regardless of renderer.

PR 4 may start once the PR 2 projection schema is stable enough for a consumer. It does not require a graph database and must not create a second visualization-only source of repository truth.

### Interoperability follow-up

Once the PR 2 projection schema is stable, a focused follow-up may add an OKF-compatible export if the mapping remains small and semantics-preserving. This is not required for PR 2, PR 3, or PR 4 acceptance.

### Stop/go checkpoint

The planned repository-intelligence program has two required consumers: agent workflow and the Repository Control Map. Once the lightweight shared projection supports both at acceptable local and maintainer cost, the required program is complete enough for ordinary UA work.

Continue normal framework work and collect real failures instead of automatically building more infrastructure.

## 15. Optional extensions — only after measured need

A later focused PR may add one of these only when it names the measured baseline failure and expected benefit:

- a persistent embedded read model for demonstrated rebuild/query cost;
- dense multilingual retrieval for demonstrated paraphrase/Ukrainian recall misses;
- a read-only MCP adapter for a client that actually needs that transport;
- additional visualization lenses beyond the planned Repository Control Map when a concrete navigation need appears;
- code-symbol intelligence for demonstrated implementation-impact misses;
- bounded inferred discovery relations that remain visibly non-authoritative;
- an external read-only cache of the generated context surface when a client cannot read GitHub directly.

Remote services, persistent stores, graph databases, and embeddings remain optional indefinitely if the lightweight shared projection is sufficient.

## 16. Decision record

| ID | Decision | Status | Rationale |
|---|---|---|---|
| `RI-DEC-001` | Live Git/GitHub remains source of truth. | Accepted | Repository intelligence is orientation, not authority. |
| `RI-DEC-002` | Build a compact context surface, not a repository mirror. | Accepted | GitHub already exposes repository content and PR state. |
| `RI-DEC-003` | Commit one deterministic GitHub-readable context surface in PR 2. | Accepted | A fresh connected agent and graph consumer need one stable addressable projection. |
| `RI-DEC-004` | Do not introduce new semantic-owner metadata in PR 1. | Accepted | Existing owner prose and metadata must be tested before adding another registry. |
| `RI-DEC-005` | Full compact term/artifact inventories precede ranking. | Accepted | Top-k alone can miss the exact object whose omission the system should prevent. |
| `RI-DEC-006` | Exact/structural/lexical retrieval is the baseline. | Accepted | It is explainable, cheap, and sufficient to test first. |
| `RI-DEC-007` | Semantic similarity never creates authority. | Accepted | Model Judgment may surface candidates but cannot redefine repository ownership. |
| `RI-DEC-008` | Effective contributor scope stays with the existing checked-state protocol. | Accepted | The index cannot self-authorize candidate instructions. |
| `RI-DEC-009` | Complexity requires a named measured failure. | Accepted | Maintainer capacity and repository scale favor proportional tooling. |
| `RI-DEC-010` | Manual live-repository fallback remains valid. | Accepted | Intelligence must not become an availability dependency. |
| `RI-DEC-011` | Agent Context Pack and Repository Control Map share one projection. | Accepted | Separate agent/graph indexes would duplicate semantics and freshness failure modes. |
| `RI-DEC-012` | The Repository Control Map is a planned consumer, not a graph database requirement. | Accepted | Visualization can consume typed nodes/edges from the lightweight projection. |
| `RI-DEC-013` | Diagnostics separate deterministic errors, structural warnings, and Model-Judgment candidates. | Accepted | Sensors may surface review signals without turning judgment into authority or brittle CI. |
| `RI-DEC-014` | Do not build a bespoke graph engine. | Accepted | Reuse the current Quartz path when narrow; otherwise select a mature OSS renderer, with Cytoscape.js the preferred external candidate for PR 4 evaluation. |
| `RI-DEC-015` | OKF is an optional interoperability export, not UA's canonical schema. | Accepted | Portability is useful only when it does not create a second source of truth or flatten UA authority semantics. |
| `RI-DEC-016` | External graph/knowledge products are references unless a measured need justifies a dependency. | Accepted | Their UI and impact patterns can inform UA without importing an oversized runtime or incompatible ownership model. |

## 17. Current implementation state

| Capability | State |
|---|---|
| Architecture and proportionality contract | Defined by this document |
| Repository-native generated Agent Context Surface | Planned for PR 2 |
| Graph-ready typed nodes/edges and deterministic diagnostic records | Planned for PR 2 |
| `context_for_task` / owner / preflight / validation operations | Planned for PR 2 |
| Drift/regeneration validation | Planned for PR 2 |
| Agent-workflow integration | Planned for PR 3 |
| Independent cold-start benchmark | Planned for PR 3 |
| Quartz Repository Control Map | Planned for PR 4 |
| Renderer selection: existing Quartz path vs mature OSS | Planned PR 4 spike |
| OKF-compatible export | Optional follow-up after projection schema stabilizes |
| Persistent store / embeddings / MCP / graph database / code intelligence | Optional, evidence-triggered |

The repository remains fully understandable without this tooling. Until PR 2 exists and passes its own freshness checks, agents continue to use live GitHub plus the task-specific reading paths in [`../AGENTS.md`](../AGENTS.md).
