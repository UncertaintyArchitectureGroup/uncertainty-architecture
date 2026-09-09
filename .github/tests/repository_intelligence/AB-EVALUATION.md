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

### 2.1 Primary pilot wave

Run **12 held-out tasks × 2 arms = 24 isolated sessions** using a paired randomized crossover design:

- identical task prompt and pinned source state within each pair;
- fresh session for every run;
- randomized A/B order per task from a frozen seed;
- pairs interleaved over time rather than all A then all B;
- same displayed model family, selectable thinking configuration, connector permissions, client class, and source commit within each pair;
- frozen scoring key;
- arm-hidden correctness scoring where practical.

Do not selectively rerun failures.

### 2.2 Confirmatory replication wave

LLM output is stochastic. A single 24-run pilot may show route differences caused by sampling variance rather than architecture.

A positive agent-benefit claim therefore requires a **second complete confirmatory wave** using the same 12 frozen tasks and scoring key:

- another 12 × 2 = 24 fresh isolated sessions;
- a second frozen randomization seed/order;
- same pinned repository state and same model/configuration target as the pilot unless a preregistered compatibility exception is invoked;
- no prompt, answer-key, scoring-rule, ecological-sampling, or cost-gate changes after pilot unblinding.

The pilot may produce `PROVISIONAL GO` or `WEAK POSITIVE`, but the repository must not claim demonstrated incremental agent value until the confirmatory wave is complete and directionally consistent.

If model/service drift makes exact replication impossible, record the difference and classify confirmatory evidence separately; do not silently combine incompatible waves.

Maximum primary evidence set when replication is required: **48 A/B sessions**.

### 2.3 Optional diagnostic C

After pilot A/B outputs and scores are frozen, an optional **RI data-only** diagnostic may run on 4–6 frozen cases.

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

Mark a primary run invalid if:

- `conversation_fresh` is false;
- held-out answer material or previous-arm output was available;
- project context contains benchmark answers;
- connector/repository access differs materially within the pair;
- known prior repository context independently supplies the expected answer rather than merely general repo familiarity.

If the product cannot determine cross-chat memory or prior repo context, record `unavailable`. Treat this as an isolation limitation; if material to interpretation, classify the study `INCONCLUSIVE` or repeat in a cleaner environment.

## 4. Held-out corpus

The first corpus contains **6 designed stress cases + 6 ecological cases**.

### 4.1 Stress cases

Across six stress cases cover a balanced subset of:

- canonical term / synonym pressure;
- overlapping artifact ownership;
- validation/companion routing;
- research-state vs framework-authority separation;
- impact reasoning where navigation/shared hubs must not inflate blast radius;
- stale/unverifiable RI fallback;
- Ukrainian or paraphrased maintainer wording.

Stress cases must not be tuned after observing A/B results or RI rankings.

### 4.2 Ecological cases and sampling frame

Ecological cases answer the practical question: does RI help on ordinary UA maintainer work, not only on scenarios designed around RI capabilities?

Before any arm run:

1. Define an **ecological source pool** of at least 15 realistic maintainer tasks from a fixed cutoff period or other frozen source set.
2. Record the pool provenance and cutoff rule outside the tested repository view.
3. Apply only preregistered exclusions, such as duplicates, tasks whose answer depends on unavailable external state, or tasks that cannot be run identically in both arms.
4. Freeze the eligible pool.
5. Select six cases using the preregistered randomization seed; do not manually replace selected cases because RI is expected to perform poorly or well.

At least one ecological case must be an easy exact-owner/negative-control case. At least one must be a legitimate-new-artifact case where no existing owner fully covers the need. If random sampling does not produce those required anchors, define them as two fixed ecological anchors before random selection and sample the remaining four from the frozen pool; preregister that rule before execution.

Report ecological results separately from stress results. A gain confined to designed stress cases is not broad routine productivity evidence.

### 4.3 Hidden prompts and answer-key secrecy

Do not commit held-out prompts or scoring keys before execution. Keep them outside the repository view exposed to tested sessions.

Preregister only non-revealing metadata and cryptographic commitments:

- corpus version and case count;
- six stress / six ecological classification;
- ecological source-pool provenance/cutoff rule;
- ecological pool SHA-256 if serialized;
- prompt-pack SHA-256;
- scoring-key SHA-256;
- source commit;
- model/configuration target;
- randomization-seed SHA-256;
- primary/secondary endpoints;
- cost gate;
- pilot/replication decision rule.

After outputs and scoring are frozen, prompts/key/raw records may be published and verified against the commitments.

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

## 9. Cost gate

A positive usefulness result requires a preregistered **numeric or otherwise mechanically decidable cost acceptance rule**. `Clearly disproportionate` must not be decided after unblinding.

The preregistration must define:

