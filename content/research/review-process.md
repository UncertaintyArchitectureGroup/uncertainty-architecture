---
title: UA Research Review Process
artifact_type: research-process
status: informative
maturity: active
module: research
topics:
  - provenance
  - repository-architecture
tags:
  - ua/module/research
  - ua/type/research-process
  - ua/status/informative
  - ua/topic/provenance
created: 2026-07-24
updated: 2026-07-30
license: CC-BY-4.0
---

# UA Research Review Process

## Purpose

This process explains how published and unpublished research enters the Uncertainty Architecture repository and how research may later influence the normative framework.

Its purpose is to preserve intellectual history, expose uncertainty and contradiction, and prevent research material from silently becoming methodology. It is not intended to impose heavyweight ceremony on routine maintainer work.

## Core principles

### Research is not automatically normative

A published statement, presentation claim, working note, or historical recommendation is not automatically a framework requirement. Research is preserved and interpreted before any deliberate normative adoption.

### Preserve intellectual history

Historical publications keep their original concepts and terminology. Repository editions may normalize formatting, metadata, links, and obvious copy errors, but they must not rewrite the past to make later evolution disappear.

### Expose uncertainty and contradiction

Research work should identify weak evidence, over-strong claims, unresolved terminology, conflicting taxonomies, later corrections, and limits of applicability. Editorial cleanup must not create false consensus.

### Use proportional process

The amount of process should match the risk and impact of the change. A typo fix, metadata update, or lightweight research note does not need the same workflow as a normative doctrine change.

### Human control over automated changes

Automated agents may prepare and validate changes, but they must not merge, force-push, delete branches, rewrite history, or make unscoped normative decisions without explicit human instruction.

Automated tools should follow the repository map and editing invariants in [`AGENTS.md`](../../AGENTS.md).

## Supported research work types

Research may be added or developed as any of the following:

### Repository edition

A normalized archive, translation, consolidated edition, or research note preserving a source for future use.

Where available, it should identify:

- original title and author;
- publication date;
- canonical and additional URLs;
- source language;
- edition type;
- material transformations;
- applicable license.

### Source-specific analysis

A focused analysis of one source, including its question, assumptions, findings, current relevance, later refinements, contradictions, terminology evolution, and possible contribution to UA.

### Multi-source synthesis

A comparison across several publications, talks, or research notes intended to identify stable concepts, changes in position, contradictions, and the emerging framework spine.

### Terminology or contradiction review

A focused document that resolves, narrows, or records disagreement around terminology, taxonomies, thresholds, or competing claims.

### Framework-candidate note

A proposal translating one or more research findings into a possible Doctrine, Pattern, Operating Model, Reference Architecture, Failure Mode, or practical artifact.

### Lightweight research note

A bounded record derived from a talk, working session, operational observation, external critique, or emerging question when a full source review is unnecessary.

## Optional review artifacts

The following are available tools rather than mandatory components of every research change:

- repository edition;
- research analysis;
- traceability delta;
- contradiction review;
- terminology review;
- framework-candidate proposal.

Use the artifacts that make the reasoning visible and proportionate to the change.

## Research-to-framework transition

The typical flow is:

```text
Research Source or Observation
→ Repository Edition or Research Note when useful
→ Analysis or Multi-Source Synthesis
→ Contradiction and Terminology Review when needed
→ Framework Candidate
→ Deliberate Normative Decision
→ Practical Artifact or Reference Implementation
```

No step is automatic, and not every item requires every intermediate document.

## Source extraction and framework crystallization

When a source may change doctrine, patterns, control capabilities, reference architectures, failure modes, or reusable artifacts, perform an explicit crystallization pass before editing the specification.

1. Preserve or register the source.
2. Extract distinct candidate items rather than treating an article, slide, table, or diagram as one indivisible contribution.
3. Classify each item as a term, doctrine-level distinction, pattern, artifact, control capability, evidence, example, responsibility, process, failure mode, reference-architecture element, or project-specific threshold.
4. Check whether the item already has a canonical owner and whether the proposed wording is stronger than the evidence supports.
5. Decide whether the item is retained, narrowed, generalized, split, rejected, or deferred.
6. Place accepted items in their owning module and replace duplicate explanations with cross-references.
7. Update [`framework-traceability.md`](framework-traceability.md) when the decision is material enough to require an auditable research-to-framework link.

Use this default ownership rule:

| Content | Canonical owner |
|---|---|
| Canonical term or concise meaning | `00-doctrine/glossary.md` |
| Foundational distinction or invariant | `00-doctrine/` |
| Reusable operational response, checklist, or gate | `01-patterns/` |
| Control capability | `02-ai-control-plane/` |
| Concrete composition | `03-reference-architectures/` |
| Reusable mechanism of loss of control | `04-failure-modes/` |
| Evidence, critique, or unresolved hypothesis | `content/research/` |
| Historical wording or chronology | `content/history/` |
| Original preserved source | `content/raw/` |

The glossary defines what a canonical term means. Doctrine explains the foundational model. A pattern explains how a team applies that model. A reference architecture shows one possible composition.

Do not move directly from source wording into normative specification. Do not duplicate full explanations across glossary, doctrine, patterns, and reference architectures. Do not dilute a clear operational procedure into abstract prose when a reusable executable pattern or artifact is the appropriate result.

When the source contains an operational procedure, preserve its executable structure through the appropriate combination of inputs, outputs, entry and exit criteria, evidence, decision rights, checklists, tables, and explicit outcomes such as pass, block, limit, escalate, revise, roll back, or stop.

Use Mermaid only when sequence, feedback, authority, state, ownership, or dependency structure is materially clearer as a diagram. The diagram and written rules must express the same model.

## Changes requiring deliberate framework review

A research change should receive explicit review before it:

- activates or materially modifies doctrine;
- declares a framework candidate normative;
- renames a core system category across the repository;
- introduces mandatory job titles, gates, controls, or processes;
- changes major repository-wide navigation or structure;
- turns illustrative thresholds into universal requirements;
- materially changes attributed work by another contributor.

These changes should normally use a dedicated branch and pull request so the full diff and rationale are visible.

## Practical branch and pull-request guidance

One logical change per pull request remains a useful default for substantial work. It is not an absolute rule for every maintainer edit.

Dedicated branches and pull requests are recommended for:

- major research synthesis;
- normative or high-impact changes;
- externally contributed work;
- automation-generated changes;
- multi-file restructuring;
- changes requiring subject-matter review.

Draft pull requests are optional. Minor maintainer-authored editorial, metadata, navigation, roadmap, or changelog updates may be committed directly.

The project owner retains final merge authority.

## Current research direction

The historical repository editions are now preserved under `content/research/publications/`. The next major research task is a cross-publication synthesis identifying:

- concepts that remained stable;
- concepts that were refined or superseded;
- unresolved contradictions;
- terminology requiring separate review;
- candidates for the framework spine;
- material that should remain research context only.

Source-specific analysis may still be added where it produces useful evidence or resolves a concrete question.

Metadata for new research process and analysis documents should follow [`DOCUMENT-METADATA.md`](../../DOCUMENT-METADATA.md).
