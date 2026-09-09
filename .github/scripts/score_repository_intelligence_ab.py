#!/usr/bin/env python3
"""Mechanically evaluate the preregistered Repository Intelligence A/B study."""
import argparse
import hashlib
import json
import math
import statistics
import sys
from pathlib import Path
PROTOCOL_VERSION = 9
CONTROL = 'RI-AB-CONTROL'
TREATMENT = 'RI-AB-TREATMENT'
PRIMARY_ARMS = {CONTROL, TREATMENT}
CORE_SCORE_FIELDS = ('owner_routing', 'evidence_sufficiency', 'authority_discipline', 'decision_quality')
OPTIONAL_SCORE_FIELD = 'companion_validation'
RESOURCE_CLASSES = {'ordinary_source', 'ri_compact_surface', 'ri_query', 'ri_full_graph', 'repository_control_map', 'other'}
RI_CLASSES = RESOURCE_CLASSES - {'ordinary_source', 'other'}
INSTRUMENTATION_SOURCES = {'machine_capture', 'exported_transcript'}
MANDATORY = {'exact-owner-recovery', 'canonical-term-synonym-pressure', 'near-synonym-source-review', 'overlapping-artifact-refinement', 'legitimate-new-artifact', 'impact-validation-routing', 'accepted-proposed-relation-change', 'branch-behind-target', 'producer-schema-self-change', 'candidate-data-boundary', 'shared-structural-hub', 'research-authority-separation', 'stale-materialization-fallback', 'ukrainian-or-paraphrased-routing'}
CRITICAL = {'accepted-proposed-relation-change', 'branch-behind-target', 'producer-schema-self-change', 'candidate-data-boundary', 'shared-structural-hub', 'stale-materialization-fallback'}
ANCHORS = {'exact-owner-recovery', 'legitimate-new-artifact'}
PREFLIGHT = ('smoke_passed', 'default_branch_tip_checks_verified', 'ordinary_control_search_verified', 'exact_ref_direct_reads_verified', 'treatment_delivery_verified', 'complete_treatment_payload_verified', 'truncation_check_passed', 'instrumentation_capture_verified', 'connector_permission_parity_verified', 'memory_disabled_verified', 'project_context_absent_verified', 'prior_product_repo_context_absent_verified', 'repository_mutation_freeze_acknowledged')

def req(condition, message):
    if not condition:
        raise ValueError(message)

def load(path, label):
    try:
        value = json.loads(Path(path).read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f'{label} is not readable JSON: {exc}') from exc
    req(isinstance(value, dict), f'{label} must be a JSON object')
    return value

def s256b(payload):
    return hashlib.sha256(payload).hexdigest()

def s256f(path):
    return s256b(Path(path).read_bytes())

def s256t(text):
    return s256b(text.encode('utf-8'))

def cjson(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False)

def csha(value):
    return s256t(cjson(value))

def git_blob_sha(payload):
    header = f'blob {len(payload)}\x00'.encode('ascii')
    return hashlib.sha1(header + payload).hexdigest()

def med(values):
    return statistics.median(values) if values else None

def rat(numerator, denominator):
    if denominator == 0:
        return 1.0 if numerator == 0 else math.inf
    return numerator / denominator

def rank(seed, label, identifier):
    return s256t(f'{seed}\x00{label}\x00{identifier}')

def arm_order(seed, task_id):
    return [CONTROL, TREATMENT] if int(rank(seed, 'arm-order', task_id), 16) % 2 == 0 else [TREATMENT, CONTROL]

def eco_select(items, seed):
    exact = [item for item in items if item['anchor_type'] == 'exact-owner']
    new = [item for item in items if item['anchor_type'] == 'legitimate-new-artifact']
    req(len(exact) >= 2 and len(new) >= 2, 'ecological pool needs at least two anchors of each required type')
    exact = sorted(exact, key=lambda item: rank(seed, 'exact-owner', item['ecological_source_id']))[:2]
    new = sorted(new, key=lambda item: rank(seed, 'legitimate-new-artifact', item['ecological_source_id']))[:2]
    used = {item['ecological_source_id'] for item in exact + new}
    rest = sorted([item for item in items if item['ecological_source_id'] not in used], key=lambda item: rank(seed, 'general', item['ecological_source_id']))[:8]
    req(len(rest) == 8, 'ecological pool needs eight non-reserved selections')
    return {'pilot': [exact[0], new[0], *rest[:4]], 'confirmatory': [exact[1], new[1], *rest[4:]]}

