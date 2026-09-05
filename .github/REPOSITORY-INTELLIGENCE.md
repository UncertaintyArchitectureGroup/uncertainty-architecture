# Repository Intelligence and Agent Context Architecture

## Status and role

This document is the informative architecture and rollout contract for repository-intelligence tooling used to orient AI-assisted contributors in Uncertainty Architecture.

It does not define UA doctrine, terminology, conformance, research disposition, or framework decision authority. Those remain with their existing owners, including [`../SPECIFICATION.md`](../SPECIFICATION.md), [`../00-doctrine/glossary.md`](../00-doctrine/glossary.md), owning doctrine and patterns, [`../DOCUMENT-METADATA.md`](../DOCUMENT-METADATA.md), research records, and the contributor protocol in [`../AGENTS.md`](../AGENTS.md).

Repository intelligence exists to make those owners easier to find and harder to accidentally duplicate. It is a derived orientation layer, never a second specification, glossary, research ledger, decision registry, or source of authority.

## 1. Problem

UA is logically dense enough that a fresh agent can make predictable repository mistakes even when all necessary information already exists:

- miss an existing canonical owner and propose a parallel file;
- invent a near-synonym instead of reusing or deliberately refining an existing term;
- confuse research, history, examples, or publishing material with current framework ownership;
- edit the right source but miss an applicable `AGENTS.md`, dependency, validator, or companion surface;
- spend large context on broad search before establishing where the answer should come from.

The repository already exposes most raw facts through Git and GitHub: tree structure, files, branches, pull requests, diffs, reviews, checks, metadata, links, and version history. The missing capability is not another copy of the repository. It is a cheap cold-start orientation surface over the repository's existing structure and ownership signals.

## 2. Baseline product

The baseline product is a compact, repository-native **Agent Context Surface** plus a task-scoped **Agent Context Pack** built from it and live GitHub state.

The context surface complements the version-control system; it must not mirror the repository body. It should summarize the structural facts that are expensive for a fresh agent to reconstruct repeatedly while leaving canonical content in its owning files.

The first useful surface should expose, at minimum:

- exact indexed source identity and a deterministic freshness identity;
- discovered root and nested `AGENTS.md` paths with structural scope roots;
- the full compact inventory of canonical glossary labels, plus explicit aliases or predecessor labels already recorded by canonical sources;
- the full compact inventory of maintained conceptual/process artifacts, with path, title/H1, module, `artifact_type`, status, topics, and existing `canonical_for` values where present;
- explicit high-value repository relationships already present in frontmatter or Markdown links;
- research-state pointers when a task intersects research;
- repository-policy, validator, and workflow pointers sufficient to build a validation plan;
- reasons and source paths for task-relevant candidates so the agent can open the owning source before deciding.

The surface should not copy full Markdown bodies, binary artifacts, Quartz implementation trees, publications, or other content that GitHub already exposes directly unless a later benchmark shows a specific recall problem that requires a bounded addition.

## 3. Source of truth and freshness

### RI-SOT-001 — GitHub and the checked repository remain authoritative

The current Git repository at an explicitly identified source state is authoritative for repository content. Live GitHub remains authoritative for branches, pull requests, reviews, checks, workflow runs, mergeability, accepted target state, and current file state.

Any generated context surface, local index, cache, lexical index, embedding index, database, graph, or adapter response is a derived projection.

If a projection and live repository state disagree, the repository wins. A stale or unverifiable projection must fall back to live repository reading.

### RI-FRESH-001 — Freshness must be deterministic and non-self-referential

The committed context surface must identify the inputs it represents without depending on the commit SHA that contains the generated surface itself.

PR 2 should use a deterministic source identity such as a digest over the declared indexed input paths and their Git blob identities while excluding the generated output itself. Regeneration/drift validation must recompute that identity and fail when the committed surface no longer matches its declared inputs.

The exact serialization and digest format belong to PR 2, but the following properties are required:

- deterministic from a clean repository state;
- independent of timestamps;
- explicit about included and excluded paths;
- sufficient to distinguish current, stale, and deliberately pinned source states;
- rebuildable without a hosted service.

## 4. Authority and routing

### RI-AUTH-001 — Retrieval discovers authority; it does not create it

Repository-intelligence ranking never determines semantic authority.

Routing uses existing repository evidence first:

1. task class and applicable contributor scope from [`../AGENTS.md`](../AGENTS.md) and nested `AGENTS.md` files;
2. explicit canonical owners identified by the repository's existing ownership and document structure;
3. glossary definitions for canonical terminology;
4. existing `canonical_for`, status, module, `artifact_type`, topics, titles, headings, and explicit relationships as navigation evidence;
5. bounded lexical matching only to surface candidates that still require source reading.

`canonical_for` remains the metadata convention already owned by [`../DOCUMENT-METADATA.md`](../DOCUMENT-METADATA.md). PR 1 does not create a second protected-responsibility registry or add new decision-surface identifiers merely to improve retrieval.

