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

## 2. One logical projection, multiple materializations

### RI-PROJECTION-001 — One semantic projection does not mean one physical file

The baseline product is one deterministic **Repository Intelligence Projection** over one explicit repository source state.

That logical projection has different consumers with different context budgets. It may therefore be materialized into more than one deterministic view, provided every view:

- derives from the same producer and source state;
- preserves the same node/relationship semantics;
- carries compatible schema and source-identity metadata;
- remains rebuildable from canonical repository sources;
- does not acquire authority merely because it is committed or rendered.

The two required materializations are:

1. a compact **Agent Context Surface** for connector-friendly cold-start orientation and preflight;
2. a fuller **Graph View** for the Quartz **Repository Control Map**.

A task-scoped **Agent Context Pack** is assembled from the compact Agent Context Surface plus live GitHub facts when the task requires them.

```text
canonical repository snapshot
          │
          ↓
 deterministic extractor
          │
          ↓
Repository Intelligence Projection
      /                    \
     /                      \
    ↓                        ↓
compact Agent           full Graph
Context Surface          View
    │                        │
    ↓                        ↓
Agent Context Pack      Repository Control Map
    ↑                        ↑
    └──── live GitHub runtime overlay ────┘
```

The graph consumer must not force ordinary agent orientation to load the complete graph-edge payload. The agent consumer must not force the graph to throw away provenance or structure needed for inspection.

### RI-MATERIALIZE-001 — Consumer-specific materialization is allowed; semantic forks are not

Materializations may omit fields or edge classes that are unnecessary for their consumer if the omission is deterministic, documented, and does not change the underlying meaning.

For example:

- the compact Agent Context Surface may keep complete term/artifact inventories and high-value ownership/control relationships while omitting bulk navigation edges;
- the full Graph View may include all explicit graph relationships required by Explore/Architecture/Impact/Diagnostics;
- both views must preserve the same identifiers and source identity for objects they share.

Do not maintain independent agent and graph schemas that must be manually reconciled.

## 3. Static repository projection versus live GitHub overlay

### RI-STATE-001 — Deterministic repository state and volatile GitHub state are separate inputs

The deterministic projection is built from one explicit repository snapshot. Live GitHub state is not serialized into the committed deterministic materialization.

```text
repository snapshot
      ↓
deterministic projection

live PR / review / check / mergeability state
      ↓
runtime overlay
```

The repository snapshot owns stable project facts such as files, metadata, glossary terms, explicit links, research-register records, contributor-scope paths, and repository policy definitions.

Live GitHub owns volatile facts such as:

- target/head refs;
- changed-file set;
- PR title/body and Draft state;
- reviews and unresolved threads;
- check/workflow state;
- mergeability and tested-merge state.

A runtime Agent Context Pack or Control Map may combine both, but it must keep accepted repository state, candidate repository state, and live PR state visibly distinct.

If live GitHub is unavailable, the deterministic projection remains usable. The missing overlay must be reported as unavailable or stale rather than silently treated as empty.

## 4. Source of truth and freshness

### RI-SOT-001 — Git/GitHub and owning sources remain authoritative

The checked Git repository at an explicitly identified source state is authoritative for repository content. Live GitHub remains authoritative for branches, pull requests, reviews, checks, workflow runs, mergeability, tested-merge state, and current file state.

Any generated context surface, graph view, local index, cache, lexical index, embedding index, database, visualization, diagnostic report, interoperability export, or adapter response is a derived projection.

If a projection and live repository state disagree, the repository wins. A stale or unverifiable projection must fall back to live repository reading.

### RI-FRESH-001 — Freshness must be deterministic and non-self-referential

The producer must identify the repository inputs represented by a generated view without depending on the commit SHA that contains the generated view itself.

PR 2 should use a deterministic source identity such as a digest over declared indexed input paths and their Git blob identities while excluding generated outputs themselves.

Required properties:

- deterministic from a clean repository state;
- independent of timestamps;
- explicit about included and excluded paths;
- sufficient to distinguish current, stale, and deliberately pinned source states;
- rebuildable without a hosted service;
- shared across the compact and graph materializations for the same source state.

