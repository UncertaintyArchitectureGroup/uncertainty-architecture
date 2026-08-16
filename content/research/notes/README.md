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
updated: 2026-08-15
license: CC-BY-4.0
---

# UA Research Notes

This directory contains bounded working notes, source-intake records, operational observations, worked-application notes, and research briefs that may inform later analysis, synthesis, or framework proposals.

Research notes are **non-normative**. A note may describe a question, planned investigation, operational observation, source-intake gap, completed translation state, or incomplete line of inquiry. Its presence does not establish evidence, consensus, or a specification requirement.

The notes migrated here from the former root-level `research/` directory are planning briefs rather than completed research outputs. They are retained for traceability and should be expanded, narrowed, superseded, or closed explicitly if their research state changes.

## Notes

- [`ai-delivery-lifecycle.md`](ai-delivery-lifecycle.md) — an early lifecycle hypothesis reclassified from doctrine. Its main project and delivery questions are now translated into the Project Control Architecture and Viability Review and the Thinking System Review. Remaining questions concern proportionality, two-level inheritance, control economics, evidence methods, incident learning, reauthorization, and real-team validation.
- [`control-theory-brief.md`](control-theory-brief.md) — planning brief for research beyond the basic control-loop mapping already active in UA, including stability, feedback adequacy, latency, and limits of control-theory transfer.
- [`designing-nondeterministic-systems-source-intake.md`](designing-nondeterministic-systems-source-intake.md) — provenance and framework-transfer record for the maintainer-supplied PDF export. The repository does not currently preserve or independently verify an editable PPTX; presentation content remains research evidence rather than specification authority. During consolidation of the article plan, two concerns from the former operational-extension note that were only partially represented—active behavioral/control baseline reconstructability and explicit fallback/common-mode/capacity/restoration evidence—were transferred into the living blueprint/manuscript. The intermediary note was then removed as redundant; Git history preserves it.
- [`metrics-brief.md`](metrics-brief.md) — planning brief for decision-useful evidence, misleading metrics, sampling, drift signals, and context-derived thresholds.
- [`on-device-cloud-source-intake.md`](on-device-cloud-source-intake.md) — traceability record for a full author-provided source that remains pending raw preservation and normalization.
- [`open-engineering-specification-article-blueprint.md`](open-engineering-specification-article-blueprint.md) — active living editorial contract for the public synthesis article. It preserves the complete argument, section responsibilities, running-example contract, figure plan, source plan, maturity boundaries, and unresolved editorial decisions while remaining non-normative research material.
- [`open-engineering-specification-article-draft.md`](open-engineering-specification-article-draft.md) — active target manuscript governed by the blueprint; the Abstract and Article §§1–4 are drafted and later sections remain planned work. The former Phase 1 completion checkpoint was removed after comparison confirmed that its current architectural/editorial content was already represented more completely in the living article artifacts; Git history preserves that record.
- [`reference-implementations-brief.md`](reference-implementations-brief.md) — planning brief for implementation evidence, two-level worked applications, and architectural examples that can test current UA doctrine and patterns.

Completed publications and repository editions belong in [`../publications/`](../publications/). Research process and traceability documents remain in the parent [`content/research/`](../) namespace.

New notes should use `status: research`, an explicit `maturity`, and the conventions in [`DOCUMENT-METADATA.md`](../../../DOCUMENT-METADATA.md).

When a framework PR or worked application changes the state of a note's question, reconcile that state under the [`Research Review Process`](../review-process.md). Do not use this directory as a session log or duplicate pull-request history.