def envelope(p, wave, task_id, arm, prompt_sha):
    return {'repository': p['repository'], 'repository_ref': p['repository_ref'], 'source_state_lock': 'stable_default_branch_window', 'wave': wave, 'task_id': task_id, 'arm': arm, 'treatment_delivery_mode': p['treatment_delivery']['mode'] if arm == TREATMENT else 'not-applicable', 'task_prompt_sha256': prompt_sha}

def validate_prereg(p):
    req(p.get('protocol_version') == PROTOCOL_VERSION, 'unsupported protocol_version')
    for field in ('study_id', 'repository', 'repository_ref', 'model_family', 'thinking_configuration', 'client_environment', 'connector'):
        req(isinstance(p.get(field), str) and p[field], f'{field} must be preregistered')
    req(p.get('execution_policy') == 'always_run_pilot_and_confirmatory', 'both primary waves must run')
    lock = p.get('source_state_lock')
    req(isinstance(lock, dict) and lock.get('mode') == 'stable_default_branch_window' and lock.get('expected_default_branch_tip_sha') == p['repository_ref'], 'invalid source_state_lock')
    for field in ('repository_mutations_prohibited_during_primary', 'pre_run_tip_check_required', 'post_run_tip_check_required', 'ordinary_default_branch_search_allowed'):
        req(lock.get(field) is True, f'source-state field {field} must be true')
    preflight = p.get('execution_preflight')
    req(isinstance(preflight, dict), 'execution_preflight required')
    for field in PREFLIGHT:
        req(preflight.get(field) is True, f'execution preflight field {field} must be true')
    isolation = p.get('isolation_requirements')
    req(isinstance(isolation, dict), 'isolation_requirements required')
    for field, expected in {'conversation_fresh': True, 'memory_enabled': False, 'project_context_present': False, 'prior_repo_context_available': False, 'previous_arm_output_exposed': False, 'corrective_scoring_feedback_before_pair_complete': False, 'future_wave_material_exposed': False, 'hidden_benchmark_material_exposed': False}.items():
        req(isolation.get(field) is expected, f'isolation {field} must be {expected}')
    delivery = p.get('treatment_delivery')
    req(isinstance(delivery, dict) and delivery.get('mode') in {'connector_compact_surface', 'local_cli', 'dedicated_adapter'}, 'invalid Treatment Delivery Mode')
    identity = delivery.get('aid_identity')
    req(isinstance(identity, dict) and identity.get('mode') == delivery['mode'], 'Treatment aid identity required')
    for field in ('identifier', 'git_blob_sha', 'content_sha256', 'source_identity'):
        req(isinstance(identity.get(field), str) and identity[field], f'Treatment aid identity {field} required')
    req(set(p.get('mandatory_scenario_families', [])) == MANDATORY, 'mandatory scenario family set mismatch')
    req(set(p.get('confirmatory_required_scenario_families', [])) >= CRITICAL, 'confirmatory critical coverage set incomplete')
    for key in ('pilot', 'confirmatory'):
        wave = p.get(key)
        req(isinstance(wave, dict) and wave.get('case_count') == 12 and wave.get('stress_cases') == 6 and wave.get('ecological_cases') == 6, f'{key} must be 6+6')
        for field in ('prompts_sha256', 'scoring_key_sha256', 'arm_order_seed_sha256'):
            req(isinstance(wave.get(field), str) and len(wave[field]) == 64, f'{key}.{field} must be SHA-256')
    eco = p.get('ecological_source_pool')
    req(isinstance(eco, dict) and eco.get('mode') == 'combined_pool', 'v9 requires one combined ecological pool')
    for field in ('normalized_eligible_pool_sha256', 'selection_seed_sha256'):
        req(isinstance(eco.get(field), str) and len(eco[field]) == 64, f'ecological_source_pool.{field} must be SHA-256')
    req(p.get('prompt_pack_schema_version') == 3 and p.get('scoring_key_schema_version') == 3, 'v9 requires schema version 3')
    req(p.get('orientation_cost_boundary') == 'task_orientation_events_only', 'orientation cost boundary invalid')
    req(p.get('claim_boundary') == 'engineering acceptance; not statistical significance or universal productivity proof', 'claim boundary invalid')