Absence of a `canonical_for` value must not be converted into a claim that no semantic owner exists. When ownership remains ambiguous, the agent opens the likely owning sources and resolves the question against their maintained prose.

### RI-GUIDANCE-001 — Contributor scope is resolved by the existing agent protocol

The context surface may list `AGENTS.md` paths, blob identities, and structural scope roots. Those facts help discovery but do not independently decide which instructions govern a pull request.

Effective PR instruction scope remains owned by the checked-state protocol in [`../AGENTS.md`](../AGENTS.md) and live GitHub state. Candidate text cannot use the repository-intelligence layer to waive target-owned controls.

## 5. Required agent operations

The baseline should support these logical operations. PR 2 may expose them through a local library, CLI, generated JSON, or another small interface; MCP is not required.

### `context_for_task`

Return the smallest orientation pack needed to decide which sources must be read for a task. The pack should include source identity, applicable instruction paths, owner candidates, relevant term/artifact candidates, explicit relationships, and likely validation surfaces.

### `find_owner`

Return typed owner candidates with evidence and paths. It must distinguish definition ownership, framework decision ownership, research-state ownership, repository-process ownership, and implementation location when those differ.

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

## 6. Lightweight retrieval baseline

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
- a Quartz graph UI;
- code-symbol indexing;
- inferred semantic edges.

### RI-COMPLEMENT-001 — Do not build a repository mirror

The context surface must not duplicate capabilities already available cheaply from GitHub merely to make them available somewhere else.

In particular, the required baseline does not copy the repository to Google Drive, another cloud drive, or a second content store. A mirror would add freshness and synchronization failure modes without solving the core ownership/interpretation problem.

An external read-only cache may later carry the generated context surface when a client needs it, but that copy gains no independent authority or freshness.

## 7. Minimal projected relationships

PR 2 should implement only relationships needed by the cold-start operations. The initial set may remain a simple deterministic structure rather than a formal graph runtime.

Useful baseline relationships include:

- repository snapshot contains maintained file;
- file contains heading/section identity when needed for source routing;
- glossary section defines term;
- file declares `canonical_for`;
- file belongs to module / `artifact_type` / status / topics;
- file explicitly links or declares `related`, `supersedes`, `superseded_by`, or `source_basis` where those fields already exist;
- file falls under one or more structural `AGENTS.md` scopes;
- repository policy or validator protects or validates a path when that relation is explicit in existing policy.

Unsupported relationship families must be reported as unsupported rather than inferred as absent.

No relationship may be promoted from semantic similarity into canonical ownership, research disposition, contributor authority, or normative status.

## 8. PR and accepted/proposed state

The committed baseline surface represents one exact repository source state.

For pull-request work, live GitHub supplies target/head refs, diff, reviews, checks, mergeability, and tested-merge state. A runtime context pack may compare accepted and proposed source facts, but it must keep them visibly separate and preserve the originating source state.

PR 2 does not need a general cross-snapshot graph. It needs only enough state separation to avoid presenting candidate ownership, metadata, or contributor scope as already accepted.

## 9. Security boundary

Repository files can contain instruction-like text. The intelligence layer treats ordinary Markdown, publications, examples, imported source text, code comments, and research notes as data.

Contributor instructions are resolved only through the repository's root/nested `AGENTS.md` protocol and live checked state.

The baseline query surface is read-only and must not:

- execute arbitrary repository code while answering a retrieval query;
- execute package scripts or validators as a side effect of retrieval;
- require network access beyond ordinary Git/GitHub operations already used by the workflow;
- allow retrieved text or model-generated relationships to grant authority;
- commit private caches, secrets, local paths, or downloaded model data.

Executable validation remains a separate explicit engineering action under existing repository controls.

## 10. Cold-start benchmark

### RI-EVAL-001 — Measure agent correctness, not search sophistication

Repository intelligence is useful only if a fresh agent makes fewer predictable UA repository mistakes with less orientation cost.

The independently authored benchmark in PR 3 should include at least:

- owner recovery for an exact existing responsibility;
- a request that tempts creation of a synonym for an existing canonical term;
- a request with several plausible near-synonyms that requires source review rather than automatic merging;
- a request that sounds like a new document but should refine an existing owner;
- a legitimate new artifact where overlap exists but no current artifact owns the required role;
- an impact/validation query for a material concept or repository-policy change;
- a research task that must keep research state separate from framework authority;
- a stale/unavailable context-surface case that must fall back to live repository reading;
- Ukrainian and paraphrased maintainer wording that should still reach the relevant candidates.

### Core gates

For benchmarked deterministic cases:

