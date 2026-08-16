from pathlib import Path

trace = Path('content/research/framework-traceability.md')
bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')

t = trace.read_text()
b = bp.read_text()


def replace_exact(text: str, old: str, new: str, label: str, expected: int = 1) -> str:
    count = text.count(old)
    if count != expected:
        raise SystemExit(f'{label}: expected {expected} occurrences, found {count}')
    return text.replace(old, new)

# 1) Traceability: make Business Authorization coverage part of the explicit lifecycle hypothesis.
t = replace_exact(
    t,
    'scoped Project Authorization is research-only when the declared experiment/change scope has an unresolved viability question or production-capable after positive Organizational Business Authorization on a viable basis; multiple scoped Project Authorizations may coexist only for disjoint scopes or with explicit overlap/nesting and precedence/interaction semantics, and material evidence must identify the applicable authorization set',
    'scoped Project Authorization is research-only when the declared experiment/change scope has an unresolved viability question or production-capable after positive Organizational Business Authorization on a viable basis; Project-only production reauthorization is permitted only while the resulting production scope remains covered by the applicable existing Organizational Business Authorization, otherwise Organization must renew, reshape, or explicitly change that Business Authorization before Project issues the corresponding production-capable baseline; multiple scoped Project Authorizations may coexist only for disjoint scopes or with explicit overlap/nesting and precedence/interaction semantics, and material evidence must identify the applicable authorization set',
    'traceability hypothesis BA coverage',
)

t = replace_exact(
    t,
    'assessment eligibility versus specific reserved-exposure research authorization, research-only versus production-capable Project Authorization, and whether multiple scoped authorizations with explicit separation/overlap/precedence improve or complicate lifecycle control',
    'assessment eligibility versus specific reserved-exposure research authorization, research-only versus production-capable Project Authorization, whether Project-only production reauthorization should remain limited to scope covered by the applicable existing Organizational Business Authorization, and whether multiple scoped authorizations with explicit separation/overlap/precedence improve or complicate lifecycle control',
    'traceability resolution BA coverage',
)

t = replace_exact(
    t,
    '- Project technical/design selection and viability / Organizational business-basis and research authorization / research-only versus production-capable Project Authorization / concurrent scoped-authorization and precedence reconciliation;',
    '- Project technical/design selection and viability / Organizational business-basis and research authorization / research-only versus production-capable Project Authorization / production-reauthorization Business-Authorization coverage / concurrent scoped-authorization and precedence reconciliation;',
    'traceability remaining topic BA coverage',
)

# 2) Validation Program 3: test the coverage boundary rather than silently assuming it.
b = replace_exact(
    b,
    'the assessment-eligibility → Project viability conclusion → Organizational specific-bounded-research/business/changed-basis decision → scoped Project Authorization handshake, research-only versus production-capable distinction, explicit coexistence/overlap/nesting/precedence semantics for multiple scoped Project Authorizations where applicable,',
    'the assessment-eligibility → Project viability conclusion → Organizational specific-bounded-research/business/changed-basis decision → scoped Project Authorization handshake, research-only versus production-capable distinction, the rule that Project-only production reauthorization remains inside the coverage of the applicable existing Organizational Business Authorization, explicit coexistence/overlap/nesting/precedence semantics for multiple scoped Project Authorizations where applicable,',
    'Program 3 claim BA coverage',
)

b = replace_exact(
    b,
    'teams cannot distinguish assessment eligibility from authorization for experiment exposure that crosses an Organizationally reserved boundary; research-only authorization either dead-ends or routinely leaks into production; concurrent scoped Project Authorizations create ambiguous precedence, unreconstructable active authority, or operational complexity that outweighs the claimed control benefit;',
    'teams cannot distinguish assessment eligibility from authorization for experiment exposure that crosses an Organizationally reserved boundary; research-only authorization either dead-ends or routinely leaks into production; teams cannot reliably distinguish a technical production change still covered by the applicable existing Organizational Business Authorization from a scope change that requires renewed/reshaped Business Authorization, or the coverage rule causes systematic over-escalation or authority ambiguity; concurrent scoped Project Authorizations create ambiguous precedence, unreconstructable active authority, or operational complexity that outweighs the claimed control benefit;',
    'Program 3 falsifier BA coverage',
)