def validate_treatment_surface(path, p):
    identity = p['treatment_delivery']['aid_identity']
    payload = Path(path).read_bytes()
    req(s256b(payload) == identity['content_sha256'], 'Treatment surface content SHA-256 mismatch')
    req(git_blob_sha(payload) == identity['git_blob_sha'], 'Treatment surface Git blob SHA mismatch')
    try:
        parsed = json.loads(payload.decode('utf-8'))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f'Treatment surface is not valid UTF-8 JSON: {exc}') from exc
    source = parsed.get('source_identity') if isinstance(parsed, dict) else None
    req(isinstance(source, dict) and source.get('digest') == identity['source_identity'], 'Treatment surface source_identity mismatch')
    return {'content_sha256': s256b(payload), 'git_blob_sha': git_blob_sha(payload), 'source_identity': source['digest'], 'utf8_bytes': len(payload)}

def validate_pool(path, p, seed):
    req(s256f(path) == p['ecological_source_pool']['normalized_eligible_pool_sha256'], 'ecological pool hash mismatch')
    req(s256t(seed) == p['ecological_source_pool']['selection_seed_sha256'], 'ecological selection seed commitment mismatch')
    pool = load(path, 'ecological pool')
    items = pool.get('items')
    req(pool.get('schema_version') == 1 and isinstance(items, list) and len(items) >= 24, 'invalid ecological pool')
    source_ids, family_ids = set(), set()
    for item in items:
        req(isinstance(item, dict) and item.get('anchor_type') in {'exact-owner', 'legitimate-new-artifact', 'none'}, 'invalid ecological pool item')
        for field in ('ecological_source_id', 'task_family_id', 'normalized_prompt'):
            req(isinstance(item.get(field), str) and item[field], f'ecological pool {field} required')
        scenarios = item.get('scenario_families')
        req(isinstance(scenarios, list) and all(value in MANDATORY for value in scenarios), 'ecological pool scenario_families invalid')
        if item['anchor_type'] == 'exact-owner':
            req('exact-owner-recovery' in scenarios, 'exact-owner pool anchor must exercise exact-owner-recovery')
        if item['anchor_type'] == 'legitimate-new-artifact':
            req('legitimate-new-artifact' in scenarios, 'new-artifact pool anchor must exercise legitimate-new-artifact')
        req(item['ecological_source_id'] not in source_ids, 'ecological source IDs must be unique')
        req(item['task_family_id'] not in family_ids, 'ecological task families must be unique')
        source_ids.add(item['ecological_source_id'])
        family_ids.add(item['task_family_id'])
    return items, eco_select(items, seed)

def validate_pack(path, expected_hash, wave_name, seed):
    req(s256f(path) == expected_hash, f'{wave_name} prompt-pack hash mismatch')
    pack = load(path, f'{wave_name} prompt pack')
    cases = pack.get('cases')
    req(pack.get('schema_version') == 3 and pack.get('wave') == wave_name and isinstance(cases, list) and len(cases) == 12, f'{wave_name} prompt pack invalid')
    out = {'ids': [], 'classes': {}, 'prompts': {}, 'prompt_text': {}, 'families': {}, 'sources': {}, 'scenarios': {}, 'orders': {}}
    for case in cases:
        task_id = case.get('task_id'); corpus = case.get('corpus_class'); prompt = case.get('prompt'); family = case.get('task_family_id'); source = case.get('ecological_source_id'); scenarios = case.get('scenario_families')
        req(isinstance(task_id, str) and task_id and task_id not in out['ids'], f'{wave_name} task_id invalid')
        req(corpus in {'stress', 'ecological'} and isinstance(prompt, str) and prompt.strip() and isinstance(family, str) and family, f'{wave_name} case invalid')
        req(isinstance(scenarios, list) and all(value in MANDATORY for value in scenarios), f'{wave_name} scenarios invalid')
        req((corpus == 'ecological' and isinstance(source, str) and source) or (corpus == 'stress' and source is None and scenarios), f'{wave_name} source/scenario contract invalid')
        order = arm_order(seed, task_id)
        req(case.get('planned_order') == order, f'{wave_name} arm order not reproduced by seed')
        out['ids'].append(task_id); out['classes'][task_id] = corpus; out['prompts'][task_id] = s256t(prompt); out['prompt_text'][task_id] = prompt; out['families'][task_id] = family; out['sources'][task_id] = source; out['scenarios'][task_id] = scenarios; out['orders'][task_id] = order
    req(list(out['classes'].values()).count('stress') == 6 and list(out['classes'].values()).count('ecological') == 6, f'{wave_name} must be 6+6')
    return out