A visually current graph or agent surface built from stale data is a correctness defect, not a cosmetic issue.

## 5. Generated-output placement and repository-policy coupling

### RI-PLACEMENT-001 — Routine regeneration must not reclassify ordinary content work as repository-policy work

Repository-intelligence implementation code, tests, policy, and workflow integration may live under `.github/` when `.github/` is their correct owner.

A routinely regenerated **read materialization** must not live under a path whose mere modification forces ordinary content-only pull requests into the repository-policy change class.

Therefore the committed compact Agent Context Surface must either:

- use a neutral generated-data location outside the protected repository-policy surface; or
- remain an uncommitted/short-lived build artifact when no committed connector-readable view is required.

PR 2 owns the exact path choice after checking current repository placement rules. If it introduces a new generated-data location, that location must have one narrow purpose and must not become a second content hierarchy.

The full Graph View does not need to be committed merely because the compact Agent Context Surface is committed. It may be produced during Quartz build, CI, or another deterministic local generation step.

Generated output never becomes an authority source for the next generation cycle.

## 6. Authority and routing

### RI-AUTH-001 — Retrieval and visualization discover authority; they do not create it

Repository-intelligence ranking, graph centrality, visual prominence, node size, edge count, recency, similarity, or model confidence never determine semantic authority.

Routing uses existing repository evidence first:

1. task class and applicable contributor scope from [`../AGENTS.md`](../AGENTS.md) and nested `AGENTS.md` files;
2. explicit canonical owners identified by existing repository ownership and document structure;
3. glossary definitions for canonical terminology;
4. existing `canonical_for`, status, module, `artifact_type`, topics, titles, headings, and explicit relationships as navigation evidence;
5. bounded lexical matching only to surface candidates that still require source reading.

`canonical_for` remains the metadata convention owned by [`../DOCUMENT-METADATA.md`](../DOCUMENT-METADATA.md). Repository intelligence does not create a second protected-responsibility registry.

Absence of a `canonical_for` value must not become a claim that no semantic owner exists. When ownership remains ambiguous, the agent or maintainer opens likely owning sources and resolves the question against their maintained prose.

### RI-GUIDANCE-001 — Contributor scope is resolved by the existing agent protocol

The projection may list `AGENTS.md` paths, blob identities, and structural scope roots. Those facts help discovery but do not independently decide which instructions govern a pull request.

Effective PR instruction scope remains owned by the checked-state protocol in [`../AGENTS.md`](../AGENTS.md) and live GitHub state. Candidate text cannot use repository intelligence to waive target-owned controls.

## 7. Projection model

### Node families

The baseline logical projection should represent at least:

- **Document** — maintained conceptual/process artifact or structural repository surface;
- **Term** — canonical glossary term;
- **Responsibility** — a **derived projection node** for an existing `canonical_for` identifier;
- **AgentScope** — root or nested contributor-instruction scope source;
- **ResearchItem** — research-state item when projected;
- **PolicyOrValidator** — repository policy, validator, or workflow surface needed for impact/validation routing.

`Responsibility` nodes do not create a new ownership registry. They materialize identifiers already declared by the existing metadata owner so a `CANONICAL_FOR` relationship has an explicit target. If the source metadata claim disappears, the derived node/edge disappears.

Additional node families should be added only when a real workflow requires them. Code symbols, external entities, and model-inferred concepts are not baseline node families.

### Edge classes

The graph should distinguish edge classes because not all explicit links carry the same engineering meaning.

#### Semantic / evolution evidence

Examples:

- `DEFINES` — canonical glossary section defines a term;
- `CANONICAL_FOR` — document declares an existing `canonical_for` responsibility;
- `RELATED_TO` — explicit high-value relation from maintained metadata;
- `SUPERSEDES` / `SUPERSEDED_BY` — explicit evolution relation;
- `SOURCE_BASIS` — explicit repository-resolved source basis;
- `RESEARCH_OWNER` / `FRAMEWORK_DESTINATION` — explicit research-state routing.

