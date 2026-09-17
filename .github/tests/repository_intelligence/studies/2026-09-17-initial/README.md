# Initial RI A/B study — preparation record

Status: **preparation; not preregistered; no primary sessions or scores**.

This directory holds the experiment supported by merged PR #119. The [v11 protocol](../../AB-EVALUATION.md) remains the procedural owner. This record applies that protocol; it does not change thresholds, declare RI acceptance, or incorporate the separate research in PR #124.

## Verified preparation baseline

| Item | Observation |
|---|---|
| Repository | https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture |
| PR #119 merged | 2026-09-17 10:24:20 UTC |
| Preparation and smoke commit | `989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3` |
| Commit tree | `ed4dcf068af29ad0eb42867e1548076e21eca67d` |
| Compact surface | `assets/repository-intelligence/agent-context.json` |
| Surface Git blob | `1b1c3f07ed7202d566fca1dda0004f89cb6e5219` |
| Complete surface SHA-256 | `bf0fb746f299c31683e3909f9532d4d560eff21326d5d59fd822fdada378ba35` |
| Source freshness evidence | [Successful main projection job](https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/actions/runs/35210305097/job/105165981358), `Verified context checkout` at 2026-09-17 10:24:44 UTC |

The job's checkout, tree, blob and complete-content hash match the values above and the local committed checkout. This is organizer preparation evidence, not the operator-client smoke result, a primary execution-window observation, or a token/transport measurement.

The main branch is **not locked during preparation or scoring**. Before primary execution, recheck the branch, all selected tasks and their expectations; freeze the actual study commit and obtain the protocol's before/after execution-window observations. A changed baseline requires a new frozen study before any primary session.

## Immediate handoff

1. Two pasted rehearsal responses are retained: [the Gemini-labelled attempt](SMOKE-01-result.md) and [the ChatGPT free/default attempt](SMOKE-CHATGPT-01-result.md). The second reports GitHub access and unverified RI with source fallback. Neither is a primary session.
2. The next action is to inspect the existing ChatGPT session: return its share link/export with visible tool inputs and outputs, if exposed, and the model/settings shown by the client. Do not rerun the task merely to produce a better-looking capture. The organizer identifies what evidence is available before requesting another rehearsal.
3. The original supplied message is [SMOKE-01](SMOKE-01.txt). [SMOKE-02.txt](SMOKE-02.txt) was prepared as a contingency, but was not handed to the maintainer before the second response arrived. The second response's exact submitted prompt and session ID remain unknown; its filename is a receipt label, not a claimed submitted Task ID.
4. The organizer checks actual model/settings, source identity, RI freshness/delivery, isolation and capture. Record failures or unavailable evidence. A model-written call table does not replace raw tool outputs. Do not invent counts, compute traffic from repository file sizes, or claim hidden state was verified by a model's assertion.

Smoke is unscored and outside the 12 tasks. It deliberately exercises search, a pinned source read and compact delivery/fallback; forced transport coverage in this probe does not change optional RI use in the primary Treatment arm. The second account's reported GitHub access addresses the first attempt's transport problem, but raw evidence and the actual model configuration are still pending. The free-plan label alone neither qualifies nor disqualifies a client. Primary execution awaits client qualification and the remaining preregistration steps. No result is discarded and no primary run is replaced.

## Pending before primary execution

- Independent maintainer selection/review of the [12 task candidates](TASK-CANDIDATES.md), their actual request provenance, required source evidence and concrete serious errors. They were prepared by the implementation-aware assistant and are not an independently selected corpus yet.
- Confirm or replace overlapping tasks, identify the document for T05 and the document pair/current premise for T09, and accept any edited historical request explicitly.
- Record actual model, thinking, client, isolation, access parity, smoke evidence and one context metric. Unknown measurements remain unavailable.
- Freeze exact prompts and keys before outcomes. Each submitted prompt must contain the full repository URL. Include any coordinator-supplied repository-address line in the frozen task text before using v11 `init`; label that context addition in the selection note, preserve the selected request's original language, and do not append unrecorded text after generation.
- Freeze a concrete follow-up rule. Proposed for maintainer review: retain the initial verdict unchanged; use a separate study only to resolve an identified transport/isolation failure or a named uncovered task family that still blocks the next RI decision. Do not selectively rerun unfavorable answers.

No valid-looking `study.json` with guessed configuration, fabricated smoke evidence or an asserted freeze is supplied at this stage. Once these decisions are complete, the organizer uses the existing evaluator to create the actual study and 24 ordered messages. No new runner or workflow is needed.

## Execution and custody

The organizer gives one prompt at a time. Each prompt uses a separate fresh conversation at the frozen source state. Odd tasks run A then B; even tasks B then A. Both arms read the same applicable instructions. A uses ordinary GitHub sources without RI aids; B uses the normal optional verified compact route and source fallback. This is instruction-level ablation with evidence review, not a claim of file-level access enforcement.

During primary sessions, do not provide answer keys, prior responses, scoring feedback or corrective hints. Retain started failures, interruptions and missing measurements. Record clarification requests without supplying substantive hints; do not silently repair or restart a run. The exact operational handling is fixed before execution.

Keep this Draft PR and all study keys/results outside test-agent inputs. Test agents read only the study commit on `main`; default-branch search is allowed only under the execution lock. Do not merge the experiment branch during collection. If a tested session accesses experiment material or another source ref, record the deviation rather than assume contamination was impossible because a prompt forbade it.

After collection, generate the arm-hidden packet and give only that packet to an independent person or isolated scoring session. The organizer conversation knows the arm mapping and cannot be the blind scorer. Freeze scores before revealing arms. Publish every pair and the original outcome, including INCONCLUSIVE or REGRESSION, with actual costs, RI delivery, evidence limitations and remaining RI-EVAL gaps.

The eventual evidence remains the protocol's three input records — study, runs with raw-evidence references, and blind scores — plus its generated report. This preparation README is a handoff record, not another evidence schema or a new source of rules.

## Progress

- [x] PR #119 merged; preparation commit and accepted RI freshness checked.
- [x] Initial operator handoff and candidate review material prepared.
- [x] SMOKE-01 pasted response preserved; connector/capture prerequisites not met.
- [x] Second ChatGPT pasted response preserved; GitHub access reported, RI unverified, original capture and model/settings pending.
- [ ] Suitable maintainer-client smoke completed with adequate access/isolation/capture evidence.
- [ ] Independent task selection, provenance and expectations confirmed.
- [ ] Study/configuration/follow-up rule frozen; source window opened.
- [ ] 24 primary sessions captured; source window closed.
- [ ] Independent blind scores frozen.
- [ ] All-pair report reviewed and results PR completed.