def validate_key(path, expected_hash, wave_name, ids):
    req(s256f(path) == expected_hash, f'{wave_name} scoring-key hash mismatch')
    key = load(path, f'{wave_name} scoring key'); cases = key.get('cases')
    req(key.get('schema_version') == 3 and key.get('wave') == wave_name and isinstance(cases, list), f'{wave_name} scoring key invalid')
    out = {}
    for case in cases:
        task_id = case.get('task_id'); req(task_id in ids and task_id not in out, f'{wave_name} scoring-key task IDs invalid'); req(type(case.get('companion_validation_applicable')) is bool, f'{task_id} companion applicability missing')
        for field in ('expected_owner_or_route', 'required_authoritative_evidence', 'serious_error_conditions', 'decision_acceptance_conditions'):
            req(isinstance(case.get(field), list) and case[field], f'{task_id} scoring key {field} must be non-empty')
        req(isinstance(case.get('acceptable_alternatives'), list), f'{task_id} acceptable_alternatives must be list')
        anchors = case.get('dimension_anchors'); req(isinstance(anchors, dict), f'{task_id} dimension_anchors missing')
        dimensions = set(CORE_SCORE_FIELDS) | ({OPTIONAL_SCORE_FIELD} if case['companion_validation_applicable'] else set()); req(set(anchors) == dimensions, f'{task_id} dimension anchors mismatch')
        for dimension, levels in anchors.items(): req(isinstance(levels, dict) and set(levels) == {'0', '1', '2'} and all(isinstance(value, str) and value for value in levels.values()), f'{task_id} {dimension} anchors invalid')
        out[task_id] = case
    req(set(out) == set(ids), f'{wave_name} scoring-key IDs must match prompt pack')
    return out

def verify_evidence(p, paths, seeds):
    pool_items, selected = validate_pool(paths['ecological_pool'], p, seeds['ecological_selection']); pool_by_id = {item['ecological_source_id']: item for item in pool_items}; packs, keys = {}, {}
    for key, wave_name in (('pilot', 'PILOT'), ('confirmatory', 'CONFIRMATORY')):
        req(s256t(seeds[key + '_arm']) == p[key]['arm_order_seed_sha256'], f'{wave_name} arm seed commitment mismatch')
        packs[key] = validate_pack(paths[key + '_prompts'], p[key]['prompts_sha256'], wave_name, seeds[key + '_arm']); keys[key] = validate_key(paths[key + '_key'], p[key]['scoring_key_sha256'], wave_name, packs[key]['ids'])
        expected_ids = sorted(item['ecological_source_id'] for item in selected[key]); actual_ids = sorted(source for source in packs[key]['sources'].values() if source); req(actual_ids == expected_ids, f'{wave_name} ecological selection not reproduced from pool+seed')
        for task_id in packs[key]['ids']:
            source_id = packs[key]['sources'][task_id]
            if not source_id: continue
            item = pool_by_id[source_id]
            req(packs[key]['families'][task_id] == item['task_family_id'], f'{wave_name} selected task family differs from pool')
            req(packs[key]['prompt_text'][task_id] == item['normalized_prompt'], f'{wave_name} selected prompt differs from frozen normalized pool')
            req(packs[key]['scenarios'][task_id] == item['scenario_families'], f'{wave_name} selected scenarios differ from frozen pool')
        eco_scenarios = {scenario for task_id, scenarios in packs[key]['scenarios'].items() if packs[key]['classes'][task_id] == 'ecological' for scenario in scenarios}; req(ANCHORS <= eco_scenarios, f'{wave_name} ecological half misses required anchors')
    req(not set(packs['pilot']['families'].values()) & set(packs['confirmatory']['families'].values()), 'task_family_id overlaps across waves')
    pilot_sources = {source for source in packs['pilot']['sources'].values() if source}; confirm_sources = {source for source in packs['confirmatory']['sources'].values() if source}; req(not pilot_sources & confirm_sources, 'ecological_source_id overlaps across waves')
    all_scenarios = {scenario for pack in packs.values() for scenarios in pack['scenarios'].values() for scenario in scenarios}; req(MANDATORY <= all_scenarios, 'held-out corpora miss mandatory scenarios')
    confirm_scenarios = {scenario for scenarios in packs['confirmatory']['scenarios'].values() for scenario in scenarios}; req(set(p['confirmatory_required_scenario_families']) <= confirm_scenarios, 'Confirmatory misses critical scenarios')
    return {'packs': packs, 'keys': keys, 'selection_replayed': True, 'arm_randomization_replayed': True}

