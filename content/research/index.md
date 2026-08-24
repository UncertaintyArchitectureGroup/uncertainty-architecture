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
updated: 2026-08-24
license: CC-BY-4.0
---

# Uncertainty Architecture Research Track

> **UA navigation**
>
> [UA Home](../../README.md) · [Specification](../../SPECIFICATION.md)
>
> **Lifecycle:** [Organization / boundaries](../../00-doctrine/nested-control-lifecycle.md#1-organizational-control-context) · [Project / architecture](../../01-patterns/project-control-architecture-and-viability-review.md) · [Delivery / release](../../01-patterns/thinking-system-review.md) · [Runtime / reassessment](../../00-doctrine/nested-control-lifecycle.md#4-runtime-operation-and-reassessment)
>
> **Explore:** [Doctrine](../../00-doctrine/) · [Patterns](../../01-patterns/) · [Control capabilities](../../02-ai-control-plane/) · [Reference architectures](../../03-reference-architectures/) · [Failure modes](../../04-failure-modes/) · [Research](index.md)

## Purpose

The Uncertainty Architecture (UA) Research Track preserves and reviews the work that led to the framework.

UA did not begin as a finished standard. It evolved through architectural, operational, governance, verification, and economic investigations. This section makes that evolution explicit and creates a controlled bridge from research to doctrine, patterns, control capabilities, reference architectures, failure modes, practical artifacts, and operating responsibilities.

## Canonical namespace

`content/research/` is the only active research namespace in the repository.

- completed or normalized publications belong in [`publications/`](publications/);
- bounded working briefs, source-intake records, observations, publication adaptations, and worked-application notes belong in [`notes/`](notes/);
- preserved unnormalized source snapshots belong in [`content/raw/`](../raw/);
- public milestones, talks, discussions, and superseded project-process records belong in [`content/history/`](../history/).

A new root-level `research/` directory should not be created.

## Normative boundary

Documents in this section are **research materials**. They are not automatically binding parts of the UA specification.

Research publications may contain early terminology, provisional role names, strong recommendations, illustrative numerical thresholds, assumptions later refined, or conclusions that conflict with later work.

A research conclusion becomes normative only after it is reviewed, translated into the appropriate framework component, and accepted through the UA contribution and change-control process.

## Content types

### Published research

Repository editions of publicly published articles. The substantive historical argument is preserved, while formatting, metadata, broken links, and platform-specific boilerplate may be normalized.

### Consolidated repository editions

Documents that combine overlapping public versions, translations, or technically richer variants. Every consolidation must explain its provenance and material transformations.

### Research analysis

Focused analysis of one or more sources that may record the research question, key findings, contributions to UA, later refinements, contradictions, terminology evolution, framework candidates, and unresolved questions.

### Research notes

Bounded working material derived from presentations, talks, working sessions, operational observations, external critique, worked applications, publication adaptations, emerging questions, or source-intake gaps.

See the [Research Notes index](notes/README.md).

### Framework traceability

A controlled map from research findings to current or possible Doctrine, Pattern, AI Control Plane, Reference Architecture, Failure Mode, practical Artifact, responsibility, process, or technical reference components.

## Review model

Research work uses a proportional review model rather than a mandatory source-by-source pipeline.

Depending on the question and impact, a change may contain one or more of:

1. a repository edition of a source;
2. a source-specific analysis;
3. a multi-source synthesis;
4. a terminology or contradiction review;
5. a traceability update;
6. a framework-candidate note;
7. a bounded publication adaptation, worked-application, or operational observation note.

Research changes do **not** automatically rewrite the framework. Normative changes are proposed separately after the relevant evidence has been synthesized and reviewed.

See [Research Review Process](review-process.md).

## Research-state reconciliation

Research is not a one-time phase that begins only after all framework concepts are merged. It operates as a feedback loop with specification work and practical application.

When a framework change, worked application, or classified material external review resolves, narrows, rejects, supersedes, or reopens a research question, update the affected source-intake note, working brief, analysis, or [`framework-traceability.md`](framework-traceability.md).

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
- [*Designing Non-Deterministic Systems*](notes/designing-nondeterministic-systems-source-intake.md) — the maintainer-supplied PDF export is the verified repository-review source and is preserved under [`content/raw/`](../raw/). An editable PPTX is not stored or independently verified. Slides 1–6 and a later bounded extraction of the controlled-object, process-shift, feedback, project-viability, and architectural-veto material have been translated through explicit framework review.

The presentation and publication corpus have now produced explicit framework decisions for:

- mixed Requirements, Operating Envelopes, Correctness, Bugs, and diagnostic sources;
- Input Interpretation, Decision Logic, and Output Mediation;
- Judgment Node boundaries;
- the delivery-level SMB Thinking System Review and template;
- placement-focused reference architectures;
- the controlled-object shift created when Consequential Runtime Responsibilities depend partly on probabilistic Model Judgment;
- UA as a control lifecycle that complements rather than replaces Agile, DevOps, QA, security, and incident response;
- organizational context, project authorization, delivery-level review, and runtime operation and reassessment as connected decision levels;
- architectural veto as a valid engineering outcome;
- the project-level [`Project Control Architecture and Viability Review`](../../01-patterns/project-control-architecture-and-viability-review.md) and its single living [`template`](../../01-patterns/project-control-architecture-and-viability-review-template.md);
- versioned project-baseline inheritance into the [`Thinking System Review`](../../01-patterns/thinking-system-review.md).

Those decisions and their source qualifications are recorded in [`framework-traceability.md`](framework-traceability.md). Unreviewed parts of the presentation and publications are not promoted by implication.

The project-level decision surface is now active at draft-framework level. The next research and application questions concern whether the connected project and delivery reviews are proportionate, understandable, non-duplicative, and economically useful in practice:

- which fields can be completed briefly for low-consequence SMB projects without hiding material risk;
- whether scenario-based risk mapping produces better control decisions than aggregate scoring;
- how teams estimate control build cost, recurring control cost, Human Authority capacity, and residual exposure with honest ranges;
- which project constraints and shared controls should be inherited directly by delivery-level Thinking System Reviews;
- which runtime findings require local correction versus project reauthorization;
- which failure modes become visible only when project and delivery reviews are applied together;
- where the required control perimeter makes the AI path structurally unattractive.

The next practical validation sequence is:

```text
Project Control Architecture and Viability Review
→ delivery-level Thinking System Review
→ runtime evidence
→ local reassessment or project reauthorization
```

This sequence should first be exercised through a two-level worked application and then through a real team or documented real system. Application evidence may refine the project review, delivery review, control-plane capability model, failure modes, or research questions.

The next major corpus task also remains a cross-publication synthesis that identifies stable concepts, refinements, contradictions, superseded claims, terminology requiring review, framework candidates, and material that should remain research context only.

Project-level validation, publication-feedback cycles, and corpus synthesis should proceed as a feedback loop rather than sequential phases.

Publication adaptations are deliberately treated as **distribution surfaces of the owning research**, not alternate conceptual authorities. The current Thinking Systems adaptation is therefore maintained by direct compression, omission, and reordering of the merged long-form Sections 1–4 wherever practical; claim-bearing paraphrases are treated as semantic-risk points rather than as harmless style changes.

## Research positioning, antecedents, and intellectual context

A substantive pre-publication review by **Maximiliano Armesto** reopened and sharpened several publication-facing questions. The current paper now states that the category predates LLMs while retaining LLM-based systems as its primary contemporary focus; separates category membership, consequence severity, and required control depth through an early low-consequence case; replaces the publication-facing **Linear Software** binary with descriptive language about explicitly authored consequential responsibilities; and acknowledges [STAMP/STPA](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf)'s existing hierarchical socio-technical control scope before testing any narrower four-horizon contribution. The review and reconciliation record is preserved in [`notes/thinking-systems-external-review-maximiliano-armesto.md`](notes/thinking-systems-external-review-maximiliano-armesto.md). These are research/editorial changes; the draft-normative glossary remains unchanged pending separate framework review.

UA is a synthesis and specification effort, not a claim that its underlying engineering primitives were invented here. UA also does not claim coinage of the phrase **Thinking Systems**; it defines a specific engineering category under that name. Current research should distinguish established foundations from UA-specific composition and should prefer primary sources when describing those foundations.

For the current Thinking Systems research line, the **maintainer-reported provenance** is that the formulation **“Thinking Systems”** entered the work through Vitalii Oborskyi's exchange with **Arkadiy Dobkin**, in the context of discussion prompted by Dobkin's public *From Fall to Rise* LinkedIn post. This is an author-attested record of dialogue provenance: the public post anchors the surrounding discussion context but is not presented as independent evidence that the phrase itself appeared in the post. The provenance concerns the formulation and research prompt, not authorship of the UA-specific definition, the Consequential Runtime Responsibility boundary, the control-capability model, or the resulting paper. Acknowledgment of the exchange does not imply Dobkin's endorsement or agreement with UA.

Relevant antecedents and adjacent traditions include:

- Nancy Leveson's [STAMP/STPA systems-theoretic safety work](https://mitpress.mit.edu/9780262016629/engineering-a-safer-world/), which applies systems thinking and systems theory to complex socio-technical safety problems;
- the Software Engineering Institute's [Simplex architecture](https://www.sei.cmu.edu/library/an-architectural-description-of-the-simplex-architecture/) for dependable and evolvable process-control systems;
- production-ML systems engineering such as Google's [Hidden Technical Debt in Machine Learning Systems](https://research.google/pubs/hidden-technical-debt-in-machine-learning-systems/), which treats production ML concerns as system-level engineering concerns rather than model behavior alone;
- the [NIST AI Risk Management Framework](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10), which is intended to help organizations operationalize risk management across the AI lifecycle.

These sources are **antecedents and comparison points, not endorsements, proofs, or exact equivalents of UA**. UA does not claim novelty for generic feedback loops, Constraints, Sensors, Controllers, Actuators, fallback, socio-technical control, or AI risk management as isolated ideas. The candidate contribution under validation is their recomposition around the Thinking System category and a connected engineering path from organizational authority through project / architecture viability and delivery release to runtime evidence, correction, and reassessment.

Additional software-engineering context should be kept visible rather than replaced by a stronger novelty claim. ISO/IEC TR 29119-11:2020 uses the category **AI-based system** for a system containing at least one AI component. Microsoft's ICSE 2019 case study documents process changes observed in teams building AI-based applications, and Martínez-Fernández et al.'s 2022 systematic mapping study synthesizes 248 studies on software engineering for AI-based systems. These sources support the existence of a substantial pre-UA engineering problem space; they do not provide the narrower Thinking-System responsibility boundary proposed here.

### Evidence maturity

UA is currently an **early-stage draft specification and systems-engineering hypothesis under validation**. Repository consistency, traceability, and external discussion are useful research controls, but they must not be presented as empirical validation of the framework. The next research priority is evidence: worked reference implementations, real project applications, recorded authorization/release/reassessment decisions, failure-and-correction traces, cross-project comparison, and explicit specification revisions when evidence contradicts current doctrine. New repository process or governance artifacts should be added only when they directly improve that evidence program or prevent a demonstrated consistency failure.

The intended synthesis corpus includes:

1. *Architecting Uncertainty: A Modern Guide to LLM-Based Software*;
2. *On-Device LLM or Cloud API?*;
3. *Uncertainty Architecture: A Modern Approach to Designing LLM Applications* together with its technically richer Ukrainian version;
4. *Uncertainty Architecture: Why AI Governance Is Actually Control Theory*;
5. *Beyond Embeddings: Neuro-Symbolic Verification of Semantic Drift in LLMs*;
6. the *Designing Non-Deterministic Systems* presentation as a synthesis source.

## Terminology decision

Current UA terminology uses **Thinking Systems** as defined in the [canonical glossary](../../00-doctrine/glossary.md#thinking-system): software systems in which one or more **Consequential Runtime Responsibilities** depend partly on probabilistic Model Judgment rather than being fully specified through explicitly encoded logic in advance. Category membership does not imply adequate control or production readiness.

Historical publications used **Behavioral Software** and **Behavioral Applications**. Current framework documents may identify the migration on first use, but should use **Thinking Systems** thereafter.

Fixed or dynamic orchestration does not determine the category. In publication-facing research, the opposite side of the boundary is described through consequential responsibilities that remain explicitly authored rather than through a required **Linear Software** binary label. Thinking-System classification depends on whether at least one Consequential Runtime Responsibility depends partly on probabilistic Model Judgment. The draft-normative glossary term remains unchanged until a separate terminology review decides whether the framework should retain, narrow, or replace it. Agentic terminology raises additional questions about autonomy and delegated authority and remains an open research topic rather than a synonym for Thinking Systems.

Historical publications and raw sources retain their original language for provenance.

## Metadata

Research documents should follow [`DOCUMENT-METADATA.md`](../../DOCUMENT-METADATA.md). Structured status and provenance fields are authoritative; tags improve retrieval but do not promote research into the specification.

## Licensing

Research publications, repository editions, analyses, and research notes are documentation and are licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0), consistent with [repository licensing](../../LICENSING.md).
