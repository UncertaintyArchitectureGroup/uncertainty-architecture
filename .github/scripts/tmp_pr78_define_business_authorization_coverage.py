from pathlib import Path

bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms = Path('content/research/notes/open-engineering-specification-article-draft.md')
trace = Path('content/research/framework-traceability.md')
cl = Path('CHANGELOG.md')

b = bp.read_text()
m = ms.read_text()
t = trace.read_text()
c = cl.read_text()


def replace_exact(text: str, old: str, new: str, label: str, expected: int = 1) -> str:
    count = text.count(old)
    if count != expected:
        raise SystemExit(f'{label}: expected {expected} occurrences, found {count}')
    return text.replace(old, new)

# 1) Manuscript §4: define what Organizational Business Authorization coverage means
# without turning Organization into the technical architecture owner.
anchor = (
    'The same Organizational horizon may also be reactivated directly by exogenous authoritative or business-basis changes, without a preceding Project finding.\n\n'
    'A specific Bounded Research Authorization is therefore downstream of Project\'s experiment design'
)
insert = (
    'The same Organizational horizon may also be reactivated directly by exogenous authoritative or business-basis changes, without a preceding Project finding.\n\n'
    'For this paper, **coverage of an Organizational Business Authorization** means the Organizationally owned production envelope against which a later production change is judged: the authorized business outcome or use scope; any population, environment, or external-exposure bounds owned at that horizon; reserved or delegated authority; data, geography, vendor, deployment, or similar restrictions **when they are explicit Organizational premises or conditions**; material service, value, or investment assumptions; and any explicit conditions that require a renewed Organizational decision. It does **not** freeze a model, prompt, routing topology, tool, implementation mechanism, vendor, or other technical design choice merely because it appeared in the viable basis; such choices remain Project / Architecture-owned unless that specific choice is itself an explicit Organizational condition. A technical redesign that remains inside this envelope may therefore be reauthorized by Project after viability reassessment; a change that crosses the envelope requires renewed, reshaped, or otherwise explicit Organizational Business Authorization before the corresponding production-capable technical baseline is issued.\n\n'
    'A specific Bounded Research Authorization is therefore downstream of Project\'s experiment design'
)
if m.count(anchor) != 1:
    raise SystemExit(f'manuscript BA coverage definition anchor: expected 1, found {m.count(anchor)}')
m = m.replace(anchor, insert)

# 2) Blueprint §4: make the same decision-boundary definition an explicit editorial invariant.
anchor = (
    'Until this exact sequencing is separately reconciled into authority-bearing lifecycle/pattern sources through framework review, describe it as a paper-level lifecycle refinement under validation rather than silently claiming that current normative wording already says the same thing.\n\n'
    '#### Common operating-frame rule for all four levels'
)
insert = (
    'Until this exact sequencing is separately reconciled into authority-bearing lifecycle/pattern sources through framework review, describe it as a paper-level lifecycle refinement under validation rather than silently claiming that current normative wording already says the same thing.\n\n'
    '**Business-Authorization coverage rule.** In this paper, coverage of an Organizational Business Authorization is the Organizationally owned production envelope, not a freeze on Project-owned architecture. At minimum, when material, that envelope may include the authorized business outcome/use scope; Organization-owned population/environment/external-exposure bounds; reserved/delegated authority; data, geography, vendor, deployment, or similar restrictions when they are explicit Organizational premises or conditions; material service/value/investment assumptions; and explicit conditions that require renewed Organizational decision. Model, prompt, routing topology, tool, implementation mechanism, vendor, and other technical realization choices remain Project / Architecture-owned unless a specific choice is itself an explicit Organizational condition. Project-only production reauthorization is therefore local only when the resulting production scope remains inside this Organizationally owned envelope after viability reassessment.\n\n'
    '#### Common operating-frame rule for all four levels'
)
if b.count(anchor) != 1:
    raise SystemExit(f'blueprint §4 BA coverage rule anchor: expected 1, found {b.count(anchor)}')
b = b.replace(anchor, insert)

# 3) Future-section ownership must preserve this distinction.
b = replace_exact(
    b,
    '**Project Authorization as a scoped technical baseline with research-only and production-capable forms, including explicit applicable-authorization-set scope/overlap/nesting/precedence semantics where multiple authorizations coexist**, the distinction between initial assessment eligibility',
    '**Project Authorization as a scoped technical baseline with research-only and production-capable forms, including explicit applicable-authorization-set scope/overlap/nesting/precedence semantics where multiple authorizations coexist**, the production-reauthorization rule that Project-only technical reauthorization remains local only while the resulting production scope stays inside the applicable existing Organizational Business Authorization\'s Organizationally owned coverage envelope rather than merely preserving a specific technical architecture, the distinction between initial assessment eligibility',
    'future-section ownership BA coverage definition',
)

# 4) §4 acceptance must protect the authority boundary explicitly.
b = replace_exact(
    b,
    '- [ ] A **production-capable Project Authorization** is issued only for a technically viable production basis covered by a positive Organizational Business Authorization.',
    '- [ ] A **production-capable Project Authorization** is issued only for a technically viable production basis covered by a positive Organizational Business Authorization.\n- [ ] **Organizational Business Authorization coverage** is defined over Organizationally owned business/authority/exposure/condition dimensions and explicit renewal conditions; it does not freeze Project-owned technical design choices unless a specific technical choice was explicitly made part of the Organizational authorization basis.',
    '§4 acceptance BA coverage definition',
)

