from pathlib import Path

bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms = Path('content/research/notes/open-engineering-specification-article-draft.md')
tr = Path('content/research/framework-traceability.md')

b = bp.read_text()
m = ms.read_text()
t = tr.read_text()


def replace_exact(text: str, old: str, new: str, label: str, expected: int = 1) -> str:
    count = text.count(old)
    if count != expected:
        raise SystemExit(f'{label}: expected {expected} occurrences, found {count}')
    return text.replace(old, new)

# 1) Research-only authorization is scoped to an unresolved experiment/change question,
# not to the global absence of any production-capable authorization.
m = replace_exact(
    m,
    'A Project Authorization may be **research-only** after a specific Organizational Bounded Research Authorization when the open question is precisely whether production viability can be demonstrated, or **production-capable** after a positive Organizational Business Authorization covers a technically viable production basis.',
    'A Project Authorization may be **research-only** after a specific Organizational Bounded Research Authorization when the experiment addresses an unresolved viability question for its declared scope, or **production-capable** after a positive Organizational Business Authorization covers a technically viable production basis.',
    'manuscript opening PA distinction',
)

m = replace_exact(
    m,
    'Organization may then issue one of two different positive authorizations: a **specific Bounded Research Authorization** when production viability remains unresolved and Project has defined a credibly bounded experiment that crosses an Organizationally reserved boundary, or an **Organizational Business Authorization** when a technically viable production basis exists and the organization chooses to pursue it.',
    'Organization may then issue one of two different positive authorizations: a **specific Bounded Research Authorization** when viability for the proposed experiment or change scope remains unresolved and Project has defined a credibly bounded experiment that crosses an Organizationally reserved boundary, or an **Organizational Business Authorization** when a technically viable production basis exists and the organization chooses to pursue it.',
    'manuscript Organization positive authorization scope',
)

m = replace_exact(
    m,
    '- **further research required** — production viability remains open, but a bounded research envelope may be technically authorizable;',
    '- **further research required** — viability for the proposed scope or change remains open, but a bounded research envelope may be technically authorizable;',
    'manuscript viability vocabulary scope',
)

b = replace_exact(
    b,
    '**Research-only Project Authorization** may follow only that specific Bounded Research Authorization while production viability remains open, provided the experiment itself has a credible bounded control envelope.',
    '**Research-only Project Authorization** may follow only that specific Bounded Research Authorization while viability for the declared experiment or change scope remains unresolved, provided the experiment itself has a credible bounded control envelope.',
    'blueprint lifecycle refinement research-only scope',
)

b = replace_exact(
    b,
    '→ Project Authorization is a scoped technical baseline: research-only after a specific Bounded Research Authorization when production viability is still open, or production-capable after a positive Organizational Business Authorization on a technically viable production basis',
    '→ Project Authorization is a scoped technical baseline: research-only after a specific Bounded Research Authorization when the declared experiment or change scope has an unresolved viability question, or production-capable after a positive Organizational Business Authorization on a technically viable production basis',
    'blueprint connected argument research-only scope',
)

b = replace_exact(
    b,
    '- Distinguish **research-only** Project Authorization from **production-capable** Project Authorization. The former follows specific Bounded Research Authorization when production viability is still open; the latter follows positive Organizational Business Authorization on a viable production basis. Neither Delivery nor Runtime may widen the active scope.',
    '- Distinguish **research-only** Project Authorization from **production-capable** Project Authorization. The former follows specific Bounded Research Authorization when the declared experiment or change scope has an unresolved viability question; the latter follows positive Organizational Business Authorization on a viable production basis. A research-only authorization may coexist with an active production-capable authorization only under explicit scope separation or overlap/nesting/precedence semantics. Neither Delivery nor Runtime may widen the active scope.',
    'blueprint accepted drafting decision research-only scope',
)