# 3) Cross-program routing: classify BA-coverage ambiguity as lifecycle evidence, not learning failure.
b = replace_exact(
    b,
    'that research-only versus production-capable authorization fails, that concurrent scoped authorizations cannot preserve clear scope/precedence and reconstructable active authority,',
    'that research-only versus production-capable authorization fails, that teams cannot determine whether a changed production scope is still covered by the applicable existing Organizational Business Authorization or requires renewed Organizational authorization, that concurrent scoped authorizations cannot preserve clear scope/precedence and reconstructable active authority,',
    'cross-program routing BA coverage',
)

# 4) §8.2: explicitly request positive and negative cases for the coverage boundary.
anchor = '- examples showing that authority/scope differences can or cannot be distinguished cleanly from lifecycle maturity in comparative application;\n'
insert = anchor + '- production-reassessment cases where a changed technical design remained covered by the applicable existing Organizational Business Authorization and Project reauthorized locally, alongside cases where the resulting production scope exceeded that coverage and required renewed/reshaped Organizational Business Authorization;\n'
if b.count(anchor) != 1:
    raise SystemExit(f'§8.2 evidence anchor: expected 1 occurrence, found {b.count(anchor)}')
b = b.replace(anchor, insert)

# 5) Blueprint acceptance contract for Program 3 must name the same subclaim.
b = replace_exact(
    b,
    '- [ ] **Validation Program 3** explicitly tests the assessment-eligibility/Project-viability/Organizational-specific-research/business/basis/scoped-Project-Authorization ownership split, research-only versus production-capable distinction, concurrent scoped-authorization separation/overlap/nesting/precedence semantics where applicable, Project-selected-design category transition, exogenous Organizational routing, and Architectural-Veto/economic-non-viability distinction as paper-level lifecycle hypotheses, alongside evidence/reassessment semantics.',
    '- [ ] **Validation Program 3** explicitly tests the assessment-eligibility/Project-viability/Organizational-specific-research/business/basis/scoped-Project-Authorization ownership split, research-only versus production-capable distinction, Project-only production reauthorization only while the resulting production scope remains covered by the applicable existing Organizational Business Authorization, concurrent scoped-authorization separation/overlap/nesting/precedence semantics where applicable, Project-selected-design category transition, exogenous Organizational routing, and Architectural-Veto/economic-non-viability distinction as paper-level lifecycle hypotheses, alongside evidence/reassessment semantics.',
    'Program 3 acceptance BA coverage',
)

# Tight guards.
joined = t + '\n' + b
required = [
    'Project-only production reauthorization is permitted only while the resulting production scope remains covered by the applicable existing Organizational Business Authorization',
    'whether Project-only production reauthorization should remain limited to scope covered by the applicable existing Organizational Business Authorization',
    'production-reauthorization Business-Authorization coverage',
    'the rule that Project-only production reauthorization remains inside the coverage of the applicable existing Organizational Business Authorization',
    'teams cannot reliably distinguish a technical production change still covered by the applicable existing Organizational Business Authorization',
    'changed production scope is still covered by the applicable existing Organizational Business Authorization or requires renewed Organizational authorization',
    'production-reassessment cases where a changed technical design remained covered by the applicable existing Organizational Business Authorization',
    'Project-only production reauthorization only while the resulting production scope remains covered by the applicable existing Organizational Business Authorization',
]
for phrase in required:
    if phrase not in joined:
        raise SystemExit('required wording missing: ' + phrase)

trace.write_text(t)
bp.write_text(b)
