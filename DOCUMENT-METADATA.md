---
title: UA Document Metadata and Tagging Convention
artifact_type: repository-process
status: informative
maturity: active
module: repository
topics:
  - repository-architecture
  - navigation
  - provenance
tags:
  - ua/module/repository
  - ua/type/repository-process
  - ua/status/informative
  - ua/topic/repository-architecture
  - ua/topic/navigation
canonical_for:
  - document-metadata
  - tag-vocabulary
---

# UA Document Metadata and Tagging Convention

## Purpose

This document defines a small, controlled metadata system for Uncertainty Architecture (UA) Markdown documents.

The system is intended to improve:

- repository navigation;
- Obsidian search, graph, and tag views;
- retrieval and orientation for language models and coding agents;
- separation of normative, research, reference, and historical material;
- traceability without creating a second specification hierarchy.

Metadata helps readers find and classify a document. It does **not** make a document normative. Normative authority is defined by [`SPECIFICATION.md`](SPECIFICATION.md), the document's explicit status, and the relevant module index.

## Scope

The convention applies to maintained UA Markdown documents that define, index, interpret, or govern project material.

It does not need to be retrofitted mechanically to:

- raw source snapshots under `content/raw/`;
- preserved historical publication bodies;
- license texts;
- generated files;
- vendored Quartz implementation files;
- the root `README.md` when frontmatter would reduce its value as the GitHub landing page.

Historical and research files may adopt the convention when they are actively edited, but provenance must not be changed merely to make metadata uniform.

## Required fields

Maintained conceptual documents should use the following YAML frontmatter:

```yaml
---
title: Human-readable document title
artifact_type: doctrine
status: draft-normative
maturity: active
module: doctrine
topics:
  - thinking-systems
  - uncertainty-boundary
tags:
  - ua/module/doctrine
  - ua/type/doctrine
  - ua/status/draft-normative
  - ua/topic/thinking-systems
  - ua/topic/uncertainty-boundary
---
```

### `title`

The human-readable document title. It should match or closely correspond to the first-level heading.

### `artifact_type`

The role of the document in the repository. Use a specific value rather than the generic word `document`.

Initial controlled values:

- `repository-index`
- `repository-guide`
- `repository-process`
- `specification-index`
- `doctrine`
- `glossary`
- `pattern-index`
- `pattern`
- `control-plane-index`
- `control-capability`
- `reference-index`
- `reference-architecture`
- `failure-mode-index`
- `failure-mode`
- `research-index`
- `research-publication`
- `research-note`
- `research-process`
- `research-template`
- `research-traceability`
- `source-archive-index`
- `history-index`
- `history-record`
- `historical-artifact`
- `publishing-index`
- `roadmap`
- `changelog`

New values should be added here only when an existing value cannot describe a recurring document role.

### `status`

The document-status vocabulary is controlled by [`SPECIFICATION.md`](SPECIFICATION.md):

- `normative`
- `draft-normative`
- `informative`
- `reference`
- `research`
- `historical`

The hyphenated metadata values are machine-friendly forms of the human-readable status labels in the specification.

Do not use `draft` as a substitute for document status. Draftness is maturity, not normative classification.

### `maturity`

Optional lifecycle state within the document's status class:

- `draft`
- `active`
- `stable`
- `superseded`

Examples:

- a developing research note: `status: research`, `maturity: draft`;
- an actively maintained research index: `status: research`, `maturity: active`;
- a retired governance proposal: `status: historical`, `maturity: superseded`.

The Quartz field `draft: true` is a publishing-visibility control. It must not be interpreted as the UA document status.

### `module`

The primary repository area responsible for the document:

- `repository`
- `doctrine`
- `patterns`
- `control-plane`
- `reference-architectures`
- `failure-modes`
- `research`
- `history`
- `publishing`

A document has one primary module even when it relates to several areas.

### `topics`

A short list of concepts materially addressed by the document. Topics are structured retrieval metadata and should not become an uncontrolled keyword dump.

Initial controlled topics:

- `thinking-systems`
- `linear-software`
- `deterministic-core`
- `model-judgment`
- `uncertainty-boundary`
- `control-loop`
- `ai-control-plane`
- `actuators`
- `constraints`
- `sensors`
- `controller`
- `evaluation`
- `evidence`
- `drift`
- `containment`
- `fallback`
- `rollback`
- `escalation`
- `human-authority`
- `conformance`
- `provenance`
- `control-economics`
- `sdlc`
- `repository-architecture`
- `navigation`

Add a topic only when it is likely to recur across documents and materially improves retrieval.

### `tags`

Tags are the Obsidian- and Quartz-friendly projection of the structured metadata.

Use hierarchical, lowercase, kebab-case tags:

- `ua/module/<module>`
- `ua/type/<artifact-type>`
- `ua/status/<status>`
- `ua/topic/<topic>`

A document should normally have three to eight tags. Do not tag every noun that appears in the text.

Structured fields are authoritative. Tags must not contradict `module`, `artifact_type`, `status`, or `topics`.

## Optional relationship fields

Use these fields when they improve machine and human navigation:

```yaml
canonical_for:
  - doctrine-vocabulary
related:
  - ../02-ai-control-plane/README.md
supersedes:
  - path/to/earlier-document.md
superseded_by:
  - path/to/current-document.md
```

### `canonical_for`

Names a repository responsibility for which the document is the canonical source, such as:

- `repository-landing`
- `specification-boundary`
- `document-status-model`
- `doctrine-vocabulary`
- `research-track`
- `project-history`
- `raw-source-archive`
- `project-roadmap`
- `change-record`
- `contribution-workflow`
- `document-metadata`
- `tag-vocabulary`
- `ai-agent-repository-guide`
- `supporting-material-publishing-portal`

Only one active document should normally claim the same `canonical_for` value.

### `related`

Lists high-value relationships that are not already obvious from the directory structure. It is not a replacement for readable links in the document body.

### `supersedes` and `superseded_by`

Record explicit evolution. These fields are especially useful for terminology decisions, historical governance artifacts, and replaced patterns.

## Tagging rules

1. Tag the document's real role, not every concept it mentions.
2. Keep status in sync with `SPECIFICATION.md`.
3. Do not use tags to promote research into normative content.
4. Do not silently retag a historical source as current doctrine.
5. Prefer an existing controlled topic over a synonym.
6. Add new controlled terms through a deliberate repository change.
7. Keep tags stable enough that Obsidian queries and LLM retrieval prompts remain reusable.
8. Use `canonical_for` sparingly; it is an authority-discovery aid, not a label for every important file.

## Obsidian examples

Find active doctrine and control-plane material:

```text
tag:#ua/status/draft-normative (tag:#ua/module/doctrine OR tag:#ua/module/control-plane)
```

Find material about drift:

```text
tag:#ua/topic/drift
```

Find research notes rather than archived publications:

```text
tag:#ua/type/research-note
```

## LLM retrieval guidance

A language model or agent should interpret metadata in this order:

1. `canonical_for`
2. `status`
3. `module`
4. `artifact_type`
5. `topics`
6. `tags`
7. directory location and inbound links

Metadata narrows where to read; it does not replace reading the relevant document or checking its evidence and status boundaries.

## Migration policy

The repository adopts this convention incrementally:

- canonical indexes and actively maintained framework documents should be tagged first;
- new documents should use the convention from creation;
- existing research and history records may be updated when touched;
- raw and preserved source bodies should not be rewritten solely for metadata uniformity.

A future validation utility may check controlled values and tag-field consistency, but the metadata convention does not require new tooling to remain useful.
