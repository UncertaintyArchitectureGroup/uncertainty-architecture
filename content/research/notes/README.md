---
title: UA Research Notes
artifact_type: research-index
status: research
maturity: active
module: research
topics:
  - provenance
  - repository-architecture
tags:
  - ua/module/research
  - ua/type/research-index
  - ua/status/research
  - ua/topic/provenance
updated: 2026-08-25
license: CC-BY-4.0
---

# UA Research Notes

This directory contains bounded working notes, source-intake records, operational observations, worked-application notes, research briefs, external-review/provenance records, and publication adaptation drafts that may inform later analysis, synthesis, framework proposals, or external review.

Research notes are **non-normative**. A note may describe a question, planned investigation, operational observation, source-intake gap, completed translation state, incomplete line of inquiry, external critique, dialogue provenance, or a publication-facing adaptation of a larger living manuscript. Its presence does not establish evidence, consensus, endorsement, or a specification requirement.

The notes migrated here from the former root-level `research/` directory are planning briefs rather than completed research outputs. They are retained for traceability and should be expanded, narrowed, superseded, or closed explicitly if their research state changes.

A publication adaptation draft also remains a research note until it is actually published. It may compress or reorder a bounded argument from a larger living paper, but must identify its derivation and must not silently become a second canonical source for framework meaning. After external publication, preserve the resulting **content edition** under [`../publications/`](../publications/) immediately, before feedback-driven reconciliation. Equivalent Medium, LinkedIn, website, or other platform copies may be recorded as renditions of that same content edition; platform-only formatting or image substitutions do not require separate repository editions unless the substantive text materially diverges.

Material terms, hypotheses, comparison questions, candidate artifacts/processes, and externally introduced research items that remain in play should also be represented in the canonical [`Research State Register`](../research-register.md). A detailed note owns the reasoning and provenance; the register owns the cross-document item identity and current research status; [`framework-traceability.md`](../framework-traceability.md) remains the source-to-framework decision ledger.

## Notes

- [`ai-delivery-lifecycle.md`](ai-delivery-lifecycle.md) — an early lifecycle hypothesis reclassified from doctrine. Its main project and delivery questions are now translated into the Project Control Architecture and Viability Review and the Thinking System Review. Remaining questions concern proportionality, two-level inheritance, control economics, evidence methods, incident learning, reauthorization, and real-team validation.
- [`control-theory-brief.md`](control-theory-brief.md) — planning brief for research beyond the basic control-loop mapping already active in UA, including stability, feedback adequacy, latency, and limits of control-theory transfer.
- [`designing-nondeterministic-systems-source-intake.md`](designing-nondeterministic-systems-source-intake.md) — provenance and framework-transfer record for the maintainer-supplied PDF export. The repository does not currently preserve or independently verify an editable PPTX; presentation content remains research evidence rather than specification authority. During consolidation of the article plan, two concerns from the former operational-extension note that were only partially represented—active behavioral/control baseline reconstructability and explicit fallback/common-mode/capacity/restoration evidence—were transferred into the living blueprint/manuscript. The intermediary note was then removed as redundant; Git history preserves it.
- [`metrics-brief.md`](metrics-brief.md) — planning brief for decision-useful evidence, misleading metrics, sampling, drift signals, and context-derived thresholds.
- [`on-device-cloud-source-intake.md`](on-device-cloud-source-intake.md) — traceability record for a full author-provided source that remains pending raw preservation and normalization.
- [`open-engineering-specification-article-blueprint.md`](open-engineering-specification-article-blueprint.md) — active living editorial contract for the long-form public synthesis paper. It preserves the complete argument, section responsibilities, running-example contract, figure plan, source plan, maturity boundaries, and unresolved editorial decisions while remaining non-normative research material.
- [`open-engineering-specification-article-draft.md`](open-engineering-specification-article-draft.md) — active long-form target manuscript governed by the blueprint. The current merged paper establishes the core argument through Article §4 while later research remains intentionally open; Draft PRs may continue the long-form work independently of publication adaptations.
- [`thinking-systems-formulation-provenance-arkadiy-dobkin.md`](thinking-systems-formulation-provenance-arkadiy-dobkin.md) — maintainer-attested provenance record for the formulation **Thinking Systems** entering the research through Vitalii Oborskyi's exchange with Arkadiy Dobkin following discussion around Dobkin's public *From Fall to Rise* post. It separates phrase provenance from the later UA definition, authorship, endorsement, and framework authority.
- [`thinking-systems-pre-publication-review-maximiliano-armesto.md`](thinking-systems-pre-publication-review-maximiliano-armesto.md) — material external-review record for Maximiliano Armesto's pre-publication critique of the standalone Thinking Systems draft. It records the terminology, pre-LLM scope, proportionality, and STAMP/STPA findings, their dispositions, and the questions that remain unresolved without publishing private correspondence verbatim.
- [`thinking-systems-release-contract-scope-review.md`](thinking-systems-release-contract-scope-review.md) — internal consistency review that reopens whether the current technology-neutral Thinking-System wording coheres with the paper's release-contract thesis across fixed learned probabilistic functions and runtime judgment processes; it tracks `TS-SCOPE-001` without treating the issue as external evidence.
- [`thinking-systems-publication-draft.md`](thinking-systems-publication-draft.md) — publication-facing adaptation titled *Uncertainty Architecture: Thinking Systems — When the Controlled Object Changes*. It preserves the category and controlled-object deduction from the long-form §§1–2, follows the manuscript's closed-loop → complete bounded-control figure sequence through Figures 6–7, and aligns publication Figure 8 with the manuscript's orthogonal model: assessment eligibility, Project-owned technical selection and category confirmation, category exit, specific research/business authorization, scoped research-only or production-capable Project Authorization, reassessment routing, and the independent capability-family axis remain visible while later operating detail stays compressed. It is intended to expose that argument to external criticism before the larger paper is completed.
- [`reference-implementations-brief.md`](reference-implementations-brief.md) — planning brief for implementation evidence, two-level worked applications, and architectural examples that can test current UA doctrine and patterns.

Completed publications and repository editions belong in [`../publications/`](../publications/). Research process, the active research register, and source-to-framework traceability documents remain in the parent [`content/research/`](../) namespace.

New notes should use `status: research`, an explicit `maturity`, and the conventions in [`DOCUMENT-METADATA.md`](../../../DOCUMENT-METADATA.md).

Publication adaptations should additionally identify their derivation, preserve material attribution/provenance, and follow the publication-adaptation cycle in [`../review-process.md`](../review-process.md) with contributor execution guidance in [`../AGENTS.md`](../AGENTS.md).

When a framework PR, worked application, material external review, dialogue, or new source changes the state of a material research item, reconcile the owning note, the [`Research State Register`](../research-register.md), and—only when the source-to-framework relationship materially changes—[`framework-traceability.md`](../framework-traceability.md). Do not use this directory as a session log or duplicate pull-request history.
