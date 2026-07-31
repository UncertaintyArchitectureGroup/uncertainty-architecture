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
updated: 2026-07-31
license: CC-BY-4.0
---

# Uncertainty Architecture Research Track

## Purpose

The Uncertainty Architecture (UA) Research Track preserves and reviews the work that led to the framework.

UA did not begin as a finished standard. It evolved through architectural, operational, governance, verification, and economic investigations. This section makes that evolution explicit and creates a controlled bridge from research to future doctrine, patterns, control capabilities, reference architectures, failure modes, practical artifacts, and operating responsibilities.

## Canonical namespace

`content/research/` is the only active research namespace in the repository.

- completed or normalized publications belong in [`publications/`](publications/);
- bounded working briefs, source-intake records, observations, and worked-application notes belong in [`notes/`](notes/);
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

Bounded working material derived from presentations, talks, working sessions, operational observations, external critique, worked applications, emerging questions, or source-intake gaps. A planning brief or intake record is not completed evidence and should state its maturity explicitly.

See the [Research Notes index](notes/README.md).

### Framework traceability

A controlled map from research findings to current or possible Doctrine, Pattern, AI Control Plane, Reference Architecture, Failure Mode, practical Artifact, responsibility, process, or technical reference components.

## Review model

Research work uses a proportional review model rather than a mandatory source-by-source pipeline.

Depending on the question and impact, a change may contain one or more of the following:

1. a repository edition of a source;
2. a source-specific analysis;
3. a multi-source synthesis;
4. a terminology or contradiction review;
5. a traceability update;
6. a framework-candidate note;
7. a bounded worked-application or operational observation note.

One logical change per pull request remains a useful default for substantial work, but every source does not require its own pull request or a fixed package of artifacts.

Research changes do **not** automatically rewrite the framework. Normative changes are proposed separately after the relevant evidence has been synthesized and reviewed.

See [Research Review Process](review-process.md).

## Research-state reconciliation

Research is not a one-time phase that begins only after all framework concepts are merged. It operates as a feedback loop with specification work and practical application.

When a framework change or worked application resolves, narrows, rejects, supersedes, or reopens a research question, update the affected source-intake note, working brief, analysis, or [`framework-traceability.md`](framework-traceability.md) as described in the [Research Review Process](review-process.md).

Do not record every editing session. Research records should capture meaningful changes in evidence, interpretation, question state, or framework destination.

## Review templates

- [Research Publication Record Template](publication-record-template.md)
- [Research Analysis Template](research-analysis-template.md)

These templates are optional working tools. Their Quartz `draft: true` field controls publishing visibility; it is not the UA document status.

## Status vocabulary

- **Research Finding** — a conclusion preserved from research material.
- **Candidate** — potentially suitable for translation into a framework component.
- **Needs Resolution** — terminology, scope, evidence, or conflict must be resolved first.
- **Proposed for Framework Review** — mature enough for a separate, deliberate normative proposal and visible review.
- **Active** — accepted into the current framework boundary, subject to the status of the owning document.
- **Superseded** — replaced by a later formulation.
- **Rejected** — considered and intentionally not adopted.

See [Research-to-Framework Traceability](framework-traceability.md).

## Current research direction

Five normalized publication editions are preserved under [`publications/`](publications/). Earlier root-level planning briefs are classified under [`notes/`](notes/) and remain research tasks rather than completed findings.

Two additional synthesis sources are tracked:

- [*On-Device LLM or Cloud API?*](notes/on-device-cloud-source-intake.md) — full author-provided Markdown source available; raw preservation and normalization remain pending;
- [*Designing Non-Deterministic Systems*](notes/designing-nondeterministic-systems-source-intake.md) — the maintainer-supplied original PPTX is the slide-level working source, while a PDF export is preserved under [`content/raw/`](../raw/). Slides 1–6 have been translated into current draft framework components; a complete Markdown transcript or normalized repository edition remains optional future work.

The slides 1–6 transfer produced explicit framework decisions for:

- mixed Requirements, Operating Envelopes, Correctness, Bugs, and diagnostic sources;
- Input Interpretation, Decision Logic, and Output Mediation;
- Judgment Node boundaries;
- the SMB Thinking System Review and template;
- placement-focused reference architectures.

Those decisions and presentation simplifications are recorded in [`framework-traceability.md`](framework-traceability.md). The rest of the deck is not promoted by implication.

The next major corpus task is a cross-publication synthesis that identifies:

- concepts that remained stable;
- concepts that were refined or superseded;
- unresolved contradictions;
- terminology requiring separate review;
- candidates for the framework spine;
- material that should remain research context only.

This synthesis should proceed alongside worked Thinking System Reviews and other practical applications. Application evidence may refine the review template, expose missing failure modes, or create more precise questions about risk, tolerance, control economics, and adoption.

Source-specific analysis may still be added when it contributes evidence, clarifies provenance, or resolves a concrete question. It is not a prerequisite for beginning corpus-level synthesis or practical validation.

The intended synthesis corpus includes:

1. *Architecting Uncertainty: A Modern Guide to LLM-Based Software*;
2. *On-Device LLM or Cloud API?*;
3. *Uncertainty Architecture: A Modern Approach to Designing LLM Applications* together with its technically richer Ukrainian version;
4. *Uncertainty Architecture: Why AI Governance Is Actually Control Theory*;
5. *Beyond Embeddings: Neuro-Symbolic Verification of Semantic Drift in LLMs*;
6. the *Designing Non-Deterministic Systems* presentation as a synthesis source.

## Terminology decision

Current UA terminology uses **Thinking Systems** for software that delegates part of runtime interpretation, judgment, planning, or decision-making to probabilistic models while retaining explicit deterministic boundaries and control responsibilities.

Historical publications used **Behavioral Software** and **Behavioral Applications**. Current framework documents may identify the migration on first use as **Thinking Systems** (previously described as **Behavioral Software** or **Behavioral Applications**), but should use **Thinking Systems** thereafter.

Agentic systems are treated as a higher-autonomy subset of Thinking Systems rather than as a synonym for the whole category.

Historical publications and raw sources retain their original language for provenance. Repository editions should include a terminology note when the legacy category is material to the text.

## Metadata

Research documents should follow [`DOCUMENT-METADATA.md`](../../DOCUMENT-METADATA.md). Structured status and provenance fields are authoritative; tags improve retrieval but do not promote research into the specification.

## Licensing

Research publications, repository editions, analyses, and research notes are documentation and are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0), consistent with [repository licensing](../../LICENSING.md).
