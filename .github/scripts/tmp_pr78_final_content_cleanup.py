from pathlib import Path

bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms = Path('content/research/notes/open-engineering-specification-article-draft.md')
cl = Path('CHANGELOG.md')

b = bp.read_text()
m = ms.read_text()
c = cl.read_text()


def replace_exact(text: str, old: str, new: str, label: str, expected: int = 1) -> str:
    count = text.count(old)
    if count != expected:
        raise SystemExit(f'{label}: expected {expected} occurrences, found {count}')
    return text.replace(old, new)

# 1) Validation Program 3 must test the concurrent scoped-authorization hypothesis itself.
b = replace_exact(
    b,
    'the assessment-eligibility → Project viability conclusion → Organizational specific-bounded-research/business/changed-basis decision → scoped Project Authorization handshake, research-only versus production-capable distinction, Project-selected-design category exit as handoff to ordinary product/software governance rather than automatic business authorization,',
    'the assessment-eligibility → Project viability conclusion → Organizational specific-bounded-research/business/changed-basis decision → scoped Project Authorization handshake, research-only versus production-capable distinction, explicit coexistence/overlap/nesting/precedence semantics for multiple scoped Project Authorizations where applicable, Project-selected-design category exit as handoff to ordinary product/software governance rather than automatic business authorization,',
    'Program 3 claim concurrency',
)

b = replace_exact(
    b,
    'research-only authorization either dead-ends or routinely leaks into production; Project and Organization cannot separate Project-owned technical/design authority from Organization-owned business-outcome/basis authority;',
    'research-only authorization either dead-ends or routinely leaks into production; concurrent scoped Project Authorizations create ambiguous precedence, unreconstructable active authority, or operational complexity that outweighs the claimed control benefit; Project and Organization cannot separate Project-owned technical/design authority from Organization-owned business-outcome/basis authority;',
    'Program 3 falsifier concurrency',
)

b = replace_exact(
    b,
    'that research-only versus production-capable authorization fails, that Project-selected-design category exit as handoff to ordinary product/software governance rather than automatic business authorization is unclear,',
    'that research-only versus production-capable authorization fails, that concurrent scoped authorizations cannot preserve clear scope/precedence and reconstructable active authority, that Project-selected-design category exit as handoff to ordinary product/software governance rather than automatic business authorization is unclear,',
    'Program 3 cross-routing concurrency',
)

# Evidence request must use scoped viability and explicitly request coexistence evidence.
b = replace_exact(
    b,
    '- bounded-research cases showing how an unresolved production-viability question became a **specific** Bounded Research Authorization and then a research-only Project Authorization, whether the research scope remained bounded, what evidence returned, and whether any team attempted or avoided silent promotion into production;',
    '- bounded-research cases showing how an unresolved viability question for a declared experiment or change scope became a **specific** Bounded Research Authorization and then a research-only Project Authorization, whether the research scope remained bounded, what evidence returned, whether any production-capable authorization remained active for another scope, whether coexistence/overlap/nesting/precedence remained unambiguous and reconstructable, and whether any team attempted or avoided silent promotion into production;',
    'Article 8 evidence request scoped research concurrency',
)

b = replace_exact(
    b,
    '- research-only and production-capable Project Authorization, delivery/release, runtime correction, Project Reauthorization, and Organizational review traces;',
    '- research-only and production-capable Project Authorization, including cases with concurrent scoped authorization sets and explicit scope/overlap/nesting/precedence semantics, plus delivery/release, runtime correction, Project Reauthorization, and Organizational review traces;',
    'Article 8 authorization trace evidence',
)

b = replace_exact(
    b,
    '- Can it use research-only authorization to gather missing evidence without either dead-ending or leaking into production?',
    '- Can it use research-only authorization to gather missing evidence without either dead-ending or leaking into production?\n- When research-only and production-capable authorizations coexist, can it keep scope and precedence explicit and reconstruct the authorization set that governed a material event without creating disproportionate operational complexity?',
    'Article 8 transfer question concurrency',
)

b = replace_exact(
    b,
    '- [ ] **Validation Program 3** explicitly tests the assessment-eligibility/Project-viability/Organizational-specific-research/business/basis/scoped-Project-Authorization ownership split, research-only versus production-capable distinction, Project-selected-design category transition, exogenous Organizational routing, and Architectural-Veto/economic-non-viability distinction as paper-level lifecycle hypotheses, alongside evidence/reassessment semantics.',
    '- [ ] **Validation Program 3** explicitly tests the assessment-eligibility/Project-viability/Organizational-specific-research/business/basis/scoped-Project-Authorization ownership split, research-only versus production-capable distinction, concurrent scoped-authorization separation/overlap/nesting/precedence semantics where applicable, Project-selected-design category transition, exogenous Organizational routing, and Architectural-Veto/economic-non-viability distinction as paper-level lifecycle hypotheses, alongside evidence/reassessment semantics.',
    'Program 3 acceptance concurrency',
)

