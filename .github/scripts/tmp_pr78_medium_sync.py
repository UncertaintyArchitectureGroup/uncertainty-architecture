from pathlib import Path
p=Path('content/research/notes/open-engineering-specification-article-blueprint.md')
s=p.read_text()

def exact(old,new,label):
    global s
    n=s.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected 1, found {n}')
    s=s.replace(old,new)

# 1) Remove remaining Organizational-selected-path semantics in later sections.
exact(
"- **Viability/business/research-authority nuance:** the paper's explicit assessment-eligibility → Project-viability → Organizational-selected-path/specific-research/business-decision → scoped-Project-Authorization handshake is a research refinement until framework reconciliation. Landscape comparison must allow an equivalent existing method/composition to distribute these decisions differently if legitimate analytical and business/design authority, bounded-research versus production semantics, category-transition semantics, veto semantics, technical authorization, and reassessment are preserved.",
"- **Viability/business/research-authority nuance:** the paper's explicit assessment-eligibility → Project technical/design selection and viability → Organizational specific-research/business/basis decision where required → scoped-Project-Authorization handshake is a research refinement until framework reconciliation. Landscape comparison must allow an equivalent existing method/composition to distribute these decisions differently if legitimate technical/design authority, business/basis authority, bounded-research versus production semantics, category-transition semantics, veto semantics, technical authorization, and reassessment are preserved.",
'section6 ownership nuance')

exact(
"This research paper proposes and tests a publication-facing synthesis that composes current specification constructs with the assessment-eligibility / Project-viability / Organizational-selected-path-and-business-or-research-authorization / scoped-Project-Authorization lifecycle refinement, carrier-sufficiency, semantic-substitution, reverse-mapping, integration-gap, and validation questions.",
"This research paper proposes and tests a publication-facing synthesis that composes current specification constructs with the assessment-eligibility / Project technical-design-and-viability / Organizational business-research-basis authority where required / scoped-Project-Authorization lifecycle refinement, carrier-sufficiency, semantic-substitution, reverse-mapping, integration-gap, and validation questions.",
'section7 core claim')

exact(
"- the four decision horizons, the paper-level assessment-eligibility / Project-viability / Organizational-selected-path-and-business-or-research-authorization / scoped-Project-Authorization handshake, Project-selected-design category exit as handoff to ordinary product/software governance rather than automatic business authorization, and reassessment routing with exogenous Organizational change separated from lower-level evidence;",
"- the four decision horizons, the paper-level assessment-eligibility / Project technical-design-and-viability / Organizational business-research-basis authority where required / scoped-Project-Authorization handshake, Project-selected-design category exit as handoff to ordinary product/software governance rather than automatic business authorization, and reassessment routing with exogenous Organizational change separated from lower-level evidence;",
'section7 do not reteach')

# 2) Split Model-Judgment necessity from economics/business escalation.
exact(
"- If the architecture remains credible but economics, price/value assumptions, Human Authority/capacity burden, Model-Judgment-necessity rationale, or business outcome no longer close, Project returns the viability conclusion to Organization for a path/business decision.",
"- If the architecture remains credible but economics, price/value assumptions, Human Authority/capacity burden, business outcome, or another Organizationally owned premise no longer closes, Project returns the relevant viability finding to Organization for a business/basis decision. If the Model-Judgment-necessity rationale changes but a simpler technical path still satisfies the standing Organizational basis, Project selects that path and confirms category locally; Organization is reactivated only when the preferred path requires changing an Organizationally owned premise or continuation decision.",
'project local escalation split')

# 3) Make the blueprint Organization example demonstrate research proportionality.
anchor="An **Architectural Veto is binding for the unchanged proposal**. Organization may change the business outcome, scope, authority, consequence profile, service promise, funding, shared capability, or other relevant assumption and ask Project / Architecture to reassess; it may not simply “accept the risk” and instruct Delivery to build the same non-credible control architecture. By contrast, a technically credible architecture whose economics do not close is a business decision surface: Organization may change business levers, authorize more research, accept a different investment horizon, simplify the use case, or stop the initiative. A simpler-design conclusion remains Project-owned when it satisfies the standing Organizational business/authority basis; Project applies the category result to that selected technical design. It returns to Organization only when the recommendation requires changing an Organizationally owned premise or business continuation decision. Bounded research is neither an override nor a provisional production approval; it authorizes a **specific** evidence-generating exposure inside a narrower scope."
addition=anchor+"\n\nFor the support-resolution running example, evaluator validation on synthetic or already-authorized offline cases with transaction tools disabled can remain Project-local inside the standing assessment envelope. Measuring real Human Authority approval load on live customer cases, using reserved customer data, production-like tool authority, or another Organizationally owned exposure is different: Project first defines the experiment and credible control/evidence envelope, Organization decides whether to issue the specific Bounded Research Authorization, and only then may Project issue the corresponding research-only technical authorization."
exact(anchor,addition,'blueprint running example proportionality')

p.write_text(s)
