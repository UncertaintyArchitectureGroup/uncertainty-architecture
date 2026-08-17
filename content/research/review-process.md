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
updated: 2026-08-17
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

A proposal translating one or more research findings into a possible Doctrine, Pattern, AI Control Plane capability, Reference Architecture, Failure Mode, practical Artifact, responsibility bundle, process, or technical reference artifact.

### Lightweight research note

A bounded record derived from a talk, working session, operational observation, external critique, worked application, or emerging question when a full source review is unnecessary.

### Publication adaptation draft

A shorter publication-facing derivative of a larger living paper or synthesis, developed before or alongside completion of the long-form work so that external review can challenge the current argument while later sections remain revisable.

A publication adaptation is not a new authority-bearing source. It remains research and must identify the living manuscript or synthesis from which it is derived.

## Optional review artifacts

The following are available tools rather than mandatory components of every research change:

- repository edition;
- research analysis;
- traceability delta;
- contradiction review;
- terminology review;
- framework-candidate proposal;
- lightweight observation or worked-application note;
- publication adaptation draft.

Use the artifacts that make the reasoning visible and proportionate to the change.

## Research-to-framework transition

The typical flow is:

```text
Research Source, Observation, or Worked Application
→ Repository Edition or Research Note when useful
→ Analysis or Multi-Source Synthesis
→ Contradiction and Terminology Review when needed
→ Framework Candidate
→ Deliberate Normative Decision
→ Practical Artifact, Worked Example, or Reference Implementation
→ New Evidence and Reassessment
```

No step is automatic, and not every item requires every intermediate document. The flow is iterative: framework application may create new evidence that reopens, narrows, or resolves a research question.

## Publication adaptation and external-feedback cycle

A long-form paper does not need to be complete before a defensible subset of its argument is exposed to external review. When later sections depend on assumptions that external experts can meaningfully challenge, the repository may develop a bounded publication adaptation under `content/research/notes/` while the larger manuscript remains a living research artifact.

Use this sequence:

```text
living blueprint + long-form manuscript
→ choose a self-contained current argument
→ create a shorter adaptation with explicit derivation/provenance
→ review for claim equivalence, omissions, and maturity boundary
→ publish externally when ready
→ collect critique, substitutions, counterexamples, and provenance corrections
→ classify only material feedback as research evidence
→ reconcile material changes into the owning blueprint/manuscript or other research record
→ continue or revise the long-form work
→ preserve the externally published edition under content/research/publications/
```

The adaptation may reorder or compress prose for distribution, but it must not silently strengthen a claim, imply that unfinished sections were completed, or promote paper-only hypotheses into specification. A material correction discovered while preparing the adaptation belongs back in the owning research pair before release.

External feedback should be triaged by effect rather than prominence of the reviewer:

- **editorial/distribution feedback** may improve the adaptation without changing research state;
- **conceptual critique** may narrow, reopen, or reject a claim and must be reconciled with the owning research record;
- **substitution evidence** may show that an existing method, platform, standard, or internal process already carries a relationship more simply and should change the remaining comparison or contribution claim;
- **provenance correction** must be repaired wherever the affected attribution appears;
- **endorsement or disagreement alone** is not framework evidence.

Acknowledgments should identify the kind of contribution accurately. A person credited for a phrase, framing, question, challenge, or dialogue is not thereby a co-author or endorser. Where a phrase came into the research through a specific exchange, distinguish that provenance from the paper's later engineering definition or synthesis.

This cycle is intentionally compatible with open-source development: publication can become a review surface for the next research iteration instead of a ceremonial endpoint after every conclusion has already hardened.

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
| Evidence, critique, unresolved hypothesis, or worked-application observation | `content/research/` |
| Historical wording or chronology | `content/history/` |
| Original preserved source | `content/raw/` |

The glossary defines what a canonical term means. Doctrine explains the foundational model. A pattern explains how a team applies that model. A reference architecture shows one possible composition.

Do not move directly from source wording into normative specification. Do not duplicate full explanations across glossary, doctrine, patterns, and reference architectures. Do not dilute a clear operational procedure into abstract prose when a reusable executable pattern or artifact is the appropriate result.

When the source contains an operational procedure, preserve its executable structure through the appropriate combination of inputs, outputs, entry and exit criteria, evidence, decision rights, checklists, tables, and explicit outcomes such as pass, block, limit, escalate, revise, roll back, or stop.

Use Mermaid only when sequence, feedback, authority, state, ownership, or dependency structure is materially clearer as a diagram. The diagram and written rules must express the same model.

## Research-state reconciliation

A repository change requires research-state reconciliation when it does one or more of the following:

- registers or materially reinterprets a source;
- resolves, narrows, rejects, supersedes, or reopens an explicit research question;
- promotes a research candidate into doctrine, a pattern, a control capability, a failure mode, an artifact, or a reference architecture;
- produces material evidence from a worked application, incident, operational observation, or reference implementation;
- changes the relationship between an existing source and the current framework.

When a trigger applies, review and update only the records whose state actually changed:

1. the owning source-intake, analysis, synthesis, or research note;
2. [`framework-traceability.md`](framework-traceability.md) when the decision needs an auditable source-to-framework link;
3. open questions, maturity, or translation status in affected briefs and working notes;
4. [`index.md`](index.md) or a local research index when the current research direction or navigation materially changes;
5. [`CHANGELOG.md`](../../CHANGELOG.md) for notable repository or specification-artifact effects.

Research records should capture meaningful state transitions, for example:

```text
Question open
→ evidence reviewed
→ candidate formulated
→ accepted, narrowed, rejected, or deferred
→ framework destination recorded
→ remaining uncertainty stated
```

Do not use the Research Track as a session log or duplicate pull-request history. Routine edits that do not change research state require no research record update. Do not create a second traceability ledger.

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
- publication adaptations derived from active long-form research when external review is intended to influence remaining sections;
- normative or high-impact changes;
- externally contributed work;
- automation-generated changes;
- multi-file restructuring;
- changes requiring subject-matter review.

Draft pull requests are optional. Minor maintainer-authored editorial, metadata, navigation, roadmap, or changelog updates may be committed directly.

The project owner retains final merge authority.

## Current research direction

The historical repository editions are preserved under `content/research/publications/`. The slides 1–6 transfer from *Designing Non-Deterministic Systems* has been translated into current draft framework components and recorded in source intake and traceability.

The next major corpus task is a cross-publication synthesis identifying:

- concepts that remained stable;
- concepts that were refined or superseded;
- unresolved contradictions;
- terminology requiring separate review;
- candidates for the framework spine;
- material that should remain research context only.

This synthesis should proceed alongside worked applications of the current framework rather than wait for every concept to be completed. Worked Thinking System Reviews, operational observations, incidents, publication-feedback cases, and reference implementations may produce evidence that refines the research questions and the practical artifact.

Source-specific analysis may still be added where it produces useful evidence or resolves a concrete question.

Metadata for new research process and analysis documents should follow [`DOCUMENT-METADATA.md`](../../DOCUMENT-METADATA.md).
