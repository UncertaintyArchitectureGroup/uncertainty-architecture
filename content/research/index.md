---
title: Uncertainty Architecture Research Track
artifact_type: research-index
status: draft
created: 2026-07-24
updated: 2026-07-24
license: CC-BY-4.0
---

# Uncertainty Architecture Research Track

## Purpose

The Uncertainty Architecture (UA) Research Track preserves and reviews the work that led to the framework.

UA did not begin as a finished standard. It evolved through a sequence of architectural, operational, governance, verification, and economic investigations. This section makes that evolution explicit and creates a controlled bridge from research to future doctrine, methodology, patterns, operating-model responsibilities, and practical artifacts.

## Normative boundary

Documents in this section are **research materials**. They are not automatically binding parts of the UA specification.

Research publications may contain:

- early terminology;
- provisional role names;
- strong recommendations;
- illustrative numerical thresholds;
- assumptions that were later refined;
- conclusions that conflict with later work.

A research conclusion becomes normative only after it is reviewed, translated into the appropriate framework component, and accepted through the UA governance process.

## Content types

### Published research

Repository editions of publicly published articles. The substantive historical argument is preserved, while formatting, metadata, broken links, and platform-specific boilerplate may be normalized.

### Consolidated repository editions

Documents that combine overlapping public versions, translations, or technically richer variants. Every consolidation must explain its provenance and material transformations.

### Research analysis

A companion analysis for each source that records:

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

Structured synthesis derived from presentations, talks, working material, or later analysis when no directly published article should be archived.

### Framework traceability

A controlled map from research findings to possible future Doctrine, Lifecycle, Pattern, Operating Model, Reference Architecture, or Artifact components.

## Review model

Each major research source is reviewed in a separate pull request.

A source pull request should normally contain:

1. a repository edition of the source;
2. a separate research analysis;
3. the source-specific delta to the traceability matrix.

A source pull request does **not** automatically rewrite the methodology. Normative changes are proposed only after the research series has been reviewed and synthesized.

See [Research Review Process](review-process.md).

## Review templates

- [Research Publication Record Template](publication-record-template.md)
- [Research Analysis Template](research-analysis-template.md)

The templates are marked as drafts so they remain repository assets without being published as normal site content.

## Status vocabulary

- **Research Finding** — a conclusion preserved from a source.
- **Candidate** — potentially suitable for a future framework component.
- **Needs Resolution** — terminology, scope, evidence, or conflict must be resolved first.
- **Proposed for RFC** — mature enough for a separate formal proposal.
- **Active** — accepted into the normative framework.
- **Superseded** — replaced by a later formulation.
- **Rejected** — considered and intentionally not adopted.

See [Research-to-Framework Traceability](framework-traceability.md).

## Planned research series

The initial sequence is expected to review:

1. *Architecting Uncertainty: A Modern Guide to LLM-Based Software*;
2. *On-Device LLM or Cloud API?*;
3. *Uncertainty Architecture: A Modern Approach to Designing LLM Applications* together with its technically richer Ukrainian version;
4. *Uncertainty Architecture: Why AI Governance Is Actually Control Theory*;
5. *Beyond Embeddings: Neuro-Symbolic Verification of Semantic Drift in LLMs*;
6. the *Designing Non-Deterministic Systems* presentation as a research synthesis.

A final synthesis pull request will compare the full track, identify stable concepts and contradictions, and propose the framework spine for separate review.

## Terminology under review

Historical publications use terms such as **Behavioral Software** and **Behavioral Applications**.

The current research direction is considering **Thinking Systems** as a clearer user-facing category for software that delegates part of runtime interpretation, judgment, planning, or decision-making to probabilistic models. Agentic systems may be treated as a higher-autonomy subset rather than as a synonym.

This terminology is **not adopted by this research scaffolding**. It requires a separate terminology review after the relevant sources have been analyzed. Historical publications will retain their original language.

## Licensing

Research publications, repository editions, analyses, and research notes are documentation and are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0), consistent with [repository licensing](../../LICENSING.md).
