#!/usr/bin/env python3
"""Regression tests for the Repository Intelligence A/B evaluator."""
import hashlib, importlib.util, json, tempfile, unittest
from pathlib import Path
M=Path(__file__).resolve().parents[2]/"scripts"/"score_repository_intelligence_ab.py"; spec=importlib.util.spec_from_file_location("ri_ab",M); E=importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
class T(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory(); self.addCleanup(self.t.cleanup); self.root=Path(self.t.name); self.ref="a"*40; self.sel="eco-seed"; self.ps="pilot-seed"; self.cs="confirm-seed"; self.ident={"mode":"connector_compact_surface","identifier":"assets/repository-intelligence/agent-context.json","git_blob_sha":"b"*40,"content_sha256":"c"*64,"source_identity":"source-v8"}; self.paths={}; self.make_files(); self.p=self.prereg(); self.r=self.record()
 def wr(self,p,v): p.write_text(json.dumps(v,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 def dg(self,p): return hashlib.sha256(p.read_bytes()).hexdigest()
 def make_files(self):
  items=[]
  for i in range(28):
   a="exact-owner" if i<4 else "legitimate-new-artifact" if i<8 else "none"; sc=["exact-owner-recovery"] if a=="exact-owner" else ["legitimate-new-artifact"] if a!="none" else []; items.append({"ecological_source_id":f"E{i:02d}","task_family_id":f"EF{i:02d}","normalized_prompt":f"Eco {i}","anchor_type":a,"scenario_families":sc})
  self.pool={"schema_version":1,"items":items}; self.paths["ecological_pool"]=self.root/"pool.json"; self.wr(self.paths["ecological_pool"],self.pool); sel=E.eco_select(items,self.sel); by={x["ecological_source_id"]:x for x in items}
  ps=[["canonical-term-synonym-pressure","near-synonym-source-review"],["overlapping-artifact-refinement","impact-validation-routing"],["research-authority-separation","ukrainian-or-paraphrased-routing"],["accepted-proposed-relation-change"],["branch-behind-target"],["producer-schema-self-change"]]; cs=[["accepted-proposed-relation-change"],["branch-behind-target"],["producer-schema-self-change"],["candidate-data-boundary"],["shared-structural-hub"],["stale-materialization-fallback"]]
  for key,w,prefix,seed,stress in (("pilot","PILOT","P",self.ps,ps),("confirmatory","CONFIRMATORY","C",self.cs,cs)):
   cases=[]; keys=[]
   for i in range(12):
    tid=f"{prefix}{i+1:02d}"; eco=i>=6; src=sel[key][i-6] if eco else None; it=by[src] if eco else None; sc=it["scenario_families"] if eco else stress[i]; fam=it["task_family_id"] if eco else f"{prefix}F{i}"; prompt=it["normalized_prompt"] if eco else f"{w} stress {i}"; cases.append({"task_id":tid,"task_family_id":fam,"corpus_class":"ecological" if eco else "stress","ecological_source_id":src,"scenario_families":sc,"planned_order":E.arm_order(seed,tid),"prompt":prompt}); app=i%3==0; dims={f:{"0":"bad","1":"partial","2":"good"} for f in E.CORE_SCORE_FIELDS};
    if app: dims[E.OPTIONAL_SCORE_FIELD]={"0":"bad","1":"partial","2":"good"}
    keys.append({"task_id":tid,"companion_validation_applicable":app,"expected_owner_or_route":["owner.md"],"acceptable_alternatives":[],"required_authoritative_evidence":["owner.md"],"serious_error_conditions":["wrong owner"],"decision_acceptance_conditions":["bounded decision"],"dimension_anchors":dims})
   pack={"schema_version":3,"wave":w,"cases":cases}; sk={"schema_version":3,"wave":w,"cases":keys}; self.paths[key+"_prompts"]=self.root/(key+"-p.json"); self.paths[key+"_key"]=self.root/(key+"-k.json"); self.wr(self.paths[key+"_prompts"],pack); self.wr(self.paths[key+"_key"],sk); setattr(self,key+"pack",pack); setattr(self,key+"key",sk)
 def prereg(self):
  pf={f:True for f in E.PREFLIGHT}; iso={"conversation_fresh":True,"memory_enabled":False,"project_context_present":False,"prior_repo_context_available":False,"previous_arm_output_exposed":False,"corrective_scoring_feedback_before_pair_complete":False,"future_wave_material_exposed":False,"hidden_benchmark_material_exposed":False}
  return {"protocol_version":8,"study_id":"S","repository":"UncertaintyArchitectureGroup/uncertainty-architecture","repository_ref":self.ref,"execution_policy":"always_run_pilot_and_confirmatory","source_state_lock":{"mode":"stable_default_branch_window","expected_default_branch_tip_sha":self.ref,"repository_mutations_prohibited_during_primary":True,"pre_run_tip_check_required":True,"post_run_tip_check_required":True,"ordinary_default_branch_search_allowed":True},"execution_preflight":pf,"isolation_requirements":iso,"model_family":"GPT-test","thinking_configuration":"fixed","client_environment":"client","connector":"GitHub","treatment_delivery":{"mode":"connector_compact_surface","aid_identity":self.ident},"mandatory_scenario_families":sorted(E.MANDATORY),"confirmatory_required_scenario_families":sorted(E.CRITICAL),"prompt_pack_schema_version":3,"scoring_key_schema_version":3,"ecological_source_pool":{"mode":"combined_pool","normalized_eligible_pool_sha256":self.dg(self.paths["ecological_pool"]),"selection_seed_sha256":E.s256t(self.sel)},"pilot":{"case_count":12,"stress_cases":6,"ecological_cases":6,"prompts_sha256":self.dg(self.paths["pilot_prompts"]),"scoring_key_sha256":self.dg(self.paths["pilot_key"]),"arm_order_seed_sha256":E.s256t(self.ps)},"confirmatory":{"case_count":12,"stress_cases":6,"ecological_cases":6,"prompts_sha256":self.dg(self.paths["confirmatory_prompts"]),"scoring_key_sha256":self.dg(self.paths["confirmatory_key"]),"arm_order_seed_sha256":E.s256t(self.cs)},"positive_reversal_quality_gate":{"minimum_each_applicable_dimension":1},"ecological_correctness_non_regression":{"minimum_per_wave":0},"connector_cost_gate":{"acceptable_median_ratio_b_over_a":1.5,"high_overhead_ratio_threshold":2.0,"acceptable_high_overhead_case_count":2},"connector_interaction_gain_rule":{"maximum_median_ratio_b_over_a_per_wave":0.8},"context_volume":{"metric":"repository_response_utf8_bytes","maximum_median_ratio_b_over_a_per_wave":1.0,"high_overhead_ratio_threshold":2.0,"acceptable_high_overhead_case_count":2},"orientation_cost_boundary":"task_orientation_events_only","final_decision_rule":{"engineering_acceptance_correctness":{"minimum_confirmatory_positive_reversals":1,"minimum_confirmatory_ecological_positive_reversals":1,"minimum_combined_positive_reversals":3}}}
 def score(self,app,ser=False): return {"owner_routing":2,"evidence_sufficiency":2,"authority_discipline":2,"companion_validation":2 if app else None,"decision_quality":2,"total_applicable_correctness":10 if app else 8,"serious_routing_error":ser}
 def event(self,n,rc,b,ident=None,phase="task_orientation"): return {"sequence":n,"phase":phase,"tool_family":"GitHub","operation":"fetch","repository":self.p["repository"],"ref":self.ref,"resource":"x","resource_class":rc,"response_bytes":b,"content_identity":ident}
 def makerun(self,w,tid,arm,order,ph,app):
  tr=arm==E.TREATMENT; ev=[self.event(1,"ordinary_source",50),self.event(2,"ri_compact_surface" if tr else "ordinary_source",50,self.ident if tr else None)]; return {"run_id":tid+arm,"arm":arm,"pair_order":order,"task_prompt_sha256":ph,"run_envelope_sha256":E.envelope_hash(self.p,w,tid,arm,ph),"conversation_fresh":True,"memory_enabled":False,"project_context_present":False,"prior_repo_context_available":False,"previous_arm_output_exposed":False,"corrective_scoring_feedback_before_pair_complete":False,"future_wave_material_exposed":False,"hidden_benchmark_material_exposed":False,"connector_state_equal":True,"source_state_pre_sha":self.ref,"source_state_post_sha":self.ref,"source_state_protocol_violation":False,"model_family":"GPT-test","thinking_configuration":"fixed","client_environment":"client","connector":"GitHub","protocol_violations":[],"tool_events":ev,"total_connector_calls":2,"default_branch_search_calls":0,"ri_payload_bytes":50 if tr else 0,"repository_response_utf8_bytes":100,"measured_input_tokens":None,"treatment_delivery_status":"delivered" if tr else "not-applicable","treatment_surface_verified":tr,"complete_treatment_payload_verified":tr,"scores":self.score(app)}
 def wave(self,key,w):
  pack=getattr(self,key+"pack"); km={x["task_id"]:x for x in getattr(self,key+"key")["cases"]}; out=[]
  for c in pack["cases"]:
   t=c["task_id"]; ph=E.s256t(E.norm(c["prompt"])); order=c["planned_order"]; runs={a:self.makerun(w,t,a,order,ph,km[t]["companion_validation_applicable"]) for a in E.PRIMARY_ARMS}; out.append({"task_id":t,"corpus_class":c["corpus_class"],"order":order,"runs":[runs[a] for a in order]})
  return out
 def record(self): return {"protocol_version":8,"study_id":"S","pilot_cases":self.wave("pilot","PILOT"),"confirmatory_cases":self.wave("confirmatory","CONFIRMATORY")}
 def evidence(self,se=None): return E.verify_evidence(self.p,self.paths,{"ecological_selection":self.sel if se is None else se,"pilot_arm":self.ps,"confirmatory_arm":self.cs})
 def eval(self): return E.evaluate(self.p,self.r,self.evidence())
 def arms(self,c): return {x["arm"]:x for x in c["runs"]}
 def test_seed_replay_and_wrong_seed(self):
  self.assertTrue(self.evidence()["selection_replayed"])
  with self.assertRaisesRegex(ValueError,"selection seed"): self.evidence("wrong")
 def test_prompt_and_envelope_identity(self):
  self.r["pilot_cases"][0]["runs"][0]["task_prompt_sha256"]="0"*64; self.assertFalse(self.eval()["pilot"]["all_pairs_valid"])
 def test_structured_log_beats_manual_flags(self):
  r=self.arms(self.r["pilot_cases"][0])[E.CONTROL]; r["tool_events"][1]=self.event(2,"ri_compact_surface",50,self.ident); self.assertFalse(self.eval()["pilot"]["all_pairs_valid"])
 def test_wrong_treatment_identity(self):
  r=self.arms(self.r["pilot_cases"][0])[E.TREATMENT]; r["tool_events"][1]["content_identity"]={**self.ident,"git_blob_sha":"f"*40}; self.assertFalse(self.eval()["pilot"]["all_pairs_valid"])
 def test_infrastructure_calls_excluded(self):
  r=self.arms(self.r["pilot_cases"][0])[E.CONTROL]; r["tool_events"].insert(0,self.event(1,"other",20,phase="study_infrastructure")); [e.__setitem__("sequence",i+1) for i,e in enumerate(r["tool_events"])]; self.assertTrue(self.eval()["pilot"]["all_pairs_valid"])
 def test_scoring_key_must_have_anchors(self):
  self.pilotkey["cases"][0]["required_authoritative_evidence"]=[]; self.wr(self.paths["pilot_key"],self.pilotkey); self.p["pilot"]["scoring_key_sha256"]=self.dg(self.paths["pilot_key"])
  with self.assertRaisesRegex(ValueError,"required_authoritative_evidence"): self.evidence()
 def test_ecological_anchor_per_wave(self):
  [c.__setitem__("scenario_families",[]) for c in self.pilotpack["cases"] if c["corpus_class"]=="ecological"]; self.wr(self.paths["pilot_prompts"],self.pilotpack); self.p["pilot"]["prompts_sha256"]=self.dg(self.paths["pilot_prompts"])
  with self.assertRaisesRegex(ValueError,"ecological half misses required anchors"): self.evidence()
 def test_correctness_acceptance_needs_confirmatory_ecological_support(self):
  for c in self.r["pilot_cases"][:2]+self.r["confirmatory_cases"][:1]: self.arms(c)[E.CONTROL]["scores"]["serious_routing_error"]=True
  self.assertFalse(self.eval()["final_conclusion"]["engineering_acceptance_correctness"])
 def test_engineering_acceptance_and_regression(self):
  for c in [self.r["pilot_cases"][0],self.r["pilot_cases"][1],self.r["confirmatory_cases"][6]]: self.arms(c)[E.CONTROL]["scores"]["serious_routing_error"]=True
  self.assertTrue(self.eval()["final_conclusion"]["engineering_acceptance_correctness"]); self.arms(self.r["confirmatory_cases"][0])[E.TREATMENT]["scores"]["serious_routing_error"]=True; self.assertEqual(self.eval()["final_conclusion"]["final_status"],"REGRESSION")
if __name__=="__main__": unittest.main()
