---
title: UA Research Review Process
artifact_type: research-process
status: draft
created: 2026-07-24
updated: 2026-07-24
license: CC-BY-4.0
---

# UA Research Review Process

## Purpose

This process governs how published and unpublished research is introduced into the Uncertainty Architecture repository and how research findings may later influence the normative framework.

The goal is to prevent research ingestion, historical rewriting, methodological decisions, and repository restructuring from being mixed into one change.

## Core principles

### Planning before modification

Every repository change starts with analysis and an explicit scope. Implementation begins only after the proposed scope has been reviewed and approved.

### One logical change per pull request

Each pull request should be small enough to answer one coherent review question. A source-specific research pull request should not silently redesign unrelated doctrine, patterns, roles, or navigation.

### Research before methodology

A published statement is not automatically a framework requirement. Research is preserved, analyzed, compared with later work, and only then considered for normative adoption.

### Preserve intellectual history

Historical publications keep their original concepts and terminology. Current analysis may explain that a concept was refined, renamed, contradicted, or superseded, but the archived source is not rewritten to make the evolution disappear.

### Expose uncertainty and contradiction

The analysis should record weak evidence, over-strong claims, unresolved terminology, conflicting taxonomies, and later corrections. Editorial cleanup must not create false consensus.

## Standard source pull request

A pull request reviewing one research source should normally include three components.

### 1. Repository edition

A normalized archive, translation, consolidated edition, or research note.

It must identify:

- original title and author;
- publication date;
- canonical and additional URLs;
- source language;
- edition type;
- material transformations;
- applicable license.

Substantive arguments should be preserved. Platform-specific promotional material, duplicate biographies, broken links, and obvious formatting errors may be removed or corrected.

### 2. Research analysis

A separate companion document should evaluate:

- the question investigated;
- the scope and assumptions;
- key findings;
- contribution to UA;
- current relevance;
- later refinements;
- contradictions with prior or later work;
- terminology evolution;
- claims requiring softer formulation;
- candidate framework components;
- unresolved questions.

### 3. Traceability delta

The pull request updates the traceability matrix only with findings derived from that source.

Each entry identifies:

- the research finding;
- the source;
- the possible framework destination;
- current status;
- work needed before normative adoption.

## What a source pull request must not do

Unless explicitly scoped and approved, a source pull request must not:

- activate a new doctrine;
- declare a framework candidate normative;
- rename the main system category across the repository;
- introduce mandatory new job titles;
- move or delete existing framework sections;
- change repository-wide navigation;
- merge directly into `main`;
- merge its own pull request.

## Review questions

Each source pull request should answer:

1. What was the author actually investigating?
2. Which conclusions are still defensible?
3. Which conclusions were later refined or contradicted?
4. Which terms changed meaning over time?
5. Which numerical thresholds are examples rather than universal requirements?
6. What belongs in Doctrine, Lifecycle, Patterns, Operating Model, Reference Architectures, or Artifacts?
7. What should remain research context only?
8. What requires a separate RFC or methodology proposal?
9. Does the source add something genuinely new, or repeat an earlier claim in different language?
10. What would an SMB team need to see on the surface, and what should remain in technical depth?

## Transition from research to framework

The intended flow is:

```text
Research Source
→ Repository Edition
→ Research Analysis
→ Contradiction and Evolution Review
→ Framework Candidate
→ RFC or Methodology Proposal when required
→ Normative Framework
→ Practical Artifact or Reference Implementation
```

No step is automatic.

## Planned pull request sequence

### PR 0 — Research scaffolding

Defines the research index, review process, templates, status vocabulary, and initial traceability structure.

### Source review pull requests

One pull request per major article or synthesis source.

### Final research synthesis

Compares the complete track, identifies stable concepts and contradictions, and proposes the framework spine.

### Separate terminology review

Evaluates the move from historical terms such as Behavioral Software toward a possible Thinking Systems taxonomy, including its relationship to agentic systems.

### Separate methodology series

Only after research synthesis should the project formalize lifecycle, risk and tolerance models, control-loop design, Human-in-the-Loop, evaluation, canary validation, control economics, responsibilities, and repository navigation.

## Branch and merge policy

All changes are prepared on a dedicated branch and opened as a Draft Pull Request against `main`.

The project owner reviews the diff and performs the merge. Automated agents must not merge, delete the branch, force-push, or rewrite history without an explicit instruction.
