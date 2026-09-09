#!/usr/bin/env python3
"""Mechanically evaluate the preregistered Repository Intelligence A/B study."""
import argparse, hashlib, json, math, statistics, sys
from pathlib import Path

PROTOCOL_VERSION=8; CONTROL="RI-AB-CONTROL"; TREATMENT="RI-AB-TREATMENT"; PRIMARY_ARMS={CONTROL,TREATMENT}
CORE_SCORE_FIELDS=("owner_routing","evidence_sufficiency","authority_discipline","decision_quality"); OPTIONAL_SCORE_FIELD="companion_validation"
RESOURCE_CLASSES={"ordinary_source","ri_compact_surface","ri_query","ri_full_graph","repository_control_map","other"}; RI_CLASSES=RESOURCE_CLASSES-{"ordinary_source","other"}
MANDATORY={"exact-owner-recovery","canonical-term-synonym-pressure","near-synonym-source-review","overlapping-artifact-refinement","legitimate-new-artifact","impact-validation-routing","accepted-proposed-relation-change","branch-behind-target","producer-schema-self-change","candidate-data-boundary","shared-structural-hub","research-authority-separation","stale-materialization-fallback","ukrainian-or-paraphrased-routing"}
CRITICAL={"accepted-proposed-relation-change","branch-behind-target","producer-schema-self-change","candidate-data-boundary","shared-structural-hub","stale-materialization-fallback"}; ANCHORS={"exact-owner-recovery","legitimate-new-artifact"}
PREFLIGHT=("smoke_passed","default_branch_tip_checks_verified","ordinary_control_search_verified","exact_ref_direct_reads_verified","treatment_delivery_verified","complete_treatment_payload_verified","truncation_check_passed","instrumentation_capture_verified","connector_permission_parity_verified","memory_disabled_verified","project_context_absent_verified","prior_product_repo_context_absent_verified","repository_mutation_freeze_acknowledged")

def req(c,m):
    if not c: raise ValueError(m)
def load(path,label):
    try: v=json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError) as e: raise ValueError(f"{label} is not readable JSON: {e}") from e
    req(isinstance(v,dict),f"{label} must be a JSON object"); return v
def s256b(b): return hashlib.sha256(b).hexdigest()
def s256f(p): return s256b(Path(p).read_bytes())
def s256t(s): return s256b(s.encode())
def cjson(v): return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def csha(v): return s256t(cjson(v))
def norm(s): return " ".join(s.split())
def med(v): return statistics.median(v) if v else None
def rat(n,d): return (1.0 if n==0 else math.inf) if d==0 else n/d
def rank(seed,label,ident): return s256t(f"{seed}\0{label}\0{ident}")
def arm_order(seed,task): return [CONTROL,TREATMENT] if int(rank(seed,"arm-order",task),16)%2==0 else [TREATMENT,CONTROL]

def eco_select(items,seed):
    exact=[x for x in items if x["anchor_type"]=="exact-owner"]; new=[x for x in items if x["anchor_type"]=="legitimate-new-artifact"]
    req(len(exact)>=2 and len(new)>=2,"ecological pool needs at least two anchors of each required type")
    exact=sorted(exact,key=lambda x:rank(seed,"exact-owner",x["ecological_source_id"]))[:2]; new=sorted(new,key=lambda x:rank(seed,"legitimate-new-artifact",x["ecological_source_id"]))[:2]
    used={x["ecological_source_id"] for x in exact+new}; rest=sorted([x for x in items if x["ecological_source_id"] not in used],key=lambda x:rank(seed,"general",x["ecological_source_id"]))[:8]
    req(len(rest)==8,"ecological pool needs eight non-reserved selections")
    return {"pilot":sorted(x["ecological_source_id"] for x in [exact[0],new[0],*rest[:4]]),"confirmatory":sorted(x["ecological_source_id"] for x in [exact[1],new[1],*rest[4:]])}