def score_total(scores, key):
    req(isinstance(scores, dict), 'scores required'); values = {}
    for field in CORE_SCORE_FIELDS: req(type(scores.get(field)) is int and 0 <= scores[field] <= 2, f'{field} score invalid'); values[field] = scores[field]
    companion = scores.get(OPTIONAL_SCORE_FIELD)
    if key['companion_validation_applicable']: req(type(companion) is int and 0 <= companion <= 2, 'companion_validation must be scored'); values[OPTIONAL_SCORE_FIELD] = companion
    else: req(companion is None, 'companion_validation must be null')
    total = sum(values.values()); req(scores.get('total_applicable_correctness') == total, 'total_applicable_correctness mismatch'); req(type(scores.get('serious_routing_error')) is bool, 'serious_routing_error must be boolean')
    return total, scores['serious_routing_error'], values

def derive(run, p):
    events = run.get('tool_events'); req(isinstance(events, list), 'tool_events must be list'); req(run.get('instrumentation_source') in INSTRUMENTATION_SOURCES, 'instrumentation_source must be machine_capture or exported_transcript'); req(isinstance(run.get('transcript_reference'), str) and run['transcript_reference'], 'transcript_reference required')
    for index, event in enumerate(events, 1): req(isinstance(event, dict) and event.get('sequence') == index and event.get('phase') in {'study_infrastructure', 'task_orientation'} and event.get('resource_class') in RESOURCE_CLASSES and event.get('repository') == p['repository'], 'invalid tool event'); req(event.get('response_bytes') is None or type(event['response_bytes']) is int and event['response_bytes'] >= 0, 'invalid response_bytes')
    task = [event for event in events if event['phase'] == 'task_orientation']; ri = [event for event in task if event['resource_class'] in RI_CLASSES]; repo_bytes = None if any(event.get('response_bytes') is None for event in task) else sum(event['response_bytes'] for event in task); ri_bytes = None if any(event.get('response_bytes') is None for event in ri) else sum(event['response_bytes'] for event in ri)
    return {'calls': len(task), 'infrastructure_calls': len(events) - len(task), 'searches': sum(event.get('operation') in {'search', 'code_search'} for event in task), 'ri': bool(ri), 'ri_bytes': 0 if not ri else ri_bytes, 'repo_bytes': repo_bytes, 'bad_control': any(event['resource_class'] in RI_CLASSES for event in task), 'identity': any(event.get('content_identity') == p['treatment_delivery']['aid_identity'] for event in ri)}

def run_valid(run, arm, wave, task_id, prompt_text, prompt_hash, order, p):
    reasons = []; expected_env = envelope(p, wave, task_id, arm, prompt_hash)
    checks = {'wrong arm': run.get('arm') == arm, 'submitted task prompt mismatch': run.get('submitted_task_prompt') == prompt_text, 'task prompt hash mismatch': run.get('task_prompt_sha256') == prompt_hash, 'run envelope object mismatch': run.get('submitted_run_envelope') == expected_env, 'run envelope hash mismatch': run.get('run_envelope_sha256') == csha(expected_env), 'conversation not fresh': run.get('conversation_fresh') is True, 'Memory not disabled': run.get('memory_enabled') is False, 'Project context present': run.get('project_context_present') is False, 'prior repo context present': run.get('prior_repo_context_available') is False, 'previous arm exposed': run.get('previous_arm_output_exposed') is False, 'corrective feedback exposed': run.get('corrective_scoring_feedback_before_pair_complete') is False, 'future wave exposed': run.get('future_wave_material_exposed') is False, 'hidden benchmark exposed': run.get('hidden_benchmark_material_exposed') is False, 'connector state mismatch': run.get('connector_state_equal') is True, 'source pre mismatch': run.get('source_state_pre_sha') == p['repository_ref'], 'source post mismatch': run.get('source_state_post_sha') == p['repository_ref'], 'source protocol violation': run.get('source_state_protocol_violation') is False, 'model mismatch': run.get('model_family') == p['model_family'], 'thinking mismatch': run.get('thinking_configuration') == p['thinking_configuration'], 'client mismatch': run.get('client_environment') == p['client_environment'], 'connector mismatch': run.get('connector') == p['connector']}
    reasons.extend(message for message, passed in checks.items() if not passed); req(run.get('pair_order') == order, 'pair_order mismatch'); req(isinstance(run.get('protocol_violations'), list), 'protocol_violations must be list')
    if run['protocol_violations']: reasons.append('protocol violations')
    derived = derive(run, p)
    for summary_field, derived_field in (('total_connector_calls', 'calls'), ('default_branch_search_calls', 'searches'), ('ri_payload_bytes', 'ri_bytes'), ('repository_response_utf8_bytes', 'repo_bytes')):
        if run.get(summary_field) != derived[derived_field]: reasons.append(f'{summary_field} does not match structured events')
    if arm == CONTROL:
        if derived['bad_control']: reasons.append('Control RI ablation contaminated by structured events')
        if run.get('treatment_delivery_status') not in {None, 'not-applicable'}: reasons.append('Control records Treatment delivery')
    else:
        if run.get('treatment_delivery_status') != 'delivered': reasons.append('Treatment delivery failed')
        if run.get('treatment_surface_verified') is not True or run.get('complete_treatment_payload_verified') is not True: reasons.append('Treatment payload not verified')
        if not derived['ri'] or not derived['identity']: reasons.append('Treatment events do not prove exact aid access')
    return reasons, derived

