---
title: Research-to-Framework Traceability
artifact_type: research-traceability
status: research
maturity: active
module: research
topics:
  - provenance
  - thinking-systems
  - repository-architecture
tags:
  - ua/module/research
  - ua/type/research-traceability
  - ua/status/research
  - ua/topic/provenance
created: 2026-07-24
updated: 2026-07-30
license: CC-BY-4.0
---

# Research-to-Framework Traceability

## Purpose

This document records how UA research influences framework components without treating every historical statement as an approved requirement.

It prevents two opposite errors:

1. building methodology without preserving the research and reasoning behind it;
2. treating every statement from an article, talk, or working note as if it were already normative.

Traceability is a synthesis aid, not a mandatory ledger for every source or sentence.

This matrix is the canonical repository record for material source-to-framework decisions. Do not create a parallel crystallization ledger elsewhere; detailed argument belongs in supporting analysis, synthesis, or source-intake notes.

## Status vocabulary

- **Research Finding** — a conclusion preserved from research material.
- **Candidate** — potentially suitable for translation into a framework component.
- **Needs Resolution** — terminology, evidence, scope, or contradiction must be resolved first.
- **Proposed for Framework Review** — mature enough for a separate, deliberate normative proposal and visible review.
- **Active** — accepted into the current framework boundary, subject to the status of the owning document.
- **Superseded** — replaced by a later formulation.
- **Rejected** — considered and intentionally not adopted.

## Candidate framework areas

Traceability entries may point toward:

- **Doctrine** — foundational concepts and distinctions;
- **Pattern** — repeatable technical or socio-technical solution;
- **Operating Model** — decision rights, responsibilities, reviews, and escalation;
- **Reference Architecture** — concrete composition of multiple patterns;
- **Artifact** — canvas, checklist, registry, evidence record, risk map, or other reusable tool;
- **Failure Mode** — recurring mechanism of technical, semantic, operational, or organizational failure.

Lifecycle concerns may be represented across these areas rather than maintained as a separate top-level specification module unless the framework later adopts one explicitly.

## Traceability matrix

The historical publication corpus is preserved, while corpus-level synthesis remains in progress. The entries below record the completed slides 1–6 transfer from the original *Designing Non-Deterministic Systems* PPTX into current UA framework material.

| Research finding or source claim | Source or synthesis | Framework area | Status | Current framework decision |
|---|---|---|---|---|
| Model-mediated runtime behavior has non-zero variance, so system design must distinguish deterministic responsibilities, model-mediated responsibilities, and the boundaries and controls between them. | Original *Designing Non-Deterministic Systems* PPTX, slides 1–6 transfer scope, refined through framework review | Doctrine | Active | Thinking Systems are mixed systems; deterministic obligations remain explicit while Model Judgment is bounded and evaluated through system-level Requirements. |
| Correctness cannot always be represented by one exact output, and requirements must define acceptable operating space. | Original PPTX, requirement and tolerance material, refined through framework review | Doctrine and glossary | Active | A Requirement is the approved operating contract; the Operating Envelope is one part of it; Correctness is satisfaction of the Requirement. |
| A stochastic defect should be reasoned about through business tolerances and observed behavior rather than code-path failure alone. | Original PPTX bug material, refined through framework review | Doctrine and glossary | Active | A Bug is a system-level Requirement violation. A tail event, metric change, or Deviation Signal is evidence until diagnosis establishes the violation and its source. |
| Model Judgment creates value in input interpretation, dynamic decision logic, and contextual output. | Original PPTX architectural-space material, refined into current terminology | Doctrine | Active | Input Interpretation, Decision Logic, and Output Mediation are functional placement classes, not a mandatory three-stage pipeline. |
| Consequential Model Judgment requires an explicit boundary around purpose, context, authority, deterministic constraints, evidence, failure handling, and ownership. | Presentation control framing plus framework synthesis | Pattern | Active | The Judgment Node Boundary pattern provides proportional minimal and extended boundary modes without requiring a separate node registry. |
| Readiness, resource cost, completion evidence, and release authorization must change together when Model Judgment affects consequential behavior. | Original PPTX development-contract material, narrowed through framework review | Pattern and artifact | Active | The Thinking System Review owns full model-mediated DoR and DoD extensions, keeps the Release Gate distinct, uses responsibility bundles rather than job titles, and records the decision in one living template. |
| Placement classes should be demonstrable in isolated and composite systems without becoming a required topology. | Placement doctrine plus slides 1–6 transfer synthesis | Reference Architecture | Active | `03-reference-architectures/judgment-placement-examples.md` shows four non-prescriptive compositions and links back to canonical doctrine and patterns. |

## Conflict and evolution register

This section records cross-source issues that required an explicit resolution rather than silent editorial normalization.

| Topic | Earlier or presentation formulation | Current UA formulation | Current status | Resolution |
|---|---|---|---|---|
| Primary system category | Behavioral Software / Behavioral Applications | Thinking Systems | Active | Use Thinking Systems in current framework documents; preserve legacy wording in historical sources and provenance records. |
| Bug under stochastic business logic | A bug is a statistical excursion beyond approved business tolerances | A Bug is a violation of an approved Requirement; a statistically evidenced tolerance excursion may establish that violation when the tolerance is part of the Requirement | Active | Event, evidence, diagnosis, accepted residual behavior, and system responsibility remain separate. |
| Requirement versus tolerance envelope | Requirement is the safe probabilistic operating area | The Operating Envelope is part of a broader Requirement | Active | Preserve intended outcome, deterministic obligations, authority, evidence expectations, resource constraints, and failure handling outside the envelope concept. |
| Statistical quality contract | Large-sample runs, fixed metrics, and confidence intervals prove readiness or completion | Evidence method and adequacy are derived from the Requirement and decision context | Active | No universal sample size, metric, confidence method, or threshold is adopted. Deterministic and behavioral evidence coexist. |
| Three connected AI planes | Intent UX → Cognitive Logic → Contextual Output | Input Interpretation, Decision Logic, and Output Mediation as optional, repeatable, combinable functions | Active | Treat the deck composition as illustrative rather than a mandatory pipeline. |
| Specialized role framing | PM, architect, QA, or other specialist titles own parts of the loop | Implementation, evaluation, operation, and release decision authority are responsibility bundles | Active | Small teams may combine responsibilities; consequential decision authority remains explicit. |
| Operational records | Separate readiness, completion, risk, role, and release artifacts | One living Thinking System Review plus versioned snapshots | Active | Additional records are optional only where independent ownership or lifecycle genuinely requires them. |

## Remaining topics for synthesis

Topics still expected to require further review include:

- the relationship between Thinking Systems and agentic systems at different autonomy levels;
- Model Control Plane terminology versus Model Context Protocol acronym conflict;
- AI Control Plane as capability model versus possible platform implementations;
- actuators versus constraints as separate control categories;
- automated controller logic versus the socio-technical controller;
- risk and tolerance mapping;
- control-economics and architectural-veto guidance;
- failure-mode taxonomy and the evidence needed to distinguish drift, defects, attacks, and invalid Requirements.

## Update rule

A research change may add findings and conflicts supported by a single source, multiple sources, a research note, or an explicit synthesis.

Entries should remain concise and decision-oriented. Detailed argument belongs in supporting analysis or synthesis documents.

Repository-wide terminology or methodology changes require separate deliberate framework review. A traceability entry alone does not activate a normative requirement.

Metadata and tags follow [`DOCUMENT-METADATA.md`](../../DOCUMENT-METADATA.md).