def envelope_hash(p,w,t,a,ph):
    return csha({"repository":p["repository"],"repository_ref":p["repository_ref"],"source_state_lock":"stable_default_branch_window","wave":w,"task_id":t,"arm":a,"treatment_delivery_mode":p["treatment_delivery"]["mode"] if a==TREATMENT else "not-applicable","task_prompt_sha256":ph})

# Stable helper aliases used by regression fixtures and external evidence tooling.
deterministic_ecological_selection=eco_select
deterministic_arm_order=arm_order
expected_envelope_hash=envelope_hash
sha256_text=s256t
normalized_prompt=norm
PREFLIGHT_TRUE_FIELDS=PREFLIGHT
MANDATORY_SCENARIO_FAMILIES=MANDATORY
CONFIRMATORY_CRITICAL_FAMILIES=CRITICAL

def validate_prereg(p):
    req(p.get("protocol_version")==8,"unsupported protocol_version")
    for f in ("study_id","repository","repository_ref","model_family","thinking_configuration","client_environment","connector"): req(isinstance(p.get(f),str) and p[f],f"{f} must be preregistered")
    req(p.get("execution_policy")=="always_run_pilot_and_confirmatory","both primary waves must run")
    l=p.get("source_state_lock"); req(isinstance(l,dict) and l.get("mode")=="stable_default_branch_window" and l.get("expected_default_branch_tip_sha")==p["repository_ref"],"invalid source_state_lock")
    for f in ("repository_mutations_prohibited_during_primary","pre_run_tip_check_required","post_run_tip_check_required","ordinary_default_branch_search_allowed"): req(l.get(f) is True,f"source-state field {f} must be true")
    pf=p.get("execution_preflight"); req(isinstance(pf,dict),"execution_preflight required")
    for f in PREFLIGHT: req(pf.get(f) is True,f"execution preflight field {f} must be true")
    iso=p.get("isolation_requirements"); req(isinstance(iso,dict),"isolation_requirements required")
    for f,v in {"conversation_fresh":True,"memory_enabled":False,"project_context_present":False,"prior_repo_context_available":False,"previous_arm_output_exposed":False,"corrective_scoring_feedback_before_pair_complete":False,"future_wave_material_exposed":False,"hidden_benchmark_material_exposed":False}.items(): req(iso.get(f) is v,f"isolation {f} must be {v}")
    d=p.get("treatment_delivery"); req(isinstance(d,dict) and d.get("mode") in {"connector_compact_surface","local_cli","dedicated_adapter"},"invalid Treatment Delivery Mode"); ident=d.get("aid_identity"); req(isinstance(ident,dict) and ident.get("mode")==d["mode"],"Treatment aid identity required")
    for f in ("identifier","git_blob_sha","content_sha256","source_identity"): req(isinstance(ident.get(f),str) and ident[f],f"Treatment aid identity {f} required")
    req(set(p.get("mandatory_scenario_families",[]))==MANDATORY,"mandatory scenario family set mismatch"); req(set(p.get("confirmatory_required_scenario_families",[]))>=CRITICAL,"confirmatory critical coverage set incomplete")
    for k in ("pilot","confirmatory"):
        w=p.get(k); req(isinstance(w,dict) and w.get("case_count")==12 and w.get("stress_cases")==6 and w.get("ecological_cases")==6,f"{k} must be 6+6")
        for f in ("prompts_sha256","scoring_key_sha256","arm_order_seed_sha256"): req(isinstance(w.get(f),str) and len(w[f])==64,f"{k}.{f} must be SHA-256")
    eco=p.get("ecological_source_pool"); req(isinstance(eco,dict) and eco.get("mode")=="combined_pool","v8 requires one combined ecological pool")
    for f in ("normalized_eligible_pool_sha256","selection_seed_sha256"): req(isinstance(eco.get(f),str) and len(eco[f])==64,f"ecological_source_pool.{f} must be SHA-256")
    req(p.get("prompt_pack_schema_version")==3 and p.get("scoring_key_schema_version")==3,"v8 requires schema version 3"); req(p.get("orientation_cost_boundary")=="task_orientation_events_only","orientation cost boundary invalid")