def eval_case(case, pack, key, wave, p):
    task_id = case.get('task_id'); req(task_id in pack['ids'] and case.get('corpus_class') == pack['classes'][task_id], 'run case mismatch'); order = pack['orders'][task_id]; req(case.get('order') == order, 'run order mismatch'); runs = case.get('runs'); req(isinstance(runs, list) and len(runs) == 2 and [run.get('arm') for run in runs] == order, 'execution order mismatch'); by_arm = {run['arm']: run for run in runs}; req(set(by_arm) == PRIMARY_ARMS, 'pair requires both arms')
    invalid, derived = {}, {}
    for arm in (CONTROL, TREATMENT): invalid[arm], derived[arm] = run_valid(by_arm[arm], arm, wave, task_id, pack['prompt_text'][task_id], pack['prompts'][task_id], order, p)
    if invalid[CONTROL] or invalid[TREATMENT]: return {'task_id': task_id, 'corpus_class': case['corpus_class'], 'valid': False, 'invalid_reasons': invalid}
    a_total, a_serious, _ = score_total(by_arm[CONTROL]['scores'], key); b_total, b_serious, b_values = score_total(by_arm[TREATMENT]['scores'], key); state = 'A-serious/B-no-serious' if a_serious and not b_serious else 'A-no-serious/B-serious' if b_serious and not a_serious else 'both-serious' if a_serious else 'neither-serious'; quality = all(value >= p['positive_reversal_quality_gate']['minimum_each_applicable_dimension'] for value in b_values.values()); metric = p['context_volume']['metric']; volume_a = derived[CONTROL]['repo_bytes'] if metric == 'repository_response_utf8_bytes' else by_arm[CONTROL].get('measured_input_tokens') if metric == 'input_tokens' else None; volume_b = derived[TREATMENT]['repo_bytes'] if metric == 'repository_response_utf8_bytes' else by_arm[TREATMENT].get('measured_input_tokens') if metric == 'input_tokens' else None
    return {'task_id': task_id, 'corpus_class': case['corpus_class'], 'valid': True, 'correctness_delta_b_minus_a': b_total - a_total, 'serious_error_outcome': state, 'qualifying_positive_reversal': state == 'A-serious/B-no-serious' and quality, 'connector_ratio_b_over_a': rat(derived[TREATMENT]['calls'], derived[CONTROL]['calls']), 'context_volume_ratio_b_over_a': None if volume_a is None or volume_b is None else rat(volume_b, volume_a), 'equal_correctness_pair': a_total == b_total and a_serious == b_serious, 'derived_infrastructure_calls_a': derived[CONTROL]['infrastructure_calls'], 'derived_infrastructure_calls_b': derived[TREATMENT]['infrastructure_calls']}

