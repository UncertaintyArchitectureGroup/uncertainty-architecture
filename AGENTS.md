---
title: Repository Guide for AI Agents
artifact_type: repository-guide
status: informative
maturity: active
module: repository
topics:
  - repository-architecture
  - navigation
  - provenance
tags:
  - ua/module/repository
  - ua/type/repository-guide
  - ua/status/informative
  - ua/topic/repository-architecture
  - ua/topic/navigation
canonical_for:
  - ai-agent-repository-guide
---

# Repository Guide for AI Agents

## Purpose

This file helps language models, coding agents, and automated review tools orient themselves in the Uncertainty Architecture (UA) repository.

It is operational guidance, not part of the normative specification. It must not be used to override [`SPECIFICATION.md`](SPECIFICATION.md), an explicit document status, or the relevant module index.

## Authority order

When repository documents appear to conflict, use this order:

1. [`SPECIFICATION.md`](SPECIFICATION.md) for specification scope, status vocabulary, conformance, and change control.
2. The relevant module README for the role and boundary of that module.
3. The explicit status and normative language of the individual document.
4. [`00-doctrine/glossary.md`](00-doctrine/glossary.md) for current canonical terminology where a term is defined.
5. [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md) for metadata and tagging conventions.
6. Research and history for evidence, provenance, evolution, and context — not automatic requirements.

A newer file, recent commit, external citation, popular discussion, or high-visibility source does not become normative merely because it is recent or prominent.

## Canonical repository map

### Public entry points

- [`README.md`](README.md) — public landing page and reader navigation.
- [`SPECIFICATION.md`](SPECIFICATION.md) — canonical specification boundary, status model, and conformance entry point.
- [`ROADMAP.md`](ROADMAP.md) — current development sequence and planned work.
- [`CHANGELOG.md`](CHANGELOG.md) — repository and specification-artifact change record.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — maintainer and contributor workflow.

### Specification modules

- [`00-doctrine/`](00-doctrine/) — foundational concepts and canonical vocabulary.
- [`01-patterns/`](01-patterns/) — reusable technical and socio-technical control patterns.
- [`02-ai-control-plane/`](02-ai-control-plane/) — actuator, sensor, controller, evidence, and corrective-action capabilities.
- [`03-reference-architectures/`](03-reference-architectures/) — non-prescriptive compositions and examples.
- [`04-failure-modes/`](04-failure-modes/) — recurring technical, semantic, operational, and governance failures.

### Supporting evidence and records

- [`content/research/`](content/research/) — research publications, notes, synthesis, review process, and traceability.
- [`content/raw/`](content/raw/) — preserved source snapshots. Do not silently edit or reinterpret them as current doctrine.
- [`content/history/`](content/history/) — timeline, talks, public stress tests, independent references, and superseded project records.
- [`content/index.md`](content/index.md) — publishing portal for the Quartz site; it is not a second specification entry point.

### Repository infrastructure

- `quartz/`, `quartz.config.ts`, `quartz.layout.ts`, Node package files, and `vercel.json` are publishing infrastructure.
- `assets/` contains diagrams and visual references.
- Infrastructure behavior is not a UA requirement unless a specification document explicitly says so.

## Current terminology

Use **Thinking Systems** for software systems whose runtime behavior depends partly on probabilistic model judgment while consequential deterministic boundaries and control responsibilities remain explicit.

Historical UA publications used **Behavioral Software** and **Behavioral Applications**. Preserve those terms inside historical sources and titles, but do not use them as the current category in new framework material.

Agentic systems are a higher-autonomy subset of Thinking Systems, not a synonym for the whole category.

Other important distinctions:

- **Deterministic Core** — rules, invariants, permissions, data handling, and responsibilities that must remain explicitly controlled.
- **Model Judgment** — probabilistic interpretation, synthesis, classification, generation, planning, or action selection.
- **Uncertainty Boundary** — the interface where deterministic responsibilities meet model-mediated judgment.
- **AI Control Plane** — the distributed capability model used to constrain, observe, evaluate, and correct model-mediated behavior; not necessarily one standalone service.
- **Controller** — the decision function that interprets evidence and authorizes corrective action. It may be technical, human, or socio-technical.