def validate_pool(path,p,seed):
    req(s256f(path)==p["ecological_source_pool"]["normalized_eligible_pool_sha256"],"ecological pool hash mismatch"); req(s256t(seed)==p["ecological_source_pool"]["selection_seed_sha256"],"ecological selection seed commitment mismatch")
    pool=load(path,"ecological pool"); items=pool.get("items"); req(pool.get("schema_version")==1 and isinstance(items,list) and len(items)>=24,"invalid ecological pool")
    ids=set(); fam=set()
    for x in items:
        req(isinstance(x,dict) and x.get("anchor_type") in {"exact-owner","legitimate-new-artifact","none"},"invalid ecological pool item")
        for f in ("ecological_source_id","task_family_id","normalized_prompt"): req(isinstance(x.get(f),str) and x[f],f"ecological pool {f} required")
        req(x["ecological_source_id"] not in ids and x["task_family_id"] not in fam,"ecological identities must be unique"); ids.add(x["ecological_source_id"]); fam.add(x["task_family_id"])
    return eco_select(items,seed)

def validate_pack(path,h,w,seed):
    req(s256f(path)==h,f"{w} prompt-pack hash mismatch"); p=load(path,f"{w} prompt pack"); cs=p.get("cases"); req(p.get("schema_version")==3 and p.get("wave")==w and isinstance(cs,list) and len(cs)==12,f"{w} prompt pack invalid")
    out={"ids":[],"classes":{},"prompts":{},"families":{},"sources":{},"scenarios":{},"orders":{}}
    for c in cs:
        t=c.get("task_id"); cl=c.get("corpus_class"); pr=c.get("prompt"); fam=c.get("task_family_id"); src=c.get("ecological_source_id"); sc=c.get("scenario_families")
        req(isinstance(t,str) and t and t not in out["ids"],f"{w} task_id invalid"); req(cl in {"stress","ecological"} and isinstance(pr,str) and pr.strip() and isinstance(fam,str) and fam,f"{w} case invalid"); req(isinstance(sc,list) and all(x in MANDATORY for x in sc),f"{w} scenarios invalid")
        req((cl=="ecological" and isinstance(src,str) and src) or (cl=="stress" and src is None and sc),f"{w} source/scenario contract invalid"); order=arm_order(seed,t); req(c.get("planned_order")==order,f"{w} arm order not reproduced by seed")
        out["ids"].append(t); out["classes"][t]=cl; out["prompts"][t]=s256t(norm(pr)); out["families"][t]=fam; out["sources"][t]=src; out["scenarios"][t]=sc; out["orders"][t]=order
    req(list(out["classes"].values()).count("stress")==6 and list(out["classes"].values()).count("ecological")==6,f"{w} must be 6+6"); return out

def validate_key(path,h,w,ids):
    req(s256f(path)==h,f"{w} scoring-key hash mismatch"); k=load(path,f"{w} scoring key"); cs=k.get("cases"); req(k.get("schema_version")==3 and k.get("wave")==w and isinstance(cs,list),f"{w} scoring key invalid"); out={}
    for c in cs:
        t=c.get("task_id"); req(t in ids and t not in out,f"{w} scoring-key task IDs invalid"); req(type(c.get("companion_validation_applicable")) is bool,f"{t} companion applicability missing")
        for f in ("expected_owner_or_route","required_authoritative_evidence","serious_error_conditions","decision_acceptance_conditions"): req(isinstance(c.get(f),list) and c[f],f"{t} scoring key {f} must be non-empty")
        req(isinstance(c.get("acceptable_alternatives"),list),f"{t} acceptable_alternatives must be list"); da=c.get("dimension_anchors"); req(isinstance(da,dict),f"{t} dimension_anchors missing"); dims=set(CORE_SCORE_FIELDS)|({OPTIONAL_SCORE_FIELD} if c["companion_validation_applicable"] else set()); req(set(da)==dims,f"{t} dimension anchors mismatch")
        for d,levels in da.items(): req(isinstance(levels,dict) and set(levels)=={"0","1","2"} and all(isinstance(v,str) and v for v in levels.values()),f"{t} {d} anchors invalid")
        out[t]=c
    req(set(out)==set(ids),f"{w} scoring-key IDs must match prompt pack"); return out

