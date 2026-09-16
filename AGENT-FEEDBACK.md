---
title: Repository Agent Feedback Candidates
artifact_type: repository-guide
status: informative
maturity: active
module: repository
topics:
  - contribution-workflow
  - provenance
tags:
  - ua/module/repository
  - ua/type/repository-guide
  - ua/status/informative
  - ua/topic/provenance
---

# Repository Agent Feedback Candidates

This is evidence and decision memory for the root contributor scope. Entries do not instruct agents or authorize changes. The behavior and approval boundary are owned by [AGENTS.md](AGENTS.md#persistent-candidates). Scoped logs use the same format beside their owning `AGENTS.md`, only when needed.

## Record format

Use one short record per failure mechanism: **ID; status; failure / candidate behavior; owner and target section; evidence** (date, distinct task/incident key, public link or sanitized maintainer-attested summary); **independent occurrences; decision / exact proposal; automation feasibility; implementation; next review trigger / observed outcome**. Unknown evidence stays unknown. This format is a writing aid, not a new machine schema or CI gate.

## CF-ROOT-001 — Corrections have no durable candidate memory

- **Status:** approved; implementation proposed in this PR, not yet accepted on `main`.
- **Failure / candidate:** the existing protocol asks contributors to classify recurring corrections and propose durable guidance, but defines no persistent candidate record, next-session read, or recurrence trigger. Add scoped records and a three-independent-incident proposal trigger, retaining explicit approval before a candidate becomes guidance.
- **Owner / section:** [AGENTS.md — Corrective feedback and control improvement](AGENTS.md#corrective-feedback-and-control-improvement), with a bootstrap read of applicable logs.
- **Evidence:** 2026-09-16, task key `context-feedback-research-intake`: maintainer explicitly requested a separate research PR and persistent candidates near agents, with repeated cases presented for approval. Maintainer-attested, sanitized from the active conversation; no public transcript. Inspection of `AGENTS.md` at `5e2e8c3f619831d3258879e7e4f363529af73a44` confirms the missing persistence/read/count mechanics.
- **Independent occurrences:** 1 verified intake incident. Earlier failures are suspected by the maintainer; their number and causes have not been established. The source inspection diagnoses this incident and is not a second occurrence.
- **Decision / proposal:** implementing the record-and-proposal mechanism is the maintainer's explicit task. This authorizes this scoped protocol change, not future inferred rules. Exact proposed wording is the `AGENTS.md` diff in this PR; the default threshold remains subject to maintainer review.
- **Automation feasibility:** file presence and formatting are observable; whether a correction represents the same cause or a useful rule requires judgment. No transcript collector, semantic CI gate, or automatic instruction writer is added.
- **Implementation:** this PR adds the root record, bootstrap read, deduplication, proposal trigger, and approval/disposition handling. Acceptance and behavioral effectiveness remain separate.
- **Next review trigger / outcome:** on the first applicable task after merge, check whether this record is discovered; evaluate the bounded pilot under [RI-FEEDBACK-001](content/research/notes/repository-context-improvement-research.md#feedback-pilot). No successful cross-session observation is claimed yet.