- `primary_cost_metric` — e.g. ecological median total connector calls;
- `acceptable_median_ratio_b_over_a` or another explicit threshold;
- `acceptable_high_overhead_case_count` and the threshold defining high overhead;
- how serious-error-prevention cases are treated in cost interpretation;
- treatment of unavailable token/time metrics.

Recommended default if the study owner has no better prior threshold:

- ecological median connector-call ratio B/A ≤ **1.50**;
- no more than **2 of 6** ecological cases with connector-call ratio > **2.00**;
- a case where B prevents a serious routing error is reported separately and does not by itself fail the cost gate, but its cost remains visible.

The exact rule must be frozen before the first run. Changing it after unblinding invalidates the preregistered GO decision and may only be reported as exploratory.

## 10. Endpoints and pilot decision

Primary endpoint: paired serious-error matrix across valid pairs:

- A wrong / B correct;
- A correct / B wrong;
- both correct;
- both wrong.

Secondary endpoints: per-case correctness delta; median paired correctness delta; observable cost metrics; stress/ecological split.

For the 12-pair **pilot**:

- **PROVISIONAL GO:** ≥2 valid `A wrong / B correct`, 0 reverse serious errors, no systematic ecological correctness regression, and preregistered cost gate passes.
- **WEAK POSITIVE / REPLICATE:** exactly 1 positive reversal, 0 reverse serious errors, otherwise non-worse correctness. Signal only.
- **GO, OPTIMIZE COST:** correctness reaches provisional-GO threshold but cost gate fails due repeated avoidable RI overhead.
- **NO INCREMENTAL VALUE SHOWN:** serious-error and material-correctness outcomes are equivalent and RI does not reduce observable cost.
- **REGRESSION:** RI introduces any serious error on a case Control handled correctly, or shows systematic uncompensated correctness/cost regression.
- **INCONCLUSIVE:** invalid pairs, isolation uncertainty, source-state mismatch, scoring ambiguity, or protocol defect prevents defensible comparison.

The pilot alone cannot produce final `DEMONSTRATED GO`.

## 11. Confirmatory decision

Run the full confirmatory 12-pair wave whenever the pilot is `PROVISIONAL GO` or `WEAK POSITIVE` and an agent-benefit claim is desired.

Final **DEMONSTRATED GO** requires:

- pilot and confirmatory waves both complete under compatible frozen conditions;
- no reverse serious-error reversal in either wave;
- combined evidence remains directionally positive rather than the confirmatory wave erasing the pilot effect;
- no systematic ecological correctness regression;
- preregistered cost gate passes in the confirmatory wave and is not materially contradicted by combined results.

A practical default consistency rule is: confirmatory wave must contain at least one `A wrong / B correct` and zero `A correct / B wrong`, while combined pilot+confirmatory positive reversals must exceed reverse reversals by at least 2. If another rule is preferred, preregister it before pilot execution.

If confirmatory results contradict the pilot, final outcome is `NOT CONFIRMED` or `INCONCLUSIVE`, not GO.

## 12. Execution lifecycle

1. Merge the protocol/infrastructure PR.
2. Freeze a specific `main` source commit for evaluation.
3. Create a preregistration record outside the tested Git tree (for example a GitHub Issue) containing only commitments/metadata, not hidden answers.
4. Freeze ecological source pool, prompt pack, scoring key, seeds, model/configuration, cost gate, and confirmatory rule.
5. Run pilot A/B.
6. Freeze pilot outputs and scores.
7. Run confirmatory A/B when required for a positive claim.
8. Optionally run C diagnostic after primary evidence is frozen.
9. Publish a separate evidence/results PR containing revealed prompts, key, hash verification, raw run records, scoring, wave results, limitations, and conclusion.
10. Merge the results PR whether the result is positive, null, regression, or inconclusive, so evidence is preserved rather than discarded.

Do not conduct the held-out experiment inside the protocol PR and then close it unmerged. The protocol is a durable repository control/evaluation artifact and should be merged before the frozen evaluation state is selected.

## 13. Result report

Include:

- preregistered hashes and source commit;
- exact model/client/configuration and isolation limitations;
- ecological source-pool provenance and selection record;
- stress/ecological classification;
- all valid and invalid runs with reasons;
- pilot serious-error matrix and correctness/cost deltas;
- confirmatory results when run;
- combined interpretation;
- optional C results separately;
- cost-gate result;
- deviations before and after unblinding, clearly distinguished;
- conclusion tied exactly to preregistered rules;
- concrete follow-up only for measured failures.

## 14. What this experiment does not prove

A successful result supports the operational RI route for the tested repository state, model/client, and task distribution. It does not prove universal productivity gain, semantic understanding by the graph, graph ranking as authority, Control Map value to agents, or future-state equivalence.

No embeddings, vector database, MCP service, graph database, inferred semantic edges, or additional retrieval layer is justified unless measured failure evidence identifies a concrete need that the simpler route cannot address.