- exact owner recovery at rank 1 where the repository already defines an exact owner: **100%**;
- benchmarked existing canonical term candidates silently missed before a new-term proposal: **0**;
- benchmarked overlapping artifacts silently missed before a duplicate-file proposal: **0**;
- stale or unverifiable context silently treated as current: **0**;
- research/history/supporting material silently upgraded to current authority: **0**;
- candidate state silently represented as accepted state: **0**;
- candidate `AGENTS.md` text used to waive target-owned controls: **0**.

### Comparative metrics

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

## 11. Rollout

### PR 1 — Architecture baseline — this PR

Purpose: define the smallest useful product, authority boundary, freshness model, preflight behavior, evaluation gates, and stop/go rule.

Included:

- this architecture document;
- changelog record;
- scoped `.github/AGENTS.md` routing to this owner.

Explicitly not included:

- generated index;
- new semantic-owner metadata;
- protected responsibility registry;
- graph/database runtime;
- embeddings;
- MCP;
- agent-workflow integration;
- cold-start benchmark implementation.

### PR 2 — Deterministic context surface and preflight

Implement the smallest working producer and consumer for:

- source/freshness identity;
- compact term inventory;
- compact maintained-artifact inventory;
- structural contributor-scope inventory;
- existing metadata and explicit relationship extraction;
- `context_for_task`;
- `find_owner`;
- `term_preflight`;
- `artifact_preflight`;
- `validation_plan`;
- deterministic committed context surface;
- drift/regeneration validation.

Use existing dependencies where practical. No model or network call is required to build the surface.

### PR 3 — Agent integration and independent benchmark

Integrate the available context/preflight operations into the actual agent workflow, add independently authored cold-start cases, compare against manual live-GitHub orientation, and record misses by cause.

Do not choose the next technology before measuring the failure.

### Stop/go checkpoint

If the lightweight path meets the benchmark gates at acceptable local and maintainer cost, the required repository-intelligence program is complete enough for ordinary UA work.

Continue normal framework work and collect real failures instead of automatically building more infrastructure.

## 12. Optional extensions — only after measured need

A later focused PR may add one of these only when it names the measured baseline failure and expected benefit:

- a persistent embedded read model for demonstrated rebuild/query cost;
- dense multilingual retrieval for demonstrated paraphrase/Ukrainian recall misses;
- a read-only MCP adapter for a client that actually needs that transport;
- Quartz relationship views for demonstrated human-navigation value;
- code-symbol intelligence for demonstrated implementation-impact misses;
- bounded inferred discovery relations that remain visibly non-authoritative;
- an external read-only cache of the generated context surface when a client cannot read GitHub directly.

Remote services, persistent stores, and embeddings remain optional indefinitely if the lightweight baseline is sufficient.

## 13. Decision record

| ID | Decision | Status | Rationale |
|---|---|---|---|
| `RI-DEC-001` | Live Git/GitHub remains source of truth. | Accepted | Repository intelligence is orientation, not authority. |
| `RI-DEC-002` | Build a compact context surface, not a repository mirror. | Accepted | GitHub already exposes repository content and PR state. |
| `RI-DEC-003` | Commit one deterministic GitHub-readable context surface in PR 2. | Accepted | A fresh connected agent needs a stable addressable orientation artifact. |
| `RI-DEC-004` | Do not introduce new semantic-owner metadata in PR 1. | Accepted | Existing owner prose and metadata must be tested before adding another registry. |
| `RI-DEC-005` | Full compact term/artifact inventories precede ranking. | Accepted | Top-k alone can miss the exact object whose omission the system should prevent. |
| `RI-DEC-006` | Exact/structural/lexical retrieval is the baseline. | Accepted | It is explainable, cheap, and sufficient to test first. |
| `RI-DEC-007` | Semantic similarity never creates authority. | Accepted | Model Judgment may surface candidates but cannot redefine repository ownership. |
| `RI-DEC-008` | Effective contributor scope stays with the existing checked-state protocol. | Accepted | The index cannot self-authorize candidate instructions. |
| `RI-DEC-009` | Complexity requires a named measured failure. | Accepted | Maintainer capacity and repository scale favor proportional tooling. |
| `RI-DEC-010` | Manual live-repository fallback remains valid. | Accepted | Intelligence must not become an availability dependency. |

## 14. Current implementation state

| Capability | State |
|---|---|
| Architecture and proportionality contract | Defined by this document |
| Repository-native generated context surface | Planned for PR 2 |
| `context_for_task` / owner / preflight / validation operations | Planned for PR 2 |
| Drift/regeneration validation | Planned for PR 2 |
| Agent-workflow integration | Planned for PR 3 |
| Independent cold-start benchmark | Planned for PR 3 |
| Persistent store / embeddings / MCP / graph UI / code intelligence | Optional, evidence-triggered |

The repository remains fully understandable without this tooling. Until PR 2 exists and passes its own freshness checks, agents continue to use live GitHub plus the task-specific reading paths in [`../AGENTS.md`](../AGENTS.md).
