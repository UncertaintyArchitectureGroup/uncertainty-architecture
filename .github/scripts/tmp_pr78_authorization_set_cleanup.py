from pathlib import Path

bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms = Path('content/research/notes/open-engineering-specification-article-draft.md')

b = bp.read_text()
m = ms.read_text()


def replace_exact(text: str, old: str, new: str, label: str, expected: int = 1) -> str:
    count = text.count(old)
    if count != expected:
        raise SystemExit(f'{label}: expected {expected} occurrences, found {count}')
    return text.replace(old, new)

# 1) Make coexistence/precedence semantics explicit for recurrent research on an active production basis.
m = replace_exact(
    m,
    'Both are technical authorizations. Neither is the Organizational decision itself, and research-only authorization does not silently mature into production permission.',
    'Both are technical authorizations. Neither is the Organizational decision itself, and research-only authorization does not silently mature into production permission. Multiple Project Authorizations may coexist only when their scopes are disjoint or when any overlap or nesting is explicit. A research-only Project Authorization does not supersede an active production-capable Project Authorization outside the declared experiment scope unless the authorization explicitly says so; material evidence must identify the applicable authorization set, scope relationship, and precedence or interaction well enough to reconstruct which authorization governed the event.',
    'manuscript authorization coexistence rule',
)

b = replace_exact(
    b,
    'For the first research cycle, the standing basis may be only initial assessment eligibility; later cycles may begin from an existing research or production basis that new evidence has caused Project to reassess.',
    'For the first research cycle, the standing basis may be only initial assessment eligibility; later cycles may begin from an existing research or production basis that new evidence has caused Project to reassess. When a research-only Project Authorization is introduced while a production-capable Project Authorization remains active elsewhere, the authorizations may coexist only through explicit scope separation or an explicit overlap/nesting rule. The research-only authorization does not supersede production scope outside the declared experiment unless that effect is stated explicitly, and material evidence must remain attributable to the applicable authorization set and its scope/precedence relationship.',
    'blueprint recurrent authorization coexistence rule',
)

b = replace_exact(
    b,
    '- **source/authorization baseline** — Organizational business/authority decision, Project Authorization type/scope, authoritative source references, and other standing decisions used by the mapping;',
    '- **source/authorization baseline** — Organizational business/authority decision, the applicable Project Authorization set (type, scope, and any overlap/nesting or precedence relationship), authoritative source references, and other standing decisions used by the mapping;',
    'mapping header authorization set',
)

# 2) Remove generic Organization-facing bounded-research shorthand from high-salience manuscript summaries/figures.
m = replace_exact(
    m,
    'Organization owns the business outcome and authoritative/investment basis plus the business decision to authorize specific bounded research, proceed with a viable production initiative, reshape that basis, defer, or stop;',
    'Organization owns the business outcome and authoritative/investment basis plus the business decision to authorize specific bounded research when the proposed experiment crosses an Organizationally reserved boundary, proceed with a viable production initiative, reshape that basis, defer, or stop;',
    'Section 4 opening research authority summary',
)

m = replace_exact(
    m,
    '- **Organization** owns authoritative boundaries, reserved decision rights, shared capabilities, exceptions, and business authority over whether the initiative should proceed, be reshaped, receive a specific bounded-research authorization, be deferred, or stop.',
    '- **Organization** owns authoritative boundaries, reserved decision rights, shared capabilities, exceptions, and business authority over whether the initiative should proceed, be reshaped, receive a specific Bounded Research Authorization for reserved-boundary research, be deferred, or stop.',
    'Section 4 Organization bullet research label',
)

m = replace_exact(
    m,
    'Organization is reactivated only when Project evidence requires a specific bounded-research decision, Business Authorization for a viable production basis, a changed Organizationally owned premise, or a continuation/defer/stop decision.',
    'Organization is reactivated only when Project evidence requires a specific reserved-boundary research decision, Business Authorization for a viable production basis, a changed Organizationally owned premise, or a continuation/defer/stop decision.',
    'Figure 8 caption research label',
)

m = replace_exact(
    m,
    'Organization is reactivated only when its business/authority/investment basis or an initiative-level research/continuation decision is implicated;',
    'Organization is reactivated only when its business/authority/investment basis or an initiative-level reserved-boundary research/continuation decision is implicated;',
    'Figure 9 caption research label',
)

