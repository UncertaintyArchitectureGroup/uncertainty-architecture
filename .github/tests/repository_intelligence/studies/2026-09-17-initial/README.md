# RI comparison — frozen descriptive study

Status: **12 tasks and 24 messages frozen before experimental outcomes; collection in progress; 4/24 collected, 0 scored**.

On 2026-09-17 the maintainer accepted the preceding task set and explicitly narrower descriptive scope with “Ок, погнали”. This is the separate post-#119 experiment in Draft PR #125. PR #124 research remains separate.

## What this comparison can establish

Compare the quality of answers under ordinary-source instructions (A) and normal optional RI instructions (B) in the maintainer's actual client. Both may use ordinary sources; B need not fetch RI. This is a comparison of assigned instructions with incomplete execution visibility. It cannot establish actual RI exposure, causal RI benefit, efficiency or general model superiority. A positive quality difference is descriptive only.

The [v11 protocol](../../AB-EVALUATION.md) retains its original meaning, evidence requirements and thresholds. Its bootstrap, source authority, ablation/fallback rules, alternating order and 0/1/2 quality anchors guide this study. The maintainer-approved deviations are explicit: assistant-prepared task selection, Auto routing without verified model parity, and incomplete source/delivery/traffic capture. This record is **not v11 preregistration**, and [sessions.json](sessions.json) is not input for the strict v11 evaluator. Do not manufacture smoke, event or configuration evidence to obtain a valid-looking v11 result.

## Frozen inputs and settings

| Item | Frozen value or evidence status |
|---|---|
| Repository | https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture |
| Study commit | `989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3` |
| Commit tree | `ed4dcf068af29ad0eb42867e1548076e21eca67d` |
| Compact surface | `assets/repository-intelligence/agent-context.json` |
| Surface Git blob | `1b1c3f07ed7202d566fca1dda0004f89cb6e5219` |
| Complete surface SHA-256 | `bf0fb746f299c31683e3909f9532d4d560eff21326d5d59fd822fdada378ba35` |
| Source freshness | [Successful main projection job](https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/actions/runs/35210305097/job/105165981358), verified checkout at 2026-09-17 10:24:44 UTC |
| Tasks / keys | [TASK-CANDIDATES.md](TASK-CANDIDATES.md), accepted wording and expectations; UTF-8 file SHA-256 `8df53543c64a883391bbc238bc6d2efb0784daf3c2dd561953d43b882dfce5b8` |
| Exact messages | [sessions.json](sessions.json); only the arm marker differs within each task pair |
| Client setting | Maintainer's other-account ChatGPT Free, default/Auto, GitHub connector configured per maintainer |
| Actual model / thinking | Unknown for future sessions; smoke page reported GPT-5.6 Luna / `gpt-5-6`; no fixed reasoning setting exposed |
| Context metric | Unavailable; no tokens/bytes/call-total estimates from narrative or repository file sizes |
| Isolation instruction | New conversation for every message, outside Projects, Memory off, no past answers/keys; operator compliance not yet observed |
| Model parity | Same visible client/Auto setting requested; backend parity unverified and must remain a limitation |

The accepted projection job and organizer checkout verify prepared source data, not what another model received. Two unscored rehearsals remain preserved: [Gemini-labelled](SMOKE-01-result.md), [ChatGPT](SMOKE-CHATGPT-01-result.md), and the latter's [extracted Share](SMOKE-CHATGPT-01-share.json). All 20 shared tool response bodies were redacted. No further connector-setup test is required; no rehearsal enters the 24-session sample.

## One-message handoff

1. Organizer supplies only the next exact `submitted_message`. Odd tasks run A then B; even tasks B then A. All 24 messages are prepared before the first outcome.
2. Maintainer opens a fresh chat on the same other account, outside Projects, with Memory disabled and the same visible default model setting. Paste the entire message once. Do not add earlier answers, repository attachments, scoring keys or task-specific hints.
3. Return the exact first answer and Share link here. A refusal, clarification request, quota interruption or failed read is a result to retain. Do not click regenerate or repair the tested conversation. Record any visible model/setting change or accidental context as a deviation; unknown model identity stays unknown.
4. Organizer preserves the response and available capture, updates the corresponding pending record, and supplies the next prompt. No mid-run scoring feedback is sent to tested sessions. An unanswered clarification is recorded and the sequence proceeds without substantive hints. Never overwrite a started attempt with a better answer.