# 2) Extend traceability so concurrent scoped Project Authorizations are explicitly part
# of the research hypothesis rather than silently contradicting the one-baseline doctrine/pattern.
old_row = '| Project technical/design selection and viability versus Organizational business/research authority | Current status-bearing Nested Control Lifecycle doctrine and Project Control Architecture and Viability Review pattern both place business outcome, project authorization, bounded research, deferral/No-Go, or closely related decision ownership on the Project surface and do not yet express the paper\'s explicit assessment-eligibility versus specific bounded-research distinction | Article research hypothesis assigns Model-Judgment necessity, technical/design selection inside the standing Organizational business/authority basis, category confirmation, and viability to Project / Architecture; initial Organizational assessment eligibility permits Project-local analysis and evidence generation inside the standing envelope but does not authorize reserved exposure; a specific Bounded Research Authorization is required when a Project-defined experiment crosses an Organizationally owned exposure/authority/data/material-commitment boundary; Organization also owns the business outcome/basis plus proceed/continue/reshape/defer/do-not-proceed decisions; scoped Project Authorization is research-only for specifically authorized bounded research before production viability is established or production-capable after positive Organizational Business Authorization on a viable basis | Needs Resolution | Do not change doctrine/pattern ownership by implication. Validate the boundary—including Project-owned simpler-design selection inside the standing basis, assessment eligibility versus specific reserved-exposure research authorization, and research-only versus production-capable Project Authorization—then deliberately accept, narrow, reject, or otherwise reconcile it through framework review across both the Nested Control Lifecycle doctrine and affected Project pattern(s) before status-bearing sources change. |'
new_row = '| Project technical/design selection and viability versus Organizational business/research authority | Current status-bearing Nested Control Lifecycle doctrine and Project Control Architecture and Viability Review pattern both place business outcome, project authorization, bounded research, deferral/No-Go, or closely related decision ownership on the Project surface, do not yet express the paper\'s explicit assessment-eligibility versus specific bounded-research distinction, and describe one versioned project authorization/baseline rather than concurrent scoped Project Authorizations | Article research hypothesis assigns Model-Judgment necessity, technical/design selection inside the standing Organizational business/authority basis, category confirmation, and viability to Project / Architecture; initial Organizational assessment eligibility permits Project-local analysis and evidence generation inside the standing envelope but does not authorize reserved exposure; a specific Bounded Research Authorization is required when a Project-defined experiment crosses an Organizationally owned exposure/authority/data/material-commitment boundary; Organization also owns the business outcome/basis plus proceed/continue/reshape/defer/do-not-proceed decisions; scoped Project Authorization is research-only when the declared experiment/change scope has an unresolved viability question or production-capable after positive Organizational Business Authorization on a viable basis; multiple scoped Project Authorizations may coexist only for disjoint scopes or with explicit overlap/nesting and precedence/interaction semantics, and material evidence must identify the applicable authorization set | Needs Resolution | Do not change doctrine/pattern ownership by implication. Validate the boundary—including Project-owned simpler-design selection inside the standing basis, assessment eligibility versus specific reserved-exposure research authorization, research-only versus production-capable Project Authorization, and whether multiple scoped authorizations with explicit separation/overlap/precedence improve or complicate lifecycle control—then deliberately accept, narrow, reject, or otherwise reconcile it through framework review across both the Nested Control Lifecycle doctrine and affected Project pattern(s) before status-bearing sources change. |'
t = replace_exact(t, old_row, new_row, 'traceability lifecycle authorization row')

t = replace_exact(
    t,
    '- Project technical/design selection and viability / Organizational business-basis and research authorization / research-only versus production-capable Project Authorization reconciliation;',
    '- Project technical/design selection and viability / Organizational business-basis and research authorization / research-only versus production-capable Project Authorization / concurrent scoped-authorization and precedence reconciliation;',
    'traceability remaining topic',
)

# Guards for the exact findings.
joined = b + '\n' + m + '\n' + t
for obsolete in [
    'when the open question is precisely whether production viability can be demonstrated',
    'when production viability remains unresolved and Project has defined a credibly bounded experiment',
    '**further research required** — production viability remains open',
    'while production viability remains open, provided the experiment itself has a credible bounded control envelope',
    'research-only after a specific Bounded Research Authorization when production viability is still open',
    'before production viability is established or production-capable',
]:
    if obsolete in joined:
        raise SystemExit('obsolete wording remains: ' + obsolete)

required = [
    'unresolved viability question for its declared scope',
    'viability for the proposed experiment or change scope remains unresolved',
    'viability for the proposed scope or change remains open',
    'declared experiment or change scope has an unresolved viability question',
    'one versioned project authorization/baseline rather than concurrent scoped Project Authorizations',
    'multiple scoped Project Authorizations may coexist only for disjoint scopes or with explicit overlap/nesting and precedence/interaction semantics',
    'concurrent scoped-authorization and precedence reconciliation',
]
for phrase in required:
    if phrase not in joined:
        raise SystemExit('required wording missing: ' + phrase)

bp.write_text(b)
ms.write_text(m)
tr.write_text(t)