def verify_evidence(p,paths,seeds):
    sel=validate_pool(paths["ecological_pool"],p,seeds["ecological_selection"]); packs={}; keys={}
    for k,w in (("pilot","PILOT"),("confirmatory","CONFIRMATORY")):
        req(s256t(seeds[k+"_arm"])==p[k]["arm_order_seed_sha256"],f"{w} arm seed commitment mismatch"); packs[k]=validate_pack(paths[k+"_prompts"],p[k]["prompts_sha256"],w,seeds[k+"_arm"]); keys[k]=validate_key(paths[k+"_key"],p[k]["scoring_key_sha256"],w,packs[k]["ids"])
        req(sorted(x for x in packs[k]["sources"].values() if x)==sel[k],f"{w} ecological selection not reproduced from pool+seed"); eco_sc={x for t,v in packs[k]["scenarios"].items() if packs[k]["classes"][t]=="ecological" for x in v}; req(ANCHORS<=eco_sc,f"{w} ecological half misses required anchors")
    req(not(set(packs["pilot"]["families"].values())&set(packs["confirmatory"]["families"].values())),"task_family_id overlaps across waves"); ps={x for x in packs["pilot"]["sources"].values() if x}; cs={x for x in packs["confirmatory"]["sources"].values() if x}; req(not(ps&cs),"ecological_source_id overlaps across waves")
    allsc={x for q in packs.values() for v in q["scenarios"].values() for x in v}; req(MANDATORY<=allsc,"held-out corpora miss mandatory scenarios"); csc={x for v in packs["confirmatory"]["scenarios"].values() for x in v}; req(set(p["confirmatory_required_scenario_families"])<=csc,"Confirmatory misses critical scenarios"); return {"packs":packs,"keys":keys,"selection_replayed":True,"arm_randomization_replayed":True}

def score_total(s,key):
    req(isinstance(s,dict),"scores required"); vals={}
    for f in CORE_SCORE_FIELDS: req(type(s.get(f)) is int and 0<=s[f]<=2,f"{f} score invalid"); vals[f]=s[f]
    comp=s.get(OPTIONAL_SCORE_FIELD)
    if key["companion_validation_applicable"]: req(type(comp) is int and 0<=comp<=2,"companion_validation must be scored"); vals[OPTIONAL_SCORE_FIELD]=comp
    else: req(comp is None,"companion_validation must be null")
    total=sum(vals.values()); req(s.get("total_applicable_correctness")==total,"total_applicable_correctness mismatch"); req(type(s.get("serious_routing_error")) is bool,"serious_routing_error must be boolean"); return total,s["serious_routing_error"],vals

def derive(run,p):
    ev=run.get("tool_events"); req(isinstance(ev,list),"tool_events must be list")
    for i,e in enumerate(ev,1): req(isinstance(e,dict) and e.get("sequence")==i and e.get("phase") in {"study_infrastructure","task_orientation"} and e.get("resource_class") in RESOURCE_CLASSES and e.get("repository")==p["repository"],"invalid tool event"); req(e.get("response_bytes") is None or type(e["response_bytes"]) is int and e["response_bytes"]>=0,"invalid response_bytes")
    task=[e for e in ev if e["phase"]=="task_orientation"]; ri=[e for e in task if e["resource_class"] in RI_CLASSES]; rb=None if any(e.get("response_bytes") is None for e in task) else sum(e["response_bytes"] for e in task); rib=None if any(e.get("response_bytes") is None for e in ri) else sum(e["response_bytes"] for e in ri)
    return {"calls":len(task),"searches":sum(e.get("operation") in {"search","code_search"} for e in task),"ri":bool(ri),"ri_bytes":0 if not ri else rib,"repo_bytes":rb,"bad_control":any(e["resource_class"] in RI_CLASSES for e in task),"identity":any(e.get("content_identity")==p["treatment_delivery"]["aid_identity"] for e in ri)}

