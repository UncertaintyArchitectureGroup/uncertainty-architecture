---
title: Uncertainty Architecture Research Track
artifact_type: research-index
status: research
maturity: active
module: research
topics:
  - provenance
  - thinking-systems
  - repository-architecture
tags:
  - ua/module/research
  - ua/type/research-index
  - ua/status/research
  - ua/topic/provenance
  - ua/topic/thinking-systems
canonical_for:
  - research-track
created: 2026-07-24
updated: 2026-07-26
license: CC-BY-4.0
---

# Uncertainty Architecture Research Track

## Purpose

The Uncertainty Architecture (UA) Research Track preserves and reviews the work that led to the framework.

UA did not begin as a finished standard. It evolved through architectural, operational, governance, verification, and economic investigations. This section makes that evolution explicit and creates a controlled bridge from research to future doctrine, patterns, operating-model responsibilities, reference architectures, failure modes, and practical artifacts.

## Canonical namespace

`content/research/` is the only active research namespace in the repository.

- completed or normalized publications belong in [`publications/`](publications/);
- bounded working briefs and observations belong in [`notes/`](notes/);
- preserved unnormalized source snapshots belong in [`content/raw/`](../raw/);
- public milestones, talks, discussions, and superseded project-process records belong in [`content/history/`](../history/).

A new root-level `research/` directory should not be created. Research material should be classified inside this namespace so that working notes, archived sources, analyses, and framework decisions do not compete as separate entry points.

## Normative boundary

Documents in this section are **research materials**. They are not automatically binding parts of the UA specification.

Research publications may contain:

- early terminology;
- provisional role names;
- strong recommendations;
- illustrative numerical thresholds;
- assumptions that were later refined;
- conclusions that conflict with later work.

A research conclusion becomes normative only after it is reviewed, translated into the appropriate framework component, and accepted through the UA contribution and change-control process.

## Content types

### Published research

Repository editions of publicly published articles. The substantive historical argument is preserved, while formatting, metadata, broken links, and platform-specific boilerplate may be normalized.

### Consolidated repository editions

Documents that combine overlapping public versions, translations, or technically richer variants. Every consolidation must explain its provenance and material transformations.

### Research analysis

Focused analysis of one or more sources that may record:

- the research question;
- key findings;
- contributions to UA;
- claims that remain useful;
- claims that were later refined or superseded;
- contradictions with other UA work;
- terminology evolution;
- framework candidates;
- unresolved questions.

### Research notes

Bounded working material derived from presentations, talks, working sessions, operational observations, external critique, or emerging questions. A planning brief is not completed evidence and should state its maturity explicitly.

See the [Research Notes index](notes/README.md).

### Framework traceability

A controlled map from research findings to possible future Doctrine, Pattern, Operating Model, Reference Architecture, Failure Mode, or practical Artifact components.

## Review model

Research work uses a proportional review model rather than a mandatory source-by-source pipeline.

Depending on the question and impact, a change may contain one or more of the following:

1. a repository edition of a source;
2. a source-specific analysis;
3. a multi-source synthesis;
4. a terminology or contradiction review;
5. a traceability update;
6. a framework-candidate note.

One logical change per pull request remains a useful default for substantial work, but every source does not require its own pull request or a fixed package of artifacts.

Research changes do **not** automatically rewrite the framework. Normative changes are proposed separately after the relevant evidence has been synthesized and reviewed.

See [Research Review Process](review-process.md).

## Review templates

- [Research Publication Record Template](publication-record-template.md)
- [Research Analysis Template](research-analysis-template.md)

These templates are optional working tools. Their Quartz `draft: true` field controls publishing visibility; it is not the UA document status.

## Status vocabulary

- **Research Finding** — a conclusion preserved from research material.
- **Candidate** — potentially suitable for translation into a framework component.
- **Needs Resolution** — terminology, scope, evidence, or conflict must be resolved first.
- **Proposed for Framework Review** — mature enough for a separate, deliberate normative proposal and visible review.
- **Active** — accepted into the normative framework.
- **Superseded** — replaced by a later formulation.
- **Rejected** — considered and intentionally not adopted.

See [Research-to-Framework Traceability](framework-traceability.md).

## Current research direction

The initial publication corpus has been preserved under [`publications/`](publications/). Earlier root-level planning briefs have been classified under [`notes/`](notes/) and remain draft research tasks rather than completed findings.

The next major task is a cross-publication synthesis that identifies:

- concepts that remained stable;
- concepts that were refined or superseded;
- unresolved contradictions;
- terminology requiring separate review;
- candidates for the framework spine;
- material that should remain research context only.

Source-specific analysis may still be added when it contributes evidence, clarifies provenance, or resolves a concrete question. It is not a prerequisite for beginning corpus-level synthesis.

The initial corpus includes:

1. *Architecting Uncertainty: A Modern Guide to LLM-Based Software*;
2. *On-Device LLM or Cloud API?*;
3. *Uncertainty Architecture: A Modern Approach to Designing LLM Applications* together with its technically richer Ukrainian version;
4. *Uncertainty Architecture: Why AI Governance Is Actually Control Theory*;
5. *Beyond Embeddings: Neuro-Symbolic Verification of Semantic Drift in LLMs*;
6. the *Designing Non-Deterministic Systems* presentation as a research synthesis source.

## Terminology decision

Current UA terminology uses **Thinking Systems** for software that delegates part of runtime interpretation, judgment, planning, or decision-making to probabilistic models while retaining explicit deterministic boundaries and control responsibilities.

Historical publications used **Behavioral Software** and **Behavioral Applications**. Current framework documents may identify the migration on first use as **Thinking Systems** (previously described as **Behavioral Software** or **Behavioral Applications**), but should use **Thinking Systems** thereafter.

Agentic systems are treated as a higher-autonomy subset of Thinking Systems rather than as a synonym for the whole category.

Historical publications and raw sources retain their original language for provenance. Repository editions should include a terminology note when the legacy category is material to the text.

## Metadata

Research documents should follow [`DOCUMENT-METADATA.md`](../../DOCUMENT-METADATA.md). Structured status and provenance fields are authoritative; tags improve retrieval but do not promote research into the specification.

## Licensing

Research publications, repository editions, analyses, and research notes are documentation and are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0), consistent with [repository licensing](../../LICENSING.md).