# 5) §7 maturity/boundary summaries must name the new paper-only semantic explicitly.
b = replace_exact(
    b,
    '- the assessment-eligibility / Project-viability / Project technical/design selection plus Organizational business/basis/specific-research/continuation decisions where required / scoped-Project-Authorization handshake, research-only versus production-capable distinction, Project-selected-design category-exit rule, direct exogenous-Organization routing, and Architectural-Veto/economic-non-viability distinction are paper-level lifecycle refinements not yet reconciled into current authority-bearing lifecycle/pattern sources; `framework-traceability.md` records the question as **Needs Resolution**;',
    '- the assessment-eligibility / Project-viability / Project technical/design selection plus Organizational business/basis/specific-research/continuation decisions where required / scoped-Project-Authorization handshake, research-only versus production-capable distinction, the Business-Authorization coverage rule for Project-only production reauthorization—including that coverage is an Organizationally owned envelope rather than a technical-architecture freeze—, Project-selected-design category-exit rule, direct exogenous-Organization routing, and Architectural-Veto/economic-non-viability distinction are paper-level lifecycle refinements not yet reconciled into current authority-bearing lifecycle/pattern sources; `framework-traceability.md` records the question as **Needs Resolution**;',
    '§7 maturity summary BA coverage',
)

b = replace_exact(
    b,
    'The exact assessment-eligibility / Project-viability / Organizational-specific-research/business/basis / scoped-Project-Authorization handshake remains paper-level research until framework reconciliation changes those status-bearing surfaces.',
    'The exact assessment-eligibility / Project-viability / Organizational-specific-research/business/basis / scoped-Project-Authorization handshake—including the Business-Authorization coverage rule for Project-only production reauthorization and the distinction between Organizationally owned coverage conditions and Project-owned technical design—remains paper-level research until framework reconciliation changes those status-bearing surfaces.',
    '§7 repository boundary BA coverage',
)

b = replace_exact(
    b,
    '- [ ] **Article §7** states the proposed contribution as a paper-level synthesis/recomposition, separates the existing specification boundary from the assessment-eligibility/Project-viability/Organizational-business-basis-specific-research-continuation-where-required/scoped-Project-Authorization refinement and other paper-only carrier/substitution/reverse-mapping/integration-gap hypotheses, defines what UA is and is not, and requires explicit framework review plus a corresponding status-bearing change before research can alter the specification.',
    '- [ ] **Article §7** states the proposed contribution as a paper-level synthesis/recomposition, separates the existing specification boundary from the assessment-eligibility/Project-viability/Organizational-business-basis-specific-research-continuation-where-required/scoped-Project-Authorization refinement—including the Business-Authorization coverage rule for Project-only production reauthorization and its Organizational-envelope-versus-technical-design distinction—and other paper-only carrier/substitution/reverse-mapping/integration-gap hypotheses, defines what UA is and is not, and requires explicit framework review plus a corresponding status-bearing change before research can alter the specification.',
    '§7 acceptance BA coverage',
)

# 6) Traceability: define coverage as an Organizational decision envelope, not architecture approval.
t = replace_exact(
    t,
    'Project-only production reauthorization is permitted only while the resulting production scope remains covered by the applicable existing Organizational Business Authorization, otherwise Organization must renew, reshape, or explicitly change that Business Authorization before Project issues the corresponding production-capable baseline; multiple scoped Project Authorizations may coexist only for disjoint scopes or with explicit overlap/nesting and precedence/interaction semantics, and material evidence must identify the applicable authorization set',
    'Project-only production reauthorization is permitted only while the resulting production scope remains covered by the applicable existing Organizational Business Authorization, otherwise Organization must renew, reshape, or explicitly change that Business Authorization before Project issues the corresponding production-capable baseline; for this hypothesis, Business Authorization coverage means the Organizationally owned production envelope—business outcome/use scope, Organization-owned exposure/population/environment bounds, reserved/delegated authority, explicit data/geography/vendor/deployment conditions where Organizationally owned, material service/value/investment assumptions, and explicit renewal conditions—and does not freeze Project-owned technical design choices unless such a choice is itself an explicit Organizational condition; multiple scoped Project Authorizations may coexist only for disjoint scopes or with explicit overlap/nesting and precedence/interaction semantics, and material evidence must identify the applicable authorization set',
    'traceability BA coverage definition',
)

# 7) Changelog: clarify that coverage is not a blanket architecture approval.
c = replace_exact(
    c,
    'Project-only production reauthorization is tested as valid only while the resulting production scope remains covered by the applicable existing Organizational Business Authorization; otherwise renewed/reshaped Organizational authorization is required before the corresponding production-capable technical baseline is issued.',
    'Project-only production reauthorization is tested as valid only while the resulting production scope remains covered by the applicable existing Organizational Business Authorization; otherwise renewed/reshaped Organizational authorization is required before the corresponding production-capable technical baseline is issued. Coverage is the Organizationally owned business/authority/exposure/condition envelope and explicit renewal conditions, not a blanket approval of the specific technical architecture.',
    'CHANGELOG BA coverage definition',
)

joined = '\n'.join([b, m, t, c])
required = [
    'coverage of an Organizational Business Authorization',
    'It does **not** freeze a model, prompt, routing topology, tool, implementation mechanism, vendor, or other technical design choice',
    '**Business-Authorization coverage rule.**',
    'Organizationally owned coverage envelope rather than merely preserving a specific technical architecture',
    '**Organizational Business Authorization coverage** is defined over Organizationally owned business/authority/exposure/condition dimensions',
    'Organizational-envelope-versus-technical-design distinction',
    'does not freeze Project-owned technical design choices unless such a choice is itself an explicit Organizational condition',
    'not a blanket approval of the specific technical architecture',
]
for phrase in required:
    if phrase not in joined:
        raise SystemExit('required wording missing: ' + phrase)

bp.write_text(b)
ms.write_text(m)
trace.write_text(t)
cl.write_text(c)