def run_valid(run,arm,w,t,ph,order,p):
    reasons=[]; checks={"wrong arm":run.get("arm")==arm,"task prompt hash mismatch":run.get("task_prompt_sha256")==ph,"run envelope hash mismatch":run.get("run_envelope_sha256")==envelope_hash(p,w,t,arm,ph),"conversation not fresh":run.get("conversation_fresh") is True,"Memory not disabled":run.get("memory_enabled") is False,"Project context present":run.get("project_context_present") is False,"prior repo context present":run.get("prior_repo_context_available") is False,"previous arm exposed":run.get("previous_arm_output_exposed") is False,"corrective feedback exposed":run.get("corrective_scoring_feedback_before_pair_complete") is False,"future wave exposed":run.get("future_wave_material_exposed") is False,"hidden benchmark exposed":run.get("hidden_benchmark_material_exposed") is False,"connector state mismatch":run.get("connector_state_equal") is True,"source pre mismatch":run.get("source_state_pre_sha")==p["repository_ref"],"source post mismatch":run.get("source_state_post_sha")==p["repository_ref"],"source protocol violation":run.get("source_state_protocol_violation") is False,"model mismatch":run.get("model_family")==p["model_family"],"thinking mismatch":run.get("thinking_configuration")==p["thinking_configuration"],"client mismatch":run.get("client_environment")==p["client_environment"],"connector mismatch":run.get("connector")==p["connector"]}; reasons += [m for m,v in checks.items() if not v]; req(run.get("pair_order")==order,"pair_order mismatch"); req(isinstance(run.get("protocol_violations"),list),"protocol_violations must be list"); reasons += ["protocol violations"] if run["protocol_violations"] else []
    d=derive(run,p)
    for sf,df in (("total_connector_calls","calls"),("default_branch_search_calls","searches"),("ri_payload_bytes","ri_bytes"),("repository_response_utf8_bytes","repo_bytes")):
        if run.get(sf)!=d[df]: reasons.append(f"{sf} does not match structured events")
    if arm==CONTROL:
        if d["bad_control"]: reasons.append("Control RI ablation contaminated by structured events")
        if run.get("treatment_delivery_status") not in {None,"not-applicable"}: reasons.append("Control records Treatment delivery")
    else:
        if run.get("treatment_delivery_status")!="delivered": reasons.append("Treatment delivery failed")
        if run.get("treatment_surface_verified") is not True or run.get("complete_treatment_payload_verified") is not True: reasons.append("Treatment payload not verified")
        if not d["ri"] or not d["identity"]: reasons.append("Treatment events do not prove exact aid access")
    return reasons,d

def eval_case(c,pack,key,w,p):
    t=c.get("task_id"); req(t in pack["ids"] and c.get("corpus_class")==pack["classes"][t],"run case mismatch"); order=pack["orders"][t]; req(c.get("order")==order,"run order mismatch"); runs=c.get("runs"); req(isinstance(runs,list) and len(runs)==2 and [x.get("arm") for x in runs]==order,"execution order mismatch"); by={x["arm"]:x for x in runs}; req(set(by)==PRIMARY_ARMS,"pair requires both arms")
    invalid={}; ds={}
    for a in (CONTROL,TREATMENT): invalid[a],ds[a]=run_valid(by[a],a,w,t,pack["prompts"][t],order,p)
    if invalid[CONTROL] or invalid[TREATMENT]: return {"task_id":t,"corpus_class":c["corpus_class"],"valid":False,"invalid_reasons":invalid}
    at,aser,_=score_total(by[CONTROL]["scores"],key); bt,bser,bvals=score_total(by[TREATMENT]["scores"],key); state="A-serious/B-no-serious" if aser and not bser else "A-no-serious/B-serious" if bser and not aser else "both-serious" if aser else "neither-serious"; q=all(v>=p["positive_reversal_quality_gate"]["minimum_each_applicable_dimension"] for v in bvals.values())
    va=ds[CONTROL]["repo_bytes"] if p["context_volume"]["metric"]=="repository_response_utf8_bytes" else by[CONTROL].get("measured_input_tokens") if p["context_volume"]["metric"]=="input_tokens" else None; vb=ds[TREATMENT]["repo_bytes"] if p["context_volume"]["metric"]=="repository_response_utf8_bytes" else by[TREATMENT].get("measured_input_tokens") if p["context_volume"]["metric"]=="input_tokens" else None
    return {"task_id":t,"corpus_class":c["corpus_class"],"valid":True,"correctness_delta_b_minus_a":bt-at,"serious_error_outcome":state,"qualifying_positive_reversal":state=="A-serious/B-no-serious" and q,"connector_ratio_b_over_a":rat(ds[TREATMENT]["calls"],ds[CONTROL]["calls"]),"context_volume_ratio_b_over_a":None if va is None or vb is None else rat(vb,va),"equal_correctness_pair":at==bt and aser==bser}