No strict source lock is claimed. Organizer observed `main` at the study commit at 2026-09-17T11:27:18.128Z via the GitHub branch API and rechecks immediately before first issuance and after collection. The branch is not protected; this is an observation plus a requested quiet window, not enforcement. Avoid merging to `main` during collection, including this experiment PR. If it moves, retain all prior outcomes, pause further issuance, record possible default-search contamination and decide a separately frozen follow-up if needed. Do not rewrite this study against a new SHA after seeing answers. Exact-ref reads are still requested; opaque/redacted payloads do not prove compliance.

## Collected receipts

- **T01/A, 1 of 24:** [shared capture](T01-A-share.json), with the exact answer in [sessions.json](sessions.json). The submitted wording matches; blank separator lines were omitted. Share reports GPT-5.6 Luna / `gpt-5-6` with Auto. All 10 exposed tool response bodies are redacted, so source and arm compliance, actual repository-call totals and traffic remain unverified. Memory-disabled operation is not confirmed; the public metadata flags are recorded without inferring actual context contamination. The answer is retained without scoring or a rerun.

- **T01/B, 2 of 24:** [shared capture](T01-B-share.json), with the exact answer in [sessions.json](sessions.json). Submitted wording matches the frozen message with blank separators omitted. Share reports GPT-5.6 Luna / `gpt-5-6` with Auto and exposes 17 redacted tool responses. The answer reports a truncated compact-RI request and ordinary-source fallback; payloads do not independently establish delivery or source compliance. Memory-disabled operation remains unconfirmed from the supplied metadata. Both T01 answers are preserved without quality scores or a rerun.

- **T02/B, 3 of 24:** [shared capture](T02-B-share.json), with the exact answer in [sessions.json](sessions.json). Submitted wording matches with blank separators omitted. Share reports GPT-5.6 Luna / `gpt-5-6` with Auto and 8 redacted tool responses. The answer reports truncation of an RI-document read and describes fallback requirements; that description is not evidence of actual compact delivery/use. Source and isolation limits remain recorded, without scoring or a rerun.

- **T02/A, 4 of 24:** [shared capture](T02-A-share.json), with the exact answer in [sessions.json](sessions.json). Submitted wording matches with blank separators omitted. Share reports GPT-5.6 Luna / `gpt-5-6` with Auto and 11 redacted tool responses. The answer reports ordinary-source reads, no compact RI or excerpts, and resource continuation after a truncated tree display; redacted payloads do not verify those claims. Source and isolation limitations remain recorded. Both T02 answers are retained without quality scores or a rerun. Next handoff: the already-frozen T03/A message in a fresh chat.

## Assessment and stopping rule

After collection, freeze all responses and retain all 12 task pairs, including missing or interrupted sessions. Prepare a self-contained packet with opaque shuffled response IDs, task prompt, frozen expectations/serious errors, verbatim answer and blank score. Withhold arm mapping, execution order, sessions, tools and settings. Do not rewrite answers that themselves reveal their route: disclose residual unblinding. The organizer has seen arm assignments and must not be the blind scorer; use a separate person or isolated scoring session given only that packet and frozen owning evidence.

Use v11's semantic anchors: **0** materially incorrect (always 0 for a concrete serious error); **1** partially correct and needs maintainer correction; **2** meets frozen expectations with owning sources. Freeze scores before revealing arms. Publish A/B scores for every task, quality wins/losses/ties for paired scoreable responses, their denominator, missing/unscoreable attempts and serious errors. Show source/isolation/model deviations beside the results. Missing responses stay missing rather than becoming favorable ties or synthetic score-zero answers. No strict v11 outcome is inferred from these descriptive counts; missing evidence would leave its RI-benefit question inconclusive.

Stop after the 24 planned slots or a recorded interruption. Do not adjust tasks, expectations, instructions, client selection or scoring anchors based on results; do not selectively rerun failures or unfavorable answers. A follow-up is a separate frozen study only for an identified transport/isolation issue or a named task family still needed for a concrete RI decision. Retain this study's original results unchanged.

## Progress

- [x] PR #119 merged; source/RI preparation checked.
- [x] Rehearsals retained and connector setup accepted as maintainer-confirmed.
- [x] Maintainer accepted the 12 tasks and descriptive scope before outcomes.
- [x] Exact messages, expectations, settings limitations and follow-up rule frozen.
- [ ] 24 session slots completed or explicitly reported missing/interrupted; final source observation recorded.
- [ ] Independent scores frozen before arm reveal.
- [ ] All-pair descriptive report published and reviewed; Draft PR #125 completed.
