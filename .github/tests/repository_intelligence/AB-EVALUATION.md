# Repository Intelligence A/B Evaluation Protocol

## Purpose and estimand

This protocol defines the independent comparative evaluation required by [`REPOSITORY-INTELLIGENCE.md`](../../REPOSITORY-INTELLIGENCE.md#14-evaluation-and-acceptance).

The primary estimand is the **incremental operational value of the normal Repository Intelligence (RI) route** over the repository's ordinary live-GitHub fallback route. The primary A/B does not isolate projection-data value from the workflow that verifies, queries, and interprets that data.

Primary question:

> Given the repository's normal contributor instructions and authority model, does the operational RI route reduce serious routing mistakes or observable orientation cost without degrading material decisions, compared with the ordinary live-GitHub route?

Both primary arms use the same pinned repository state, same model/configuration, same root and scoped `AGENTS.md`, same connector permissions, same client class, and same task prompt. The existing deterministic 12-case corpus remains a regression suite and is not independent held-out evidence.

## 1. Shared `AGENTS.md` baseline

Removing `AGENTS.md` from Control would create a different repository contract and confound the experiment. Both arms therefore read the same instructions.

- `RI-AB-CONTROL`: RI is deliberately unavailable; use ordinary live GitHub tree/search/direct-source reads.
- `RI-AB-TREATMENT`: follow the normal operational RI route.
- `RI-AB-DATA-ONLY`: optional post-primary diagnostic; use only the verified compact Agent Context Surface supplied for the pinned state, without RI query operations or task-specific RI routing output.

The root owner map is shared baseline information. Easy exact-owner cases are ceiling/negative controls. The benchmark marker itself is a small observer intervention and must not be counted as evidence for RI value.

## 2. Experimental design

The unit is one **task × arm** run in a fresh isolated session.

The primary study uses **two independent held-out corpora**, frozen before the first run:

- **Pilot corpus P:** 12 tasks = 6 stress + 6 ecological.
- **Confirmatory corpus C:** 12 different tasks = 6 stress + 6 ecological.

No task prompt may appear in both corpora, and the confirmatory prompts must remain unused until the pilot wave is complete. Both prompt packs, both scoring keys, both ecological selections, and all randomization commitments are frozen before Pilot begins.

### 2.1 Pilot wave

Run **12 pilot tasks × 2 arms = 24 isolated sessions** using a paired randomized crossover design:

- identical task prompt and pinned source state within each pair;
- fresh session for every run;
- randomized A/B order per task from a frozen pilot arm-order seed;
- pairs interleaved over time rather than all A then all B;
- same displayed model family, selectable thinking configuration, connector permissions, client class, and source commit within each pair;
- frozen Pilot scoring key;
- arm-hidden correctness scoring where practical.

Do not selectively rerun failures.

### 2.2 Independent confirmatory wave

LLM output is stochastic, and repeating the same tasks would test repeatability more strongly than generalization. Confirmation therefore uses the **different, independently held-out confirmatory corpus C** frozen before Pilot.

Run **12 confirmatory tasks × 2 arms = 24 additional fresh isolated sessions**:

- confirmatory tasks are disjoint from Pilot tasks;
- another 6 stress + 6 ecological cases are used;
- confirmatory prompts and scoring key were committed by hash before any Pilot run but were not exposed during Pilot;
- A/B order uses a separate frozen confirmatory arm-order seed;
- ecological case selection uses a separate frozen confirmatory selection seed or a deterministic non-overlapping allocation from one combined frozen pool;
- same pinned repository state and same model/configuration target as Pilot unless a preregistered compatibility exception is invoked;
- no prompt, answer-key, scoring-rule, ecological-sampling, cost-gate, or decision-rule changes after Pilot unblinding.

The default study executes the confirmatory wave **regardless of Pilot outcome**. This avoids outcome-dependent stopping and strengthens null/regression evidence as well as positive evidence. A preregistration may choose a conditional confirmation policy only if that stopping rule is fixed before Pilot and the resulting claim is correspondingly narrower.

If model/service drift makes compatible confirmation impossible, record the difference and classify confirmatory evidence separately; do not silently combine incompatible waves.

Primary evidence set under the default protocol: **48 A/B sessions across 24 distinct tasks**.

### 2.3 Optional diagnostic C arm

After **both primary A/B waves and their correctness scores are frozen**, an optional **RI data-only** diagnostic may run on 4–6 frozen cases.

C receives the verified compact Agent Context Surface for the pinned state but no RI query-operation output or task-specific routing suggestion. The agent decides how to use that data and still reads authoritative sources before material decisions.

Interpret C only diagnostically:

- B > A and C ≈ B: projection/data likely carries most of the gain;
- B > C and C ≈ A: workflow/query route likely carries most of the gain;
- B ≈ C ≈ A: no incremental agent value on those diagnostic cases.

C cannot rewrite the primary A/B conclusion.

## 3. Isolation and run validity

Record for every run:

- `conversation_fresh`;
- `memory_enabled`;
- `project_context_present`;
- `prior_repo_context_available`;
- `connector_state_equal` within the pair;
- exact displayed `model_family`;
- exact selectable `thinking_configuration`, or `unavailable`;
- client/environment class.

Required conditions:

1. Fresh conversation for every run.
2. No project/workspace that injects held-out prompts, answer keys, prior-arm output, or prior benchmark-design discussion.
3. No previous-arm output exposed to the paired run.
4. No corrective scoring feedback before both runs in a pair are complete.
5. Equivalent repository/connector access within each pair.
6. Confirmatory prompts remain unexposed to tested sessions until the confirmatory wave starts.

Mark a primary run invalid if:

- `conversation_fresh` is false;
- held-out answer material or previous-arm output was available;
- project context contains benchmark answers;
- connector/repository access differs materially within the pair;
- known prior repository context independently supplies the expected answer rather than merely general repo familiarity.

If the product cannot determine cross-chat memory or prior repo context, record `unavailable`. Treat this as an isolation limitation; if material to interpretation, classify the study `INCONCLUSIVE` or repeat in a cleaner environment.

## 4. Held-out corpora

Each primary wave contains **6 designed stress cases + 6 ecological cases**, for 24 distinct tasks total.

### 4.1 Stress cases

Across each six-case stress half cover a balanced subset of:

- canonical term / synonym pressure;
- overlapping artifact ownership;
- validation/companion routing;
- research-state vs framework-authority separation;
- impact reasoning where navigation/shared hubs must not inflate blast radius;
- stale/unverifiable RI fallback;
- Ukrainian or paraphrased maintainer wording.

Pilot and confirmatory stress prompts must be different. All 12 stress prompts and both scoring-key sections are frozen before the first Pilot run. Stress cases must not be tuned after observing A/B results or RI rankings.

### 4.2 Ecological cases and sampling frame

Ecological cases answer the practical question: does RI help on ordinary UA maintainer work, not only on scenarios designed around RI capabilities?

Before any arm run:

1. Define one **combined ecological source pool** of at least 24 eligible realistic maintainer tasks from a fixed cutoff period or other frozen source set, or define two separately frozen pools of at least 12 eligible tasks per wave.
2. Record pool provenance, cutoff rule, exact exclusion rules, and serialized pool hash outside the tested repository view.
3. Apply only preregistered exclusions, such as duplicate task families, tasks whose answer depends on unavailable external state, or tasks that cannot be run identically in both arms.
4. Freeze the eligible pool before selection.
5. Select six Pilot ecological cases and six **different** confirmatory ecological cases using preregistered seeded selection, without replacement across waves.
6. Freeze selected opaque case IDs and selection hashes before Pilot begins.
7. Do not manually replace a selected case because RI is expected to perform poorly or well.

Across the combined 12 ecological cases include at least two easy exact-owner/negative-control cases and at least two legitimate-new-artifact cases where no existing owner fully covers the need, with at least one of each anchor type allocated to each wave. If those anchors are fixed rather than randomly produced, identify and allocate them before seeded selection and sample the remaining slots from the frozen pool.

Report ecological results separately from stress results and separately by wave. A gain confined to designed stress cases is not broad routine productivity evidence.

### 4.3 Hidden prompts and answer-key secrecy

Do not commit held-out prompts or scoring keys before execution. Keep them outside the repository view exposed to tested sessions.

Preregister only non-revealing metadata and cryptographic commitments:

- protocol/corpus version;
- Pilot and confirmatory case counts and 6/6 classifications;
- confirmation-corpus non-overlap rule;
- ecological source-pool provenance/cutoff rule;
- ecological pool SHA-256;
- Pilot selected ecological IDs SHA-256;
- confirmatory selected ecological IDs SHA-256;
- Pilot prompt-pack SHA-256 and scoring-key SHA-256;
- confirmatory prompt-pack SHA-256 and scoring-key SHA-256;
- source commit;
- model/configuration target;
- Pilot and confirmatory arm-order seed SHA-256 values;
- ecological selection seed commitment(s);
- primary/secondary endpoints;
- cost acceptance gate and efficiency threshold;
- final decision rule.

After all primary outputs and scoring are frozen, prompts/key/raw records may be published and verified against the commitments.

## 5. Primary arms

### A — Control

Allowed:

- GitHub tree/directory reads;
- code/file search;
- direct file reads;
- PR/diff/review/check/branch/commit reads when task-relevant;
- maintained source cross-links/navigation.

Disallowed for orientation:

- `assets/repository-intelligence/agent-context.json`;
- full/generated Graph View;
- RI query operations such as `context-for-task`, `find-owner`, `term-preflight`, `artifact-preflight`, `validation-plan`;
- Repository Control Map;
- copied RI results from another session.

Control may read `.github/REPOSITORY-INTELLIGENCE.md` only when the task itself is specifically about RI architecture.

### B — Treatment

Treatment follows the production RI route:

- verify compact-surface freshness for the pinned state;
- use the narrowest appropriate RI operation;
- read owning sources before material decisions;
- use live GitHub fallback when RI is stale, missing, truncated, ambiguous, or unsupported;
- never infer authority from ranking/graph structure;
- avoid loading the full graph when compact data is sufficient.

The A/B result supports or rejects the **operational RI route**, not projection-only value.

## 6. Neutral run envelope

```text
Repository: UncertaintyArchitectureGroup/uncertainty-architecture
Pinned source state: <commit SHA>
Experiment arm: RI-AB-CONTROL | RI-AB-TREATMENT | RI-AB-DATA-ONLY
Task ID: <opaque ID>
Wave: PILOT | CONFIRMATORY | DIAGNOSTIC

Follow the repository's applicable contributor instructions and complete the task below. Do not ask for or search for benchmark answer keys, prior experiment outputs, or hidden scoring material. Report repository sources relied on and distinguish verified facts from inference.

Task:
<held-out prompt>
```

Opaque IDs must not reveal expected owner or category. Do not tell either arm what RI is expected to improve.

## 7. Observable instrumentation

Never use hidden model reasoning or infer when the model internally knew the answer.

Record where observable:

- ordered connector/tool calls;
- total connector calls to final answer;
- broad search calls to final answer;
- ordered files opened;
- total distinct files opened;
- calls before first explicit visible owner/route assertion, when observable;
- RI operations and returned payload bytes;
- measured input/context/token volume when exposed;
- elapsed time only when reliably observable;
- tool errors, truncation, stale-context events, fallbacks;
- final response/transcript reference.

Do not estimate unavailable token counts or latency from prose length.

## 8. Correctness scoring

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

Preferred blind scoring order: remove arm labels/route metadata from scoring copies, randomize pair order, score against frozen key, lock scores, then reveal arms and add cost data.

For ecological correctness, preregister a mechanically decidable non-regression rule. The recommended default is **median paired total correctness delta (B−A) >= 0** within each wave, with zero ecological `A correct / B wrong` serious-error reversals.

## 9. Cost accounting and acceptance gate

A positive usefulness result requires a preregistered **numeric or otherwise mechanically decidable cost rule**. `Clearly disproportionate` must not be decided after unblinding.

### 9.1 Primary cost accounting

The primary cost gate includes **all valid ecological cases**, including cases where Treatment prevents a serious routing error. Correctness value may justify a high-cost case in interpretation, but the case must not be removed from primary cost accounting.

The preregistration must define:

- `primary_cost_metric` — e.g. ecological median total connector calls;
- `acceptable_median_ratio_b_over_a` or another explicit threshold;
- `acceptable_high_overhead_case_count` and the threshold defining high overhead;
- ratio behavior when the Control denominator is zero;
- treatment of unavailable token/time metrics.

Recommended default if the study owner has no better prior threshold:

- ecological median connector-call ratio B/A <= **1.50**;
- no more than **2 of 6** ecological cases with connector-call ratio > **2.00**;
- if A=0 and B=0, define the case ratio as 1.0; if A=0 and B>0, define it as infinity for gate purposes;
- serious-error-prevention cases remain included in both median and high-overhead counts.

Apply the cost gate independently to Pilot and confirmatory ecological halves. Also report the combined 12-case ecological view.

### 9.2 Equal-correctness sensitivity view

Report a secondary cost view using only ecological pairs whose total correctness score and serious-error status are equal across arms. This estimates orientation efficiency when correctness is held observationally equal.

This sensitivity view does **not** replace the all-case primary cost gate. If no equal-correctness ecological pairs exist, report the view as unavailable.

### 9.3 Efficiency-gain threshold

Because the primary question allows RI to demonstrate value through lower orientation cost even when correctness is equivalent, preregister an **efficiency-gain threshold** separately from the maximum acceptable-overhead gate.

Recommended default: ecological median primary-cost ratio B/A <= **0.80** in each wave, with the ecological correctness non-regression rule satisfied and zero reverse serious-error reversals. A different threshold may be used only if frozen before Pilot.

Changing any cost or efficiency threshold after unblinding invalidates the preregistered GO decision and may only be reported as exploratory.

## 10. Endpoints and Pilot interpretation

Primary endpoint: paired serious-error matrix across valid pairs:

- A wrong / B correct;
- A correct / B wrong;
- both correct;
- both wrong.

Secondary endpoints: per-case correctness delta; median paired correctness delta; observable cost metrics; equal-correctness cost sensitivity; stress/ecological split.

For the 12-pair **Pilot**, report an interim descriptive classification only:

- **PROVISIONAL CORRECTNESS SIGNAL:** >=2 valid `A wrong / B correct`, 0 reverse serious errors, ecological correctness non-regression passes, and Pilot cost gate passes.
- **WEAK CORRECTNESS SIGNAL:** exactly 1 positive reversal, 0 reverse serious errors, ecological correctness non-regression passes.
- **PROVISIONAL EFFICIENCY SIGNAL:** correctness is non-worse, zero reverse serious errors, and the preregistered efficiency-gain threshold passes.
- **NO PILOT SIGNAL:** neither correctness nor efficiency signal is met.
- **PILOT REGRESSION:** Treatment introduces a reverse serious-error reversal or fails the preregistered ecological correctness non-regression rule without a predefined interpretation exception.
- **PILOT INCONCLUSIVE:** invalid pairs, isolation uncertainty, source-state mismatch, scoring ambiguity, or protocol defect prevents defensible interpretation.

Under the default always-run protocol, Pilot classification does not stop or alter the confirmatory wave. Pilot alone cannot produce final `DEMONSTRATED GO`.

## 11. Confirmatory and final decision

The confirmatory wave uses its independent held-out corpus and is scored without changing any rule after Pilot.

### 11.1 Correctness-value route

Final **DEMONSTRATED CORRECTNESS GO** requires all of:

- both 12-pair waves complete under compatible frozen conditions;
- confirmatory wave contains at least **1** `A wrong / B correct` serious-error reversal;
- confirmatory wave contains **0** `A correct / B wrong` serious-error reversals;
- combined Pilot+confirmatory positive serious-error reversals are at least **3**;
- combined reverse serious-error reversals are **0**;
- ecological correctness non-regression passes independently in both waves;
- primary all-case cost gate passes independently in both waves.

If Pilot shows a correctness signal but the independent confirmatory corpus does not satisfy these rules, the correctness claim is **NOT CONFIRMED** rather than GO.

### 11.2 Efficiency-value route

Final **DEMONSTRATED EFFICIENCY GO** requires all of:

- both waves complete under compatible frozen conditions;
- zero reverse serious-error reversals in either wave;
- ecological correctness non-regression passes independently in both waves;
- the preregistered efficiency-gain threshold passes independently in both waves.

This route does not require serious-error reversals because it claims reduced orientation cost without degraded material decisions, not improved correctness.

### 11.3 Other final outcomes

- **CORRECTNESS GAIN / COST NOT ACCEPTED:** correctness reversal thresholds are met, but the primary all-case cost gate fails in either wave.
- **NO INCREMENTAL VALUE SHOWN:** neither demonstrated correctness nor demonstrated efficiency route is met, with no material Treatment regression.
- **REGRESSION:** any reverse serious-error reversal occurs, or the preregistered ecological correctness non-regression rule fails materially under otherwise valid conditions.
- **INCONCLUSIVE:** invalid pairs, incompatible model/source conditions, isolation uncertainty, scoring ambiguity, or protocol defects prevent a defensible final comparison.

Do not substitute narrative judgment for these preregistered rules after unblinding.

## 12. Execution lifecycle

1. Merge the protocol/infrastructure PR.
2. Freeze a specific `main` source commit for evaluation.
3. Create a preregistration record outside the tested Git tree (for example a GitHub Issue) containing only commitments/metadata, not hidden answers.
4. Freeze **both independent prompt packs**, both scoring keys, the combined/separate ecological source pools, non-overlapping ecological selections, all seeds, model/configuration, cost/efficiency gates, and final decision rules.
5. Run Pilot A/B on corpus P.
6. Freeze Pilot outputs and scores; do not modify confirmatory material.
7. Run confirmatory A/B on independent corpus C under the already-frozen rules.
8. Freeze all primary outputs and scores.
9. Optionally run C diagnostic only after both primary waves are frozen.
10. Publish a separate evidence/results PR containing revealed prompts, both keys, hash verification, raw run records, scoring, wave results, limitations, and conclusion.
11. Merge the results PR whether the result is positive, null, regression, or inconclusive, so evidence is preserved rather than discarded.

Do not conduct the held-out experiment inside the protocol PR and then close it unmerged. The protocol is a durable repository control/evaluation artifact and should be merged before the frozen evaluation state is selected.

The protocol, example templates, and narrow benchmark markers remain in the repository after the study so future RI changes can be reevaluated without redesigning the methodology. Completed study prompts/results become historical evidence; they are not operational RI input unless another explicit process says otherwise.

## 13. Result report

Include:

- preregistered hashes and source commit;
- exact model/client/configuration and isolation limitations;
- Pilot and confirmatory corpus hashes and proof of non-overlap;
- ecological source-pool provenance and non-overlapping selection record;
- stress/ecological classification per wave;
- all valid and invalid runs with reasons;
- serious-error matrices per wave and combined;
- correctness-score deltas per wave and combined;
- all-case primary cost-gate results per wave and combined;
- equal-correctness cost sensitivity view;
- efficiency-gain threshold results;
- optional C results separately;
- deviations before and after unblinding, clearly distinguished;
- conclusion tied exactly to preregistered rules;
- concrete follow-up only for measured failures.

## 14. What this experiment does not prove

A successful result supports the operational RI route for the tested repository state, model/client, and task distribution. It does not prove universal productivity gain, semantic understanding by the graph, graph ranking as authority, Control Map value to agents, or future-state equivalence.

No embeddings, vector database, MCP service, graph database, inferred semantic edges, or additional retrieval layer is justified unless measured failure evidence identifies a concrete need that the simpler route cannot address.
