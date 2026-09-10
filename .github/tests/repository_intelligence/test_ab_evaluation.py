#!/usr/bin/env python3
import copy, hashlib, importlib.util, json, subprocess, sys, tempfile, unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[2] / 'scripts' / 'score_repository_intelligence_ab.py'
spec = importlib.util.spec_from_file_location('ri_ab', MODULE_PATH)
E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)

def dump(path, obj):
    path.write_text(json.dumps(obj, sort_keys=True, ensure_ascii=False)+'\n', encoding='utf-8')
    return hashlib.sha256(path.read_bytes()).hexdigest()

def score(app, serious=False, value=2):
    out={k:value for k in E.CORE_SCORE_FIELDS}; out[E.OPTIONAL_SCORE_FIELD]=value if app else None
    out['total_applicable_correctness']=value*(len(E.CORE_SCORE_FIELDS)+(1 if app else 0)); out['serious_routing_error']=serious
    return out

class T(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup); self.root=Path(self.tmp.name)
        self.ref='a'*40; self.eco='eco-v10'; self.pseed='p-v10'; self.cseed='c-v10'
        self.surface=self.root/'surface.json'; dump(self.surface, {'source_identity':{'digest':'source-v10'},'data':['x']}); payload=self.surface.read_bytes()
        self.identity={'mode':E.TREATMENT_MODE,'identifier':E.TREATMENT_IDENTIFIER,'git_blob_sha':E.git_blob_sha(payload),'content_sha256':hashlib.sha256(payload).hexdigest(),'source_identity':'source-v10'}
        frame=[]; pool=[]
        for i in range(26):
            ok=i<24; sid=f'E{i:02d}'; sha=hashlib.sha256(sid.encode()).hexdigest(); ref=f'https://example.invalid/{sid}'
            frame.append({'source_event_id':sid,'source_event_reference':ref,'source_event_sha256':sha,'eligible':ok,'inclusion_rule_ids':['maintainer-task'] if ok else [],'exclusion_rule_id':None if ok else 'not-self-contained'})
            if ok:
                anchor='exact-owner' if i<2 else 'legitimate-new-artifact' if i<4 else 'none'
                scenarios=['exact-owner-recovery'] if i<2 else ['legitimate-new-artifact'] if i<4 else ['near-synonym-source-review']
                pool.append({'ecological_source_id':sid,'source_event_reference':ref,'source_event_sha256':sha,'normalization_reference':ref+'#norm','normalized_from_source_only':True,'task_family_id':'F-'+sid,'normalized_prompt':'Ecological '+sid,'anchor_type':anchor,'scenario_families':scenarios})
        self.frame=self.root/'frame.json'; self.frame_hash=dump(self.frame,{'schema_version':1,'items':frame})
        self.pool=self.root/'pool.json'; self.pool_hash=dump(self.pool,{'schema_version':2,'items':pool}); self.selected=E.eco_select(pool,self.eco)
        self.paths={'ecological_frame':self.frame,'ecological_pool':self.pool}; self._packs()
        self.p=self._prereg(); self.record=self._record(); self.ev=E.verify_evidence(self.p,self.paths,{'ecological_selection':self.eco,'pilot_arm':self.pseed,'confirmatory_arm':self.cseed}); self.ev['treatment_surface']=E.validate_treatment_surface(self.surface,self.p)
        self.blind=self.root/'blind.json'; self.bundle=self._blind(); self.record['blind_scoring']={'scoring_bundle_sha256':dump(self.blind,self.bundle),'scoring_evidence_reference':'https://example.invalid/blind'}; self.scores=E.validate_blind_scores(self.blind,self.record,self.p,self.ev)
    def _packs(self):
        p_stress=[['canonical-term-synonym-pressure','impact-validation-routing'],['overlapping-artifact-refinement','research-authority-separation'],['accepted-proposed-relation-change','branch-behind-target'],['producer-schema-self-change','candidate-data-boundary'],['shared-structural-hub','stale-materialization-fallback'],['ukrainian-or-paraphrased-routing']]
        c_stress=[['accepted-proposed-relation-change'],['branch-behind-target'],['producer-schema-self-change'],['candidate-data-boundary'],['shared-structural-hub'],['stale-materialization-fallback']]
        for key,wave,prefix,seed,stress in [('pilot','PILOT','P',self.pseed,p_stress),('confirmatory','CONFIRMATORY','C',self.cseed,c_stress)]:
            cases=[]; keys=[]
            for i in range(12):
                tid=f'{prefix}{i+1:02d}'
                if i<6: prompt=f'{wave} stress {i}'; family=f'{wave}-F-{i}'; source=None; scenarios=stress[i]
                else:
                    x=self.selected[key][i-6]; prompt=x['normalized_prompt']; family=x['task_family_id']; source=x['ecological_source_id']; scenarios=x['scenario_families']
                cases.append({'task_id':tid,'task_family_id':family,'corpus_class':'stress' if i<6 else 'ecological','ecological_source_id':source,'scenario_families':scenarios,'planned_order':E.arm_order(seed,tid),'prompt':prompt})
                app=i%2==0; dims={k:{'0':'bad','1':'partial','2':'good'} for k in E.CORE_SCORE_FIELDS};
                if app: dims[E.OPTIONAL_SCORE_FIELD]={'0':'bad','1':'partial','2':'good'}
                keys.append({'task_id':tid,'expected_owner_or_route':['owner'],'acceptable_alternatives':[],'required_authoritative_evidence':['source'],'serious_error_conditions':['wrong owner'],'decision_acceptance_conditions':['bounded'],'companion_validation_applicable':app,'dimension_anchors':dims})
            pp=self.root/(key+'-prompts.json'); kk=self.root/(key+'-key.json'); ph=dump(pp,{'schema_version':3,'wave':wave,'cases':cases}); kh=dump(kk,{'schema_version':3,'wave':wave,'cases':keys}); self.paths[key+'_prompts']=pp; self.paths[key+'_key']=kk; setattr(self,key+'_ph',ph); setattr(self,key+'_kh',kh)
    def _prereg(self):
        return {'protocol_version':10,'study_id':'S','repository':'UncertaintyArchitectureGroup/uncertainty-architecture','repository_ref':self.ref,'default_branch':'main','execution_policy':'always_run_pilot_and_confirmatory','source_state_lock':{'mode':'stable_default_branch_window','expected_default_branch_tip_sha':self.ref,'repository_mutations_prohibited_during_primary':True,'pre_run_tip_check_required':True,'post_run_tip_check_required':True,'ordinary_default_branch_search_allowed':True},'execution_preflight':{'smoke_evidence_reference':'smoke','smoke_evidence_sha256':'1'*64,**{x:True for x in E.PREFLIGHT}},'isolation_requirements':{'conversation_fresh':True,'memory_enabled':False,'project_context_present':False,'prior_repo_context_available':False,'previous_arm_output_exposed':False,'corrective_scoring_feedback_before_pair_complete':False,'future_wave_material_exposed':False,'hidden_benchmark_material_exposed':False},'model_family':'GPT-X','thinking_configuration':'High','client_environment':'clean','connector':'GitHub','treatment_delivery':{'mode':E.TREATMENT_MODE,'aid_identity':self.identity},'prompt_pack_schema_version':3,'scoring_key_schema_version':3,'blind_scoring_schema_version':1,'mandatory_scenario_families':sorted(E.MANDATORY),'confirmatory_required_scenario_families':sorted(E.CRITICAL),'ecological_sampling_frame':{'manifest_sha256':self.frame_hash,'commitment_reference':'frame-ref','source_window':'window','cutoff':'2026-09-09','inclusion_rule_ids':['maintainer-task'],'exclusion_rule_ids':['not-self-contained']},'ecological_source_pool':{'mode':'complete_eligible_frame','normalized_eligible_pool_sha256':self.pool_hash,'selection_seed_sha256':E.s256t(self.eco),'minimum_eligible_count':24,'selection_algorithm':'protocol-v10-stratified-sha256-ranking'},'randomization_provenance':{'method':'independent_assessor_after_pool_commitment','pool_commitment_reference':'pool-ref','pool_commitment_sha256':self.pool_hash,**{x:{'independent_assessor':'A','generation_reference':x,'generated_after_pool_commitment':True,'single_generation_attested':True} for x in ('ecological_selection','pilot_arm_order','confirmatory_arm_order')}},'pilot':{'case_count':12,'stress_cases':6,'ecological_cases':6,'prompts_sha256':self.pilot_ph,'scoring_key_sha256':self.pilot_kh,'arm_order_seed_sha256':E.s256t(self.pseed)},'confirmatory':{'case_count':12,'stress_cases':6,'ecological_cases':6,'prompts_sha256':self.confirmatory_ph,'scoring_key_sha256':self.confirmatory_kh,'arm_order_seed_sha256':E.s256t(self.cseed)},'positive_reversal_quality_gate':{'minimum_each_applicable_dimension':1},'ecological_correctness_non_regression':{'metric':'median paired total correctness delta B-A','minimum_per_wave':0,'maximum_reverse_serious_error_reversals_per_wave':0},'connector_cost_gate':{'acceptable_median_ratio_b_over_a':1.5,'high_overhead_ratio_threshold':2.0,'acceptable_high_overhead_case_count':2},'connector_interaction_gain_rule':{'maximum_median_ratio_b_over_a_per_wave':0.8},'context_volume':{'metric':'repository_response_utf8_bytes','maximum_median_ratio_b_over_a_per_wave':1.0,'high_overhead_ratio_threshold':2.0,'acceptable_high_overhead_case_count':2},'orientation_cost_boundary':'task_orientation_events_only','final_decision_rule':{'engineering_acceptance_correctness':{'minimum_confirmatory_positive_reversals':1,'minimum_confirmatory_ecological_positive_reversals':1,'minimum_combined_positive_reversals':3,'maximum_combined_reverse_serious_reversals':0,'ecological_non_regression_must_pass_both_waves':True,'connector_cost_gate_must_pass_both_waves':True,'all_primary_pairs_must_be_valid':True}},'claim_boundary':'engineering acceptance; not statistical significance or universal productivity proof'}
    def _events(self,arm):
        out=[{'sequence':1,'phase':'study_infrastructure','tool_family':'GitHub','operation':'branch_tip_pre','repository':self.p['repository'],'ref':'main','resource':'main','resource_class':'other','response_bytes':40,'observed_ref_sha':self.ref}]
        if arm==E.CONTROL: out.append({'sequence':2,'phase':'task_orientation','tool_family':'GitHub','operation':'fetch','repository':self.p['repository'],'ref':self.ref,'resource':'AGENTS.md','resource_class':'ordinary_source','response_bytes':120,'content_identity':None})
        else:
            b=self.surface.read_bytes(); out.append({'sequence':2,'phase':'task_orientation','tool_family':'GitHub','operation':'fetch','repository':self.p['repository'],'ref':self.ref,'resource':E.TREATMENT_IDENTIFIER,'resource_class':'ri_compact_surface','response_bytes':len(b),'content_identity':self.identity,'payload_byte_start':0,'payload_byte_end':len(b),'payload_chunk_sha256':hashlib.sha256(b).hexdigest()})
        out.append({'sequence':3,'phase':'study_infrastructure','tool_family':'GitHub','operation':'branch_tip_post','repository':self.p['repository'],'ref':'main','resource':'main','resource_class':'other','response_bytes':40,'observed_ref_sha':self.ref}); return out
    def _run(self,wave,c,arm):
        ph=E.s256t(c['prompt']); env=E.envelope(self.p,wave,c['task_id'],arm,ph); msg=E.full_message(self.p,wave,c['task_id'],arm,c['prompt'],ph); ev=self._events(arm); task=[x for x in ev if x['phase']=='task_orientation']; resp='response '+c['task_id']+' '+arm
        return {'run_id':c['task_id']+arm,'arm':arm,'pair_order':c['planned_order'],'submitted_task_prompt':c['prompt'],'task_prompt_sha256':ph,'submitted_run_envelope':env,'run_envelope_sha256':E.csha(env),'submitted_full_message':msg,'submitted_full_message_sha256':E.s256t(msg),'model_response':resp,'model_response_sha256':E.s256t(resp),'blind_response_id':hashlib.sha256(resp.encode()).hexdigest()[:24],'conversation_fresh':True,'memory_enabled':False,'project_context_present':False,'prior_repo_context_available':False,'previous_arm_output_exposed':False,'corrective_scoring_feedback_before_pair_complete':False,'future_wave_material_exposed':False,'hidden_benchmark_material_exposed':False,'connector_state_equal':True,'source_state_pre_sha':self.ref,'source_state_post_sha':self.ref,'source_state_protocol_violation':False,'model_family':'GPT-X','thinking_configuration':'High','client_environment':'clean','connector':'GitHub','protocol_violations':[],'instrumentation_source':'exported_transcript','raw_evidence_reference':'raw','raw_evidence_sha256':'2'*64,'event_extractor_version':'v1','tool_events':ev,'event_log_sha256':E.csha(ev),'total_connector_calls':len(task),'default_branch_search_calls':0,'ri_payload_bytes':0 if arm==E.CONTROL else len(self.surface.read_bytes()),'repository_response_utf8_bytes':sum(x['response_bytes'] for x in task),'measured_input_tokens':None,'treatment_delivery_status':'not-applicable' if arm==E.CONTROL else 'delivered','complete_treatment_payload_verified':arm==E.TREATMENT}
    def _record(self):
        r={'protocol_version':10,'study_id':'S','execution_preflight':{'eligible_to_start_primary':True,'smoke_evidence_reference':'smoke','smoke_evidence_sha256':'1'*64,**{x:True for x in E.PREFLIGHT}},'pilot_cases':[],'confirmatory_cases':[]}
        for key,wave in [('pilot','PILOT'),('confirmatory','CONFIRMATORY')]:
            for c in json.loads(self.paths[key+'_prompts'].read_text())['cases']: r[key+'_cases'].append({'task_id':c['task_id'],'corpus_class':c['corpus_class'],'order':c['planned_order'],'runs':[self._run(wave,c,a) for a in c['planned_order']]})
        return r
    def _blind(self):
        km={x['task_id']:x for k in ('pilot','confirmatory') for x in json.loads(self.paths[k+'_key'].read_text())['cases']}; entries=[]
        for ck in ('pilot_cases','confirmatory_cases'):
            for c in self.record[ck]:
                for r in c['runs']: entries.append({'blind_response_id':r['blind_response_id'],'task_id':c['task_id'],'model_response_sha256':r['model_response_sha256'],'scores':score(km[c['task_id']]['companion_validation_applicable'])})
        return {'schema_version':1,'study_id':'S','scorer_identity':'blind','scoring_evidence_reference':'evidence','scoring_completed_before_arm_reveal':True,'arm_labels_present':False,'pilot_scoring_key_sha256':self.p['pilot']['scoring_key_sha256'],'confirmatory_scoring_key_sha256':self.p['confirmatory']['scoring_key_sha256'],'responses':entries}
    def eval(self,r=None,s=None): return E.evaluate(self.p,r or self.record,self.ev,s or self.scores)
    def test_baseline(self): self.assertTrue(self.eval()['final_conclusion']['all_primary_pairs_valid'])
    def test_frame_pool_complete(self):
        pool=json.loads(self.pool.read_text()); pool['items'].pop(); dump(self.pool,pool); p=copy.deepcopy(self.p); p['ecological_source_pool']['normalized_eligible_pool_sha256']=hashlib.sha256(self.pool.read_bytes()).hexdigest()
        with self.assertRaisesRegex(ValueError,'must contain every eligible'): E.verify_evidence(p,self.paths,{'ecological_selection':self.eco,'pilot_arm':self.pseed,'confirmatory_arm':self.cseed})
    def test_floor_cannot_weaken(self):
        p=copy.deepcopy(self.p); p['final_decision_rule']['engineering_acceptance_correctness']['minimum_combined_positive_reversals']=0
        with self.assertRaisesRegex(ValueError,'at least three'): E.validate_prereg(p)
    def test_connector_only(self):
        p=copy.deepcopy(self.p); p['treatment_delivery']['mode']='local_cli'
        with self.assertRaisesRegex(ValueError,'connector_compact_surface only'): E.validate_prereg(p)
    def test_source_lock_events_required(self):
        r=copy.deepcopy(self.record); run=r['pilot_cases'][0]['runs'][0]; run['tool_events']=run['tool_events'][:-1]; run['event_log_sha256']=E.csha(run['tool_events'])
        with self.assertRaisesRegex(ValueError,'branch_tip_pre and branch_tip_post'): self.eval(r)
    def test_blind_arm_label_rejected(self):
        b=copy.deepcopy(self.bundle); b['responses'][0]['arm']=E.CONTROL; p=self.root/'bad.json'; h=dump(p,b); r=copy.deepcopy(self.record); r['blind_scoring']['scoring_bundle_sha256']=h
        with self.assertRaisesRegex(ValueError,'blind scoring response fields'): E.validate_blind_scores(p,r,self.p,self.ev)
    def test_inline_scores_invalid(self):
        r=copy.deepcopy(self.record); r['pilot_cases'][0]['runs'][0]['scores']={'owner_routing':2}; self.assertFalse(self.eval(r)['pilot']['all_pairs_valid'])
    def test_query_aid_invalid(self):
        r=copy.deepcopy(self.record); tr=next(x for x in r['pilot_cases'][0]['runs'] if x['arm']==E.TREATMENT); q={'sequence':3,'phase':'task_orientation','tool_family':'GitHub','operation':'query','repository':self.p['repository'],'ref':self.ref,'resource':'find-owner','resource_class':'ri_query','response_bytes':5,'content_identity':None}; tr['tool_events'].insert(2,q)
        for i,e in enumerate(tr['tool_events'],1): e['sequence']=i
        tr['event_log_sha256']=E.csha(tr['tool_events']); tr['total_connector_calls']=2; tr['ri_payload_bytes']+=5; tr['repository_response_utf8_bytes']+=5; self.assertFalse(self.eval(r)['pilot']['all_pairs_valid'])
    def test_partial_surface_invalid(self):
        r=copy.deepcopy(self.record); tr=next(x for x in r['pilot_cases'][0]['runs'] if x['arm']==E.TREATMENT); e=tr['tool_events'][1]; b=self.surface.read_bytes(); n=len(b)//2; e['payload_byte_end']=n; e['response_bytes']=n; e['payload_chunk_sha256']=hashlib.sha256(b[:n]).hexdigest(); tr['event_log_sha256']=E.csha(tr['tool_events']); tr['ri_payload_bytes']=n; tr['repository_response_utf8_bytes']=n; self.assertFalse(self.eval(r)['pilot']['all_pairs_valid'])
    def test_full_message_invalid(self):
        r=copy.deepcopy(self.record); r['pilot_cases'][0]['runs'][0]['submitted_full_message']+=' extra'; self.assertFalse(self.eval(r)['pilot']['all_pairs_valid'])
    def test_cross_wave_overlap(self):
        c=json.loads(self.paths['confirmatory_prompts'].read_text()); ppack=json.loads(self.paths['pilot_prompts'].read_text()); c['cases'][0]['prompt']=ppack['cases'][0]['prompt']; dump(self.paths['confirmatory_prompts'],c); p=copy.deepcopy(self.p); p['confirmatory']['prompts_sha256']=hashlib.sha256(self.paths['confirmatory_prompts'].read_bytes()).hexdigest()
        with self.assertRaisesRegex(ValueError,'normalized prompt text overlaps'): E.verify_evidence(p,self.paths,{'ecological_selection':self.eco,'pilot_arm':self.pseed,'confirmatory_arm':self.cseed})

    def _cli(self, record):
        prereg = self.root / 'prereg.json'
        runs = self.root / 'runs.json'
        output = self.root / 'report.json'
        dump(prereg, self.p)
        dump(runs, record)
        if output.exists():
            output.unlink()
        args = [
            sys.executable, str(MODULE_PATH),
            '--preregistration', str(prereg), '--run-record', str(runs),
            '--ecological-frame', str(self.frame), '--ecological-pool', str(self.pool),
            '--ecological-selection-seed', self.eco,
            '--pilot-arm-seed', self.pseed, '--confirmatory-arm-seed', self.cseed,
            '--blind-scores', str(self.blind), '--treatment-surface', str(self.surface),
            '--output', str(output),
        ]
        for key in ('pilot_prompts', 'pilot_key', 'confirmatory_prompts', 'confirmatory_key'):
            args.extend(['--' + key.replace('_', '-'), str(self.paths[key])])
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        return result, json.loads(output.read_text()) if output.exists() else None

    def test_each_read_requires_study_source_evidence(self):
        for arm in (E.CONTROL, E.TREATMENT):
            for ref in ('b' * 40, 'other-branch', 'main', None, ''):
                with self.subTest(arm=arm, ref=ref):
                    record = copy.deepcopy(self.record)
                    run = next(run for run in record['pilot_cases'][0]['runs'] if run['arm'] == arm)
                    run['tool_events'][1]['ref'] = ref
                    run['event_log_sha256'] = E.csha(run['tool_events'])
                    with self.assertRaisesRegex(ValueError, 'source ref'):
                        self.eval(record)

    def test_resolved_default_branch_reads_preserve_supported_fallback(self):
        for arm in (E.CONTROL, E.TREATMENT):
            for ref in ('main', None):
                with self.subTest(arm=arm, ref=ref):
                    record = copy.deepcopy(self.record)
                    run = next(run for run in record['pilot_cases'][0]['runs'] if run['arm'] == arm)
                    event = run['tool_events'][1]
                    event['ref'] = ref
                    event['observed_ref_sha'] = self.ref
                    run['event_log_sha256'] = E.csha(run['tool_events'])
                    self.assertTrue(self.eval(record)['final_conclusion']['all_primary_pairs_valid'])

    def test_default_branch_search_remains_valid_under_source_lock(self):
        for operation in ('search', 'code_search'):
            for ref in ('main', None, self.ref):
                with self.subTest(operation=operation, ref=ref):
                    record = copy.deepcopy(self.record)
                    run = next(run for run in record['pilot_cases'][0]['runs'] if run['arm'] == E.CONTROL)
                    event = run['tool_events'][1]
                    event.update(operation=operation, ref=ref)
                    run['default_branch_search_calls'] = 1
                    run['event_log_sha256'] = E.csha(run['tool_events'])
                    self.assertTrue(self.eval(record)['final_conclusion']['all_primary_pairs_valid'])

    def test_search_and_resolved_reads_reject_contradictory_source_evidence(self):
        for operation, ref, observed in (
            ('search', 'b' * 40, None),
            ('code_search', 'other-branch', self.ref),
            ('search', None, 'b' * 40),
            ('fetch', self.ref, 'b' * 40),
            ('fetch', 'main', 'b' * 40),
            ('fetch', 'other-branch', self.ref),
        ):
            with self.subTest(operation=operation, ref=ref, observed=observed):
                record = copy.deepcopy(self.record)
                run = next(run for run in record['pilot_cases'][0]['runs'] if run['arm'] == E.CONTROL)
                run['tool_events'][1].update(operation=operation, ref=ref, observed_ref_sha=observed)
                run['event_log_sha256'] = E.csha(run['tool_events'])
                with self.assertRaisesRegex(ValueError, 'source ref'):
                    self.eval(record)

    def test_infrastructure_label_does_not_exempt_source_reads(self):
        record = copy.deepcopy(self.record)
        run = record['pilot_cases'][0]['runs'][0]
        event = copy.deepcopy(run['tool_events'][1])
        event.update(phase='study_infrastructure', ref='b' * 40)
        run['tool_events'].insert(2, event)
        for index, event in enumerate(run['tool_events'], 1):
            event['sequence'] = index
        run['event_log_sha256'] = E.csha(run['tool_events'])
        with self.assertRaisesRegex(ValueError, 'source ref'):
            self.eval(record)

    def test_branch_tip_checks_identify_preregistered_default_branch(self):
        for index in (0, 2):
            with self.subTest(index=index):
                record = copy.deepcopy(self.record)
                run = record['pilot_cases'][0]['runs'][0]
                run['tool_events'][index].update(ref='other-branch', resource='other-branch')
                run['event_log_sha256'] = E.csha(run['tool_events'])
                with self.assertRaisesRegex(ValueError, 'default branch'):
                    self.eval(record)

    def test_blind_bundle_rejects_extra_fields_at_every_level(self):
        for level in ('bundle', 'response', 'scores'):
            for field, value in (
                ('tool_events', self.record['pilot_cases'][0]['runs'][0]['tool_events']),
                ('treatment_delivery_status', 'delivered'),
                ('metadata', {'arm': E.CONTROL}),
            ):
                with self.subTest(level=level, field=field):
                    bundle = copy.deepcopy(self.bundle)
                    target = bundle if level == 'bundle' else bundle['responses'][0]
                    if level == 'scores':
                        target = target['scores']
                    target[field] = value
                    record = copy.deepcopy(self.record)
                    record['blind_scoring']['scoring_bundle_sha256'] = dump(self.blind, bundle)
                    with self.assertRaisesRegex(ValueError, 'fields'):
                        E.validate_blind_scores(self.blind, record, self.p, self.ev)

    def test_blind_bundle_requires_exact_fields_at_every_level(self):
        for level, field in (('bundle', 'scorer_identity'), ('response', 'task_id'), ('scores', 'companion_validation')):
            with self.subTest(level=level):
                bundle = copy.deepcopy(self.bundle)
                target = bundle if level == 'bundle' else bundle['responses'][0]
                if level == 'scores':
                    target = target['scores']
                del target[field]
                record = copy.deepcopy(self.record)
                record['blind_scoring']['scoring_bundle_sha256'] = dump(self.blind, bundle)
                with self.assertRaisesRegex(ValueError, 'fields'):
                    E.validate_blind_scores(self.blind, record, self.p, self.ev)

    def test_cli_rejects_wrong_read_sha_and_blind_metadata(self):
        record = copy.deepcopy(self.record)
        run = record['pilot_cases'][0]['runs'][0]
        run['tool_events'][1]['ref'] = 'b' * 40
        run['event_log_sha256'] = E.csha(run['tool_events'])
        result, report = self._cli(record)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn('source ref', result.stderr)
        self.assertIsNone(report)

        bundle = copy.deepcopy(self.bundle)
        bundle['responses'][0]['tool_events'] = run['tool_events']
        record = copy.deepcopy(self.record)
        record['blind_scoring']['scoring_bundle_sha256'] = dump(self.blind, bundle)
        result, report = self._cli(record)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn('fields', result.stderr)
        self.assertIsNone(report)

    def test_cli_invalid_ecological_pairs_write_inconclusive_report(self):
        for metric in ('repository_response_utf8_bytes', 'input_tokens', 'unavailable'):
            for waves, all_cases in ((('pilot',), False), (('confirmatory',), False), (('pilot', 'confirmatory'), True)):
                with self.subTest(metric=metric, waves=waves, all_cases=all_cases):
                    self.p['context_volume']['metric'] = metric
                    record = copy.deepcopy(self.record)
                    for wave in ('pilot', 'confirmatory'):
                        for case in record[wave + '_cases']:
                            for run in case['runs']:
                                run['measured_input_tokens'] = 100
                                if wave in waves and (all_cases or case['corpus_class'] == 'ecological'):
                                    run['conversation_fresh'] = False
                    result, report = self._cli(record)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIsNotNone(report)
                    self.assertEqual(report['final_conclusion']['final_status'], 'INCONCLUSIVE')
                    self.assertFalse(report['final_conclusion']['all_primary_pairs_valid'])
                    for wave in waves:
                        self.assertIsNone(report[wave]['ecological_median_context_volume_ratio'])
                        self.assertIsNone(report[wave]['ecological_median_connector_ratio'])
                        self.assertFalse(report[wave]['context_volume_gate_passed'])
                        self.assertFalse(report[wave]['orientation_efficiency_passed'])
                        invalid = [case for case in report[wave]['cases'] if not case['valid']]
                        self.assertEqual(len(invalid), 12 if all_cases else 6)
                        self.assertTrue(all('conversation not fresh' in reasons for case in invalid for reasons in case['invalid_reasons'].values()))

    def test_partial_ecological_sample_cannot_pass_context_volume_gate(self):
        record = copy.deepcopy(self.record)
        case = next(case for case in record['pilot_cases'] if case['corpus_class'] == 'ecological')
        case['runs'][0]['conversation_fresh'] = False
        report = self.eval(record)
        self.assertEqual(report['final_conclusion']['final_status'], 'INCONCLUSIVE')
        self.assertIsNotNone(report['pilot']['ecological_median_context_volume_ratio'])
        self.assertFalse(report['pilot']['context_volume_gate_passed'])

    def test_cli_complete_sample_preserves_context_volume_gate(self):
        result, report = self._cli(self.record)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(report['final_conclusion']['final_status'], 'NO INCREMENTAL VALUE SHOWN')
        for wave in ('pilot', 'confirmatory'):
            self.assertTrue(report[wave]['all_pairs_valid'])
            self.assertTrue(report[wave]['context_volume_gate_passed'])

    @staticmethod
    def _refresh_events(run):
        # Keep submitted summaries consistent so a bad event cannot be rejected
        # merely because the regression forgot to update its hash or costs.
        for index, event in enumerate(run['tool_events'], 1):
            event['sequence'] = index
        task = [event for event in run['tool_events'] if event['phase'] == 'task_orientation']
        run['event_log_sha256'] = E.csha(run['tool_events'])
        run['total_connector_calls'] = len(task)
        run['default_branch_search_calls'] = sum(event['operation'] in {'search', 'code_search'} for event in task)
        run['repository_response_utf8_bytes'] = sum(event['response_bytes'] for event in task)
        run['ri_payload_bytes'] = sum(event['response_bytes'] for event in task if event['resource_class'] in E.RI_CLASSES)

    def _correctness_record(self):
        record = copy.deepcopy(self.record)
        bundle = copy.deepcopy(self.bundle)
        positive_ids = set()
        for wave, index in (('pilot', 0), ('confirmatory', 0), ('confirmatory', 6)):
            run = next(run for run in record[wave + '_cases'][index]['runs'] if run['arm'] == E.CONTROL)
            positive_ids.add(run['blind_response_id'])
        for entry in bundle['responses']:
            if entry['blind_response_id'] in positive_ids:
                entry['scores'] = score(entry['scores'][E.OPTIONAL_SCORE_FIELD] is not None, serious=True, value=1)
        record['blind_scoring']['scoring_bundle_sha256'] = dump(self.blind, bundle)
        return record

    def _efficiency_record(self):
        self.p['context_volume']['metric'] = 'input_tokens'
        record = copy.deepcopy(self.record)
        for wave in ('pilot', 'confirmatory'):
            for case in record[wave + '_cases']:
                for run in case['runs']:
                    run['measured_input_tokens'] = 100
                    if run['arm'] == E.CONTROL:
                        extra = copy.deepcopy(run['tool_events'][1])
                        extra['resource'] = 'SPECIFICATION.md'
                        run['tool_events'].insert(2, extra)
                        self._refresh_events(run)
        return record

    def test_cli_correctness_acceptance_remains_available(self):
        record = self._correctness_record()
        case = record['pilot_cases'][0]
        control = next(run for run in case['runs'] if run['arm'] == E.CONTROL)
        treatment = next(run for run in case['runs'] if run['arm'] == E.TREATMENT)
        treatment['tool_events'].insert(2, copy.deepcopy(control['tool_events'][1]))
        self._refresh_events(treatment)
        result, report = self._cli(record)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(report['final_conclusion']['final_status'], 'ENGINEERING ACCEPTANCE — CORRECTNESS')

    def test_cli_compact_resource_and_identity_cannot_be_classed_as_ordinary(self):
        baseline = self._correctness_record()
        for arm in (E.CONTROL, E.TREATMENT):
            for resource, identity, byte_fields in ((E.TREATMENT_IDENTIFIER, None, False), ('AGENTS.md', self.identity, False), ('AGENTS.md', None, True)):
                for resource_class in ('ordinary_source', 'other'):
                    with self.subTest(arm=arm, resource=resource, resource_class=resource_class, byte_fields=byte_fields):
                        record = copy.deepcopy(baseline)
                        run = next(run for run in record['pilot_cases'][0]['runs'] if run['arm'] == arm)
                        event = copy.deepcopy(self._events(E.TREATMENT)[1])
                        event.update(resource=resource, content_identity=identity, resource_class=resource_class)
                        if not byte_fields:
                            for field in ('payload_byte_start', 'payload_byte_end', 'payload_chunk_sha256'):
                                del event[field]
                        run['tool_events'].insert(2, event)
                        self._refresh_events(run)
                        result, report = self._cli(record)
                        self.assertEqual(result.returncode, 2, result.stderr)
                        self.assertIn('resource_class', result.stderr)
                        self.assertIsNone(report)

    def test_cli_repository_access_cannot_be_hidden_as_infrastructure(self):
        baseline = self._correctness_record()
        for arm in (E.CONTROL, E.TREATMENT):
            for resource_class in ('ordinary_source', 'ri_compact_surface', 'ri_query', 'ri_full_graph', 'repository_control_map'):
                with self.subTest(arm=arm, resource_class=resource_class):
                    record = copy.deepcopy(baseline)
                    run = next(run for run in record['pilot_cases'][0]['runs'] if run['arm'] == arm)
                    event = copy.deepcopy(self._events(E.TREATMENT if resource_class == 'ri_compact_surface' else E.CONTROL)[1])
                    event.update(phase='study_infrastructure', resource_class=resource_class)
                    run['tool_events'].insert(2, event)
                    self._refresh_events(run)
                    result, report = self._cli(record)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(report['final_conclusion']['final_status'], 'INCONCLUSIVE')
                    reasons = report['pilot']['cases'][0]['invalid_reasons'][arm]
                    self.assertIn('repository access recorded outside task orientation', reasons)

    def test_cli_noncanonical_fetch_paths_cannot_hide_compact_access(self):
        baseline = self._correctness_record()
        for resource in ('./' + E.TREATMENT_IDENTIFIER, 'assets/../' + E.TREATMENT_IDENTIFIER, '/' + E.TREATMENT_IDENTIFIER, E.TREATMENT_IDENTIFIER.replace('/', '\\'), 'https://github.com/' + self.p['repository'] + '/blob/' + self.ref + '/' + E.TREATMENT_IDENTIFIER):
            with self.subTest(resource=resource):
                record = copy.deepcopy(baseline)
                run = next(run for run in record['pilot_cases'][0]['runs'] if run['arm'] == E.CONTROL)
                run['tool_events'][1]['resource'] = resource
                self._refresh_events(run)
                result, report = self._cli(record)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIn('canonical repository-relative path', result.stderr)
                self.assertIsNone(report)

    def test_cli_actual_event_transport_and_operation_enforce_connector_route(self):
        baseline = self._correctness_record()
        for arm in (E.CONTROL, E.TREATMENT):
            for family, operation in (('local_cli', 'read_file'), ('local_cli', 'fetch'), ('dedicated_adapter', 'fetch'), ('GitHub', 'read_file'), ('GitHub', 'query')):
                with self.subTest(arm=arm, family=family, operation=operation):
                    record = copy.deepcopy(baseline)
                    run = next(run for run in record['pilot_cases'][0]['runs'] if run['arm'] == arm)
                    run['tool_events'][1].update(tool_family=family, operation=operation)
                    self._refresh_events(run)
                    result, report = self._cli(record)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(report['final_conclusion']['final_status'], 'INCONCLUSIVE')
                    self.assertIn('tool events use an unsupported connector route', report['pilot']['cases'][0]['invalid_reasons'][arm])

    def test_preregistered_connector_cannot_enable_local_primary(self):
        for connector in ('local_cli', 'dedicated_adapter', 'unregistered'):
            with self.subTest(connector=connector):
                prereg = copy.deepcopy(self.p)
                prereg['connector'] = connector
                with self.assertRaisesRegex(ValueError, 'GitHub connector'):
                    E.validate_prereg(prereg)

    def test_cli_branch_tip_evidence_requires_registered_connector(self):
        baseline = self._correctness_record()
        for arm in (E.CONTROL, E.TREATMENT):
            for index in (0, 2):
                with self.subTest(arm=arm, index=index):
                    record = copy.deepcopy(baseline)
                    run = next(run for run in record['pilot_cases'][0]['runs'] if run['arm'] == arm)
                    run['tool_events'][index]['tool_family'] = 'local_cli'
                    self._refresh_events(run)
                    result, report = self._cli(record)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(report['final_conclusion']['final_status'], 'INCONCLUSIVE')
                    self.assertIn('tool events use an unsupported connector route', report['pilot']['cases'][0]['invalid_reasons'][arm])

    def test_cli_mutable_or_malformed_study_ref_is_rejected(self):
        baseline = self._correctness_record()
        for ref in ('main', 'refs/tags/v1', 'a' * 7, 'g' * 40, '<40-char study commit sha>'):
            with self.subTest(ref=ref):
                self.p['repository_ref'] = ref
                self.p['source_state_lock']['expected_default_branch_tip_sha'] = ref
                record = copy.deepcopy(baseline)
                for wave in ('pilot', 'confirmatory'):
                    for case in record[wave + '_cases']:
                        for run in case['runs']:
                            run['submitted_run_envelope'] = E.envelope(self.p, wave.upper(), case['task_id'], run['arm'], run['task_prompt_sha256'])
                            run['run_envelope_sha256'] = E.csha(run['submitted_run_envelope'])
                            run['submitted_full_message'] = E.full_message(self.p, wave.upper(), case['task_id'], run['arm'], run['submitted_task_prompt'], run['task_prompt_sha256'])
                            run['submitted_full_message_sha256'] = E.s256t(run['submitted_full_message'])
                            run['source_state_pre_sha'] = run['source_state_post_sha'] = ref
                            for event in run['tool_events']:
                                if event['operation'] in ('branch_tip_pre', 'branch_tip_post'):
                                    event['observed_ref_sha'] = ref
                                else:
                                    event['ref'] = ref
                            self._refresh_events(run)
                result, report = self._cli(record)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIn('40-character commit SHA', result.stderr)
                self.assertIsNone(report)

    def test_cli_invalid_token_counts_cannot_produce_efficiency_acceptance(self):
        baseline = self._efficiency_record()
        for arm in (E.CONTROL, E.TREATMENT):
            for value in (-100, '100', True, 1.5, float('inf'), float('nan')):
                with self.subTest(arm=arm, value=value):
                    record = copy.deepcopy(baseline)
                    for wave in ('pilot', 'confirmatory'):
                        for case in record[wave + '_cases']:
                            next(run for run in case['runs'] if run['arm'] == arm)['measured_input_tokens'] = value
                    result, report = self._cli(record)
                    self.assertEqual(result.returncode, 2, result.stderr)
                    self.assertIn('measured_input_tokens', result.stderr)
                    self.assertNotIn('Traceback', result.stderr)
                    self.assertIsNone(report)

    def test_token_count_validation_is_independent_of_metric_and_run_validity(self):
        for metric in ('repository_response_utf8_bytes', 'input_tokens', 'unavailable'):
            with self.subTest(metric=metric):
                self.p['context_volume']['metric'] = metric
                record = copy.deepcopy(self.record)
                run = record['pilot_cases'][0]['runs'][0]
                run.update(measured_input_tokens=-1, conversation_fresh=False)
                with self.assertRaisesRegex(ValueError, 'measured_input_tokens'):
                    self.eval(record)

    def test_cli_token_boundaries_and_missing_measurements(self):
        baseline = self._efficiency_record()
        for a, b, expected in ((100, 100, 'ENGINEERING ACCEPTANCE — ORIENTATION EFFICIENCY'), (100, 0, 'ENGINEERING ACCEPTANCE — ORIENTATION EFFICIENCY'), (0, 0, 'ENGINEERING ACCEPTANCE — ORIENTATION EFFICIENCY'), (100, None, 'ENGINEERING SIGNAL — CONNECTOR INTERACTION ONLY'), (None, 100, 'ENGINEERING SIGNAL — CONNECTOR INTERACTION ONLY')):
            with self.subTest(a=a, b=b):
                record = copy.deepcopy(baseline)
                for wave in ('pilot', 'confirmatory'):
                    for case in record[wave + '_cases']:
                        for run in case['runs']:
                            run['measured_input_tokens'] = a if run['arm'] == E.CONTROL else b
                result, report = self._cli(record)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(report['final_conclusion']['final_status'], expected)

    def test_cli_connector_search_retains_valid_cost_accounting(self):
        record = self._efficiency_record()
        for wave in ('pilot', 'confirmatory'):
            for case in record[wave + '_cases']:
                run = next(run for run in case['runs'] if run['arm'] == E.CONTROL)
                run['tool_events'][1].update(operation='code_search', ref=None)
                self._refresh_events(run)
        result, report = self._cli(record)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(report['final_conclusion']['final_status'], 'ENGINEERING ACCEPTANCE — ORIENTATION EFFICIENCY')
        for wave in ('pilot', 'confirmatory'):
            self.assertEqual(report[wave]['ecological_median_connector_ratio'], 0.5)
            self.assertTrue(all(case['derived_infrastructure_calls_a'] == 2 and case['derived_infrastructure_calls_b'] == 2 for case in report[wave]['cases']))

if __name__=='__main__': unittest.main()