def eval_wave(name, cases, pack, keys, p):
    req(isinstance(cases, list) and len(cases) == 12, f'{name} needs 12 cases'); by_id = {case.get('task_id'): case for case in cases}; req(set(by_id) == set(pack['ids']), f'{name} task IDs mismatch'); evaluated = [eval_case(by_id[task_id], pack, keys[task_id], name, p) for task_id in pack['ids']]; valid = [case for case in evaluated if case['valid']]; ecological = [case for case in valid if case['corpus_class'] == 'ecological']; all_valid = len(valid) == 12 and len(ecological) == 6; positive = sum(case.get('qualifying_positive_reversal') is True for case in valid); ecological_positive = sum(case.get('qualifying_positive_reversal') is True for case in ecological); reverse = sum(case.get('serious_error_outcome') == 'A-no-serious/B-serious' for case in valid); ecological_reverse = sum(case.get('serious_error_outcome') == 'A-no-serious/B-serious' for case in ecological); deltas = [case['correctness_delta_b_minus_a'] for case in ecological]; nonreg = all_valid and med(deltas) >= p['ecological_correctness_non_regression']['minimum_per_wave'] and ecological_reverse == 0; connector_ratios = [case['connector_ratio_b_over_a'] for case in ecological]; connector_median = med(connector_ratios); connector_gate = all_valid and connector_median <= p['connector_cost_gate']['acceptable_median_ratio_b_over_a'] and sum(value > p['connector_cost_gate']['high_overhead_ratio_threshold'] for value in connector_ratios) <= p['connector_cost_gate']['acceptable_high_overhead_case_count']; connector_gain = all_valid and nonreg and reverse == 0 and connector_median <= p['connector_interaction_gain_rule']['maximum_median_ratio_b_over_a_per_wave']; volume_ratios = [case['context_volume_ratio_b_over_a'] for case in ecological]; complete_volume = p['context_volume']['metric'] != 'unavailable' and all(value is not None for value in volume_ratios); volume_gate = complete_volume and med(volume_ratios) <= p['context_volume']['maximum_median_ratio_b_over_a_per_wave'] and sum(value > p['context_volume']['high_overhead_ratio_threshold'] for value in volume_ratios) <= p['context_volume']['acceptable_high_overhead_case_count']
    return {'name': name, 'cases': evaluated, 'all_pairs_valid': all_valid, 'qualifying_positive_reversals': positive, 'qualifying_ecological_positive_reversals': ecological_positive, 'reverse_serious_reversals': reverse, 'ecological_correctness_non_regression_passed': nonreg, 'ecological_median_connector_ratio': connector_median, 'connector_cost_gate_passed': connector_gate, 'connector_interaction_gain_passed': connector_gain, 'ecological_median_context_volume_ratio': med(volume_ratios) if complete_volume else None, 'context_volume_gate_passed': volume_gate, 'orientation_efficiency_passed': connector_gain and volume_gate}

def final(pilot, confirmatory, p):
    all_valid = pilot['all_pairs_valid'] and confirmatory['all_pairs_valid']; positive = pilot['qualifying_positive_reversals'] + confirmatory['qualifying_positive_reversals']; reverse = pilot['reverse_serious_reversals'] + confirmatory['reverse_serious_reversals']; rule = p['final_decision_rule']['engineering_acceptance_correctness']; thresholds = confirmatory['qualifying_positive_reversals'] >= rule['minimum_confirmatory_positive_reversals'] and confirmatory['qualifying_ecological_positive_reversals'] >= rule['minimum_confirmatory_ecological_positive_reversals'] and positive >= rule['minimum_combined_positive_reversals'] and reverse <= rule['maximum_combined_reverse_serious_reversals'] and pilot['ecological_correctness_non_regression_passed'] and confirmatory['ecological_correctness_non_regression_passed']; cost_ok = pilot['connector_cost_gate_passed'] and confirmatory['connector_cost_gate_passed']; correctness_acceptance = all_valid and thresholds and cost_ok; connector_signal = all_valid and reverse == 0 and pilot['connector_interaction_gain_passed'] and confirmatory['connector_interaction_gain_passed']; efficiency_acceptance = connector_signal and pilot['orientation_efficiency_passed'] and confirmatory['orientation_efficiency_passed']; regression = all_valid and (reverse > 0 or not pilot['ecological_correctness_non_regression_passed'] or not confirmatory['ecological_correctness_non_regression_passed'])
    if not all_valid: status = 'INCONCLUSIVE'
    elif regression: status = 'REGRESSION'
    elif correctness_acceptance and efficiency_acceptance: status = 'ENGINEERING ACCEPTANCE — CORRECTNESS + ORIENTATION EFFICIENCY'
    elif correctness_acceptance: status = 'ENGINEERING ACCEPTANCE — CORRECTNESS'
    elif efficiency_acceptance: status = 'ENGINEERING ACCEPTANCE — ORIENTATION EFFICIENCY'
    elif thresholds and not cost_ok: status = 'CORRECTNESS SIGNAL / COST NOT ACCEPTED'
    elif connector_signal: status = 'ENGINEERING SIGNAL — CONNECTOR INTERACTION ONLY'
    elif pilot['qualifying_positive_reversals']: status = 'NOT CONFIRMED'
    else: status = 'NO INCREMENTAL VALUE SHOWN'
    return {'all_primary_pairs_valid': all_valid, 'combined_qualifying_positive_reversals': positive, 'combined_reverse_serious_reversals': reverse, 'engineering_acceptance_correctness': correctness_acceptance, 'engineering_acceptance_orientation_efficiency': efficiency_acceptance, 'connector_interaction_signal': connector_signal, 'inferential_significance_claimed': False, 'regression': regression, 'final_status': status}

