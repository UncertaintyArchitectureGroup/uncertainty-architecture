# Repository Intelligence A/B Evaluation Protocol

> Protocol version: 9

## Purpose

This protocol defines the independent comparative evaluation required by [`REPOSITORY-INTELLIGENCE.md`](../../REPOSITORY-INTELLIGENCE.md#14-evaluation-and-acceptance).

The primary estimand is the **incremental operational value of the normal Repository Intelligence (RI) route** over the repository's ordinary live-GitHub orientation route under one stable repository state.

Primary question:

> Given the same repository instructions, model/client configuration, source state, and task prompt, does the operational RI route reduce serious routing mistakes or observable orientation cost without degrading material decisions compared with ordinary live-GitHub bootstrap/search?

The primary A/B tests the complete operational RI route through one preregistered delivery mode. It does **not** by itself isolate value from graph relations, graph visualization, or the Repository Control Map.

## 1. Shared baseline and arms

Both arms read the same root and scoped `AGENTS.md` files and use the same repository authority model.

- `RI-AB-CONTROL`: ordinary live-GitHub orientation with RI deliberately unavailable.
- `RI-AB-TREATMENT`: the same baseline plus one preregistered RI delivery mode.
- `RI-AB-DATA-ONLY`: optional post-primary diagnostic only.

The benchmark marker is an unavoidable observer intervention. The model is arm-aware, which can create demand-characteristic effects; report this limitation explicitly.

## 2. Study design

The unit is one **task × arm** run in a fresh isolated session.

The primary study uses two independently held-out waves frozen before Pilot:

- Pilot: 12 tasks = 6 stress + 6 ecological.
- Confirmatory: 12 different tasks = 6 stress + 6 ecological.

Each task runs once in each arm, yielding **48 primary sessions across 24 distinct tasks**.

Both waves run regardless of Pilot performance unless experiment infrastructure validity fails. Do not selectively rerun unfavorable valid results.

## 3. Stable source state

Use a preregistered `stable_default_branch_window`:

1. select the exact study commit;
2. require the default-branch tip to equal that commit before the study;
3. freeze repository mutations through all primary sessions;
4. verify the default-branch tip before and after every run;
5. stop the study on lock failure and invalidate affected runs;
6. use exact-ref reads where supported;
7. preserve ordinary default-branch search in both arms while the lock is valid.

Search-index lag is baseline behavior and is not silently corrected out of Control.

If the default branch cannot remain stable, use a separately preregistered immutable evaluation repository copied from the selected source state.

## 4. Treatment delivery and identity

Preregister exactly one delivery mode:

- `connector_compact_surface`;
- `local_cli`;
- `dedicated_adapter`.

For `connector_compact_surface`, freeze the exact committed `assets/repository-intelligence/agent-context.json` identity:

- repository path;
- Git blob SHA;
- full-content SHA-256;
- RI source identity/digest.

The evaluator receives the exact Treatment surface as evidence and recomputes all three identities from its bytes.

A different blob, digest, source identity, truncated payload, or unverifiable payload is **Treatment delivery failure**.

Task-level RI fallback after successful delivery is valid Treatment behavior and remains part of the measured route.

## 5. Execution eligibility and isolation

Before Pilot, run a non-scored smoke test in the actual client. The preregistration freezes both an immutable smoke-evidence reference and its SHA-256 and must prove:

- source-state pre/post checks;
- ordinary Control search;
- exact-ref reads where supported;
- Treatment delivery for the same state;
- complete-payload and truncation verification;
- instrumentation capture;
- connector-permission parity;
- Memory disabled;
- Project/workspace context absent;
- prior product-supplied repository context absent;
- repository-mutation freeze acknowledged.

The run record must carry the same smoke-evidence reference and digest. A different or missing smoke evidence object invalidates primary eligibility.

Primary runs require a fresh conversation, Memory disabled, no Project/workspace context, no prior product-supplied repository context, no previous-arm output, no corrective scoring feedback before pair completion, no future-wave or hidden benchmark material, the same displayed model family/thinking configuration/client/connector/source state, and no protocol violation.

If a required isolation condition cannot be established, primary evidence is `INCONCLUSIVE`.

## 6. Held-out corpora

### 6.1 Mandatory scenario coverage

Across the 24 tasks cover every mandatory scenario family inherited from `RI-EVAL-001`:

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

Confirmatory must itself cover `accepted-proposed-relation-change`, `branch-behind-target`, `producer-schema-self-change`, `candidate-data-boundary`, `shared-structural-hub`, and `stale-materialization-fallback`.

The evaluator verifies declared coverage, but human review of the revealed corpus must still confirm that prompts genuinely exercise their declared scenarios.

### 6.2 Ecological pool and neutral normalization

Use one frozen combined normalized ecological pool with at least 24 eligible tasks.

Normalization may add only facts explicitly present in the source event/context that are required to make the task self-contained. It must not add expected owners, paths, validators, canonical terms, RI vocabulary, answer-key facts, or later repository findings.

Each pool item contains `ecological_source_id`, `task_family_id`, exact normalized prompt, `anchor_type` (`exact-owner`, `legitimate-new-artifact`, or `none`), and declared scenario families.

`ecological_source_id`, `task_family_id`, and whitespace-normalized/case-folded prompt text must each be unique inside the eligible pool.

### 6.3 Seed-shopping control and replayable ecological sampling

Randomization is valid only when the frozen pool is committed **before** the random seeds are generated. The preregistration records the pool commitment and independent seed-generation provenance.

Required sequence:

1. freeze and publish/record the exact ecological pool hash;
2. after that commitment, an independent assessor generates exactly one ecological-selection seed and exactly one arm-order seed for each wave;
3. record an immutable generation reference for each seed and attest that alternatives were not sampled and selected by outcome;
4. commit only the seed hashes before primary execution;
5. reveal the seeds only after primary evidence is frozen;
6. let the evaluator reproduce selection and order from the revealed seeds.

This provenance is externally auditable. The local evaluator verifies the declared contract and seed/hash replay; it cannot by itself prove the independent assessor did not privately generate unreported alternatives.

Ecological selection algorithm:

1. rank exact-owner anchors by `SHA256(seed + NUL + "exact-owner" + NUL + ecological_source_id)` and choose the first two;
2. rank legitimate-new-artifact anchors similarly and choose the first two;
3. remove those four IDs, rank the remaining eligible items by `SHA256(seed + NUL + "general" + NUL + ecological_source_id)`, and choose the first eight;
4. Pilot receives the first selected anchor of each type plus the first four general selections;
5. Confirmatory receives the second selected anchor of each type plus the remaining four general selections.

The revealed seed must hash to the preregistered `selection_seed_sha256`.

### 6.4 Replayable arm randomization

For task ID `t`, compute `h = SHA256(seed + NUL + "arm-order" + NUL + t)`. If the integer value of `h` is even, order is Control→Treatment; otherwise Treatment→Control.

The prompt pack stores the resulting `planned_order`, and the evaluator reproduces it from the independently generated revealed seed. A committed plan hash alone is not sufficient evidence of randomization.

### 6.5 Prompt-pack schema and wave independence

Prompt packs use schema version 3. Every case includes `task_id`, `task_family_id`, `corpus_class`, `ecological_source_id`, `scenario_families`, `planned_order`, and exact `prompt` text.

Pilot and Confirmatory must have no overlap in:

- concrete `task_family_id`;
- ecological `ecological_source_id`;
- whitespace-normalized/case-folded exact prompt text.

The evaluator rejects any cross-wave normalized prompt collision even when family or source IDs differ.

## 7. Frozen scoring key

A hash commitment to an empty or underspecified key is not sufficient. Scoring keys use schema version 3 and every case must freeze:

- `expected_owner_or_route` — one or more accepted owner/route outcomes;
- `acceptable_alternatives` — explicitly allowed alternatives, possibly empty;
- `required_authoritative_evidence` — nonempty evidence anchors;
- `serious_error_conditions` — nonempty case-specific conditions;
- `decision_acceptance_conditions` — nonempty bounded acceptance conditions;
- `companion_validation_applicable`;
- `dimension_anchors` defining concrete `0`, `1`, and `2` criteria for every applicable score dimension.

The assessor still performs semantic scoring, but the judgment boundary must exist before any run.

## 8. Exact input identity per run

Every run records the exact held-out prompt text, `task_prompt_sha256`, the canonical run-envelope object and SHA-256, and the exact full message delivered to the model plus its SHA-256.

`task_prompt_sha256` hashes the exact UTF-8 prompt, not a normalized representation. Normalization is used only for duplicate/overlap detection.

The canonical envelope includes repository, study ref, wave, task ID, arm, Treatment Delivery Mode or `not-applicable`, and `task_prompt_sha256`.

The canonical full message is deterministic and contains only:

1. `Experiment arm`;
2. study repository;
3. study ref;
4. wave;
5. task ID;
6. Treatment Delivery Mode;
7. the exact task prompt.

No extra hint, owner guess, explanation, or arm-specific prose may be appended. The evaluator reconstructs both envelope and full message from the frozen prompt pack and preregistration. A pair is invalid if either arm received a different prompt, envelope, or full message.

## 9. Structured instrumentation and provenance

Every run contains a canonical `tool_events` list. Each event records contiguous `sequence`, `phase` (`study_infrastructure` or `task_orientation`), tool family, operation, repository, ref when available, resource, `resource_class`, exact response bytes when measurable, and content identity when the event delivers RI aid.

Allowed `resource_class` values are `ordinary_source`, `ri_compact_surface`, `ri_query`, `ri_full_graph`, `repository_control_map`, and `other`.

Each run also freezes:

- `instrumentation_source` = `machine_capture` or `exported_transcript`;
- immutable `raw_evidence_reference`;
- `raw_evidence_sha256`;
- `event_extractor_version`;
- `event_log_sha256` over canonical JSON for `tool_events`.

The evaluator verifies the event-log digest and derives task-orientation connector calls, search calls, RI access, RI payload bytes, repository-response bytes, prohibited Control RI access, and Treatment identity/completeness from events. Summary fields are accepted only when they equal reconstructed values.

Raw transcript/capture evidence remains independently auditable. The evaluator does not inspect hidden reasoning and does not claim to reconstruct unavailable private model state.

### 9.1 Orientation cost boundary

Primary connector-cost metrics count **only `task_orientation` events**. Study-infrastructure calls such as pre/post branch-tip checks, smoke checks, recorder bookkeeping, or hash verification are excluded. Treatment acquisition of RI aid is task-orientation cost and is included.

If `input_tokens` is selected as the context-volume metric, exact client-exposed token counts may remain a direct recorded metric because they are not derivable from connector events.

## 10. Contrast integrity and complete Treatment delivery

A valid Control run must have no task-orientation event classified as any RI resource class.

A valid Treatment run must record successful delivery and prove exact Treatment access from events.

For `connector_compact_surface`, every compact-surface event additionally records:

- `payload_byte_start`;
- `payload_byte_end` (half-open range);
- `payload_chunk_sha256`.

The evaluator compares every chunk directly with the frozen Treatment-surface bytes and requires the ranges to cover byte interval `[0, surface_size)` exactly once with no gaps, overlap, duplicates, wrong identity, or mismatched chunk hash. `complete_treatment_payload_verified` is accepted only when it equals that derived result.

For other delivery modes, the selected protocol must define equivalent exact-aid evidence before execution; at minimum an exact identity-bearing RI event is required.

A contaminated Control or incomplete/wrong Treatment delivery invalidates the pair. Manual flags cannot override contradictory event evidence.

## 11. Correctness scoring

Dimensions are Owner/routing correctness (0–2), Evidence sufficiency (0–2), Authority discipline (0–2), Companion/validation completeness (0–2) when applicable, and Decision quality (0–2).

Serious-error matrix labels are `A-serious/B-no-serious`, `A-no-serious/B-serious`, `both-serious`, and `neither-serious`.

An `A-serious/B-no-serious` pair counts as a qualifying positive reversal only when every applicable Treatment dimension meets the preregistered minimum quality floor, default `>=1`.

Ecological correctness non-regression defaults to median paired total correctness delta `B−A >= 0` in each wave and zero ecological reverse serious-error reversals.

## 12. Cost and efficiency

For each ecological pair define `r_i = B_i/A_i` from **task-orientation connector calls only**. `0/0 -> 1.0`; `A=0, B>0 -> infinity`.

Default correctness-route connector gate per wave: median paired `r_i <= 1.50`, with no more than 2 of 6 ecological cases above `2.00`.

An `ENGINEERING SIGNAL — CONNECTOR INTERACTION ONLY` requires median `r_i <= 0.80` in both waves, ecological correctness non-regression in both waves, and zero reverse serious errors.

`ENGINEERING ACCEPTANCE — ORIENTATION EFFICIENCY` additionally requires one exact preregistered context-volume metric for every ecological run: reconstructed `repository_response_utf8_bytes`, exact client-exposed `input_tokens`, or `unavailable`. Default volume gate per wave is all six pairs measured, median B/A `<=1.00`, and no more than 2 of 6 above `2.00`. If exact volume is unavailable or incomplete, orientation-efficiency acceptance is unavailable by design.

## 13. Final outcomes

Pilot is descriptive only and cannot stop Confirmatory.

The correctness route is an **engineering acceptance criterion**, not a statistical significance claim.

`ENGINEERING ACCEPTANCE — CORRECTNESS` requires all 24 pairs valid; at least 1 qualifying Confirmatory positive reversal; at least 1 qualifying Confirmatory **ecological** positive reversal; at least 3 qualifying positive reversals combined; zero reverse serious-error reversals combined; ecological correctness non-regression in both waves; and connector-cost gate pass in both waves.

Do not present this status as proof of a population-level effect or p-value threshold. With only 24 pairs, the study is an engineering acceptance experiment.

Other outcomes are `ENGINEERING ACCEPTANCE — CORRECTNESS + ORIENTATION EFFICIENCY`, `ENGINEERING ACCEPTANCE — ORIENTATION EFFICIENCY`, `ENGINEERING SIGNAL — CONNECTOR INTERACTION ONLY`, `CORRECTNESS SIGNAL / COST NOT ACCEPTED`, `NOT CONFIRMED`, `NO INCREMENTAL VALUE SHOWN`, `REGRESSION`, and `INCONCLUSIVE`.

## 14. Deterministic evaluator

`.github/scripts/score_repository_intelligence_ab.py` verifies:

- preregistration and smoke eligibility;
- independent-after-pool randomization provenance fields;
- revealed ecological-selection seed and replay;
- revealed arm seeds and arm-order replay;
- prompt/key hashes;
- task-family/source/normalized-prompt independence;
- mandatory/critical scenario coverage;
- ecological anchors per wave;
- scoring-key completeness;
- exact per-run prompt/envelope/full-message identity;
- model/client/source/isolation parity;
- structured instrumentation digest and reconstruction;
- Control ablation integrity;
- exact Treatment-surface identity from bytes;
- complete connector-surface byte coverage;
- paired correctness/cost/context metrics;
- final engineering classification.

The evaluator never inspects hidden model reasoning.

Example invocation after primary evidence is frozen:

```bash
python3 .github/scripts/score_repository_intelligence_ab.py \
  --preregistration /secure/ab-preregistration.json \
  --run-record /secure/ab-run-record.json \
  --ecological-pool /secure/ecological-normalized-pool.json \
  --ecological-selection-seed "$ECO_SELECTION_SEED" \
  --pilot-arm-seed "$PILOT_ARM_SEED" \
  --confirmatory-arm-seed "$CONFIRM_ARM_SEED" \
  --pilot-prompts /secure/pilot-prompts.json \
  --pilot-key /secure/pilot-scoring-key.json \
  --confirmatory-prompts /secure/confirmatory-prompts.json \
  --confirmatory-key /secure/confirmatory-scoring-key.json \
  --treatment-surface /secure/agent-context.json \
  --output /secure/ab-evaluation-report.json
```

## 15. Lifecycle

1. Merge this protocol/infrastructure PR after generated RI surface freshness, tests, companions, and checkpoint are green.
2. Select the exact study commit and establish the repository-mutation freeze.
3. Run the non-scored smoke test in the actual client and freeze its evidence object/reference.
4. Freeze and commit the normalized ecological pool hash **before random seed generation**.
5. Have the independent assessor generate exactly one ecological-selection seed and one arm-order seed per wave; record immutable generation references and seed hashes.
6. Freeze both prompt packs and both strong scoring keys outside the tested Git tree.
7. Preregister model/client, exact Treatment identity, randomization provenance, thresholds, and decision rules.
8. Run Pilot A/B in replayed seeded order and freeze Pilot outputs/scores without changing Confirmatory material.
9. Run Confirmatory A/B in its replayed seeded order and freeze all primary evidence.
10. Reveal seeds and run the deterministic evaluator.
11. Optionally run data-only C or a separate flat-inventory-vs-relational diagnostic.
12. Publish a separate evidence/results PR with revealed evidence, evaluator output, limitations, and conclusion; merge it whether positive, null, regression, or inconclusive.
13. Release the repository-mutation freeze after primary evidence is frozen.

The protocol, templates, evaluator, and narrow benchmark markers remain durable repository test infrastructure after the study.

## 16. What the experiment does not prove

A successful result supports only the tested operational RI route for the tested repository state, model/client, delivery mode, and task distribution. It does not prove universal productivity gain, graph semantics, graph visualization value, Control Map value to agents, another delivery mode, or future-state equivalence.

If relational graph value matters after primary evidence, run a separate flat-owner/inventory versus relational-evidence decomposition diagnostic rather than inferring graph value from this A/B.