Check the glossary before inventing a synonym or redefining an existing term.

## Reading strategy by task

### Understanding UA

1. Read `README.md`.
2. Read `SPECIFICATION.md`.
3. Read `00-doctrine/README.md` and `00-doctrine/glossary.md`.
4. Read the module relevant to the question.
5. Use research and history only when provenance or evolution matters.

### Changing normative or draft-normative content

1. Identify the module that owns the concept.
2. Check the glossary and cross-module dependencies.
3. Find supporting research, operational evidence, or design rationale.
4. State compatibility, supersession, and unresolved uncertainty.
5. Update the relevant module index, metadata, links, and changelog when material.
6. Do not promote research by implication; make the normative decision explicit.

### Working with research

1. Start with `content/research/index.md`.
2. Distinguish source preservation, analysis, synthesis, and framework candidates.
3. Preserve attributed wording and publication provenance.
4. Use `content/research/framework-traceability.md` for decision-oriented mapping.
5. Do not treat illustrative thresholds, examples, or role names as universal requirements.

### Working with history or external recognition

1. Start with `content/history/README.md`.
2. Distinguish publication, discussion, citation, recommendation, advisory relationship, invited talk, implementation, adoption, and certification.
3. Do not convert views, reactions, reposts, or invitations into technical validation.
4. Preserve criticism and alternative interpretations where they are material.

### Working with the publishing site

1. Treat `content/index.md` as a publishing portal, not the canonical repository landing page.
2. Do not move specification authority into Quartz configuration or generated navigation.
3. Keep publishing changes separate from methodology changes when practical.

## Editing invariants

An agent must not:

- rewrite raw source snapshots to match current terminology;
- silently modernize historical titles or attributed publication bodies;
- present research, a talk, external recognition, or a reference architecture as normative adoption;
- introduce universal numerical thresholds without an explicit risk- and context-derived basis;
- turn example job titles into mandatory organizational roles;
- assume that telemetry creates control without decision authority and a corrective mechanism;
- describe one prompt, evaluator, guardrail, agent, or metric as sufficient control for a system-level failure mode;
- create a second canonical entry point for material already owned elsewhere;
- create new top-level namespaces without explaining why an existing canonical area is insufficient;
- use `Behavioral Software` or `Behavioral Applications` as current framework terminology.

## Metadata and tags

Follow [`DOCUMENT-METADATA.md`](DOCUMENT-METADATA.md).

For retrieval, prefer structured frontmatter in this order:

1. `canonical_for`
2. `status`
3. `module`
4. `artifact_type`
5. `topics`
6. hierarchical `ua/...` tags

Do not infer normative authority from tags alone. Check the document and `SPECIFICATION.md`.

## Link and navigation rules

- Use repository-relative links for internal documents.
- Link to the canonical index of a directory rather than duplicating its document list elsewhere.
- Keep one canonical location per material type.
- When moving a document, preserve provenance and update inbound navigation.
- Avoid links to nonexistent planned files. Planned artifacts belong in `ROADMAP.md` until created.

## Quality checklist

Before proposing a repository change, verify:

- the target document has the correct status;
- current terminology is used outside historical material;
- examples are not written as universal requirements;
- role names are responsibilities unless the specification explicitly requires a title;
- research and history remain outside the normative boundary;
- metadata fields and tags agree;
- internal links resolve to existing paths;
- no duplicate canonical route is introduced;
- moved or superseded material remains traceable;
- the changelog and roadmap are updated only when the change is material.

## Scope of this file

`AGENTS.md` is the repository's tool-neutral agent guide. Tool-specific files such as `CLAUDE.md` should not duplicate this map. If a tool-specific adapter is ever required, it should point here and contain only the minimal tool-specific delta.