m = replace_exact(
    m,
    '**Question owned:** Within which authoritative boundaries may Project / Architecture assessment proceed—and, when a Project finding implicates an Organizationally owned basis or initiative-level decision, should the organization authorize specific bounded research, proceed with a viable production initiative, reshape it, defer it, or stop it?',
    '**Question owned:** Within which authoritative boundaries may Project / Architecture assessment proceed—and, when a Project finding implicates an Organizationally owned basis or initiative-level decision, should the organization authorize specific bounded research that crosses an Organizationally reserved boundary, proceed with a viable production initiative, reshape it, defer it, or stop it?',
    'Organization owned question research label',
)

m = replace_exact(
    m,
    'Organization may then issue one of two different positive authorizations: a **specific Bounded Research Authorization** when production viability remains unresolved but Project has defined a credibly bounded experiment, or an **Organizational Business Authorization** when a technically viable production basis exists and the organization chooses to pursue it.',
    'Organization may then issue one of two different positive authorizations: a **specific Bounded Research Authorization** when production viability remains unresolved and Project has defined a credibly bounded experiment that crosses an Organizationally reserved boundary, or an **Organizational Business Authorization** when a technically viable production basis exists and the organization chooses to pursue it.',
    'Organization positive authorization qualification',
)

m = replace_exact(
    m,
    'D["Organizational decision<br/> assessment eligibility · bounded research · proceed<br/> reshape · defer · do not proceed"]',
    'D["Organizational decision<br/> assessment eligibility · reserved-boundary research · proceed<br/> reshape · defer · do not proceed"]',
    'Figure 10 decision node research label',
)

m = replace_exact(
    m,
    'OD["Organization<br/> specific bounded research · proceed / continue<br/> reshape business / authority basis · defer · do not proceed"]',
    'OD["Organization<br/> reserved-boundary research · proceed / continue<br/> reshape business / authority basis · defer · do not proceed"]',
    'Figure 11 Organization node research label',
)

m = replace_exact(
    m,
    'Organizational action is required when Project requests a specific bounded experiment, presents a viable production basis that needs Business Authorization, finds that economics or another Organizational premise must change, raises an Architectural Veto that can only be addressed by changing the proposal, or needs an initiative-level continue/defer/stop decision.',
    'Organizational action is required when Project requests reserved-boundary bounded research, presents a viable production basis that needs Business Authorization, finds that economics or another Organizational premise must change, raises an Architectural Veto that can only be addressed by changing the proposal, or needs an initiative-level continue/defer/stop decision.',
    'Project output research activation qualification',
)

m = replace_exact(
    m,
    '| **Organization** | May this business initiative be assessed, receive a specific bounded-research authorization, or pursue bounded automated refund authority—and under which authoritative/business assumptions?',
    '| **Organization** | May this business initiative be assessed, receive a specific Bounded Research Authorization for reserved-boundary research, or pursue bounded automated refund authority—and under which authoritative/business assumptions?',
    'running example Organization question label',
)

# Blueprint high-salience Organization wording.
b = replace_exact(
    b,
    '- a Project viability conclusion requiring a proceed/continuation, reshape of an Organizational premise, specific bounded research, or do-not-proceed decision;',
    '- a Project viability conclusion requiring a proceed/continuation, reshape of an Organizational premise, specific reserved-boundary research, or do-not-proceed decision;',
    'blueprint Organization activation research label',
)

# Guard exact defects from this review.
joined = b + '\n' + m
for obsolete in [
    'Organization is reactivated only when Project evidence requires a specific bounded-research decision',
    'assessment eligibility · bounded research · proceed',
    'Organization<br/> specific bounded research · proceed / continue',
    'Organization owns the business outcome and authoritative/investment basis plus the business decision to authorize specific bounded research, proceed',
    'Project requests a specific bounded experiment, presents a viable production basis',
    'Project Authorization type/scope, authoritative source references',
]:
    if obsolete in joined:
        raise SystemExit('obsolete wording remains: ' + obsolete)

required = [
    'Multiple Project Authorizations may coexist only when their scopes are disjoint or when any overlap or nesting is explicit.',
    'applicable authorization set, scope relationship, and precedence or interaction',
    'applicable Project Authorization set (type, scope, and any overlap/nesting or precedence relationship)',
    'specific reserved-boundary research decision',
    'reserved-boundary research · proceed',
    'reserved-boundary bounded research',
    'specific Bounded Research Authorization for reserved-boundary research',
]
for phrase in required:
    if phrase not in joined:
        raise SystemExit('required wording missing: ' + phrase)

bp.write_text(b)
ms.write_text(m)