def eval_wave(name,cases,pack,keys,p):
    req(isinstance(cases,list) and len(cases)==12,f"{name} needs 12 cases"); by={c.get("task_id"):c for c in cases}; req(set(by)==set(pack["ids"]),f"{name} task IDs mismatch"); ev=[eval_case(by[t],pack,keys[t],name,p) for t in pack["ids"]]; valid=[c for c in ev if c["valid"]]; eco=[c for c in valid if c["corpus_class"]=="ecological"]; allv=len(valid)==12 and len(eco)==6; pos=sum(c.get("qualifying_positive_reversal") is True for c in valid); epos=sum(c.get("qualifying_positive_reversal") is True for c in eco); rev=sum(c.get("serious_error_outcome")=="A-no-serious/B-serious" for c in valid); erev=sum(c.get("serious_error_outcome")=="A-no-serious/B-serious" for c in eco); deltas=[c["correctness_delta_b_minus_a"] for c in eco]; nonreg=allv and med(deltas)>=p["ecological_correctness_non_regression"]["minimum_per_wave"] and erev==0; cr=[c["connector_ratio_b_over_a"] for c in eco]; cm=med(cr); cg=allv and cm<=p["connector_cost_gate"]["acceptable_median_ratio_b_over_a"] and sum(x>p["connector_cost_gate"]["high_overhead_ratio_threshold"] for x in cr)<=p["connector_cost_gate"]["acceptable_high_overhead_case_count"]; gain=allv and nonreg and rev==0 and cm<=p["connector_interaction_gain_rule"]["maximum_median_ratio_b_over_a_per_wave"]; vr=[c["context_volume_ratio_b_over_a"] for c in eco]; complete=p["context_volume"]["metric"]!="unavailable" and all(x is not None for x in vr); vg=complete and med(vr)<=p["context_volume"]["maximum_median_ratio_b_over_a_per_wave"] and sum(x>p["context_volume"]["high_overhead_ratio_threshold"] for x in vr)<=p["context_volume"]["acceptable_high_overhead_case_count"]
    return {"name":name,"cases":ev,"all_pairs_valid":allv,"qualifying_positive_reversals":pos,"qualifying_ecological_positive_reversals":epos,"reverse_serious_reversals":rev,"ecological_correctness_non_regression_passed":nonreg,"ecological_median_connector_ratio":cm,"connector_cost_gate_passed":cg,"connector_interaction_gain_passed":gain,"ecological_median_context_volume_ratio":med(vr) if complete else None,"context_volume_gate_passed":vg,"orientation_efficiency_passed":gain and vg}

