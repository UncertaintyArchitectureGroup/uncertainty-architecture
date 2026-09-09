#!/usr/bin/env python3
import copy
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[2] / 'scripts' / 'score_repository_intelligence_ab.py'
spec = importlib.util.spec_from_file_location('ri_ab', MODULE_PATH)
E = importlib.util.module_from_spec(spec)
spec.loader.exec_module(E)


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8')
    return hashlib.sha256(path.read_bytes()).hexdigest()


class EvaluatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.ref = 'a' * 40
        self.eco_seed = 'eco-seed-v9'
        self.pilot_seed = 'pilot-seed-v9'
        self.confirm_seed = 'confirm-seed-v9'
        self.surface_path = self.root / 'agent-context.json'
        surface = {'schema_version': 2, 'source_identity': {'digest': 'source-v9'}, 'data': ['x', 'y']}
        dump(self.surface_path, surface)
        payload = self.surface_path.read_bytes()
        self.identity = {
            'mode': 'connector_compact_surface',
            'identifier': 'assets/repository-intelligence/agent-context.json',
            'git_blob_sha': E.git_blob_sha(payload),
            'content_sha256': hashlib.sha256(payload).hexdigest(),
            'source_identity': 'source-v9',
        }
        self.pool_path = self.root / 'pool.json'
        self.pool_items = self.make_pool()
        self.pool_hash = dump(self.pool_path, {'schema_version': 1, 'items': self.pool_items})
        self.selected = E.eco_select(self.pool_items, self.eco_seed)
        self.paths = {}
        self.make_prompt_and_key_files()
        self.prereg = self.make_prereg()
        self.record = self.make_record()
        self.evidence = E.verify_evidence(
            self.prereg,
            self.paths,
            {'ecological_selection': self.eco_seed, 'pilot_arm': self.pilot_seed, 'confirmatory_arm': self.confirm_seed},
        )
        self.evidence['treatment_surface'] = E.validate_treatment_surface(self.surface_path, self.prereg)

    def make_pool(self):
        items = []
        for i in range(24):
            if i < 2:
                anchor = 'exact-owner'
                scenarios = ['exact-owner-recovery']
            elif i < 4:
                anchor = 'legitimate-new-artifact'
                scenarios = ['legitimate-new-artifact']
            else:
                anchor = 'none'
                scenarios = ['ukrainian-or-paraphrased-routing'] if i == 4 else ['near-synonym-source-review']
            items.append({
                'ecological_source_id': f'E{i:02d}',
                'task_family_id': f'ECO-FAMILY-{i:02d}',
                'normalized_prompt': f'Ecological task {i:02d}: determine the repository owner and required evidence.',
                'anchor_type': anchor,
                'scenario_families': scenarios,
            })
        return items

    def make_prompt_and_key_files(self):
        pilot_stress = [
            ['canonical-term-synonym-pressure', 'impact-validation-routing'],
            ['overlapping-artifact-refinement', 'research-authority-separation'],
            ['accepted-proposed-relation-change', 'branch-behind-target'],
            ['producer-schema-self-change', 'candidate-data-boundary'],
            ['shared-structural-hub', 'stale-materialization-fallback'],
            ['ukrainian-or-paraphrased-routing', 'near-synonym-source-review'],
        ]
        confirm_stress = [
            ['accepted-proposed-relation-change'],
            ['branch-behind-target'],
            ['producer-schema-self-change'],
            ['candidate-data-boundary'],
            ['shared-structural-hub'],
            ['stale-materialization-fallback'],
        ]
        for key, wave, prefix, seed, stress in (
            ('pilot', 'PILOT', 'P', self.pilot_seed, pilot_stress),
            ('confirmatory', 'CONFIRMATORY', 'C', self.confirm_seed, confirm_stress),
        ):
            cases = []
            scoring = []
            for i in range(12):
                task_id = f'{prefix}{i+1:02d}'
                if i < 6:
                    prompt = f'{wave} stress task {i+1}: inspect repository routing scenario {i+1}.'
                    family = f'{wave}-STRESS-FAMILY-{i+1}'
                    source = None
                    scenarios = stress[i]
                else:
                    item = self.selected[key][i-6]
                    prompt = item['normalized_prompt']
                    family = item['task_family_id']
                    source = item['ecological_source_id']
                    scenarios = item['scenario_families']
                cases.append({
                    'task_id': task_id,
                    'task_family_id': family,
                    'corpus_class': 'stress' if i < 6 else 'ecological',
                    'ecological_source_id': source,
                    'scenario_families': scenarios,
                    'planned_order': E.arm_order(seed, task_id),
                    'prompt': prompt,
                })
                applicable = i % 2 == 0
                dims = {field: {'0': 'wrong', '1': 'bounded partial', '2': 'correct and evidenced'} for field in E.CORE_SCORE_FIELDS}
                if applicable:
                    dims[E.OPTIONAL_SCORE_FIELD] = {'0': 'missed', '1': 'partial', '2': 'complete'}
                scoring.append({
                    'task_id': task_id,
                    'expected_owner_or_route': ['expected owner'],
                    'acceptable_alternatives': [],
                    'required_authoritative_evidence': ['authoritative source'],
                    'serious_error_conditions': ['routes to wrong canonical owner'],
                    'decision_acceptance_conditions': ['bounded repository decision'],
                    'companion_validation_applicable': applicable,
                    'dimension_anchors': dims,
                })
            pp = self.root / f'{key}-prompts.json'
            kk = self.root / f'{key}-key.json'
            ph = dump(pp, {'schema_version': 3, 'wave': wave, 'cases': cases})
            kh = dump(kk, {'schema_version': 3, 'wave': wave, 'cases': scoring})
            self.paths[f'{key}_prompts'] = pp
            self.paths[f'{key}_key'] = kk
            setattr(self, f'{key}_prompt_hash', ph)
            setattr(self, f'{key}_key_hash', kh)
        self.paths['ecological_pool'] = self.pool_path

    def make_prereg(self):
        return {
            'protocol_version': 9,
            'study_id': 'RI-AB-TEST',
            'repository': 'UncertaintyArchitectureGroup/uncertainty-architecture',
            'repository_ref': self.ref,
            'default_branch': 'main',
            'execution_policy': 'always_run_pilot_and_confirmatory',
            'source_state_lock': {
                'mode': 'stable_default_branch_window',
                'expected_default_branch_tip_sha': self.ref,
                'repository_mutations_prohibited_during_primary': True,
                'pre_run_tip_check_required': True,
                'post_run_tip_check_required': True,
                'ordinary_default_branch_search_allowed': True,
            },
            'execution_preflight': {
                'smoke_evidence_reference': 'https://example.invalid/smoke/1',
                'smoke_evidence_sha256': '1' * 64,
                **{field: True for field in E.PREFLIGHT},
            },
            'isolation_requirements': {
                'conversation_fresh': True,
                'memory_enabled': False,
                'project_context_present': False,
                'prior_repo_context_available': False,
                'previous_arm_output_exposed': False,
                'corrective_scoring_feedback_before_pair_complete': False,
                'future_wave_material_exposed': False,
                'hidden_benchmark_material_exposed': False,
            },
            'model_family': 'GPT-X',
            'thinking_configuration': 'High',
            'client_environment': 'clean-test-client',
            'connector': 'GitHub',
            'treatment_delivery': {'mode': 'connector_compact_surface', 'aid_identity': self.identity},
            'prompt_pack_schema_version': 3,
            'scoring_key_schema_version': 3,
            'mandatory_scenario_families': sorted(E.MANDATORY),
            'confirmatory_required_scenario_families': sorted(E.CRITICAL),
            'ecological_source_pool': {
                'mode': 'combined_pool',
                'normalized_eligible_pool_sha256': self.pool_hash,
                'selection_seed_sha256': E.s256t(self.eco_seed),
                'minimum_eligible_count': 24,
                'selection_algorithm': 'protocol-v9-stratified-sha256-ranking',
            },
            'randomization_provenance': {
                'method': 'independent_assessor_after_pool_commitment',
                'pool_commitment_reference': 'https://example.invalid/commit/pool',
                'pool_commitment_sha256': self.pool_hash,
                'ecological_selection': {
                    'independent_assessor': 'assessor-A',
                    'generation_reference': 'https://example.invalid/seed/eco',
                    'generated_after_pool_commitment': True,
                    'single_generation_attested': True,
                },
                'pilot_arm_order': {
                    'independent_assessor': 'assessor-A',
                    'generation_reference': 'https://example.invalid/seed/pilot',
                    'generated_after_pool_commitment': True,
                    'single_generation_attested': True,
                },
                'confirmatory_arm_order': {
                    'independent_assessor': 'assessor-A',
                    'generation_reference': 'https://example.invalid/seed/confirm',
                    'generated_after_pool_commitment': True,
                    'single_generation_attested': True,
                },
            },
            'pilot': {
                'case_count': 12, 'stress_cases': 6, 'ecological_cases': 6,
                'prompts_sha256': self.pilot_prompt_hash,
                'scoring_key_sha256': self.pilot_key_hash,
                'arm_order_seed_sha256': E.s256t(self.pilot_seed),
            },
            'confirmatory': {
                'case_count': 12, 'stress_cases': 6, 'ecological_cases': 6,
                'prompts_sha256': self.confirmatory_prompt_hash,
                'scoring_key_sha256': self.confirmatory_key_hash,
                'arm_order_seed_sha256': E.s256t(self.confirm_seed),
            },
            'positive_reversal_quality_gate': {'minimum_each_applicable_dimension': 1},
            'ecological_correctness_non_regression': {'metric': 'median paired total correctness delta B-A', 'minimum_per_wave': 0, 'maximum_reverse_serious_error_reversals_per_wave': 0},
            'connector_cost_gate': {'acceptable_median_ratio_b_over_a': 1.5, 'high_overhead_ratio_threshold': 2.0, 'acceptable_high_overhead_case_count': 2},
            'connector_interaction_gain_rule': {'maximum_median_ratio_b_over_a_per_wave': 0.8},
            'context_volume': {'metric': 'repository_response_utf8_bytes', 'maximum_median_ratio_b_over_a_per_wave': 10.0, 'high_overhead_ratio_threshold': 20.0, 'acceptable_high_overhead_case_count': 6},
            'orientation_cost_boundary': 'task_orientation_events_only',
            'final_decision_rule': {'engineering_acceptance_correctness': {
                'minimum_confirmatory_positive_reversals': 1,
                'minimum_confirmatory_ecological_positive_reversals': 1,
                'minimum_combined_positive_reversals': 3,
                'maximum_combined_reverse_serious_reversals': 0,
                'ecological_non_regression_must_pass_both_waves': True,
                'connector_cost_gate_must_pass_both_waves': True,
                'all_primary_pairs_must_be_valid': True,
            }},
            'claim_boundary': 'engineering acceptance; not statistical significance or universal productivity proof',
        }

    def score(self, applicable, serious=False, value=2):
        out = {field: value for field in E.CORE_SCORE_FIELDS}
        out[E.OPTIONAL_SCORE_FIELD] = value if applicable else None
        total = value * (len(E.CORE_SCORE_FIELDS) + (1 if applicable else 0))
        out['total_applicable_correctness'] = total
        out['serious_routing_error'] = serious
        return out

    def tool_event(self, sequence, arm):
        if arm == E.CONTROL:
            return {
                'sequence': sequence,
                'phase': 'task_orientation',
                'tool_family': 'GitHub',
                'operation': 'fetch',
                'repository': self.prereg['repository'],
                'ref': self.ref,
                'resource': 'AGENTS.md',
                'resource_class': 'ordinary_source',
                'response_bytes': 120,
                'content_identity': None,
            }
        payload = self.surface_path.read_bytes()
        return {
            'sequence': sequence,
            'phase': 'task_orientation',
            'tool_family': 'GitHub',
            'operation': 'fetch',
            'repository': self.prereg['repository'],
            'ref': self.ref,
            'resource': 'assets/repository-intelligence/agent-context.json',
            'resource_class': 'ri_compact_surface',
            'response_bytes': len(payload),
            'content_identity': self.identity,
            'payload_byte_start': 0,
            'payload_byte_end': len(payload),
            'payload_chunk_sha256': hashlib.sha256(payload).hexdigest(),
        }

    def make_run(self, wave, case, arm, applicable):
        prompt = case['prompt']
        prompt_sha = E.s256t(prompt)
        env = E.envelope(self.prereg, wave, case['task_id'], arm, prompt_sha)
        message = E.full_message(self.prereg, wave, case['task_id'], arm, prompt, prompt_sha)
        events = [self.tool_event(1, arm)]
        return {
            'run_id': f"{case['task_id']}-{arm}",
            'arm': arm,
            'pair_order': case['planned_order'],
            'submitted_task_prompt': prompt,
            'task_prompt_sha256': prompt_sha,
            'submitted_run_envelope': env,
            'run_envelope_sha256': E.csha(env),
            'submitted_full_message': message,
            'submitted_full_message_sha256': E.s256t(message),
            'conversation_fresh': True,
            'memory_enabled': False,
            'project_context_present': False,
            'prior_repo_context_available': False,
            'previous_arm_output_exposed': False,
            'corrective_scoring_feedback_before_pair_complete': False,
            'future_wave_material_exposed': False,
            'hidden_benchmark_material_exposed': False,
            'connector_state_equal': True,
            'source_state_pre_sha': self.ref,
            'source_state_post_sha': self.ref,
            'source_state_protocol_violation': False,
            'model_family': self.prereg['model_family'],
            'thinking_configuration': self.prereg['thinking_configuration'],
            'client_environment': self.prereg['client_environment'],
            'connector': 'GitHub',
            'protocol_violations': [],
            'instrumentation_source': 'exported_transcript',
            'raw_evidence_reference': f"https://example.invalid/raw/{case['task_id']}/{arm}",
            'raw_evidence_sha256': '2' * 64,
            'event_extractor_version': 'ri-ab-events-v1',
            'tool_events': events,
            'event_log_sha256': E.csha(events),
            'total_connector_calls': 1,
            'default_branch_search_calls': 0,
            'ri_payload_bytes': 0 if arm == E.CONTROL else len(self.surface_path.read_bytes()),
            'repository_response_utf8_bytes': 120 if arm == E.CONTROL else len(self.surface_path.read_bytes()),
            'measured_input_tokens': None,
            'treatment_delivery_status': 'not-applicable' if arm == E.CONTROL else 'delivered',
            'complete_treatment_payload_verified': False if arm == E.CONTROL else True,
            'scores': self.score(applicable),
        }

    def make_record(self):
        record = {
            'protocol_version': 9,
            'study_id': self.prereg['study_id'],
            'execution_preflight': {
                'eligible_to_start_primary': True,
                'smoke_evidence_reference': self.prereg['execution_preflight']['smoke_evidence_reference'],
                'smoke_evidence_sha256': self.prereg['execution_preflight']['smoke_evidence_sha256'],
                **{field: True for field in E.PREFLIGHT},
            },
            'pilot_cases': [],
            'confirmatory_cases': [],
        }
        for key, wave in (('pilot', 'PILOT'), ('confirmatory', 'CONFIRMATORY')):
            pack = json.loads(self.paths[f'{key}_prompts'].read_text())['cases']
            scoring = {x['task_id']: x for x in json.loads(self.paths[f'{key}_key'].read_text())['cases']}
            dest = record[f'{key}_cases']
            for case in pack:
                app = scoring[case['task_id']]['companion_validation_applicable']
                runs = [self.make_run(wave, case, arm, app) for arm in case['planned_order']]
                dest.append({'task_id': case['task_id'], 'corpus_class': case['corpus_class'], 'order': case['planned_order'], 'runs': runs})
        return record

    def evaluate(self, prereg=None, record=None, evidence=None):
        return E.evaluate(prereg or self.prereg, record or self.record, evidence or self.evidence)

    def test_baseline_evaluates(self):
        out = self.evaluate()
        self.assertTrue(out['final_conclusion']['all_primary_pairs_valid'])

    def test_seed_provenance_required(self):
        p = copy.deepcopy(self.prereg)
        p['randomization_provenance']['ecological_selection']['single_generation_attested'] = False
        with self.assertRaisesRegex(ValueError, 'attest one generation'):
            E.validate_prereg(p)

    def test_wrong_seed_rejected(self):
        with self.assertRaisesRegex(ValueError, 'seed commitment mismatch'):
            E.verify_evidence(self.prereg, self.paths, {'ecological_selection': 'wrong', 'pilot_arm': self.pilot_seed, 'confirmatory_arm': self.confirm_seed})

    def test_cross_wave_prompt_overlap_rejected(self):
        confirm = json.loads(self.paths['confirmatory_prompts'].read_text())
        pilot = json.loads(self.paths['pilot_prompts'].read_text())
        confirm['cases'][0]['prompt'] = pilot['cases'][0]['prompt']
        dump(self.paths['confirmatory_prompts'], confirm)
        p = copy.deepcopy(self.prereg)
        p['confirmatory']['prompts_sha256'] = hashlib.sha256(self.paths['confirmatory_prompts'].read_bytes()).hexdigest()
        with self.assertRaisesRegex(ValueError, 'normalized prompt text overlaps'):
            E.verify_evidence(p, self.paths, {'ecological_selection': self.eco_seed, 'pilot_arm': self.pilot_seed, 'confirmatory_arm': self.confirm_seed})

    def test_full_message_mismatch_invalidates_pair(self):
        r = copy.deepcopy(self.record)
        r['pilot_cases'][0]['runs'][0]['submitted_full_message'] += '\nextra hint'
        out = self.evaluate(record=r)
        self.assertFalse(out['pilot']['all_pairs_valid'])

    def test_control_ri_contamination_invalid(self):
        r = copy.deepcopy(self.record)
        case = r['pilot_cases'][0]
        control = next(x for x in case['runs'] if x['arm'] == E.CONTROL)
        payload = self.surface_path.read_bytes()
        control['tool_events'] = [self.tool_event(1, E.TREATMENT)]
        control['event_log_sha256'] = E.csha(control['tool_events'])
        control['total_connector_calls'] = 1
        control['ri_payload_bytes'] = len(payload)
        control['repository_response_utf8_bytes'] = len(payload)
        out = self.evaluate(record=r)
        self.assertFalse(out['pilot']['all_pairs_valid'])

    def test_event_log_hash_is_authoritative(self):
        r = copy.deepcopy(self.record)
        r['pilot_cases'][0]['runs'][0]['event_log_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'event_log_sha256'):
            self.evaluate(record=r)

    def test_treatment_partial_surface_invalid(self):
        r = copy.deepcopy(self.record)
        case = r['pilot_cases'][0]
        treatment = next(x for x in case['runs'] if x['arm'] == E.TREATMENT)
        event = treatment['tool_events'][0]
        payload = self.surface_path.read_bytes()
        half = len(payload) // 2
        event['payload_byte_end'] = half
        event['response_bytes'] = half
        event['payload_chunk_sha256'] = hashlib.sha256(payload[:half]).hexdigest()
        treatment['event_log_sha256'] = E.csha(treatment['tool_events'])
        treatment['ri_payload_bytes'] = half
        treatment['repository_response_utf8_bytes'] = half
        out = self.evaluate(record=r)
        self.assertFalse(out['pilot']['all_pairs_valid'])
        reasons = out['pilot']['cases'][0]['invalid_reasons'][E.TREATMENT]
        self.assertIn('Treatment events do not prove complete aid delivery', reasons)

    def test_treatment_two_chunks_complete(self):
        r = copy.deepcopy(self.record)
        case = r['pilot_cases'][0]
        treatment = next(x for x in case['runs'] if x['arm'] == E.TREATMENT)
        payload = self.surface_path.read_bytes()
        half = len(payload) // 2
        events = []
        for idx, (start, end) in enumerate(((0, half), (half, len(payload))), 1):
            events.append({
                'sequence': idx,
                'phase': 'task_orientation',
                'tool_family': 'GitHub',
                'operation': 'fetch',
                'repository': self.prereg['repository'],
                'ref': self.ref,
                'resource': 'assets/repository-intelligence/agent-context.json',
                'resource_class': 'ri_compact_surface',
                'response_bytes': end-start,
                'content_identity': self.identity,
                'payload_byte_start': start,
                'payload_byte_end': end,
                'payload_chunk_sha256': hashlib.sha256(payload[start:end]).hexdigest(),
            })
        treatment['tool_events'] = events
        treatment['event_log_sha256'] = E.csha(events)
        treatment['total_connector_calls'] = 2
        treatment['ri_payload_bytes'] = len(payload)
        treatment['repository_response_utf8_bytes'] = len(payload)
        out = self.evaluate(record=r)
        self.assertTrue(out['pilot']['cases'][0]['valid'])

    def test_wrong_treatment_chunk_identity_rejected(self):
        r = copy.deepcopy(self.record)
        case = r['pilot_cases'][0]
        treatment = next(x for x in case['runs'] if x['arm'] == E.TREATMENT)
        treatment['tool_events'][0]['content_identity'] = {**self.identity, 'source_identity': 'wrong'}
        treatment['event_log_sha256'] = E.csha(treatment['tool_events'])
        with self.assertRaisesRegex(ValueError, 'wrong identity'):
            self.evaluate(record=r)

    def test_smoke_evidence_link_must_match(self):
        r = copy.deepcopy(self.record)
        r['execution_preflight']['smoke_evidence_sha256'] = 'f' * 64
        with self.assertRaisesRegex(ValueError, 'smoke evidence SHA-256 mismatch'):
            self.evaluate(record=r)

    def test_strong_scoring_key_required(self):
        key = json.loads(self.paths['pilot_key'].read_text())
        key['cases'][0]['serious_error_conditions'] = []
        dump(self.paths['pilot_key'], key)
        p = copy.deepcopy(self.prereg)
        p['pilot']['scoring_key_sha256'] = hashlib.sha256(self.paths['pilot_key'].read_bytes()).hexdigest()
        with self.assertRaisesRegex(ValueError, 'serious_error_conditions must be non-empty'):
            E.verify_evidence(p, self.paths, {'ecological_selection': self.eco_seed, 'pilot_arm': self.pilot_seed, 'confirmatory_arm': self.confirm_seed})

    def test_engineering_acceptance_needs_confirmatory_ecological_support(self):
        r = copy.deepcopy(self.record)
        for case in r['pilot_cases'][:2]:
            control = next(x for x in case['runs'] if x['arm'] == E.CONTROL)
            control['scores']['serious_routing_error'] = True
        eco_case = next(c for c in r['confirmatory_cases'] if c['corpus_class'] == 'ecological')
        control = next(x for x in eco_case['runs'] if x['arm'] == E.CONTROL)
        control['scores']['serious_routing_error'] = True
        out = self.evaluate(record=r)
        self.assertTrue(out['final_conclusion']['engineering_acceptance_correctness'])

    def test_reverse_serious_is_regression(self):
        r = copy.deepcopy(self.record)
        case = r['confirmatory_cases'][0]
        treatment = next(x for x in case['runs'] if x['arm'] == E.TREATMENT)
        treatment['scores']['serious_routing_error'] = True
        out = self.evaluate(record=r)
        self.assertEqual(out['final_conclusion']['final_status'], 'REGRESSION')


if __name__ == '__main__':
    unittest.main()