These edges are evidence about meaning, provenance, lifecycle, or ownership discovery. They still do not create authority independently of the owning source.

#### Repository / control structure

Examples:

- `CONTAINS` — structural containment used for routing;
- `SCOPED_BY` — path falls under structural `AGENTS.md` scope;
- `VALIDATED_BY` — objective repository policy/validator relation derivable from existing contracts.

These edges help answer impact and validation questions.

#### Navigation

- `LINKS_TO` — explicit maintained repository-relative Markdown link.

Navigation edges are useful for Explore and backlinks, but they are noisy. They should not dominate the default Architecture or Impact views and do not imply semantic dependence merely because one document links to another.

### Provenance

Every explicit edge exposed by the full Graph View must carry enough provenance to explain why it exists: source path plus the declaration, field, link, contract, or other deterministic origin that created it.

Unsupported relationship families must be reported as unsupported rather than inferred as absent.

No relationship may be promoted from semantic similarity into canonical ownership, research disposition, contributor authority, or normative status.

### Signal records

The deterministic projection may expose signals for repository defects and impact orientation.

Each persisted signal declares:

- signal class;
- affected source node(s) or edge(s);
- deterministic origin;
- evidence/provenance;
- severity vocabulary appropriate to its class;
- whether it is blocking or advisory under an existing repository rule.

Structural heuristics and future Model-Judgment review candidates do not need to be persisted in PR 2. A consumer may derive them later while keeping them visibly non-authoritative.

## 8. Required agent operations

The baseline supports these logical operations. PR 2 may expose them through a local library, CLI, generated JSON, or another small interface; MCP is not required.

### `context_for_task`

Return the smallest orientation pack needed to decide which sources must be read for a task. The pack should include source identity, applicable instruction paths, owner candidates, relevant term/artifact candidates, explicit high-value relationships, deterministic signals when relevant, and likely validation surfaces.

Routine use must not require loading the full Graph View.

### `find_owner`

Return typed owner candidates with evidence and paths. It must distinguish definition ownership, framework decision ownership, research-state ownership, repository-process ownership, implementation location, and machine-readable `canonical_for` evidence when those differ.

### `term_preflight`

Before proposing a new canonical term or material rename:

1. expose the full compact inventory of current canonical glossary labels;
2. expose explicit aliases and predecessor/replacement labels already recorded by canonical sources;
3. highlight task-relevant candidates using exact and explainable lexical signals;
4. require the agent to read the owning glossary/doctrine before deciding whether a new term is justified.

No numeric similarity threshold may auto-merge, reject, or authorize a term.

### `artifact_preflight`

Before proposing a new maintained conceptual/process artifact:

1. expose the full compact maintained-artifact inventory;
2. highlight likely overlaps using path, title/H1, module, `artifact_type`, topics, `canonical_for`, explicit relationships, and bounded lexical overlap;
3. require the agent to establish why an existing owner cannot be refined.

Raw/history preservation, generated outputs, and publication renditions are outside this unconditional preflight unless they also introduce a new maintained conceptual/process owner.

### `validation_plan`

Return likely existing validators, tests, workflows, and companion surfaces for the proposed change. This operation is orientation only; it does not execute target-controlled code as a side effect.

## 9. Lightweight retrieval baseline

### RI-RET-001 — Exact and structural signals come first

The baseline retrieval path is:

