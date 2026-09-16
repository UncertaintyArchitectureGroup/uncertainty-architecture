---
title: Repository Context Improvement Research
artifact_type: research-note
status: research
maturity: draft
module: research
topics:
  - repository-architecture
  - provenance
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/repository-architecture
  - ua/topic/provenance
created: 2026-09-16
updated: 2026-09-16
license: CC-BY-4.0
---

# Repository Context Improvement Research

**Planning record; no experiment results yet.** Research items: `RI-CONTEXT-001` and `RI-FEEDBACK-001`. The [Research State Register](../research-register.md) owns their lifecycle states. This note owns the questions, source boundaries, and next decisions. It does not change UA doctrine or the Repository Intelligence projection contract.

## Purpose and restart trigger

Find a small improvement that helps an agent locate, use, and correct repository context without increasing maintainer effort more than the errors it prevents. The maintainer requested this separate research PR on 2026-09-16 to retain the context-management discussion and investigate why corrective feedback appears to disappear between tasks.

**Next reviewer:** the maintainer with the agent handling the next Repository Intelligence improvement. Revisit this note when [PR #119](https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/pull/119) has evaluation results, or before the next change to context retrieval or corrective-feedback guidance, whichever comes first. The [roadmap](../../../ROADMAP.md#repository-intelligence) retains this open action. There is no scheduled job or automatic reminder.

Keep #119's A/B protocol and results separate. This note neither changes its experiment nor claims that its sessions have run. Pin and record the actual protocol/source version when consuming its future results.

## Starting evidence and limits

- At baseline commit `5e2e8c3f619831d3258879e7e4f363529af73a44`, [Repository Intelligence](../../../.github/REPOSITORY-INTELLIGENCE.md) already defines a deterministic projection, task context, source identities, explicit ownership, fallback, and validation discovery. Its [benchmark record](../../../.github/tests/repository_intelligence/README.md) distinguishes fixture/transport evidence from independent agent effectiveness.
- The baseline [corrective-feedback protocol](../../../AGENTS.md#corrective-feedback-and-control-improvement) already asks for diagnosis, recurrence assessment, narrow ownership, and candidate approval. It has no defined cross-session candidate log, reread trigger, incident-counting rule, or proposal threshold. This is a concrete storage/workflow gap; it does not prove that every prior failure had this cause, or that a log alone solves it.
- The maintainer supplied a screenshot of Dattaraj Rao's [LinkedIn post](https://lnkd.in/p/dTCaQ-4W), displaying a diagram titled *Verizon's Enterprise Context Management Practice*, attributed there to Gartner and adapted from Verizon. The screenshot was inspected during this intake; its original publication date and the underlying paid report were not independently established, and the short link did not resolve during intake. The diagram separates knowledge engineering, context management, context delivery, and context governance around enterprise context. Rao's accompanying commentary proposes agent feedback under human oversight; this is not evidence that the pictured system implements that feedback.
- That screenshot supplies research questions, not empirical validation, an implementation specification, or endorsement of UA by Rao, Verizon, or Gartner. No private correspondence or screenshot is republished here.
- Microsoft's [tgrep repository](https://github.com/microsoft/tgrep), consulted 2026-09-16, describes trigram-indexed regex search and a local client/server arrangement. It is a candidate discovery backend to investigate, not an ownership model or an adopted dependency. Its published performance measurements do not establish benefit for this repository or connector-only access.

## Context questions to investigate

| Question | Smallest comparison | Evidence needed for a follow-up |
|---|---|---|
| Is useful context missing, irrelevant, or simply unused? | On a real failed task, inspect the current `context-for-task` result and the source reads actually observed. | Separate delivered candidates, observed reads, correct use in the output, and unknowns. File delivery alone does not prove use. |
| Would a clearer task context help? | Try a small presentation change using existing owner, source identity, relationship, and validation data. | Fewer owner/scope mistakes or less search with no loss of relevant coverage. Do not add a second context schema merely to rename existing fields. |
| Does discovery need another backend? | First classify lexical, language, ranking, connector, and stale-source failures; compare direct sources and current RI. Test tgrep only if repeated local scanning is the measured bottleneck. | End-to-end task cost, index build/update cost, memory, missing/stale results, and source verification. Local speed is not connector availability or immutable-source evidence. |
| Can observed agent outcomes improve context? | Link a correction, failed test, missed owner, or review finding to one scoped candidate. | Auditable action/output evidence and a reviewed change to the existing owner; no automatic promotion of model-generated advice. |

For the first context probe, select at most three real failures before changing retrieval. Record the task, model/tool access, source ref, original query, required owners, answer correctness, reads/calls/bytes, elapsed time, and maintainer review time. Use the same source and access conditions for the existing route and one proposed change. Keep setup cost and unavailable measurements visible. This is a diagnostic probe, not a powered benchmark or a replacement for #119.

Record each finding here as **source/ref → observed failure → candidate change → evidence/cost → adopt, defer, or reject**. Search primary documentation and comparable open-source implementations for the diagnosed failure before building anything. Record the specific version and relevant limitations rather than treating a product diagram or popularity as evidence.

## Feedback pilot

`RI-FEEDBACK-001` asks whether persistent scoped candidates reduce repeated corrections at acceptable cost. The requested implementation lives in [AGENTS.md](../../../AGENTS.md#persistent-candidates); [AGENT-FEEDBACK.md](../../../AGENT-FEEDBACK.md) stores the first real intake incident. The note does not define another agent protocol.

Run a manual pilot over the next **ten repository tasks after adoption**, then review even if no candidate reaches the proposal threshold. This sample size is an effort limit, not statistical validation. Maintain a small evidence table here during the pilot: task/PR key, applicable scope, log read (yes/no/unknown), material correction present, candidate/count or justified one-off, proposal/disposition, extra maintainer minutes, and repeated failure after an implemented change. Use sanitized summaries where evidence is private. Ten tasks is the review trigger; update both this note and the register then. Do not silently count unobserved sessions as successful captures.

The maintainer and participating agent append one row at task completion, including tasks without corrections. If the pilot is not maintained, record it as unperformed or incomplete; merging its plan does not execute it.

| Task/PR key and scope | Log read | Correction / candidate / independent count | Proposal or disposition | Extra maintainer minutes | Recurrence after implementation |
|---|---|---|---|---|---|

No pilot tasks have been recorded yet.

Check these practical cases against actual tasks where possible; label any rehearsal synthetic and exclude it from recurrence counts:

1. A one-off content edit is applied without inventing a durable preference.
2. Three requests to finish the same correction remain one incident, including across sessions.
3. The same failure in three independent tasks yields one concrete proposal in the correct scope. It does not edit `AGENTS.md` before candidate approval.
4. A new session reads an existing candidate and updates its evidence without copying it into every agent scope.
5. Rejected/deferred, conflicting, and already-covered candidates are handled without repeated approval requests or duplicated rules.
6. An approved change is tracked separately from evidence that the failure subsequently became less frequent.

At review, report observed capture misses, unjustified candidate merges/splits, proposal usefulness, repeated errors, added instruction length, and review time. State denominators and unknown tasks. A skipped log read is a failure of this protocol, not proof that more prose is needed: investigate a cheap existing task-completion hook only if that failure is observed. No hidden reasoning traces are required; use visible actions, source reads, output changes, test results, and user/reviewer corrections.

## Decision and complexity budget

The initial implementation is Markdown records, a short extension to existing agent guidance, and the existing research register/roadmap. No new service, database, workflow, transcript collector, or automatic rule writer is justified by the present evidence. Scoped logs are created only with a real candidate; they are not preallocated for every agent.

At either review trigger, choose one disposition: retain the current route, propose one bounded improvement, defer with a named evidence gap and revisit condition, or reject the candidate as disproportionate. Record why. Keep the context probe and feedback pilot independent: either can finish without the other.

Stop expanding the mechanism if simpler wording/discovery fixes the measured failure, or if recording/review cost outweighs the observed benefit. Any universal effectiveness claim, new backend, automatic extraction, or generalized open-source product needs evidence beyond this pilot. Framework adoption, if later proposed, requires a separate explicit decision and traceability update.
