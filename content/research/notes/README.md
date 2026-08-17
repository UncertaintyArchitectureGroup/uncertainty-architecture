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
updated: 2026-08-17
license: CC-BY-4.0
---

# UA Research Notes

This directory contains bounded working notes, source-intake records, operational observations, worked-application notes, research briefs, and publication adaptation drafts that may inform later analysis, synthesis, framework proposals, or external review.

Research notes are **non-normative**. A note may describe a question, planned investigation, operational observation, source-intake gap, completed translation state, incomplete line of inquiry, or a publication-facing adaptation of a larger living manuscript. Its presence does not establish evidence, consensus, or a specification requirement.

The notes migrated here from the former root-level `research/` directory are planning briefs rather than completed research outputs. They are retained for traceability and should be expanded, narrowed, superseded, or closed explicitly if their research state changes.

A publication adaptation draft also remains a research note until it is actually published. It may compress or reorder a bounded argument from a larger living paper, but must identify its derivation and must not silently become a second canonical source for framework meaning. After external publication, preserve the resulting **content edition** under [`../publications/`](../publications/) immediately, before feedback-driven reconciliation. Equivalent Medium, LinkedIn, website, or other platform copies may be recorded as renditions of that same content edition; platform-only formatting or image substitutions do not require separate repository editions unless the substantive text materially diverges.

## Notes

- [`ai-delivery-lifecycle.md`](ai-delivery-lifecycle.md) — an early lifecycle hypothesis reclassified from doctrine. Its main project and delivery questions are now translated into the Project Control Architecture and Viability Review and the Thinking System Review. Remaining questions concern proportionality, two-level inheritance, control economics, evidence methods, incident learning, reauthorization, and real-team validation.
- [`control-theory-brief.md`](control-theory-brief.md) — planning brief for research beyond the basic control-loop mapping already active in UA, including stability, feedback adequacy, latency, and limits of control-theory transfer.
- [`designing-nondeterministic-systems-source-intake.md`](designing-nondeterministic-systems-source-intake.md) — provenance and framework-transfer record for the maintainer-supplied PDF export. The repository does not currently preserve or independently verify an editable PPTX; presentation content remains research evidence rather than specification authority. During consolidation of the article plan, two concerns from the former operational-extension note that were only partially represented—active behavioral/control baseline reconstructability and explicit fallback/common-mode/capacity/restoration evidence—were transferred into the living blueprint/manuscript. The intermediary note was then removed as redundant; Git history preserves it.
- [`metrics-brief.md`](metrics-brief.md) — planning brief for decision-useful evidence, misleading metrics, sampling, drift signals, and context-derived thresholds.
- [`on-device-cloud-source-intake.md`](on-device-cloud-source-intake.md) — traceability record for a full author-provided source that remains pending raw preservation and normalization.
- [`open-engineering-specification-article-blueprint.md`](open-engineering-specification-article-blueprint.md) — active living editorial contract for the long-form public synthesis paper. It preserves the complete argument, section responsibilities, running-example contract, figure plan, source plan, maturity boundaries, and unresolved editorial decisions while remaining non-normative research material.
- [`open-engineering-specification-article-draft.md`](open-engineering-specification-article-draft.md) — active long-form target manuscript governed by the blueprint. The current merged paper establishes the core argument through Article §4 while later research remains intentionally open; Draft PRs may continue the long-form work independently of publication adaptations.
- [`thinking-systems-publication-draft.md`](thinking-systems-publication-draft.md) — publication-facing adaptation titled *Thinking Systems: When the Controlled Object Changes*. It preserves the category and controlled-object deduction from the long-form §§1–2, follows the manuscript's closed-loop → complete bounded-control figure sequence through Figures 6–7, and carries the Section §4 orthogonality claim into Figure 8 so decision ownership and capability functions remain separate models while lifecycle detail stays compressed for publication. It is intended to expose that argument to external criticism before the larger paper is completed.
- [`reference-implementations-brief.md`](reference-implementations-brief.md) — planning brief for implementation evidence, two-level worked applications, and architectural examples that can test current UA doctrine and patterns.

Completed publications and repository editions belong in [`../publications/`](../publications/). Research process and traceability documents remain in the parent [`content/research/`](../) namespace.

New notes should use `status: research`, an explicit `maturity`, and the conventions in [`DOCUMENT-METADATA.md`](../../../DOCUMENT-METADATA.md).

Publication adaptations should additionally identify their derivation, preserve material attribution/provenance, and follow the publication-adaptation cycle in [`../review-process.md`](../review-process.md) with contributor execution guidance in [`../AGENTS.md`](../AGENTS.md).

When a framework PR, worked application, or material external review changes the state of a note's question, reconcile that state under the [`Research Review Process`](../review-process.md). Do not use this directory as a session log or duplicate pull-request history.