```text
task intent
→ contributor scope
→ exact paths / canonical terms / existing metadata
→ full compact term and artifact inventories
→ explicit high-value relationships
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
- a repository mirror;
- a bespoke graph-rendering engine;
- code-symbol indexing;
- inferred semantic edges.

### RI-COMPLEMENT-001 — Do not build a repository mirror

The projection must not duplicate capabilities already available cheaply from GitHub merely to make them available somewhere else.

The required baseline does not copy the repository to Google Drive, another cloud drive, or a second content store. An external read-only cache may later carry a generated materialization when a client needs it, but that copy gains no independent authority or freshness.

## 10. Repository Control Map

### RI-MAP-001 — The graph is a control/impact view, not a decorative knowledge graph

The planned Repository Control Map is an interactive Quartz consumer over the full Graph View plus an optional live GitHub overlay.

It provides four lenses.

### Explore

Purpose: local navigation around a selected artifact or term.

Default behavior:

- show one or two hops rather than the entire repository;
- allow `LINKS_TO` and backlinks to help navigation;
- emphasize maintained conceptual/process artifacts and canonical terms;
- keep full global view available but secondary.

### Architecture

Purpose: show typed ownership, evolution, research, contributor-scope, and validation structure.

Default behavior:

- prioritize semantic/evolution and repository/control edges;
- hide or de-emphasize bulk `LINKS_TO` navigation edges unless requested;
- allow filters by module, status, artifact type, node family, edge family, research/framework boundary, contributor scope, and validator relation;
- make edge provenance inspectable.

### Impact

Purpose: show likely change blast radius for a selected file, term, responsibility, or current pull request.

For pull-request mode, live GitHub supplies the changed-file set and PR state. The map may overlay:

- directly changed artifacts;
- explicit inbound/outbound high-value relationships;
- canonical terms or responsibility claims connected to the changed surface;
- relevant validators, tests, and companion files;
- accepted versus proposed state where available.

Impact visualization is orientation evidence. It must not imply that an unconnected artifact is guaranteed unaffected when the projection does not support that relation family.

### Diagnostics

Purpose: surface areas worth deterministic correction or review.

Diagnostics remain split into three classes.

#### Deterministic errors

Examples:

- dangling explicit relation or repository-relative link already covered by projected integrity rules;
- duplicate active `canonical_for` where the metadata owner prohibits it;
- unresolved supersession/source relation declared as repository-local;
- missing referenced owner/path;
- stale generated materialization;
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

A hotspot score may combine explicit graph centrality with repository change frequency, but it remains advisory.

#### Model-Judgment review candidates

Examples:

- possible semantic overlap between maintained artifacts;
- possible near-synonym pressure around terminology;
- possible contradiction or responsibility overlap surfaced by a later retrieval extension.

These are `review-only` Sensor signals requiring source inspection. They never become authority or blocking CI merely because a model assigned confidence.

### Inspector and evidence

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
- derived responsibility nodes;
- high-value policies/validators;
- explicit research-state nodes when relevant.

Raw archives, history, binary assets, generated output, publication renditions, low-level Quartz internals, and bulk navigation edges are hidden by default or shown through filters unless needed for provenance or impact.

## 11. Live-overlay degraded mode and browser security

### RI-LIVE-001 — The map remains useful without live GitHub

The accepted-state Repository Control Map must remain useful when the live GitHub overlay is unavailable, rate-limited, or intentionally disabled.

The UI must distinguish:

- deterministic projection state;
- live overlay state;
- stale or unavailable overlay state.

Absence of an overlay must not be rendered as evidence that no PR impact, review, or check state exists.

### RI-CLIENT-001 — No repository credential in the browser bundle

The static Quartz client must not embed a GitHub token, repository secret, or equivalent credential merely to power the live overlay.

If live PR data requires authenticated access in a future deployment, that access belongs behind an explicitly designed boundary rather than in client-delivered JavaScript.

## 12. Graph implementation strategy: reuse mature open source

### RI-GRAPH-001 — Do not build a graph rendering engine

UA owns repository semantics, projection, diagnostics, and impact behavior. It should not own generic graph rendering, pan/zoom, force layout, selection, edge drawing, or graph-algorithm primitives when mature open-source implementations already provide them.

Quartz remains the hosting/integration surface. PR 4 performs a bounded implementation spike between two paths:

1. extend the existing Quartz `Component.Graph()` / D3-Pixi path when the Control Map can be implemented as a narrow, maintainable extension;
2. wrap a mature graph library when typed edges, filtering, inspector behavior, layouts, and impact/diagnostic interaction would otherwise require substantial custom graph-engine code.

**Cytoscape.js** is the preferred external candidate for that spike, not a mandatory architecture dependency. The implementation PR must compare maintenance cost, bundle impact, accessibility, mobile/iPad interaction, upstream health, and required behavior against the existing Quartz path.

The Control Map has one behavioral owner and one logical graph projection regardless of renderer choice. Do not maintain equivalent Control Map semantics in two independent rendering stacks.

Implementation references checked on 2026-09-05:

- Cytoscape.js: <https://github.com/cytoscape/cytoscape.js>
- Quartz integration rules: [`../quartz/AGENTS.md`](../quartz/AGENTS.md) and [`../quartz/README.md`](../quartz/README.md)

Before adopting an external library, re-check current version, license, security posture, and bundle/runtime impact.

## 13. Interoperability: Open Knowledge Format as an evidence-triggered export

### RI-INTEROP-001 — Compatibility exports do not own UA metadata

Google's **Open Knowledge Format (OKF)** is a useful interoperability reference because it represents knowledge as Markdown with YAML frontmatter and separates the interchange format from a required platform. The public v0.2 material includes provenance/freshness-related metadata and additional verification-oriented fields while leaving broader attestation lifecycle work outside the completed format.

UA should not migrate its canonical repository metadata to OKF merely to gain interoperability. Existing UA metadata and ownership rules remain canonical.

An OKF-compatible export is considered only after:

1. the Repository Intelligence Projection schema is stable enough to map deliberately;
2. a concrete external consumer, tool, or interchange need exists;
3. the mapping is low-cost and semantics-preserving.

Any such export must:

- derive from the same logical projection rather than be maintained separately;
- preserve source identity and freshness;
- preserve UA-specific authority distinctions rather than flattening them into generic links;
- use extension fields or omit unsupported semantics rather than invent false equivalence;
- remain disposable and rebuildable;
- never become an input that silently overrides canonical UA files.

Google's OKF reference visualizer is useful as a UI/reference pattern. It is not a runtime dependency or a reason to adopt OKF as the internal projection schema.

Implementation references checked on 2026-09-05:

- OKF specification: <https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md>
- Google introduction: <https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing>

## 14. Evaluation and acceptance

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
- a stale/unavailable materialization case that must fall back to live repository reading;
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

### Connector/iPad acceptance

The compact Agent Context Surface must be tested through the actual maintainer path: ChatGPT/iPad using the GitHub connector.

Acceptance must show that routine cold-start orientation:

- does not require loading the full Graph View;
- completes with a bounded number of connector reads;
- does not silently truncate the compact surface;
- preserves complete term/artifact preflight coverage needed by the benchmark;
- can fall back to direct live-GitHub source reading when the generated view is missing or stale.

PR 2 should record the tested materialization size and connector behavior rather than encode an eternal byte limit in this architecture.

### Comparative agent metrics

Compare:

```text
manual live-GitHub bootstrap/search
vs
compact Agent Context Surface + preflight
```

Measure:

- broad searches before the correct owner is found;
- files opened before a correct material decision;
- connector reads and context/token volume needed for orientation;
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
- navigation edges do not dominate default Architecture/Impact views;
- deterministic errors are reproducible from repository facts;
- structural warnings remain advisory and explain their basis;
- Model-Judgment candidates remain visibly review-only;
- a PR impact view starts from the live changed-file set when the overlay is available and keeps accepted/proposed state separate;
- the map still works meaningfully when the live overlay is unavailable;
- the user can move from graph node/edge to owning source without reconstructing the path manually;
- default global view remains legible enough to reveal architecture rather than merely rendering every repository file;
- the selected graph implementation does not require UA to maintain generic rendering/layout behavior already owned by an adopted library.

## 15. Rollout

### PR 1 — Architecture baseline — this PR

Purpose: define the smallest useful logical projection, authority/freshness boundaries, physical materialization rules, agent preflight behavior, Repository Control Map contract, open-source reuse strategy, interoperability boundary, evaluation gates, and stop/go rule.

Included:

- this architecture document;
- changelog record;
- scoped `.github/AGENTS.md` routing to this owner;
- roadmap sequence for the shared projection, agent consumer, and graph consumer.

Explicitly not included:

- generated context files;
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

### PR 2 — Deterministic projection and materializations

Implement one deterministic producer for the logical projection and the smallest working consumers for agent preflight.

Required behavior:

- deterministic source/freshness identity;
- compact term inventory;
- compact maintained-artifact inventory;
- structural contributor-scope inventory;
- derived `Responsibility` nodes for existing `canonical_for` identifiers;
- explicit relationship extraction with edge classes and provenance;
- deterministic diagnostic signals backed by existing repository rules;
- `context_for_task`;
- `find_owner`;
- `term_preflight`;
- `artifact_preflight`;
- `validation_plan`;
- a compact connector-friendly Agent Context Surface;
- a fuller graph materialization usable by PR 4;
- drift/regeneration validation;
- generated-view placement that does not make ordinary content regeneration a repository-policy change merely because the read materialization changed.

The compact view and graph view share one producer/source identity but need not be one file. The graph view may be an uncommitted build/CI artifact. No model or network call is required to build the deterministic projection.

Live PR/check/review state is explicitly outside the deterministic materializations.

### PR 3 — Agent integration and independent benchmark

Integrate context/preflight operations into the actual agent workflow, add independently authored cold-start cases, and compare against manual live-GitHub orientation.

The benchmark must include the actual ChatGPT/iPad/GitHub-connector path and connector-size/read-cost behavior.

Do not choose the next retrieval technology before measuring the failure.

### PR 4 — Quartz Repository Control Map

Build the human-facing graph/impact/diagnostics consumer over the full graph materialization.

Target behavior:

- Explore, Architecture, Impact, and Diagnostics lenses;
- type/module/status/relation filters;
- local-first navigation with global view available on demand;
- node/edge inspector with provenance and direct source navigation;
- optional live PR changed-file overlay and explicit blast-radius paths;
- deterministic error, structural warning, and Model-Judgment review-candidate distinction;
- degraded operation without live GitHub overlay;
- no GitHub credential embedded in the static client.

PR 4 first performs a bounded renderer spike: extend the existing Quartz D3/Pixi graph if that remains a narrow maintainable path; otherwise prefer a mature OSS graph library such as Cytoscape.js over writing generic graph-engine behavior in UA.

### Interoperability follow-up

Only after a concrete external consumer or interchange need exists may a focused follow-up add an OKF-compatible export.

### Stop/go checkpoint

The required repository-intelligence program has two consumers: agent workflow and the Repository Control Map.

Once the lightweight logical projection and its materializations support both at acceptable local, connector, and maintainer cost, the required program is complete enough for ordinary UA work.

Continue normal framework work and collect real failures instead of automatically building more infrastructure.

## 16. Optional extensions — only after measured need

A later focused PR may add one of these only when it names the measured baseline failure and expected benefit:

- a persistent embedded read model for demonstrated rebuild/query cost;
- dense multilingual retrieval for demonstrated paraphrase/Ukrainian recall misses;
- a read-only MCP adapter for a client that actually needs that transport;
- additional visualization lenses beyond the planned Repository Control Map when a concrete navigation need appears;
- code-symbol intelligence for demonstrated implementation-impact misses;
- bounded inferred discovery relations that remain visibly non-authoritative;
- an external read-only cache of a generated materialization when a client cannot read GitHub directly.

Remote services, persistent stores, graph databases, and embeddings remain optional indefinitely if the lightweight baseline is sufficient.

## 17. Decision record

| ID | Decision | Status | Rationale |
|---|---|---|---|
| `RI-DEC-001` | Live Git/GitHub and owning files remain source of truth. | Accepted | Repository intelligence is orientation, not authority. |
| `RI-DEC-002` | Build a compact derived projection, not a repository mirror. | Accepted | GitHub already exposes repository content and PR state. |
| `RI-DEC-003` | One logical projection may have multiple deterministic materializations. | Accepted | Agent cold-start and graph visualization have materially different context budgets. |
| `RI-DEC-004` | Compact agent and full graph views share producer semantics and source identity. | Accepted | Different physical views must not become semantic forks. |
| `RI-DEC-005` | Keep live GitHub state as a runtime overlay. | Accepted | PR/check/review state is volatile and should not corrupt deterministic projection freshness. |
| `RI-DEC-006` | Routine generated read materializations must not live under a path that makes ordinary regeneration repository-policy work. | Accepted | Generated orientation data should not create governance tax for unrelated content edits. |
| `RI-DEC-007` | Full compact term/artifact inventories precede ranking. | Accepted | Top-k alone can miss the exact object whose omission the system should prevent. |
| `RI-DEC-008` | Exact/structural/lexical retrieval is the baseline. | Accepted | It is explainable, cheap, and sufficient to test first. |
| `RI-DEC-009` | Semantic similarity never creates authority. | Accepted | Model Judgment may surface candidates but cannot redefine repository ownership. |
| `RI-DEC-010` | Effective contributor scope stays with the checked-state protocol. | Accepted | The projection cannot self-authorize candidate instructions. |
| `RI-DEC-011` | `Responsibility` is a derived node for existing `canonical_for` identifiers. | Accepted | The graph needs an explicit edge target without creating a new responsibility registry. |
| `RI-DEC-012` | Separate semantic/evolution, repository/control, and navigation edge classes. | Accepted | A Markdown link is not equivalent to ownership, provenance, or validation dependence. |
| `RI-DEC-013` | `LINKS_TO` is navigation and is hidden/de-emphasized by default in Architecture/Impact. | Accepted | Bulk links are useful for browsing but otherwise dominate the graph signal. |
| `RI-DEC-014` | Diagnostics separate deterministic errors, structural warnings, and Model-Judgment candidates. | Accepted | Sensors may surface review signals without turning judgment into authority or brittle CI. |
| `RI-DEC-015` | Manual live-repository fallback remains valid. | Accepted | Intelligence must not become an availability dependency. |
| `RI-DEC-016` | The Control Map must degrade safely without live GitHub. | Accepted | Accepted-state architecture should remain usable without overlay availability. |
| `RI-DEC-017` | Do not embed GitHub credentials in the static browser client. | Accepted | Live overlay convenience must not create a new secret boundary in Quartz. |
| `RI-DEC-018` | Do not build a bespoke graph engine. | Accepted | Reuse the current Quartz path when narrow; otherwise evaluate a mature OSS renderer such as Cytoscape.js. |
| `RI-DEC-019` | OKF is evidence-triggered interoperability only. | Accepted | Export complexity is justified only by a concrete consumer or interchange need. |
| `RI-DEC-020` | Complexity requires a named measured failure or consumer need. | Accepted | Maintainer capacity and repository scale favor proportional tooling. |

## 18. Current implementation state

| Capability | State |
|---|---|
| Architecture and proportionality contract | Defined by this document |
| Deterministic logical Repository Intelligence Projection | Planned for PR 2 |
| Compact connector-friendly Agent Context Surface | Planned for PR 2 |
| Full Graph View materialization | Planned for PR 2 / consumed by PR 4 |
| `Responsibility` derived nodes and typed edge classes | Planned for PR 2 |
| `context_for_task` / owner / preflight / validation operations | Planned for PR 2 |
| Drift/regeneration validation | Planned for PR 2 |
| Agent-workflow integration | Planned for PR 3 |
| Independent connector-aware cold-start benchmark | Planned for PR 3 |
| Quartz Repository Control Map | Planned for PR 4 |
| Renderer selection: existing Quartz path vs mature OSS | Planned PR 4 spike |
| OKF-compatible export | Optional after concrete consumer need |
| Persistent store / embeddings / MCP / graph database / code intelligence | Optional, evidence-triggered |

The repository remains fully understandable without this tooling. Until PR 2 exists and passes its own freshness and connector-size checks, agents continue to use live GitHub plus the task-specific reading paths in [`../AGENTS.md`](../AGENTS.md).