def validate_run_record(record, p):
    req(record.get('protocol_version') == PROTOCOL_VERSION and record.get('study_id') == p['study_id'], 'run record protocol/study mismatch'); preflight = record.get('execution_preflight'); req(isinstance(preflight, dict) and preflight.get('eligible_to_start_primary') is True, 'run record preflight/eligibility missing')
    for field in PREFLIGHT: req(preflight.get(field) is True, f'run record preflight {field} must be true')

def evaluate(p, record, evidence):
    validate_prereg(p); validate_run_record(record, p); pilot = eval_wave('PILOT', record.get('pilot_cases'), evidence['packs']['pilot'], evidence['keys']['pilot'], p); confirmatory = eval_wave('CONFIRMATORY', record.get('confirmatory_cases'), evidence['packs']['confirmatory'], evidence['keys']['confirmatory'], p)
    return {'evaluation_version': 4, 'protocol_version': PROTOCOL_VERSION, 'study_id': p['study_id'], 'repository_ref': p['repository_ref'], 'evidence_verification': {'selection_replayed': True, 'arm_randomization_replayed': True, 'pool_materialization_matches_selected_prompts': True, 'treatment_surface_identity_verified_from_bytes': True, 'strong_scoring_keys_verified': True}, 'pilot': pilot, 'confirmatory': confirmatory, 'final_conclusion': final(pilot, confirmatory, p)}

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument('--preregistration', type=Path, required=True); parser.add_argument('--run-record', type=Path, required=True); parser.add_argument('--ecological-pool', type=Path, required=True); parser.add_argument('--ecological-selection-seed', required=True); parser.add_argument('--pilot-arm-seed', required=True); parser.add_argument('--confirmatory-arm-seed', required=True); parser.add_argument('--pilot-prompts', type=Path, required=True); parser.add_argument('--pilot-key', type=Path, required=True); parser.add_argument('--confirmatory-prompts', type=Path, required=True); parser.add_argument('--confirmatory-key', type=Path, required=True); parser.add_argument('--treatment-surface', type=Path, required=True); parser.add_argument('--output', type=Path, required=True); args = parser.parse_args(argv)
    try:
        prereg = load(args.preregistration, 'preregistration'); record = load(args.run_record, 'run record'); validate_prereg(prereg); treatment_evidence = validate_treatment_surface(args.treatment_surface, prereg); evidence = verify_evidence(prereg, {'ecological_pool': args.ecological_pool, 'pilot_prompts': args.pilot_prompts, 'pilot_key': args.pilot_key, 'confirmatory_prompts': args.confirmatory_prompts, 'confirmatory_key': args.confirmatory_key}, {'ecological_selection': args.ecological_selection_seed, 'pilot_arm': args.pilot_arm_seed, 'confirmatory_arm': args.confirmatory_arm_seed}); evidence['treatment_surface'] = treatment_evidence; output = evaluate(prereg, record, evidence); output['evidence_verification']['treatment_surface'] = treatment_evidence; args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(json.dumps(output, indent=2, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8'); print('Repository Intelligence A/B evaluation: ' + output['final_conclusion']['final_status']); return 0
    except (OSError, ValueError) as exc: print(f'Repository Intelligence A/B evaluation error: {exc}', file=sys.stderr); return 2

deterministic_ecological_selection = eco_select
deterministic_arm_order = arm_order
expected_envelope = envelope
sha256_text = s256t
PREFLIGHT_TRUE_FIELDS = PREFLIGHT
MANDATORY_SCENARIO_FAMILIES = MANDATORY
CONFIRMATORY_CRITICAL_FAMILIES = CRITICAL
if __name__ == '__main__':
    raise SystemExit(main())
