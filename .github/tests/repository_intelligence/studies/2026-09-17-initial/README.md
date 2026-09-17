# RI comparison — frozen descriptive study

Status: **12 tasks and 24 messages frozen before experimental outcomes; collection resumed; 6/24 original slots collected plus 1 supplemental attempt, 0 scored**.

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

- **T02/A, 4 of 24:** [shared capture](T02-A-share.json), with the exact answer in [sessions.json](sessions.json). Submitted wording matches with blank separators omitted. Share reports GPT-5.6 Luna / `gpt-5-6` with Auto and 11 redacted tool responses. The answer reports ordinary-source reads, no compact RI or excerpts, and resource continuation after a truncated tree display; redacted payloads do not verify those claims. Source and isolation limitations remain recorded. Both T02 answers are retained without quality scores or a rerun.

- **T03/A, 5 of 24:** [shared capture](T03-A-share.json), with the exact answer in [sessions.json](sessions.json). Submitted wording matches with blank separators omitted. Share reports GPT-5.6 Luna / `gpt-5-6` with Auto and 14 redacted tool responses. The answer reports ordinary-source reads, no compact RI or excerpts, and full blob reads after transport truncation; redacted payloads do not verify those claims. Source and isolation limitations remain recorded, without scoring or a rerun.

- **T03/B, 6 of 24:** [shared capture](T03-B-share.json), with the exact refusal in [sessions.json](sessions.json). Submitted wording and study SHA match, with blank separators omitted. The response reports an unavailable ref, but quotes `989fc1398fc221ffca4e1f7a141b2c03bfc7cf3`, different from the correctly submitted study SHA. Both tool responses are redacted, so actual connector arguments and the claimed error remain unverified. Share reports `gpt-5-6-mini` under Auto, unlike the preceding five sessions (`gpt-5-6`); backend parity cannot be assumed. The original refusal remains a collected attempt without a substantive task answer or score; the supplemental repeat below does not replace it. Source and isolation limitations remain recorded. The subsequent maintainer update and planned follow-up are recorded below.

## Maintainer-directed follow-up after T03/B

Recorded on 2026-09-17, after the first six responses and before any retry outcome. The maintainer reported that the previously used model had become temporarily unavailable on the Free account and would return later, and explicitly requested a repeat of the last test. This is new operator testimony after the T03/B receipt; the original capture remains unchanged. Share reports `gpt-5-6-mini` for T03/B versus `gpt-5-6` for T03/A. The availability explanation, reset time and routing cause have not been independently verified.

This is a disclosed post-outcome addition outside the frozen 24-session comparison. The original no-replacement rule and all six received records remain intact. The follow-up question is whether T03/B can produce a substantive answer after reported restoration of model availability; one repeat cannot establish why the first attempt failed or isolate an RI effect.

- **Pause (original plan):** hold T04/B and later primary slots while the maintainer waits for availability to return. At the time this plan was recorded, no retry had started or been collected. Before resuming, recheck the original study source; if main moved, retain results and apply the existing source-movement rule.
- **One supplemental attempt, T03-B-R1:** after the maintainer reports restored availability, use a fresh chat on the same account, outside Projects, with Memory off and the same visible model setting. Copy the exact frozen T03/B `submitted_message` from sequence 6 in [sessions.json](sessions.json), including its original study SHA and task ID. The retry label belongs only in the organizer record; add no correction, previous answer, failure diagnosis or task hint to the tested prompt.
- **Preservation:** save the first returned retry response and Share separately as T03-B-R1, even if it refuses again or reports another model. Record exposed model metadata and operator observations without inferring backend parity. Do not overwrite T03/B, erase its refusal, or repeat until success. T04/B remains the next original slot after this one follow-up.
- **Reporting:** keep the original 24 slots and denominators. Show the supplemental attempt separately, using the same frozen expectations and independent scoring after collection. Any comparison with the existing T03/A is exploratory, reuses that response and occurs at a different time; it is not an additional independent pair or a replacement result. Report the original and retry together, including their model/access limitations.

## Supplemental receipt and resumption

**T03-B-R1:** [shared capture and verbatim answer](T03-B-R1-share.json), received on 2026-09-17 after the maintainer-requested pause. The submitted text matches the frozen T03/B wording and study SHA, with blank separator lines omitted and one trailing newline added. Share again reports GPT-5.6 Luna / `gpt-5-6` under Auto, matching the label reported for T03/A; this does not independently verify backend parity or the account's quota reset. The returned answer is retained without scoring.

All 9 exposed tool response records are redacted. The answer reports direct reading of known owners, no compact RI use, and transport truncation of root `AGENTS.md` and `CONTRIBUTING.md`. Actual reads, full-bootstrap compliance, source/delivery completeness and traffic remain unverified or unavailable. Memory-disabled isolation is still not confirmed by the available metadata. These limitations are recorded in the capture's organizer receipt without inferring actual contamination.

The organizer rechecked main at `989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3` at 2026-09-17T16:57:36.475Z. All original task, session and capture files remain unchanged: **6/24 original slots plus this one supplemental attempt, 0 scored**. Resume the original sequence with the unchanged **T04/B** prompt in a fresh chat. No further repeat is scheduled; the original refusal and this later response will both remain visible in the report.

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
