# Repository Intelligence A/B Evaluation Protocol

> Protocol version: 6

## Purpose and estimand

This protocol defines the independent comparative evaluation required by [`REPOSITORY-INTELLIGENCE.md`](../../REPOSITORY-INTELLIGENCE.md#14-evaluation-and-acceptance).

The primary estimand is the **incremental operational value of the normal Repository Intelligence (RI) route** over the repository's ordinary live-GitHub orientation route under one stable repository state. The primary A/B does not isolate projection-data value from the workflow that verifies, interprets, and uses that data.

Primary question:

> Given the repository's normal contributor instructions and authority model, does the operational RI route reduce serious routing mistakes or observable orientation cost without degrading material decisions, compared with ordinary live-GitHub bootstrap/search on the same repository state?

Both primary arms use the same repository state, same root and scoped `AGENTS.md`, same model/configuration, same connector permissions, same client class, and same task prompt. The existing deterministic 12-case corpus remains a regression suite and is not independent held-out evidence.

## 1. Shared `AGENTS.md` baseline

Removing `AGENTS.md` from Control would create a different repository contract and confound the experiment. Both arms therefore read the same instructions.

- `RI-AB-CONTROL`: RI is deliberately unavailable; use the ordinary live-GitHub route permitted by the source-state lock in this protocol.
- `RI-AB-TREATMENT`: follow the normal operational RI route through the preregistered Treatment Delivery Mode.
- `RI-AB-DATA-ONLY`: optional post-primary diagnostic; use only the verified compact Agent Context Surface supplied for the study state, without RI query operations or task-specific RI routing output.

The root owner map is shared baseline information. Easy exact-owner cases are ceiling/negative controls. The benchmark marker itself is a small observer intervention and must not be counted as evidence for RI value.

## 2. Experimental design

The unit is one **task × arm** run in a fresh isolated session.

The primary study uses **two independent held-out corpora**, frozen before the first run:

- **Pilot corpus P:** 12 tasks = 6 stress + 6 ecological.
- **Confirmatory corpus C:** 12 different tasks = 6 stress + 6 ecological.

No task prompt may appear in both corpora. Both prompt packs, both scoring keys, ecological selections, randomization commitments, thresholds, and source-state controls are frozen before Pilot begins.

### 2.1 Pilot wave

Run **12 Pilot tasks × 2 arms = 24 isolated sessions** using a paired randomized crossover design:

- identical task prompt and study source state within each pair;
- fresh session for every run;
- randomized A/B order per task from a frozen Pilot arm-order seed;
- pairs interleaved over time rather than all A then all B;
- same displayed model family, selectable thinking configuration, connector permissions, client class, and source state within each pair;
- frozen Pilot scoring key;
- arm-hidden correctness scoring where practical.

Do not selectively rerun unfavorable results. An infrastructure retry is allowed only under a rule preregistered before the first run and never replaces a valid unfavorable result.

### 2.2 Independent confirmatory wave

LLM output is stochastic, and repeating the same tasks would test repeatability more strongly than generalization. Confirmation therefore uses the **different, independently held-out confirmatory corpus C** frozen before Pilot.

Run **12 confirmatory tasks × 2 arms = 24 additional fresh isolated sessions**:

- confirmatory tasks are disjoint from Pilot tasks;
- another 6 stress + 6 ecological cases are used;
- confirmatory prompts and scoring key are committed by hash before any Pilot run but remain hidden from tested sessions until the confirmatory wave starts;
- A/B order uses a separate frozen confirmatory arm-order seed;
- ecological selection uses a separate frozen seed or a deterministic non-overlapping allocation from one combined frozen pool;
- the same study source state, model/configuration target, connector, client class, and Treatment Delivery Mode are used as Pilot;
- no prompt, answer-key, scoring-rule, sampling, cost gate, execution mode, or decision rule changes after Pilot unblinding.

The default study executes the confirmatory wave **regardless of Pilot outcome**. Pilot performance must not change the confirmatory corpus or stopping rule.

If model/service drift makes compatible confirmation impossible, record the difference and classify the primary study `INCONCLUSIVE`; do not silently pool incompatible waves.

Primary evidence set under the default protocol: **48 A/B sessions across 24 distinct tasks**.

### 2.3 Optional diagnostic C arm

After **both primary A/B waves and their correctness scores are frozen**, an optional **RI data-only** diagnostic may run on 4–6 frozen cases.

C receives the verified compact Agent Context Surface for the study state but no RI query-operation output or task-specific routing suggestion. The agent decides how to use that data and still reads authoritative repository sources before material decisions.

Interpret C only diagnostically:

- B > A and C ≈ B: projection/data likely carries most of the gain;
- B > C and C ≈ A: workflow/query route likely carries most of the gain;
- B ≈ C ≈ A: no incremental agent value on those diagnostic cases.

C cannot rewrite the primary A/B conclusion.

## 3. Execution eligibility and source-state lock

The held-out study must not start merely because a commit SHA has been chosen. The actual client/tooling used for the study must first demonstrate that both arms can operate against the same stable state, that ordinary Control search remains available, and that Treatment can actually receive the intended RI aid.

### 3.1 Stable default-branch source-state lock

The comparative baseline owned by `REPOSITORY-INTELLIGENCE.md` is ordinary **live-GitHub bootstrap/search**, not an artificially weakened tree-traversal-only agent. The primary study therefore uses a preregistered **stable-default-branch window**:

1. record the exact 40-character study commit and the repository default branch (`main` for the initial study);
2. before the first primary run, verify that the default-branch tip equals the study commit;
3. freeze repository mutations until all 48 primary sessions are complete;
4. before and after **every run**, read the default-branch tip and verify that it still equals the study commit;
5. stop the study immediately if the tip changes; a run whose pre/post checks do not both equal the study commit is invalid;
6. direct file/tree reads should use the exact study commit whenever the client supports a ref parameter;
7. ordinary default-branch GitHub search is allowed in both arms when appropriate because the active source-state lock keeps the default branch on the study commit.

Default-branch search may use a lagging provider index. That lag is part of the observed ordinary live-GitHub route and must not be silently corrected out of Control. Any candidate path returned by search still requires source reading before a material decision.

The lock does **not** permit search across another branch, a later commit, another repository copy with different contents, or historical benchmark outputs. If the maintainer cannot hold `main` stable for the full primary study, use a separate evaluation repository whose default branch is an exact immutable copy of the chosen source commit and preregister that repository identity before freezing corpora. Do not switch execution repositories mid-study.

### 3.2 Treatment Delivery Mode

The study preregisters exactly one primary **Treatment Delivery Mode** and uses it consistently across all Treatment runs:

- `local_cli` — the accepted RI producer/query CLI is available against the study state;
- `connector_compact_surface` — the agent receives the complete verified compact Agent Context Surface through the connector/client and performs the documented bounded interpretation itself;
- `dedicated_adapter` — an explicitly identified adapter exposes accepted RI operations for the study state.

Do not mix delivery modes within one primary study. A later study may compare delivery modes explicitly.

For the first ChatGPT + GitHub-connector evaluation, `connector_compact_surface` is the preferred mode because it measures the architecture in the client environment that motivated this benchmark. In that mode, logical operations such as `find_owner` or `validation_plan` are **not presumed to be executable RPCs**. The treatment is the documented use of the complete verified compact surface plus authoritative source reads.

The complete compact surface may be delivered in several deterministic connector chunks when a single response is truncated. Every chunk counts as a connector call and, when measurable, toward context-volume accounting. The run is eligible only if the complete payload is reconstructed/verified against the preregistered Git blob or full-payload SHA-256; a silently truncated surface is not Treatment.

Preregistration records the chosen mode, surface path, pinned blob identity or full-payload SHA-256, freshness evidence, and complete-payload/truncation checks.

### 3.3 Treatment delivery failure versus task-level fallback

Production RI correctly falls back to live repository reading when task-specific evidence is ambiguous or unsupported. The experiment distinguishes that behavior from failure to deliver Treatment itself:

- **Treatment delivery failure:** the preregistered RI surface/adapter/CLI cannot be obtained, verified, or read completely for the study state, or the actual run receives a different delivery mode. The run is invalid; do not score it as if Treatment simply chose Control.
- **Task-level RI fallback:** Treatment was successfully delivered and verified, but the task-specific RI evidence is ambiguous or unsupported and the documented production route falls back to ordinary live sources under the same source-state lock. This remains valid Treatment behavior and its cost/outcome count normally.

Systematic Treatment delivery failure is an experiment-infrastructure defect and makes the study `INCONCLUSIVE`; it is not evidence that RI has no incremental value.

### 3.4 Non-scored execution smoke test

Before freezing the preregistration as executable, run a **non-scored smoke test** using synthetic/non-held-out tasks that are not derived from either primary corpus and disclose no held-out answer material.

The smoke test must establish, in the actual study client:

1. the default-branch tip can be checked before and after runs;
2. ordinary Control bootstrap/search is available during the stable source-state window;
3. direct source reads can use the exact study commit where supported;
4. the selected Treatment Delivery Mode works for that same state;
5. the complete Treatment payload can be verified and is not silently truncated;
6. required connector-call, source-state, and scoring records can actually be captured;
7. Control and Treatment have equivalent connector permissions aside from the deliberate RI ablation;
8. cross-chat Memory is disabled and Project/workspace context is absent;
9. no held-out prompt, scoring key, prior-arm output, or cross-wave material is exposed.

Record smoke-test evidence outside the tested Git tree. **Do not start the 48 primary sessions unless all mandatory eligibility checks pass.**

## 4. Isolation and run validity

The primary experiment requires a genuinely cold product context, not merely a visually empty conversation.

Record for every run:

- `conversation_fresh`;
- `memory_enabled`;
- `project_context_present`;
- `prior_repo_context_available`;
- `connector_state_equal` within the pair;
- exact displayed `model_family`;
- exact selectable `thinking_configuration`, or `unavailable`;
- client/environment class;
- source-state pre-run and post-run tip SHAs;
- Treatment Delivery Mode where applicable;
- protocol violations;
- Treatment delivery status and task-level fallback status where applicable.

Required conditions:

1. Fresh conversation for every run.
2. Product cross-chat Memory is disabled: `memory_enabled = false`.
3. No Project/workspace or other context injection: `project_context_present = false`.
4. No known prior repository context is supplied to the session by the product: `prior_repo_context_available = false`.
5. No previous-arm output is exposed to the paired run.
6. No corrective scoring feedback is exposed before both runs in a pair are complete.
7. Equivalent repository/connector access within each pair.
8. Confirmatory prompts remain unexposed to tested sessions until the confirmatory wave starts.
9. Pre-run and post-run default-branch tip checks both equal the preregistered study commit.
10. Treatment uses the preregistered delivery mode and exact verified aid identity.

Mark a primary run invalid if any required condition above is not met. `unavailable` is not acceptable for Memory, Project context, prior product context, or source-state checks in the primary study. If the product cannot establish those conditions, use a cleaner environment or classify the primary study `INCONCLUSIVE`.

General model pretraining or public-Internet knowledge is not separately controllable and is shared between arms; do not claim the experiment excludes it.

## 5. Held-out corpora

Each primary wave contains **6 designed stress cases + 6 ecological cases**, for 24 distinct tasks total.

### 5.1 Stress cases

Across each six-case stress half cover a balanced subset of:

- canonical term / synonym pressure;
- overlapping artifact ownership;
- validation/companion routing;
- research-state vs framework-authority separation;
- impact reasoning where navigation/shared hubs must not inflate blast radius;
- stale/unverifiable RI fallback;
- Ukrainian or paraphrased maintainer wording;
- a legitimate-new-artifact case where no current owner fully covers the requested role.

Pilot and confirmatory stress prompts must be different. All 12 stress prompts and both scoring-key sections are frozen before the first Pilot run. Stress cases must not be tuned after observing A/B results or RI rankings.

### 5.2 Ecological cases, sampling frame, and neutral normalization

Ecological cases answer the practical question: does RI help on ordinary UA maintainer work, not only on scenarios designed around RI capabilities?

Real maintainer requests are often conversational fragments such as “fix it”, “review this PR”, or “what next?”. A fresh benchmark session cannot use those fragments without missing context. The ecological pool therefore uses a frozen **neutral normalization** step before seeded selection.

Normalization may:

- expand pronouns or omitted references with facts explicitly present in the source event/context;
- include the minimal artifact/PR/change facts needed to make the task self-contained;
- preserve the original requested outcome, language where practical, and uncertainty.

Normalization must not:

- name or hint the expected canonical owner unless the original request itself did so;
- add an expected repository path, validator, companion file, canonical term, or RI vocabulary that was not necessary to restate the source request;
- add facts learned from RI rankings, the answer key, or later repository investigation;
- simplify a difficult source task into an easier owner-identification prompt.

If a source request cannot be made self-contained without materially revealing the expected answer, exclude it under the preregistered normalization-exclusion rule.

Before any arm run:

1. define one combined raw ecological source pool from a fixed cutoff/source set, or two separately frozen raw pools;
2. record raw-pool provenance, cutoff rule, and raw serialized pool SHA-256 outside the tested repository view;
3. apply only preregistered exclusions;
4. neutrally normalize every remaining eligible source item **before seeded case selection**;
5. freeze the normalized eligible pool and its serialized SHA-256;
6. require at least 24 eligible tasks for a combined pool, or at least 12 per separate wave pool;
7. select six Pilot ecological cases and six **different** confirmatory ecological cases using preregistered seeded selection without replacement across waves;
8. freeze selected opaque case IDs and selection hashes before Pilot;
9. do not manually replace a selected case because RI is expected to perform poorly or well.

Across the combined 12 ecological cases include at least two easy exact-owner/negative-control cases and at least two legitimate-new-artifact cases, with at least one of each anchor type allocated to each wave. If anchors are fixed rather than randomly produced, identify and normalize them before seeded selection and sample the remaining slots from the frozen eligible pool.

Report ecological results separately from stress results and separately by wave. A gain confined to designed stress cases is not broad routine productivity evidence.

### 5.3 Hidden prompt-pack and scoring-key format

Held-out prompts and keys stay outside the repository view exposed to tested sessions until all primary outputs and scores are frozen.

For deterministic verification, each hidden prompt pack uses JSON with:

```json
{
  "schema_version": 1,
  "wave": "PILOT",
  "cases": [
    {
      "task_id": "P01",
      "corpus_class": "stress",
      "ecological_source_id": null,
      "prompt": "..."
    }
  ]
}
```

The confirmatory pack uses `wave: "CONFIRMATORY"`. Each pack has exactly 12 unique task IDs, exactly 6 stress and 6 ecological cases, and nonempty prompts. Exact normalized prompt text must not overlap across waves.

Each scoring key is also JSON with `schema_version: 1`, matching `wave`, and one object per task ID. Key internals may contain the repository-verifiable expected evidence and scoring notes required by the assessor; the deterministic evaluator verifies identity/hash coverage but does not replace assessor judgment.

### 5.4 Preregistration commitments

Preregister only non-revealing metadata and cryptographic commitments in the tested repository view:

- protocol/corpus version;
- Pilot and confirmatory case counts and 6/6 classifications;
- prompt-pack and scoring-key SHA-256 values;
- proof rule for zero prompt overlap;
- ecological raw/normalized pool provenance and hashes;
- ecological selected-ID hashes and seeds;
- study commit and stable-default-branch lock;
- Treatment Delivery Mode and verified aid identity;
- smoke-test result/evidence reference;
- model/configuration target and isolation requirements;
- Pilot and confirmatory arm-order seed SHA-256 values;
- primary/secondary endpoints;
- connector-cost gate;
- connector-interaction gain threshold;
- context-volume metric/gate or explicit `unavailable`;
- final decision rule.

After all primary outputs and scores are frozen, prompts/keys/raw records may be published and verified against the commitments.

## 6. Primary arms

### A — Control

Control follows ordinary repository authority and contributor rules but receives no RI aid.

Allowed for primary orientation under the active source-state lock:

- ordinary GitHub connector search against the stable default branch;
- ref-addressable tree/directory/direct-file reads at the study commit;
- ref-addressable PR/diff/review/check/branch/commit reads when task-relevant and compatible with the frozen task;
- maintained cross-links/navigation discovered from authoritative source files.

Disallowed for orientation:

- `assets/repository-intelligence/agent-context.json`;
- full/generated Graph View;
- RI query operations such as `context-for-task`, `find-owner`, `term-preflight`, `artifact-preflight`, `validation-plan`;
- Repository Control Map;
- copied RI results from another session.

Control may read `.github/REPOSITORY-INTELLIGENCE.md` only when the benchmark task itself is specifically about RI architecture.

This arm intentionally preserves the repository's real manual-live baseline. Search staleness, extra source reads, or a broad query that fails to find the right owner are observed outcomes, not protocol defects, as long as the source-state lock itself remains valid.

### B — Treatment

Treatment follows the production RI route through the preregistered Treatment Delivery Mode:

- establish/verify the exact compact surface, CLI, or adapter identity for the study state;
- use that accepted RI aid for orientation/preflight according to its delivery mode;
- read owning sources at the study commit before material decisions;
- use ordinary live-GitHub fallback/search under the same source-state lock when task-level RI evidence is ambiguous or unsupported;
- never infer authority from ranking/graph structure;
- avoid loading the full graph when compact data is sufficient.

For `connector_compact_surface`, the LLM inspects the complete verified surface directly; do not pretend unavailable local CLI operations were executed. Record which logical RI task was attempted and which surface evidence was used.

The A/B result supports or rejects the **operational RI route as delivered through the preregistered mode**, not projection-only value and not untested delivery modes.

## 7. Neutral run envelope

```text
Repository: UncertaintyArchitectureGroup/uncertainty-architecture
Study source commit: <40-character SHA>
Source-state lock: stable-default-branch window
Expected default-branch tip: <same SHA>
Experiment arm: RI-AB-CONTROL | RI-AB-TREATMENT | RI-AB-DATA-ONLY
Treatment delivery mode: <mode or not-applicable>
Task ID: <opaque ID>
Wave: PILOT | CONFIRMATORY | DIAGNOSTIC

Follow the repository's applicable contributor instructions and complete the task below using repository facts attributable to the study source state. The default branch is intentionally held at the study commit during primary execution. Ordinary GitHub search is allowed when it is part of the arm's permitted route. Do not ask for or search for benchmark answer keys, prior experiment outputs, hidden scoring material, or another wave's task material. Report repository sources relied on and distinguish verified facts from inference.

Task:
<held-out prompt>
```

Opaque IDs must not reveal expected owner or category. Do not tell either arm what RI is expected to improve.

## 8. Observable instrumentation

Never use hidden model reasoning or infer when the model internally knew the answer.

Record where observable:

- pre-run and post-run default-branch tip SHAs;
- ordered connector/tool calls;
- whether direct repository reads were ref-addressable to the study commit;
- total connector calls to final answer;
- default-branch search calls and other broad searches to final answer;
- ordered files opened;
- total distinct source files opened;
- calls before first explicit visible owner/route assertion, when observable;
- Treatment Delivery Mode and delivery-verification status;
- RI logical operations/evidence used and returned payload bytes when applicable;
- task-level RI fallback events separately from Treatment delivery failure;
- total repository-response UTF-8 bytes to final answer when deterministically measurable;
- exact input-token volume when exposed by the client;
- elapsed time only when reliably observable;
- tool errors, truncation, stale-context events, and fallbacks;
- final response/transcript reference.

Do not estimate unavailable token counts, byte counts, or latency from prose length.

## 9. Correctness scoring

Each case has a frozen repository-verifiable key.

Dimensions:

- **Owner/routing correctness (0–2)**: wrong/missing; partial; correct canonical owner/route.
- **Evidence sufficiency (0–2)**: unsupported/material evidence gap; directionally correct with material uncertainty; sufficiently supported by authoritative evidence.
- **Authority discipline (0–2)**: authority promoted/inferred incorrectly; minor ambiguity; correct source-of-truth distinctions.
- **Companion/validation completeness (0–2)** when applicable: material omission; partial; complete.
- **Decision quality (0–2)**: wrong action/proposal; directionally correct with material gap; correct bounded decision.

`Evidence sufficiency` rewards support, not file count. Read volume is cost only.

A **serious routing error** includes:

- wrong canonical owner asserted as authoritative;
- duplicate canonical term/artifact proposed despite an owner that should be refined;
- research/history/example material promoted to framework authority;
- required scoped `AGENTS.md` missed in a way that changes permissible workflow;
- material validator/companion omitted such that the proposed action violates an existing repository contract;
- candidate/proposed state presented as accepted state.

Preferred blind scoring order: remove arm labels/route metadata from scoring copies, randomize pair order, score against the frozen key, lock scores, then reveal arms and add cost data.

For ecological correctness, preregister a mechanically decidable non-regression rule. The default is **median paired total correctness delta (B−A) >= 0** within each wave, with zero ecological `A correct / B wrong` serious-error reversals.

The assessor supplies the dimension scores and serious-error classification. The deterministic evaluator recomputes totals, pair outcomes, cost ratios, gates, and final study classification; prefilled aggregate fields are not authoritative.

## 10. Cost accounting and efficiency claims

### 10.1 Primary paired connector-cost statistic

For each valid ecological pair `i`, define:

`r_i = B_i / A_i`

where `A_i` and `B_i` are total connector calls to final answer for Control and Treatment.

Zero-denominator rule:

- `A_i = 0` and `B_i = 0` → `r_i = 1.0`;
- `A_i = 0` and `B_i > 0` → `r_i = infinity` for gate purposes.

The per-wave statistic is the **median of paired ratios `r_i` across all six ecological pairs**. It is not the ratio of group medians.

### 10.2 Primary connector-cost acceptance gate

The correctness-value route includes all valid ecological cases, including cases where Treatment prevents a serious routing error.

Default gate:

- median paired ecological connector-call ratio <= **1.50**;
- no more than **2 of 6** ecological cases with `r_i > 2.00`.

Apply the gate independently to Pilot and confirmatory ecological halves and also report the combined 12-case ecological median.

### 10.3 Equal-correctness connector sensitivity

Report a secondary connector-cost view using only ecological pairs whose total correctness score and serious-error status are equal across arms. Compute the same median-of-paired-ratios statistic on that filtered set.

This sensitivity view does **not** replace the all-case primary cost gate. If no equal-correctness ecological pairs exist, report it as unavailable.

### 10.4 Connector-interaction gain threshold

A lower connector-call count is useful but is not by itself proof of lower overall orientation cost.

Default threshold for the narrower claim **DEMONSTRATED CONNECTOR-INTERACTION GAIN**:

- median paired ecological connector-call ratio <= **0.80** in each wave;
- ecological correctness non-regression passes in each wave;
- zero reverse serious-error reversals in either wave.

This claim means fewer connector interactions under non-worse correctness. It must not be shortened to “efficiency” when context volume is unmeasured or materially worse.

### 10.5 Context-volume gate for orientation-efficiency claims

Before Pilot, preregister exactly one context-volume metric:

- `repository_response_utf8_bytes` — exact total UTF-8 bytes returned from repository connector responses to final answer, when the study recorder can measure them deterministically;
- `input_tokens` — exact model input tokens when the client exposes them;
- `unavailable` — neither can be measured reliably.

Do not mix volume metrics across runs or waves.

When a metric is available, for each ecological pair define `v_i = B_i / A_i` using the same zero-denominator rule as connector calls. Default context-volume gate:

- all six ecological pairs in each wave have the selected metric;
- median `v_i` <= **1.00** in each wave;
- no more than **2 of 6** ecological cases with `v_i > 2.00`.

Final **DEMONSTRATED ORIENTATION EFFICIENCY GO** requires both the connector-interaction gain threshold and the context-volume gate independently in both waves, with zero reverse serious errors and ecological correctness non-regression.

If the preregistered metric is `unavailable`, or measurement is incomplete, **orientation-efficiency GO is unavailable by design**. A qualifying connector-call result may still be reported using the narrower connector-interaction claim.

Changing cost, interaction, or context-volume thresholds after unblinding invalidates the preregistered GO decision and may only be reported as exploratory.

## 11. Endpoints and Pilot interpretation

Primary endpoint: paired serious-error matrix across valid pairs:

- A wrong / B correct;
- A correct / B wrong;
- both correct;
- both wrong.

Secondary endpoints: per-case correctness delta; median paired correctness delta; connector-cost metrics; equal-correctness sensitivity; selected context-volume metric; stress/ecological split; Treatment-delivery/fallback behavior.

For the 12-pair **Pilot**, report an interim descriptive classification only:

- **PROVISIONAL CORRECTNESS SIGNAL:** >=2 valid `A wrong / B correct`, 0 reverse serious errors, ecological correctness non-regression passes, and Pilot connector-cost gate passes.
- **WEAK CORRECTNESS SIGNAL:** exactly 1 positive reversal, 0 reverse serious errors, ecological correctness non-regression passes.
- **PROVISIONAL ORIENTATION EFFICIENCY SIGNAL:** orientation-efficiency requirements pass for Pilot.
- **PROVISIONAL CONNECTOR-INTERACTION SIGNAL:** connector-interaction threshold passes but orientation-efficiency is unavailable or its volume gate does not pass.
- **NO PILOT SIGNAL:** none of the above signals is met.
- **PILOT REGRESSION:** Treatment introduces a reverse serious-error reversal or fails ecological correctness non-regression.
- **PILOT INCONCLUSIVE:** invalid pairs, source-state lock failure, isolation failure, Treatment-delivery failure, source/model mismatch, scoring ambiguity, or protocol defect prevents defensible interpretation.

Pilot classification does not stop or alter the confirmatory wave unless experiment infrastructure validity has failed. Pilot alone cannot produce final `DEMONSTRATED GO`.

## 12. Confirmatory and final decision

### 12.1 Correctness-value route

Final **DEMONSTRATED CORRECTNESS GO** requires all of:

- all 24 primary pairs complete and valid under compatible frozen conditions and the same Treatment Delivery Mode;
- confirmatory wave contains at least **1** `A wrong / B correct` serious-error reversal;
- confirmatory wave contains **0** `A correct / B wrong` serious-error reversals;
- combined Pilot+confirmatory positive serious-error reversals are at least **3**;
- combined reverse serious-error reversals are **0**;
- ecological correctness non-regression passes independently in both waves;
- primary connector-cost gate passes independently in both waves;
- no source-state, isolation, Treatment-delivery, or scoring defect invalidates the evidence.

If Pilot shows a correctness signal but the independent confirmatory corpus does not satisfy these rules, the correctness claim is **NOT CONFIRMED** rather than GO.

### 12.2 Orientation-efficiency route

Final **DEMONSTRATED ORIENTATION EFFICIENCY GO** requires all of:

- all 24 primary pairs complete and valid;
- zero reverse serious-error reversals in either wave;
- ecological correctness non-regression passes independently in both waves;
- connector-interaction gain threshold passes independently in both waves;
- the preregistered context-volume metric is available for all ecological runs and its volume gate passes independently in both waves;
- the same Treatment Delivery Mode and source-state lock remain valid throughout.

This route does not require serious-error reversals because it claims lower observable orientation cost without degraded material decisions.

### 12.3 Narrow connector-interaction result

If connector-interaction gain passes in both waves but orientation-efficiency cannot be demonstrated because context volume is unavailable or fails its gate, report **DEMONSTRATED CONNECTOR-INTERACTION GAIN ONLY**. Do not relabel that result as overall efficiency.

### 12.4 Other final outcomes

- **CORRECTNESS GAIN / COST NOT ACCEPTED:** correctness reversal thresholds are met, but the primary connector-cost gate fails in either wave.
- **NOT CONFIRMED:** Pilot shows a correctness signal that is not supported by the independent confirmatory corpus.
- **NO INCREMENTAL VALUE SHOWN:** neither demonstrated correctness nor demonstrated orientation efficiency nor connector-interaction gain is met, with no material Treatment regression and valid Treatment delivery.
- **REGRESSION:** any reverse serious-error reversal occurs, or ecological correctness non-regression fails materially under otherwise valid conditions.
- **INCONCLUSIVE:** invalid pairs, source-state lock failure, isolation failure, Treatment-delivery failure, incompatible model/source conditions, scoring ambiguity, or protocol defects prevent a defensible final comparison.

Do not substitute narrative judgment for these preregistered rules after unblinding.

## 13. Deterministic evaluator

The repository owns a small mechanical evaluator at [`.github/scripts/score_repository_intelligence_ab.py`](../../scripts/score_repository_intelligence_ab.py), with regressions in `test_ab_evaluation.py`.

The evaluator:

- verifies protocol version and preregistered source/isolation requirements;
- verifies prompt-pack and scoring-key file hashes supplied at scoring time;
- checks prompt-pack case counts, 6/6 stress/ecological classification, task IDs, and zero exact normalized prompt overlap between waves;
- requires exactly one Control and one Treatment run per primary task;
- derives run validity from fresh-session, Memory-off, no-Project, prior-context, connector-parity, source-state pre/post, and Treatment-delivery records rather than trusting a manually typed `valid` flag;
- recomputes applicable correctness totals from assessor-entered dimension scores;
- recomputes serious-error matrices, paired deltas, connector ratios, context-volume ratios, wave gates, and final classification;
- never reads or scores hidden model reasoning.

The assessor still makes the repository-verifiable semantic scoring judgment against the frozen key. Automation begins only after those observable scores are entered.

The final scoring invocation uses the hidden evidence files outside the tested repository view:

```bash
python3 .github/scripts/score_repository_intelligence_ab.py \
  --preregistration /secure/ab-preregistration.json \
  --run-record /secure/ab-run-record.json \
  --pilot-prompts /secure/pilot-prompts.json \
  --pilot-key /secure/pilot-scoring-key.json \
  --confirmatory-prompts /secure/confirmatory-prompts.json \
  --confirmatory-key /secure/confirmatory-scoring-key.json \
  --output /secure/ab-evaluation-report.json
```

A scoring-script failure is a protocol/instrumentation defect, not a license to calculate a more favorable result by hand.

## 14. Execution lifecycle

1. Merge the protocol/infrastructure PR only after its policy companions, deterministic tests, committed RI surface freshness, and required agent checkpoint are reconciled.
2. Select the exact `main` commit that will be the study state.
3. Establish a repository-mutation freeze and verify the default-branch tip equals that commit.
4. Run the non-scored execution smoke test in the actual study client, including ordinary Control search, source-state pre/post checks, Memory-off/no-Project isolation, and complete Treatment delivery.
5. Create a preregistration record outside the tested Git tree containing commitments/metadata and smoke evidence, not hidden answers.
6. Freeze both independent prompt packs, both scoring keys, raw/normalized ecological pools, non-overlapping ecological selections, seeds, model/configuration, cost/volume gates, and final decision rules.
7. Run Pilot A/B on corpus P, checking the default-branch tip before and after every session.
8. Freeze Pilot outputs and scores; do not modify confirmatory material.
9. Run confirmatory A/B on independent corpus C under the already-frozen rules.
10. Freeze all primary outputs and scores.
11. Run the deterministic evaluator against the committed hashes and hidden evidence files.
12. Optionally run C diagnostic only after both primary waves and scores are frozen.
13. Publish a separate evidence/results PR containing revealed prompts, keys, hash verification, raw run records, deterministic scoring output, wave results, execution evidence, limitations, and conclusion.
14. Merge that results PR whether the result is positive, null, regression, or inconclusive so evidence is preserved rather than discarded.
15. Release the repository-mutation freeze only after the primary study evidence is frozen.

Do not conduct the held-out experiment inside the protocol PR and then close it unmerged. The protocol is a durable repository control/evaluation artifact and should be merged before the study state is selected.

The benchmark protocol, templates, evaluator, and narrow arm markers remain in the repository after the study so future RI changes can be reevaluated without redesigning the methodology. Completed study prompts/results become historical evidence; they are not operational RI input unless another explicit process says otherwise.

## 15. Result report

Include:

- preregistered hashes and study commit;
- default-branch source-state lock evidence and any violations;
- Treatment Delivery Mode, exact aid identity, smoke evidence, delivery failures, and task-level fallbacks;
- exact model/client/configuration and verified isolation state;
- Pilot and confirmatory corpus hashes and evaluator-verified non-overlap;
- ecological raw-pool provenance, normalization contract/hash, and non-overlapping selection record;
- stress/ecological classification per wave;
- all valid and invalid runs with reasons;
- serious-error matrices per wave and combined;
- correctness-score deltas per wave and combined;
- all-case connector-cost gate results per wave and combined;
- equal-correctness connector sensitivity view;
- connector-interaction gain result;
- context-volume metric, completeness, ratios, and gate result or explicit `unavailable`;
- deterministic evaluator output;
- optional C results separately;
- deviations before and after unblinding, clearly distinguished;
- conclusion tied exactly to preregistered rules;
- concrete follow-up only for measured failures.

## 16. What this experiment does not prove

A successful result supports the operational RI route **through the tested Treatment Delivery Mode** for the tested repository state, model/client, and task distribution. It does not prove universal productivity gain, semantic understanding by the graph, graph ranking as authority, Control Map value to agents, another RI delivery mode, or future-state equivalence.

A connector-interaction gain does not prove lower total context cost. An orientation-efficiency claim requires the preregistered context-volume evidence defined above.

No embeddings, vector database, MCP service, graph database, inferred semantic edges, or additional retrieval layer is justified unless measured failure evidence identifies a concrete need that the simpler route cannot address.