# 2) Figures 12 and 14 must not visually imply mutually exclusive full-system PA states.
m = replace_exact(
    m,
    'PA["Project Authorization<br/> research-only or production-capable<br/> technical baseline + evidence obligations"]',
    'PA["Applicable Project Authorization scope / set<br/> research-only and/or production-capable<br/> explicit scope · precedence · evidence obligations"]',
    'Figure 12 PA node',
)

m = replace_exact(
    m,
    'RA["Research-only Project Authorization"]',
    'RA["Research-only Project Authorization<br/>issue · retain · update scoped member"]',
    'Figure 14 research PA node',
)

m = replace_exact(
    m,
    'PA["Production-capable Project Authorization"]',
    'PA["Production-capable Project Authorization<br/>issue · retain · update scoped member"]',
    'Figure 14 production PA node',
)

m = replace_exact(
    m,
    '**Figure 14 — Evidence and change routing.** Local realization defects stay with Delivery. Evidence about architecture, Model-Judgment necessity, capacity, fallback, evidence sufficiency, economics, or the result of a bounded experiment first returns to Project / Architecture because Project owns the viability analysis. A requested authority expansion also reaches Organization through Project analysis when an Organizational boundary must change. **Exogenous** authoritative or business-basis changes originate outside the Delivery/Runtime evidence lane and activate Organization directly; Project then reassesses technical consequences where the active baseline is affected. This avoids both escalation theater and false causality.',
    '**Figure 14 — Evidence and change routing.** Local realization defects stay with Delivery. Evidence about architecture, Model-Judgment necessity, capacity, fallback, evidence sufficiency, economics, or the result of a bounded experiment first returns to Project / Architecture because Project owns the viability analysis. The research-only and production-capable branches show which scoped authorization member Project may issue, retain, or update after reassessment; they are not mutually exclusive full-system states when an explicitly separated or nested authorization set is active. A requested authority expansion also reaches Organization through Project analysis when an Organizational boundary must change. **Exogenous** authoritative or business-basis changes originate outside the Delivery/Runtime evidence lane and activate Organization directly; Project then reassesses technical consequences where the active baseline is affected. This avoids both escalation theater and false causality.',
    'Figure 14 caption coexistence',
)

# 3) Changelog should record the final concurrency/precedence hypothesis explicitly.
c = replace_exact(
    c,
    'Exogenous Organizational authoritative/business changes are treated as direct Organization inputs rather than as Runtime/Delivery evidence. These semantics remain research under validation and do not change status-bearing doctrine or patterns by implication.',
    'Exogenous Organizational authoritative/business changes are treated as direct Organization inputs rather than as Runtime/Delivery evidence. The paper also tests whether multiple scoped Project Authorizations may coexist for disjoint or explicitly overlapping/nested scopes when precedence/interaction is explicit and material evidence can reconstruct the applicable authorization set. These semantics remain research under validation and do not change status-bearing doctrine or patterns by implication.',
    'changelog authorization concurrency',
)

joined = b + '\n' + m + '\n' + c
for obsolete in [
    'unresolved production-viability question became a **specific** Bounded Research Authorization',
    'Project Authorization<br/> research-only or production-capable<br/> technical baseline + evidence obligations',
    'RA["Research-only Project Authorization"]',
    'PA["Production-capable Project Authorization"]',
]:
    if obsolete in joined:
        raise SystemExit('obsolete wording remains: ' + obsolete)

required = [
    'explicit coexistence/overlap/nesting/precedence semantics for multiple scoped Project Authorizations where applicable',
    'concurrent scoped Project Authorizations create ambiguous precedence',
    'unresolved viability question for a declared experiment or change scope',
    'Applicable Project Authorization scope / set',
    'issue · retain · update scoped member',
    'not mutually exclusive full-system states',
    'multiple scoped Project Authorizations may coexist for disjoint or explicitly overlapping/nested scopes',
]
for phrase in required:
    if phrase not in joined:
        raise SystemExit('required wording missing: ' + phrase)

bp.write_text(b)
ms.write_text(m)
cl.write_text(c)
