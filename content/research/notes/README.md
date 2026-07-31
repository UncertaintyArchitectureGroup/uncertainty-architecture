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
updated: 2026-07-31
license: CC-BY-4.0
---

# UA Research Notes

This directory contains bounded working notes, source-intake records, operational observations, worked-application notes, and research briefs that may inform later analysis, synthesis, or framework proposals.

Research notes are **non-normative**. A note may describe a question, planned investigation, operational observation, source-intake gap, completed translation state, or incomplete line of inquiry. Its presence does not establish evidence, consensus, or a specification requirement.

The notes migrated here from the former root-level `research/` directory are planning briefs rather than completed research outputs. They are retained for traceability and should be expanded, narrowed, superseded, or closed explicitly if their research state changes.

## Notes

- [`ai-delivery-lifecycle.md`](ai-delivery-lifecycle.md) — an early lifecycle hypothesis reclassified from doctrine. Its main project and delivery questions are now translated into the Project Control Architecture and Viability Review and the Thinking System Review. Remaining questions concern proportionality, two-level inheritance, control economics, evidence methods, incident learning, reauthorization, and real-team validation.
- [`control-theory-brief.md`](control-theory-brief.md) — planning brief for research beyond the basic control-loop mapping already active in UA, including stability, feedback adequacy, latency, and limits of control-theory transfer.
- [`designing-nondeterministic-systems-source-intake.md`](designing-nondeterministic-systems-source-intake.md) — provenance and translation record for the maintainer-supplied original PPTX and the preserved PDF export. Slides 1–6 and a later bounded extraction covering the controlled-object shift, process implications, feedback, and architectural veto have been translated through explicit framework review; a complete transcript remains optional future work.
- [`metrics-brief.md`](metrics-brief.md) — planning brief for decision-useful evidence, misleading metrics, sampling, drift signals, and context-derived thresholds.
- [`on-device-cloud-source-intake.md`](on-device-cloud-source-intake.md) — traceability record for a full author-provided source that remains pending raw preservation and normalization.
- [`open-engineering-specification-article-blueprint.md`](open-engineering-specification-article-blueprint.md) — detailed editorial blueprint for a public article presenting the current UA specification spine from controlled-object shift and system control through the four-level lifecycle, inheritance, two living artifacts, worked application, platform boundary, maturity limits, and external validation request.
- [`reference-implementations-brief.md`](reference-implementations-brief.md) — planning brief for implementation evidence, two-level worked applications, and architectural examples that can test current UA doctrine and patterns.

Completed publications and repository editions belong in [`../publications/`](../publications/). Research process and traceability documents remain in the parent [`content/research/`](../) namespace.

New notes should use `status: research`, an explicit `maturity`, and the conventions in [`DOCUMENT-METADATA.md`](../../../DOCUMENT-METADATA.md).

When a framework PR or worked application changes the state of a note's question, reconcile that state under the [`Research Review Process`](../review-process.md). Do not use this directory as a session log or duplicate pull-request history.