def final(pilot,conf,p):
    allv=pilot["all_pairs_valid"] and conf["all_pairs_valid"]; pos=pilot["qualifying_positive_reversals"]+conf["qualifying_positive_reversals"]; rev=pilot["reverse_serious_reversals"]+conf["reverse_serious_reversals"]; r=p["final_decision_rule"]["engineering_acceptance_correctness"]; th=conf["qualifying_positive_reversals"]>=r["minimum_confirmatory_positive_reversals"] and conf["qualifying_ecological_positive_reversals"]>=r["minimum_confirmatory_ecological_positive_reversals"] and pos>=r["minimum_combined_positive_reversals"] and rev==0 and pilot["ecological_correctness_non_regression_passed"] and conf["ecological_correctness_non_regression_passed"]; cost=pilot["connector_cost_gate_passed"] and conf["connector_cost_gate_passed"]; acc=allv and th and cost; gain=allv and rev==0 and pilot["connector_interaction_gain_passed"] and conf["connector_interaction_gain_passed"]; eff=gain and pilot["orientation_efficiency_passed"] and conf["orientation_efficiency_passed"]; reg=allv and (rev>0 or not pilot["ecological_correctness_non_regression_passed"] or not conf["ecological_correctness_non_regression_passed"])
    status="INCONCLUSIVE" if not allv else "REGRESSION" if reg else "ENGINEERING ACCEPTANCE — CORRECTNESS + ORIENTATION EFFICIENCY" if acc and eff else "ENGINEERING ACCEPTANCE — CORRECTNESS" if acc else "CORRECTNESS SIGNAL / COST NOT ACCEPTED" if th and not cost else "DEMONSTRATED ORIENTATION EFFICIENCY GO" if eff else "DEMONSTRATED CONNECTOR-INTERACTION GAIN ONLY" if gain else "NOT CONFIRMED" if pilot["qualifying_positive_reversals"] else "NO INCREMENTAL VALUE SHOWN"
    return {"all_primary_pairs_valid":allv,"combined_qualifying_positive_reversals":pos,"combined_reverse_serious_reversals":rev,"engineering_acceptance_correctness":acc,"demonstrated_orientation_efficiency_go":eff,"demonstrated_connector_interaction_gain":gain,"regression":reg,"final_status":status}

def evaluate(p,record,e):
    validate_prereg(p); req(record.get("protocol_version")==8 and record.get("study_id")==p["study_id"],"run record protocol/study mismatch"); pil=eval_wave("PILOT",record.get("pilot_cases"),e["packs"]["pilot"],e["keys"]["pilot"],p); con=eval_wave("CONFIRMATORY",record.get("confirmatory_cases"),e["packs"]["confirmatory"],e["keys"]["confirmatory"],p); return {"evaluation_version":3,"protocol_version":8,"study_id":p["study_id"],"repository_ref":p["repository_ref"],"evidence_verification":{"selection_replayed":True,"arm_randomization_replayed":True},"pilot":pil,"confirmatory":con,"final_conclusion":final(pil,con,p)}
def main(argv=None):
    a=argparse.ArgumentParser(description=__doc__); a.add_argument("--preregistration",type=Path,required=True); a.add_argument("--run-record",type=Path,required=True); a.add_argument("--ecological-pool",type=Path,required=True); a.add_argument("--ecological-selection-seed",required=True); a.add_argument("--pilot-arm-seed",required=True); a.add_argument("--confirmatory-arm-seed",required=True); a.add_argument("--pilot-prompts",type=Path,required=True); a.add_argument("--pilot-key",type=Path,required=True); a.add_argument("--confirmatory-prompts",type=Path,required=True); a.add_argument("--confirmatory-key",type=Path,required=True); a.add_argument("--output",type=Path,required=True); x=a.parse_args(argv)
    try:
        p=load(x.preregistration,"preregistration"); r=load(x.run_record,"run record"); validate_prereg(p); e=verify_evidence(p,{"ecological_pool":x.ecological_pool,"pilot_prompts":x.pilot_prompts,"pilot_key":x.pilot_key,"confirmatory_prompts":x.confirmatory_prompts,"confirmatory_key":x.confirmatory_key},{"ecological_selection":x.ecological_selection_seed,"pilot_arm":x.pilot_arm_seed,"confirmatory_arm":x.confirmatory_arm_seed}); out=evaluate(p,r,e); x.output.parent.mkdir(parents=True,exist_ok=True); x.output.write_text(json.dumps(out,indent=2,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8"); print("Repository Intelligence A/B evaluation: "+out["final_conclusion"]["final_status"]); return 0
    except (OSError,ValueError) as exc: print(f"Repository Intelligence A/B evaluation error: {exc}",file=sys.stderr); return 2
if __name__=="__main__": raise SystemExit(main())
