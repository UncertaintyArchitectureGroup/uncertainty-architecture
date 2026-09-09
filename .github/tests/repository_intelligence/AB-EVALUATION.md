# Repository Intelligence A/B Evaluation Protocol

> Protocol version: 5

## Purpose and estimand

This protocol defines the independent comparative evaluation required by [`REPOSITORY-INTELLIGENCE.md`](../../REPOSITORY-INTELLIGENCE.md#14-evaluation-and-acceptance).

The primary estimand is the **incremental operational value of the normal Repository Intelligence (RI) route** over the repository's ordinary live-GitHub fallback route under one pinned repository state. The primary A/B does not isolate projection-data value from the workflow that verifies, queries, and interprets that data.

Primary question:

> Given the repository's normal contributor instructions and authority model, does the operational RI route reduce serious routing mistakes or observable orientation cost without degrading material decisions, compared with a pinned-state live-GitHub fallback route?

Both primary arms use the same pinned repository state, same model/configuration, same root and scoped `AGENTS.md`, same connector permissions, same client class, and same task prompt. The existing deterministic 12-case corpus remains a regression suite and is not independent held-out evidence.

## 1. Shared `AGENTS.md` baseline

Removing `AGENTS.md` from Control would create a different repository contract and confound the experiment. Both arms therefore read the same instructions.

- `RI-AB-CONTROL`: RI is deliberately unavailable; use the pinned-state live GitHub route defined by this protocol.
- `RI-AB-TREATMENT`: follow the normal operational RI route through the preregistered Treatment Delivery Mode.
- `RI-AB-DATA-ONLY`: optional post-primary diagnostic; use only the verified compact Agent Context Surface supplied for the pinned state, without RI query operations or task-specific RI routing output.

The root owner map is shared baseline information. Easy exact-owner cases are ceiling/negative controls. The benchmark marker itself is a small observer intervention and must not be counted as evidence for RI value.

## 2. Experimental design

The unit is one **task × arm** run in a fresh isolated session.

The primary study uses **two independent held-out corpora**, frozen before the first run:

- **Pilot corpus P:** 12 tasks = 6 stress + 6 ecological.
- **Confirmatory corpus C:** 12 different tasks = 6 stress + 6 ecological.

No task prompt may appear in both corpora, and the confirmatory prompts must remain unused until the Pilot wave is complete. Both prompt packs, both scoring keys, both ecological selections, and all randomization commitments are frozen before Pilot begins.

### 2.1 Pilot wave

Run **12 Pilot tasks × 2 arms = 24 isolated sessions** using a paired randomized crossover design:

- identical task prompt and pinned source state within each pair;
- fresh session for every run;
- randomized A/B order per task from a frozen Pilot arm-order seed;
- pairs interleaved over time rather than all A then all B;
- same displayed model family, selectable thinking configuration, connector permissions, client class, and source commit within each pair;
- frozen Pilot scoring key;
- arm-hidden correctness scoring where practical.

Do not selectively rerun failures unless a separate infrastructure-retry rule was preregistered before the first run. A rerun never replaces a valid unfavorable result.

### 2.2 Independent confirmatory wave

LLM output is stochastic, and repeating the same tasks would test repeatability more strongly than generalization. Confirmation therefore uses the **different, independently held-out confirmatory corpus C** frozen before Pilot.

Run **12 confirmatory tasks × 2 arms = 24 additional fresh isolated sessions**:

- confirmatory tasks are disjoint from Pilot tasks;
- another 6 stress + 6 ecological cases are used;
- confirmatory prompts and scoring key were committed by hash before any Pilot run but were not exposed during Pilot;
- A/B order uses a separate frozen confirmatory arm-order seed;
- ecological case selection uses a separate frozen confirmatory selection seed or a deterministic non-overlapping allocation from one combined frozen pool;
- same pinned repository state and same model/configuration target as Pilot unless a preregistered compatibility exception is invoked;
- no prompt, answer-key, scoring-rule, ecological-sampling, cost-gate, execution-mode, or decision-rule changes after Pilot unblinding.

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

## 3. Execution eligibility and pinned-state contract

The held-out study must not start merely because a commit SHA has been chosen. The actual client/tooling used for the study must first demonstrate that both arms can operate against the **same exact frozen state** and that Treatment can actually receive the intended RI aid.

### 3.1 Pinned-state tool policy

All repository facts used for scoring must be attributable to the preregistered source commit.

For both primary arms:

- direct file reads, directory/tree reads, commit facts, and other repository operations used as evidence must be explicitly ref-addressable to the frozen source state;
- a tool operation that only searches or indexes the repository's moving default branch is **unpinned** and must not be used for primary orientation, candidate discovery, or evidence;
- unpinned search results must not be used merely as hints and then revalidated at the frozen SHA, because path/name leakage from a later repository state would still contaminate orientation;
- if the client later provides a demonstrably ref-addressable search operation, its exact mode may be preregistered and used identically wherever applicable;
- any accidental unpinned repository search during a primary run is recorded as a pinned-state protocol violation and invalidates that run unless the preregistered scorer can prove the call returned no repository information and could not influence the run.

The default connector-only Control route is therefore **pinned tree/directory traversal + direct pinned source reads + ref-addressable GitHub facts**, not moving-default-branch code search.

### 3.2 Treatment Delivery Mode

The study must preregister exactly one primary **Treatment Delivery Mode** and use it consistently across all Treatment runs:

- `local_cli` — the accepted RI producer/query CLI is available against the pinned state;
- `connector_compact_surface` — the agent receives the complete verified compact Agent Context Surface through the connector/client and performs the documented bounded interpretation itself;
- `dedicated_adapter` — an explicitly identified adapter exposes the accepted RI operations for the pinned state.

Do not mix delivery modes within one primary study. A later study may compare delivery modes explicitly.

For the first ChatGPT + GitHub-connector evaluation, `connector_compact_surface` is the preferred mode because it measures the architecture in the client environment that motivated this benchmark. In that mode, logical operations such as `find_owner` or `validation_plan` are **not presumed to be executable RPCs**. The treatment is the documented use of the complete verified compact surface plus authoritative pinned source reads.

Preregistration records the chosen mode, surface path, pinned blob identity or full-payload SHA-256, freshness evidence, and whether complete-payload delivery/truncation checks passed.

### 3.3 Treatment delivery failure versus task-level fallback

Production RI correctly falls back to live repository reading when a query is ambiguous or unsupported. The experiment distinguishes that behavior from failure to deliver Treatment itself:

- **Treatment delivery failure:** the preregistered RI surface/adapter/CLI cannot be obtained, verified, or read completely for the pinned state, or the actual run silently receives a different delivery mode. The run is invalid; do not score it as if Treatment simply chose Control.
- **Task-level RI fallback:** Treatment was successfully delivered and verified, but the task-specific RI evidence is ambiguous, stale in a task-specific way, or unsupported and the documented production route falls back to pinned live sources. This remains a valid Treatment behavior and its cost/outcome count normally.

Systematic Treatment delivery failure is an experiment-infrastructure defect and may make the study `INCONCLUSIVE`; it is not evidence that RI has no incremental value.

### 3.4 Non-scored execution smoke test

Before freezing the preregistration as executable, run a **non-scored smoke test** using one or more synthetic/non-held-out tasks that are not derived from either primary corpus and disclose no held-out answer material.

The smoke test must establish, in the actual study client:

1. pinned tree/direct-file access works for the frozen source commit;
2. unpinned search can be prevented or is absent from the allowed primary tool route;
3. the selected Treatment Delivery Mode works for the same commit;
4. the complete Treatment surface/payload can be verified and is not truncated;
5. required run-record fields can actually be observed and captured;
6. Control and Treatment have equivalent connector permissions aside from the deliberate RI ablation;
7. no held-out prompt, scoring key, prior-arm output, or cross-wave material is exposed.

Record smoke-test evidence in the preregistration record outside the tested Git tree. **Do not start the 48 primary sessions unless all mandatory execution-eligibility checks pass.** If the frozen commit cannot satisfy Treatment delivery, select a different eligible frozen commit before hashing the study corpora or fix the infrastructure first.

## 4. Isolation and run validity

Record for every run:

- `conversation_fresh`;
- `memory_enabled`;
- `project_context_present`;
- `prior_repo_context_available`;
- `connector_state_equal` within the pair;
- exact displayed `model_family`;
- exact selectable `thinking_configuration`, or `unavailable`;
- client/environment class;
- Treatment Delivery Mode where applicable;
- pinned-state protocol violations;
- Treatment delivery status and task-level fallback status where applicable.

Required conditions:

1. Fresh conversation for every run.
2. No project/workspace that injects held-out prompts, answer keys, prior-arm output, or prior benchmark-design discussion.
3. No previous-arm output exposed to the paired run.
4. No corrective scoring feedback before both runs in a pair are complete.
5. Equivalent repository/connector access within each pair.
6. Confirmatory prompts remain unexposed to tested sessions until the confirmatory wave starts.
7. All repository evidence used for orientation/scoring obeys the pinned-state tool policy.
8. Treatment uses the preregistered delivery mode and exact pinned surface/adapter identity.

Mark a primary run invalid if:

- `conversation_fresh` is false;
- held-out answer material or previous-arm output was available;
- project context contains benchmark answers;
- connector/repository access differs materially within the pair;
- known prior repository context independently supplies the expected answer rather than merely general repo familiarity;
- unpinned repository search or other moving-state evidence contaminates the run;
- Treatment delivery fails before task-level RI reasoning can occur.

If the product cannot determine cross-chat memory or prior repo context, record `unavailable`. Treat this as an isolation limitation; if material to interpretation, classify the study `INCONCLUSIVE` or repeat in a cleaner environment.

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
- Ukrainian or paraphrased maintainer wording.

Pilot and confirmatory stress prompts must be different. All 12 stress prompts and both scoring-key sections are frozen before the first Pilot run. Stress cases must not be tuned after observing A/B results or RI rankings.

### 5.2 Ecological cases, sampling frame, and neutral normalization

Ecological cases answer the practical question: does RI help on ordinary UA maintainer work, not only on scenarios designed around RI capabilities?

Real maintainer requests are often conversational fragments such as “fix it”, “review this PR”, or “what next?”. A fresh benchmark session cannot use those fragments without their missing context. The ecological pool therefore uses a frozen **neutral normalization** step before seeded selection.

Normalization may:

- expand pronouns or omitted references with facts explicitly present in the source event/context;
- include the minimal artifact/PR/change facts needed to make the task self-contained;
- preserve the original requested outcome, language where practical, and uncertainty.

Normalization must not:

- name or hint the expected canonical owner unless the original request itself did so;
- add an expected repository path, validator, companion file, canonical term, or RI vocabulary that was not necessary to restate the source request;
- add facts learned from RI rankings, the answer key, or later repository investigation;
- simplify a difficult source task into an easier owner-identification prompt.

If a source request cannot be made self-contained without materially revealing the expected answer, exclude it under a preregistered normalization-exclusion rule rather than rewriting it opportunistically.

Before any arm run:

1. Define one **combined raw ecological source pool** of realistic maintainer tasks from a fixed cutoff period or other frozen source set, or define two separately frozen raw pools.
2. Record raw-pool provenance, cutoff rule, and raw serialized pool hash outside the tested repository view.
3. Apply only preregistered exclusions, including duplicate task families, tasks whose answer depends on unavailable external state, tasks that cannot be run identically in both arms, and tasks that cannot be neutrally normalized.
4. Neutrally normalize every remaining eligible source item **before seeded case selection**.
5. Freeze the normalized eligible pool and its serialized SHA-256.
6. The combined normalized eligible pool must contain at least 24 tasks, or each separate wave pool must contain at least 12.
7. Select six Pilot ecological cases and six **different** confirmatory ecological cases using preregistered seeded selection, without replacement across waves.
8. Freeze selected opaque case IDs and selection hashes before Pilot begins.
9. Do not manually replace a selected case because RI is expected to perform poorly or well.

Across the combined 12 ecological cases include at least two easy exact-owner/negative-control cases and at least two legitimate-new-artifact cases where no existing owner fully covers the need, with at least one of each anchor type allocated to each wave. If those anchors are fixed rather than randomly produced, identify and normalize them before seeded selection and sample the remaining slots from the frozen normalized pool.

Report ecological results separately from stress results and separately by wave. A gain confined to designed stress cases is not broad routine productivity evidence.

### 5.3 Hidden prompts and answer-key secrecy

Do not commit held-out prompts or scoring keys before execution. Keep them outside the repository view exposed to tested sessions.

Preregister only non-revealing metadata and cryptographic commitments:

- protocol/corpus version;
- Pilot and confirmatory case counts and 6/6 classifications;
- confirmation-corpus non-overlap rule;
- ecological raw source-pool provenance/cutoff rule and SHA-256;
- ecological normalization contract/version and normalized eligible-pool SHA-256;
- Pilot selected ecological IDs SHA-256;
- confirmatory selected ecological IDs SHA-256;
- Pilot prompt-pack SHA-256 and scoring-key SHA-256;
- confirmatory prompt-pack SHA-256 and scoring-key SHA-256;
- source commit;
- pinned-state tool policy;
- Treatment Delivery Mode and verified surface/adapter identity;
- execution smoke-test result/evidence reference;
- model/configuration target;
- Pilot and confirmatory arm-order seed SHA-256 values;
- ecological selection seed commitment(s);
- primary/secondary endpoints;
- cost acceptance gate and efficiency threshold;
- final decision rule.

After all primary outputs and scoring are frozen, prompts/key/raw records may be published and verified against the commitments.

## 6. Primary arms

### A — Control

Control follows ordinary repository authority and contributor rules but receives no RI aid.

Allowed for primary orientation:

- ref-addressable GitHub tree/directory reads at the frozen source state;
- direct file reads at the frozen source state;
- ref-addressable PR/diff/review/check/branch/commit reads when task-relevant and when their use is compatible with the frozen-state task;
- maintained cross-links/navigation discovered from pinned source files.

Conditionally allowed:

- code/file search only when the exact client operation is proven and preregistered to search the frozen ref rather than the moving default branch.

Disallowed for orientation:

- unpinned/default-branch repository search;
- `assets/repository-intelligence/agent-context.json`;
- full/generated Graph View;
- RI query operations such as `context-for-task`, `find-owner`, `term-preflight`, `artifact-preflight`, `validation-plan`;
- Repository Control Map;
- copied RI results from another session.

Control may read `.github/REPOSITORY-INTELLIGENCE.md` only when the task itself is specifically about RI architecture.

### B — Treatment

Treatment follows the production RI route through the preregistered Treatment Delivery Mode:

- establish/verify the exact compact surface, CLI, or adapter identity for the frozen state;
- use that accepted RI aid for orientation/preflight according to its delivery mode;
- read owning sources at the frozen state before material decisions;
- use pinned live-GitHub fallback when task-level RI evidence is ambiguous or unsupported;
- never infer authority from ranking/graph structure;
- avoid loading the full graph when compact data is sufficient.

For `connector_compact_surface`, the LLM inspects the complete verified surface directly; do not pretend unavailable local CLI operations were executed. Record which logical RI task was attempted and which surface evidence was used.

The A/B result supports or rejects the **operational RI route as delivered through the preregistered mode**, not projection-only value and not untested delivery modes.

## 7. Neutral run envelope

```text
Repository: UncertaintyArchitectureGroup/uncertainty-architecture
Pinned source state: <commit SHA>
Experiment arm: RI-AB-CONTROL | RI-AB-TREATMENT | RI-AB-DATA-ONLY
Treatment delivery mode: <mode or not-applicable>
Task ID: <opaque ID>
Wave: PILOT | CONFIRMATORY | DIAGNOSTIC

Follow the repository's applicable contributor instructions and complete the task below using only repository facts attributable to the pinned source state. Do not ask for or search for benchmark answer keys, prior experiment outputs, hidden scoring material, or another wave's task material. Report repository sources relied on and distinguish verified facts from inference. Follow the benchmark protocol's pinned-state tool rules; do not use moving-default-branch repository search unless the preregistration explicitly proves that operation is ref-addressable to the pinned state.

Task:
<held-out prompt>
```

Opaque IDs must not reveal expected owner or category. Do not tell either arm what RI is expected to improve.

## 8. Observable instrumentation

Never use hidden model reasoning or infer when the model internally knew the answer.

Record where observable:

- ordered connector/tool calls;
- whether each repository call was explicitly pinned/ref-addressable;
- total connector calls to final answer;
- broad search calls to final answer, separated into allowed ref-addressable search and prohibited/unpinned search;
- ordered files opened;
- total distinct source files opened;
- calls before first explicit visible owner/route assertion, when observable;
- Treatment Delivery Mode and delivery-verification status;
- RI logical operations/evidence used and returned payload bytes when applicable;
- task-level RI fallback events separately from Treatment delivery failure;
- measured input/context/token volume when exposed;
- elapsed time only when reliably observable;
- tool errors, truncation, stale-context events, fallbacks;
- final response/transcript reference.

Do not estimate unavailable token counts or latency from prose length.

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

Preferred blind scoring order: remove arm labels/route metadata from scoring copies, randomize pair order, score against frozen key, lock scores, then reveal arms and add cost data.

For ecological correctness, preregister a mechanically decidable non-regression rule. The recommended default is **median paired total correctness delta (B−A) >= 0** within each wave, with zero ecological `A correct / B wrong` serious-error reversals.

## 10. Cost accounting and acceptance gate

A positive usefulness result requires a preregistered **numeric or otherwise mechanically decidable cost rule**. `Clearly disproportionate` must not be decided after unblinding.

### 10.1 Primary paired-cost statistic

For each valid ecological pair `i`, define the per-case connector-call ratio:

`r_i = B_i / A_i`

where `A_i` and `B_i` are total connector calls to final answer for Control and Treatment respectively.

Zero-denominator rule:

- `A_i = 0` and `B_i = 0` → `r_i = 1.0`;
- `A_i = 0` and `B_i > 0` → `r_i = infinity` for gate purposes.

The primary per-wave cost statistic is **the median of the paired ratios `r_i` across all valid ecological pairs in that wave**. It is not the ratio of `median(B_i)` to `median(A_i)`.

A high-overhead ecological case is one whose own `r_i` exceeds the preregistered high-overhead threshold.

### 10.2 Primary cost gate

The primary cost gate includes **all valid ecological cases**, including cases where Treatment prevents a serious routing error. Correctness value may justify a high-cost case in interpretation, but the case must not be removed from primary cost accounting.

Recommended default if the study owner has no better prior threshold:

- median of paired ecological connector-call ratios <= **1.50**;
- no more than **2 of 6** ecological cases with `r_i > 2.00`;
- serious-error-prevention cases remain included in both the median and high-overhead counts.

Apply the cost gate independently to Pilot and confirmatory ecological halves. Also report the combined 12-case ecological median of paired ratios.

### 10.3 Equal-correctness sensitivity view

Report a secondary cost view using only ecological pairs whose total correctness score and serious-error status are equal across arms. Compute the same median-of-paired-ratios statistic on that filtered set.

This sensitivity view does **not** replace the all-case primary cost gate. If no equal-correctness ecological pairs exist, report the view as unavailable.

### 10.4 Efficiency-gain threshold

Because the primary question allows RI to demonstrate value through lower orientation cost even when correctness is equivalent, preregister an **efficiency-gain threshold** separately from the maximum acceptable-overhead gate.

Recommended default: median of paired ecological primary-cost ratios <= **0.80** in each wave, with the ecological correctness non-regression rule satisfied and zero reverse serious-error reversals. A different threshold may be used only if frozen before Pilot.

Changing any cost or efficiency threshold after unblinding invalidates the preregistered GO decision and may only be reported as exploratory.

## 11. Endpoints and Pilot interpretation

Primary endpoint: paired serious-error matrix across valid pairs:

- A wrong / B correct;
- A correct / B wrong;
- both correct;
- both wrong.

Secondary endpoints: per-case correctness delta; median paired correctness delta; observable cost metrics; equal-correctness cost sensitivity; stress/ecological split; Treatment-delivery/fallback behavior.

For the 12-pair **Pilot**, report an interim descriptive classification only:

- **PROVISIONAL CORRECTNESS SIGNAL:** >=2 valid `A wrong / B correct`, 0 reverse serious errors, ecological correctness non-regression passes, and Pilot cost gate passes.
- **WEAK CORRECTNESS SIGNAL:** exactly 1 positive reversal, 0 reverse serious errors, ecological correctness non-regression passes.
- **PROVISIONAL EFFICIENCY SIGNAL:** correctness is non-worse, zero reverse serious errors, and the preregistered efficiency-gain threshold passes.
- **NO PILOT SIGNAL:** neither correctness nor efficiency signal is met.
- **PILOT REGRESSION:** Treatment introduces a reverse serious-error reversal or fails the preregistered ecological correctness non-regression rule without a predefined interpretation exception.
- **PILOT INCONCLUSIVE:** invalid pairs, Treatment-delivery failure, pinned-state contamination, isolation uncertainty, source-state mismatch, scoring ambiguity, or protocol defect prevents defensible interpretation.

Under the default always-run protocol, Pilot classification does not stop or alter the confirmatory wave unless infrastructure validity has failed. Pilot alone cannot produce final `DEMONSTRATED GO`.

## 12. Confirmatory and final decision

The confirmatory wave uses its independent held-out corpus and is scored without changing any rule after Pilot.

### 12.1 Correctness-value route

Final **DEMONSTRATED CORRECTNESS GO** requires all of:

- both 12-pair waves complete under compatible frozen conditions and the same Treatment Delivery Mode;
- confirmatory wave contains at least **1** `A wrong / B correct` serious-error reversal;
- confirmatory wave contains **0** `A correct / B wrong` serious-error reversals;
- combined Pilot+confirmatory positive serious-error reversals are at least **3**;
- combined reverse serious-error reversals are **0**;
- ecological correctness non-regression passes independently in both waves;
- primary all-case cost gate passes independently in both waves;
- no material pinned-state contamination or systematic Treatment-delivery failure invalidates the evidence.

If Pilot shows a correctness signal but the independent confirmatory corpus does not satisfy these rules, the correctness claim is **NOT CONFIRMED** rather than GO.

### 12.2 Efficiency-value route

Final **DEMONSTRATED EFFICIENCY GO** requires all of:

- both waves complete under compatible frozen conditions and the same Treatment Delivery Mode;
- zero reverse serious-error reversals in either wave;
- ecological correctness non-regression passes independently in both waves;
- the preregistered efficiency-gain threshold passes independently in both waves;
- no material pinned-state contamination or systematic Treatment-delivery failure invalidates the evidence.

This route does not require serious-error reversals because it claims reduced orientation cost without degraded material decisions, not improved correctness.

### 12.3 Other final outcomes

- **CORRECTNESS GAIN / COST NOT ACCEPTED:** correctness reversal thresholds are met, but the primary all-case cost gate fails in either wave.
- **NOT CONFIRMED:** Pilot shows a correctness signal that is not supported by the independent confirmatory corpus.
- **NO INCREMENTAL VALUE SHOWN:** neither demonstrated correctness nor demonstrated efficiency route is met, with no material Treatment regression and valid Treatment delivery.
- **REGRESSION:** any reverse serious-error reversal occurs, or the preregistered ecological correctness non-regression rule fails materially under otherwise valid conditions.
- **INCONCLUSIVE:** invalid pairs, Treatment-delivery failure, pinned-state contamination, incompatible model/source conditions, isolation uncertainty, scoring ambiguity, or protocol defects prevent a defensible final comparison.

Do not substitute narrative judgment for these preregistered rules after unblinding.

## 13. Execution lifecycle

1. Merge the protocol/infrastructure PR.
2. Identify a candidate `main` source commit for evaluation.
3. Run the non-scored execution smoke test against that exact commit in the actual study client.
4. Verify pinned-state access, the selected Treatment Delivery Mode, complete/non-truncated RI payload, surface identity/freshness evidence, connector parity, and instrumentation capture.
5. Only after the smoke test passes, designate the commit as the frozen study source state.
6. Create a preregistration record outside the tested Git tree (for example a GitHub Issue) containing commitments/metadata, Treatment delivery evidence, and smoke-test evidence, not hidden answers.
7. Freeze **both independent prompt packs**, both scoring keys, the raw and normalized ecological pools, non-overlapping ecological selections, all seeds, model/configuration, cost/efficiency gates, and final decision rules.
8. Run Pilot A/B on corpus P.
9. Freeze Pilot outputs and scores; do not modify confirmatory material.
10. Run confirmatory A/B on independent corpus C under the already-frozen rules.
11. Freeze all primary outputs and scores.
12. Optionally run C diagnostic only after both primary waves are frozen.
13. Publish a separate evidence/results PR containing revealed prompts, both keys, hash verification, raw run records, scoring, wave results, execution evidence, limitations, and conclusion.
14. Merge the results PR whether the result is positive, null, regression, or inconclusive, so evidence is preserved rather than discarded.

Do not conduct the held-out experiment inside the protocol PR and then close it unmerged. The protocol is a durable repository control/evaluation artifact and should be merged before the frozen evaluation state is selected.

The protocol, example templates, and narrow benchmark markers remain in the repository after the study so future RI changes can be reevaluated without redesigning the methodology. Completed study prompts/results become historical evidence; they are not operational RI input unless another explicit process says otherwise.

## 14. Result report

Include:

- preregistered hashes and source commit;
- pinned-state tool policy and any violations;
- Treatment Delivery Mode, exact surface/adapter identity, smoke-test evidence, delivery failures, and task-level fallbacks;
- exact model/client/configuration and isolation limitations;
- Pilot and confirmatory corpus hashes and proof of non-overlap;
- ecological raw-pool provenance, normalization contract/hash, and non-overlapping selection record;
- stress/ecological classification per wave;
- all valid and invalid runs with reasons;
- serious-error matrices per wave and combined;
- correctness-score deltas per wave and combined;
- all-case primary cost-gate results per wave and combined using the frozen median-of-paired-ratios formula;
- equal-correctness cost sensitivity view;
- efficiency-gain threshold results;
- optional C results separately;
- deviations before and after unblinding, clearly distinguished;
- conclusion tied exactly to preregistered rules;
- concrete follow-up only for measured failures.

## 15. What this experiment does not prove

A successful result supports the operational RI route **through the tested Treatment Delivery Mode** for the tested repository state, model/client, and task distribution. It does not prove universal productivity gain, semantic understanding by the graph, graph ranking as authority, Control Map value to agents, another RI delivery mode, or future-state equivalence.

No embeddings, vector database, MCP service, graph database, inferred semantic edges, or additional retrieval layer is justified unless measured failure evidence identifies a concrete need that the simpler route cannot address.
