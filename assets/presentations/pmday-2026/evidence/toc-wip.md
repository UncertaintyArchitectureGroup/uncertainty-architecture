---
title: "Theory of Constraints and work in progress"
artifact_type: repository-guide
status: informative
maturity: draft
module: publishing
draft: true
topics:
  - provenance
tags:
  - ua/module/publishing
  - ua/type/repository-guide
  - ua/status/informative
  - ua/topic/provenance
---

# Theory of Constraints and work in progress

Slide 3 uses a **Theory of Constraints lens** associated with Eliyahu M. Goldratt and Jeff Cox's *The Goal*. It does not treat the SDLC drawing as a new empirical study.

Software-specific sources: DORA's [Work in process limits](https://dora.dev/capabilities/wip-limits/) and [Working in small batches](https://dora.dev/capabilities/working-in-small-batches/), checked 2026-09-21. They discuss whole-value-stream bottlenecks, invisible software inventory, delayed feedback, batch size and quality risks. DORA's text is CC BY 4.0; this note is a summary.

## Conditional mechanism

At fixed bottleneck capacity, accelerating another step alone cannot raise the system's maximum output. When actual inflow exceeds completed outflow, unfinished inventory grows. In software, that may mean queued reviews, unintegrated changes and unvalidated features. Longer waits and larger batches can increase rework and quality risk.

This is **not** a rule that every non-bottleneck improvement necessarily degrades quality. Cost reduction or spare capacity can still help. A pull policy/WIP limit can prevent extra upstream capacity from turning into extra inventory. AI may also improve the bottleneck itself; its effect on Intent, Design and all later stages requires measurement.

## Illustrative arithmetic, not observed team data

Assume comparable work items, steady inflow of 100 changes/week, integrated outflow of 8/week, fixed capacity, no discard and no WIP admission limit. Inventory grows by **100 − 8 = 92 changes/week** across unfinished work. Integration is the hypothetical bottleneck here; it is not asserted to be the bottleneck of every team. A quality decrease is a possible operational consequence, not implied by the subtraction alone.
