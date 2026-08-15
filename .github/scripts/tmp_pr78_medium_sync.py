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

# 3) Make the blueprint running example demonstrate research proportionality.
exact(
"For the support-resolution example, Organization might reserve refunds above €50 to Human Authority, constrain customer-data access to approved paths, and permit only approved transaction capabilities. Initial assessment eligibility lets Project compare candidate designs and define evidence gaps. If Project later needs evidence about approval load or evaluator validity, it proposes a concrete experiment; Organization may then issue a specific Bounded Research Authorization for a research-only experiment with no customer-facing transaction authority. If Project later concludes that the production architecture is credible but Human Authority makes each resolution too expensive, Organization may change the business model or scope. If Project concludes that no credible realization can prevent unauthorized transactions for the proposed path, the unchanged proposal cannot proceed merely because its expected revenue is attractive.",
"For the support-resolution example, Organization might reserve refunds above €50 to Human Authority, constrain customer-data access to approved paths, and permit only approved transaction capabilities. Initial assessment eligibility lets Project compare candidate designs and define evidence gaps. If Project needs to validate evaluator behavior on synthetic or already-authorized offline cases with transaction tools disabled, that work can remain Project-local inside the standing assessment envelope. If Project instead needs to measure real approval load using live customer cases, reserved customer data, production-like tool authority, or another Organizationally owned exposure, it first defines the concrete experiment and control/evidence envelope; Organization may then issue a specific Bounded Research Authorization, after which Project may issue the corresponding research-only technical authorization. If Project later concludes that the production architecture is credible but Human Authority makes each resolution too expensive, Organization may change the business model or scope. If Project concludes that no credible realization can prevent unauthorized transactions for the proposed path, the unchanged proposal cannot proceed merely because its expected revenue is attractive.",
'blueprint running example proportionality')

p.write_text(s)
