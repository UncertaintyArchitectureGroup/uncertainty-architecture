# Repository Intelligence A/B Evaluation Protocol

> Protocol version: 7

## Purpose and estimand

This protocol defines the independent comparative evaluation required by [`REPOSITORY-INTELLIGENCE.md`](../../REPOSITORY-INTELLIGENCE.md#14-evaluation-and-acceptance).

The primary estimand is the **incremental operational value of the normal Repository Intelligence (RI) route** over the repository's ordinary live-GitHub orientation route under one stable repository state. The primary A/B does not isolate projection-data value from the workflow that verifies, interprets, and uses that data.

Primary question:

> Given the repository's normal contributor instructions and authority model, does the operational RI route reduce serious routing mistakes or observable orientation cost without degrading material decisions, compared with ordinary live-GitHub bootstrap/search on the same repository state?

Both primary arms use the same repository state, same root and scoped `AGENTS.md`, same displayed model family, same selectable thinking configuration, same connector permissions, same client class, and same task prompt. The existing deterministic 12-case corpus remains a regression suite and is not independent held-out evidence.

A successful primary result supports only the operational RI route through the tested Treatment Delivery Mode. It does not by itself prove that graph relations, graph visualization, or the Repository Control Map add value beyond the compact structured projection.

## 1. Shared `AGENTS.md` baseline

Removing `AGENTS.md` from Control would create a different repository contract and confound the experiment. Both arms therefore read the same instructions.

- `RI-AB-CONTROL`: RI is deliberately unavailable; use the ordinary live-GitHub route allowed by the source-state lock.
- `RI-AB-TREATMENT`: follow the normal operational RI route through the preregistered Treatment Delivery Mode.
- `RI-AB-DATA-ONLY`: optional post-primary diagnostic; use only the verified compact Agent Context Surface supplied for the study state, without task-specific RI query output.

The root owner map is shared baseline information. Easy exact-owner cases are ceiling/negative controls. The benchmark marker itself is a small observer intervention and must not be counted as RI evidence.

## 2. Experimental design

The unit is one **task × arm** run in a fresh isolated session.

The primary study uses two independent held-out corpora, frozen before the first run:

- **Pilot corpus P:** 12 tasks = 6 stress + 6 ecological.
- **Confirmatory corpus C:** 12 different tasks = 6 stress + 6 ecological.

No prompt, concrete task family, or ecological source event may appear in both waves. Both prompt packs, both scoring keys, source/task identities, scenario-coverage assignments, pair orders, ecological selections, thresholds, model/client target, Treatment identity, and source-state controls are frozen before Pilot.

### 2.1 Pilot

Run **12 Pilot tasks × 2 arms = 24 isolated sessions**:

- identical task and source state within each pair;
- fresh session for every run;
- frozen randomized A/B order per task;
- pairs interleaved over time rather than all A then all B;
- same displayed model family, thinking configuration, connector permissions, client class, and source state;
- frozen Pilot scoring key;
- arm-hidden semantic scoring where practical.

Do not selectively rerun unfavorable valid results. Infrastructure retries are allowed only under a preregistered rule.

### 2.2 Independent confirmatory wave

Confirmation uses **12 different tasks** rather than rerunning Pilot prompts. The confirmatory pack and key are committed by hash before Pilot, remain hidden from tested sessions until the confirmatory wave begins, and use a separate frozen arm-order seed.

The confirmatory wave runs regardless of Pilot performance. Pilot results must not change the confirmatory corpus, scoring key, thresholds, coverage, or stopping rule.

If model/service drift makes compatible confirmation impossible, classify the primary study `INCONCLUSIVE`; do not silently pool incompatible waves.

Primary evidence under this protocol is **48 A/B sessions across 24 distinct tasks**.

### 2.3 Optional diagnostic C

After both A/B waves and their correctness scores are frozen, an optional `RI-AB-DATA-ONLY` diagnostic may run on 4–6 frozen cases. C receives the verified compact surface but no task-specific RI routing suggestion. It is diagnostic only and cannot rewrite the primary result.

A separate future decomposition may compare a flat owner/inventory-only materialization with the same compact surface plus relational evidence. That is the appropriate experiment for asking whether graph relations themselves add value; it is not silently inferred from the primary A/B.

## 3. Execution eligibility and source-state lock

### 3.1 Stable default-branch window

The Control baseline is ordinary live-GitHub bootstrap/search, not a tree-traversal-only artificial baseline. The primary study therefore uses a preregistered **stable-default-branch window**:

1. record the exact 40-character study commit and default branch;
2. verify the default-branch tip equals the study commit before the first primary run;
3. freeze repository mutations until all 48 primary sessions are complete;
4. verify the default-branch tip before and after every run;
5. invalidate a run whose pre/post tip differs from the study commit and stop the study on lock failure;
6. use the exact study ref for direct file/tree reads where supported;
7. allow ordinary default-branch GitHub search in both arms while the lock remains valid.

Search-index lag is observed baseline behavior, not silently corrected out of Control. Search candidates still require source reading before material decisions.

If `main` cannot remain stable, use a separately preregistered evaluation repository whose default branch is an exact immutable copy of the selected source state. Do not change execution repository mid-study.

### 3.2 Fixed Treatment Delivery Mode and identity

Preregister exactly one Treatment Delivery Mode:

- `local_cli`;
- `connector_compact_surface`;
- `dedicated_adapter`.

Do not mix modes within one primary study.

For ChatGPT + GitHub connector, `connector_compact_surface` is preferred. In that mode the agent receives the complete committed `assets/repository-intelligence/agent-context.json` surface and interprets it directly. Do not pretend local query RPCs were executed when they were not.

The preregistration freezes an exact Treatment aid identity. For `connector_compact_surface`, it includes:

- mode;
- repository path;
- Git blob SHA;
- full-content SHA-256;
- RI source identity/digest.

Every Treatment run records the same identity. A different blob, content digest, source identity, mode, truncated payload, or unverifiable payload is **Treatment delivery failure**, not ordinary RI fallback.

The complete surface may arrive in deterministic connector chunks. Every chunk counts as a connector call and, when measurable, context volume. The complete payload must be reconstructed/verified against the preregistered identity.

### 3.3 Contrast integrity

A valid A/B requires proof that A remained Control and B actually received the preregistered Treatment.

For every **Control** run:

- `ri_aid_accessed = false`;
- `ri_payload_bytes = 0`;
- no RI logical operation/evidence is recorded;
- no compact Agent Context Surface is consumed;
- no full Graph View is consumed;
- no Repository Control Map is consumed;
- no copied RI result from another run is consumed.

For every **Treatment** run:

- Treatment delivery status is `delivered`;
- complete payload verification succeeds;
- the exact per-run Treatment aid identity equals preregistration;
- `ri_aid_accessed = true`;
- connector compact-surface mode records positive RI payload bytes.

A contaminated Control or wrong Treatment identity invalidates the pair. It must never be scored as ordinary variance.

### 3.4 Non-scored smoke test

Before preregistration becomes executable, run a synthetic/non-held-out smoke test in the actual client. It must prove:

1. default-branch pre/post tip checks;
2. ordinary Control search;
3. exact-ref direct reads where supported;
4. selected Treatment delivery for the same state;
5. complete-payload and truncation verification;
6. connector-call/instrumentation capture;
7. connector-permission parity;
8. Memory disabled;
9. Project/workspace context absent;
10. prior product-supplied repository context absent;
11. repository-mutation freeze acknowledged.

All mandatory smoke fields must be `true` in preregistration and the run record. If they cannot be established, do not start the 48 primary sessions.

## 4. Isolation and per-run validity

Primary runs require a genuinely cold product context, not merely an empty-looking conversation.

Every run records and must satisfy:

- `conversation_fresh = true`;
- `memory_enabled = false`;
- `project_context_present = false`;
- `prior_repo_context_available = false`;
- `previous_arm_output_exposed = false`;
- `corrective_scoring_feedback_before_pair_complete = false`;
- `future_wave_material_exposed = false`;
- `hidden_benchmark_material_exposed = false`;
- connector state equal within the pair;
- source-state pre/post SHAs equal the study commit;
- no source-state protocol violation;
- exact preregistered `model_family`;
- exact preregistered `thinking_configuration`;
- exact preregistered `client_environment`;
- exact preregistered connector;
- no protocol violation.

`unavailable` is not acceptable for Memory, Project context, prior product context, source-state checks, or model/client identity in primary evidence. General model pretraining and public-Internet knowledge are not separately controllable and are shared limitations.

## 5. Held-out corpora and independence

### 5.1 Mandatory scenario coverage

The combined 24 tasks must cover every mandatory scenario family inherited from `RI-EVAL-001`:

- `exact-owner-recovery`;
- `canonical-term-synonym-pressure`;
- `near-synonym-source-review`;
- `overlapping-artifact-refinement`;
- `legitimate-new-artifact`;
- `impact-validation-routing`;
- `accepted-proposed-relation-change`;
- `branch-behind-target`;
- `producer-schema-self-change`;
- `candidate-data-boundary`;
- `shared-structural-hub`;
- `research-authority-separation`;
- `stale-materialization-fallback`;
- `ukrainian-or-paraphrased-routing`.

One case may cover more than one family when the task genuinely exercises both. Scenario-family assignments live inside the hashed prompt packs and are frozen before Pilot.

The Confirmatory wave must itself cover these critical trust-boundary families:

- `accepted-proposed-relation-change`;
- `branch-behind-target`;
- `producer-schema-self-change`;
- `candidate-data-boundary`;
- `shared-structural-hub`;
- `stale-materialization-fallback`.

The deterministic evaluator verifies declared coverage. Human review of the revealed corpus must still confirm that the prompt genuinely exercises the declared scenario; a label cannot manufacture coverage.

### 5.2 Stress cases

Each wave has six designed stress cases. Stress cases must be different concrete tasks across waves. Every case has an opaque `task_family_id`; the two waves must have zero `task_family_id` overlap even if prompts are paraphrased.

Stress prompts and scoring-key sections are frozen before Pilot and are not tuned after viewing RI rankings or A/B output.

### 5.3 Ecological cases and neutral normalization

Ecological cases come from real UA maintainer work. Conversational fragments are neutrally normalized into self-contained prompts before seeded selection.

Normalization may add only facts explicitly present in the source event/context that are needed for self-containment. It must not add expected owners, repository paths, validators, canonical terms, RI vocabulary, answer-key facts, or later repository findings.

If a source request cannot be made self-contained without materially revealing the answer, exclude it under the preregistered rule.

Before any arm run:

1. freeze raw ecological source-pool provenance/cutoff and SHA-256;
2. apply only preregistered exclusions;
3. normalize all eligible source items before selection;
4. freeze normalized-pool SHA-256;
5. require at least 24 eligible items for a combined pool, or at least 12 per separate wave pool;
6. select six Pilot and six different Confirmatory ecological cases without replacement;
7. assign immutable opaque `ecological_source_id` and `task_family_id` values;
8. freeze selected-ID commitments;
9. never replace a selected case because RI is expected to perform poorly or well.

Ecological source IDs and concrete task-family IDs must be disjoint across waves. Textual paraphrase is not sufficient independence.

Across the 12 ecological cases include at least two easy exact-owner negative controls and at least two legitimate-new-artifact cases, with at least one of each anchor type per wave.

### 5.4 Hidden prompt-pack format

Each hidden prompt pack uses schema version 2:

```json
{
  "schema_version": 2,
  "wave": "PILOT",
  "cases": [
    {
      "task_id": "P01",
      "task_family_id": "opaque-family-01",
      "corpus_class": "stress",
      "ecological_source_id": null,
      "scenario_families": ["branch-behind-target"],
      "planned_order": ["RI-AB-CONTROL", "RI-AB-TREATMENT"],
      "prompt": "..."
    }
  ]
}
```

Each pack has exactly 12 unique task IDs, 6 stress and 6 ecological tasks, unique task-family IDs within the wave, and a frozen pair order per task.

The evaluator rejects cross-wave overlap in normalized prompt text, concrete task-family IDs, or ecological source IDs. It also verifies selected ecological-ID and arm-order-plan commitments.

### 5.5 Hidden scoring-key format

Each scoring key uses schema version 2 and one object per task ID. Every case must declare:

```json
{
  "task_id": "P01",
  "companion_validation_applicable": true,
  "expected_evidence": ["..."]
}
```

`companion_validation_applicable` is frozen before runs. The evaluator requires both arms of that task to use the same applicability: score `0..2` when applicable and `null` when not applicable.

### 5.6 Preregistration commitments

Preregister non-revealing metadata and cryptographic commitments outside the tested Git tree, including:

- study commit/default-branch lock;
- smoke evidence;
- model/thinking/client/connector target;
- isolation rules;
- Treatment mode and exact aid identity;
- prompt-pack and scoring-key hashes;
- task/source independence rules;
- arm-order seeds and frozen order-plan hashes;
- ecological pool/selection hashes;
- mandatory and Confirmatory-critical coverage rules;
- positive-reversal quality gate;
- cost/context thresholds;
- final decision rule.

After all primary outputs and scores are frozen, reveal prompt packs, keys, and run evidence and verify them against commitments.

## 6. Primary arms

### A — Control

Control follows ordinary repository authority and contributor rules but receives no RI aid.

Allowed:

- ordinary GitHub search against the stable default branch;
- ref-addressable tree/directory/direct-file reads at the study commit;
- task-relevant ref-addressable PR/diff/review/check/branch/commit reads;
- maintained navigation discovered from source files.

Disallowed for orientation:

- compact Agent Context Surface;
- full/generated Graph View;
- RI query operations;
- Repository Control Map;
- copied RI output from another session.

Control may read `.github/REPOSITORY-INTELLIGENCE.md` only when the benchmark task itself is specifically about RI architecture.

### B — Treatment

Treatment follows the production RI route through the fixed delivery mode:

- verify exact Treatment identity;
- consume the accepted aid for orientation/preflight;
- read owning sources before material decisions;
- use ordinary live-GitHub fallback/search when task-specific RI evidence is ambiguous or unsupported;
- never infer authority from ranking/graph structure;
- avoid loading the full graph when compact data is sufficient.

Task-level fallback after successful Treatment delivery is valid Treatment behavior. Failure to obtain/verify the preregistered aid is not.

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

Follow the repository's applicable contributor instructions and complete the task below using repository facts attributable to the study source state. Ordinary GitHub search is allowed when permitted by the arm. Do not search for hidden prompt packs, keys, prior-arm output, or another wave's task material. Report repository sources relied on and distinguish verified fact from inference.

Task:
<held-out prompt>
```

Opaque IDs must not reveal expected owner, scenario, or answer.

## 8. Observable instrumentation

Never use hidden model reasoning or infer when the model internally knew an answer.

Record where observable:

- source-state pre/post tip SHAs;
- exact per-run model/thinking/client/connector identity;
- ordered connector/tool calls;
- direct exact-ref reads;
- default-branch/broad search calls;
- total connector calls;
- ordered files opened and distinct-file count;
- Treatment identity/delivery/complete-payload verification;
- RI payload bytes and RI logical evidence/operations;
- explicit Control prohibited-aid flags;
- task-level fallback separately from Treatment delivery failure;
- exact repository-response UTF-8 bytes when measurable;
- exact input tokens when exposed;
- elapsed time only when reliable;
- tool errors and protocol violations;
- transcript reference.

Do not estimate unavailable token, byte, or latency data from prose length.

## 9. Correctness scoring

Each task has a frozen repository-verifiable key.

Dimensions:

- **Owner/routing correctness (0–2)**;
- **Evidence sufficiency (0–2)**;
- **Authority discipline (0–2)**;
- **Companion/validation completeness (0–2)** when the frozen key marks it applicable;
- **Decision quality (0–2)**.

A **serious routing error** includes wrong canonical authority, duplicate canonical term/artifact despite an owner, promotion of research/history/example material to framework authority, material scoped-instruction miss, material validator/companion omission that violates a contract, or candidate state presented as accepted.

Do not label the serious-error matrix as “wrong/correct.” The four observable states are:

- `A-serious/B-no-serious`;
- `A-no-serious/B-serious`;
- `both-serious`;
- `neither-serious`.

An `A-serious/B-no-serious` pair counts as a **qualifying positive reversal** only when Treatment also meets the preregistered quality floor: every applicable Treatment dimension is at least `1` by default. A vacuous, unsupported, or unusable non-serious answer therefore cannot create a correctness win.

Preferred scoring order: remove arm labels/route metadata from copies, randomize pair display, score against the frozen key, freeze scores, then reveal arms and cost data.

Ecological correctness non-regression defaults to median paired total correctness delta `B−A >= 0` in each wave and zero ecological `A-no-serious/B-serious` reversals.

## 10. Cost and efficiency

For each valid ecological pair define `r_i = B_i/A_i` using total connector calls. `0/0 -> 1.0`; if `A_i=0` and `B_i>0`, ratio is infinity.

Per-wave connector statistic: **median of six paired ratios**, not ratio of group medians.

Default correctness-route connector gate per wave:

- median `r_i <= 1.50`;
- no more than 2 of 6 cases with `r_i > 2.00`.

A narrower **DEMONSTRATED CONNECTOR-INTERACTION GAIN** requires median `r_i <= 0.80` in both waves, ecological correctness non-regression in both waves, and zero reverse serious-error reversals.

A stronger **DEMONSTRATED ORIENTATION EFFICIENCY GO** additionally requires one exact preregistered context-volume metric for every ecological run:

- `repository_response_utf8_bytes`;
- `input_tokens`;
- or `unavailable`.

When available, define `v_i = B_i/A_i` with the same zero-denominator rule. Default volume gate per wave:

- all six ecological pairs measured;
- median `v_i <= 1.00`;
- no more than 2 of 6 cases with `v_i > 2.00`.

If exact context volume is unavailable/incomplete, orientation-efficiency GO is unavailable by design. A connector-interaction result must not be relabelled as total efficiency.

## 11. Pilot interpretation

Pilot is descriptive only:

- **PROVISIONAL CORRECTNESS SIGNAL:** at least 2 qualifying positive reversals, zero reverse serious reversals, ecological non-regression, connector-cost gate pass;
- **WEAK CORRECTNESS SIGNAL:** exactly 1 qualifying positive reversal with zero reverse serious reversals and ecological non-regression;
- **PROVISIONAL ORIENTATION EFFICIENCY SIGNAL** when Pilot passes connector and context gates;
- **PROVISIONAL CONNECTOR-INTERACTION SIGNAL** when connector gain passes but full efficiency is unavailable/not passed;
- **NO PILOT SIGNAL** otherwise;
- **PILOT REGRESSION** on reverse serious reversal or ecological regression;
- **PILOT INCONCLUSIVE** on invalid evidence or infrastructure failure.

Pilot does not stop or alter Confirmatory unless experiment infrastructure validity fails.

## 12. Confirmatory and final decision

### 12.1 Demonstrated correctness

Final **DEMONSTRATED CORRECTNESS GO** requires:

- all 24 A/B pairs valid;
- at least 1 qualifying positive reversal in Confirmatory;
- at least 1 qualifying **ecological** positive reversal in Confirmatory;
- at least 3 qualifying positive reversals combined;
- zero `A-no-serious/B-serious` reversals combined;
- ecological correctness non-regression in both waves;
- connector-cost gate pass in both waves;
- valid source-state, isolation, Treatment identity/delivery, coverage, scoring, and model/client evidence.

The ecological Confirmatory requirement prevents stress-only gains from being reported as demonstrated routine repository value.

If Pilot shows a correctness signal but independent Confirmatory does not support final correctness, report `NOT CONFIRMED` unless another separately demonstrated result applies.

### 12.2 Orientation efficiency

Final **DEMONSTRATED ORIENTATION EFFICIENCY GO** requires all pairs valid, zero reverse serious reversals, ecological correctness non-regression, connector-interaction gain, and complete context-volume gate pass in both waves.

### 12.3 Other outcomes

- `CORRECTNESS GAIN / COST NOT ACCEPTED` when correctness thresholds are met but connector overhead gate fails;
- `DEMONSTRATED CONNECTOR-INTERACTION GAIN ONLY` when connector gain is demonstrated but full orientation efficiency is not;
- `NOT CONFIRMED` when Pilot correctness signal is not independently confirmed;
- `NO INCREMENTAL VALUE SHOWN` when no demonstrated route succeeds and no material regression occurs;
- `REGRESSION` on any reverse serious reversal or material ecological correctness regression under otherwise valid conditions;
- `INCONCLUSIVE` on contrast contamination, invalid pair, source-state failure, isolation failure, wrong Treatment identity/delivery, incompatible model/client, missing required scenario coverage, scoring ambiguity, or protocol defect.

## 13. Deterministic evaluator

`.github/scripts/score_repository_intelligence_ab.py` mechanically verifies observable protocol conditions after assessor-entered semantic scores are frozen. It verifies:

- protocol/source/isolation/preflight requirements;
- prompt and scoring-key hashes;
- prompt/task/source cross-wave independence;
- selected ecological-ID and pair-order commitments;
- mandatory scenario coverage and Confirmatory critical coverage;
- exactly one Control and Treatment run per task in frozen order;
- per-run model/thinking/client/connector identity;
- Control RI ablation integrity;
- exact Treatment aid identity and delivery;
- companion-score applicability from the frozen key;
- serious-error states and qualifying positive reversals;
- paired correctness/cost/context metrics;
- final classification.

The evaluator does not inspect hidden reasoning and cannot replace assessor judgment about whether a prompt genuinely represents its declared scenario or whether semantic scores are correct.

Final invocation:

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

A scorer failure is an instrumentation/protocol defect, not permission to choose a more favorable manual formula.

## 14. Execution lifecycle

1. Merge the protocol/infrastructure PR only after companion files, generated RI surface freshness, deterministic tests, and checked-state checkpoint are reconciled.
2. Select the exact `main` study commit.
3. Establish repository-mutation freeze.
4. Run the non-scored smoke test in the actual client.
5. Create preregistration outside the tested Git tree.
6. Freeze both prompt packs, keys, task/source identities, scenario coverage, pair orders, ecological selections, model/client, Treatment identity, thresholds, and decision rules.
7. Run Pilot A/B with source-state checks before/after every session.
8. Freeze Pilot outputs/scores without altering Confirmatory material.
9. Run independent Confirmatory A/B.
10. Freeze all primary output/scores.
11. Run deterministic evaluator.
12. Optionally run data-only C or a later flat-vs-relational decomposition diagnostic.
13. Publish a separate evidence/results PR with revealed packs/keys, hash verification, run records, evaluator output, limitations, and conclusion.
14. Merge the results PR whether positive, null, regression, or inconclusive.
15. Release repository-mutation freeze after primary evidence is frozen.

Do not conduct the held-out experiment inside the protocol PR and close it unmerged. The protocol is a durable evaluation artifact. The protocol, templates, evaluator, and narrow arm markers remain after the study; completed study material becomes historical evidence and is not operational RI input by default.

## 15. Result report

Publish at least:

- preregistration hashes and study commit;
- source-state lock evidence;
- exact model/thinking/client/connector;
- smoke and isolation evidence;
- Treatment Delivery Mode and exact aid identity;
- prompt/task-family/ecological-source non-overlap verification;
- mandatory/critical scenario coverage matrix;
- stress/ecological split per wave;
- all valid/invalid runs with reasons;
- serious-error states and qualifying positive reversals;
- correctness deltas;
- connector/context gates;
- task-level fallback and delivery failures;
- deterministic evaluator output;
- optional diagnostic results separately;
- deviations before/after unblinding;
- conclusion tied exactly to preregistered rules.

## 16. What this experiment does not prove

A successful result supports the operational RI route **through the tested Treatment Delivery Mode** for the tested repository state, model/client, and task distribution. It does not prove universal productivity gain, semantic understanding by a graph, graph ranking as authority, Control Map value to agents, another delivery mode, or future-state equivalence.

A connector-interaction gain does not prove lower total context cost. An orientation-efficiency claim requires exact preregistered context-volume evidence.

The primary A/B does not isolate relational graph value from flat inventory/ownership value. If that distinction matters after primary evidence, run the explicitly separate post-primary decomposition diagnostic rather than inferring it.

No embeddings, vector database, MCP service, graph database, inferred semantic edges, or additional retrieval layer is justified unless measured failure evidence identifies a concrete need the simpler route cannot address.
