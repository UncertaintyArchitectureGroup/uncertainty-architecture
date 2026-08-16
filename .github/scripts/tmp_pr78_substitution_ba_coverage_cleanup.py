from pathlib import Path

bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
cl = Path('CHANGELOG.md')

b = bp.read_text()
c = cl.read_text()


def replace_exact(text: str, old: str, new: str, label: str, expected: int = 1) -> str:
    count = text.count(old)
    if count != expected:
        raise SystemExit(f'{label}: expected {expected} occurrences, found {count}')
    return text.replace(old, new)

# §5: make the Organizational Business Authorization coverage relation explicit in the mapping baseline.
b = replace_exact(
    b,
    '- **source/authorization baseline** — Organizational business/authority decision, the applicable Project Authorization set (type, scope, and any overlap/nesting or precedence relationship), authoritative source references, and other standing decisions used by the mapping;',
    '- **source/authorization baseline** — Organizational business/authority decision, including the scope/coverage of the applicable existing Organizational Business Authorization relevant to any production reauthorization, the applicable Project Authorization set (type, scope, and any overlap/nesting or precedence relationship), authoritative source references, and other standing decisions used by the mapping;',
    '§5 mapping header BA coverage',
)

anchor = '- **change log / supersedes** — what changed from the previous mapping version and why.\n\nDo **not** embed a self-referential repository commit SHA in the mapping header.'
insert = '- **change log / supersedes** — what changed from the previous mapping version and why.\n\nWhen production reauthorization is in scope, the canonical material set must represent the **Business-Authorization coverage → Project production-reauthorization boundary** explicitly: whether the changed production scope remains inside the applicable existing Organizational Business Authorization or requires renewed/reshaped Organizational authorization before Project can issue or update the corresponding production-capable technical baseline. This is a material authority/lifecycle relationship, not merely mapping-header metadata.\n\nDo **not** embed a self-referential repository commit SHA in the mapping header.'
if b.count(anchor) != 1:
    raise SystemExit(f'§5 material relationship insertion: expected 1 anchor, found {b.count(anchor)}')
b = b.replace(anchor, insert)

# §6 core hypothesis: preserve BA-coverage semantics when production reauthorization is material.
b = replace_exact(
    b,
    'Where research authorization is material, semantic equivalence also requires preserving the distinction among initial assessment eligibility, specific bounded evidence-generation authorization, and production permission rather than merely matching labels.',
    'Where research authorization is material, semantic equivalence also requires preserving the distinction among initial assessment eligibility, specific bounded evidence-generation authorization, and production permission rather than merely matching labels. Where production reauthorization is material, semantic equivalence also requires preserving the boundary between Project-owned technical reauthorization that remains inside the applicable existing Organizational Business Authorization and a changed production scope that requires renewed/reshaped Organizational authorization.',
    '§6 core hypothesis BA coverage',
)

# §6 frozen relationship basis: make the coverage relation a required semantic property.
b = replace_exact(
    b,
    '+ viability-decision semantics: Project viability owner/conclusion, Organizational business/basis/research/continuation-decision consumer/options where required, scoped Project Authorization handoff where applicable, and reassessment trigger',
    '+ viability-decision semantics: Project viability owner/conclusion, Organizational business/basis/research/continuation-decision consumer/options where required, scoped Project Authorization handoff where applicable, Business-Authorization coverage boundary for Project-only production reauthorization where applicable, and reassessment trigger',
    '§6 frozen basis BA coverage',
)

# §6 explanatory equivalence paragraph: state the legitimate-equivalent rule explicitly.
b = replace_exact(
    b,
    'If bounded research is part of the tested lifecycle, an equivalent composition must preserve the difference between initial eligibility and specific non-production experiment permission rather than merely call an experiment “approved.” If a simpler technical path is selected, an equivalent composition must preserve Project-level architecture/category authority separately from Organization-level authority over the business outcome and basis.',
    'If bounded research is part of the tested lifecycle, an equivalent composition must preserve the difference between initial eligibility and specific non-production experiment permission rather than merely call an experiment “approved.” If production reauthorization is part of the tested lifecycle, an equivalent composition must preserve the distinction between Project-owned technical reauthorization that remains covered by the applicable existing Organizational Business Authorization and a changed production scope that requires renewed/reshaped Organizational authorization, or preserve a legitimate equivalent authority boundary. If a simpler technical path is selected, an equivalent composition must preserve Project-level architecture/category authority separately from Organization-level authority over the business outcome and basis.',
    '§6 equivalence paragraph BA coverage',
)

# Program 6: include the coverage relationship in the semantic-substitution hypothesis.
b = replace_exact(
    b,
    'including equivalent ownership of technical viability analysis, Organizational business/basis authority, assessment-versus-specific-research authority, bounded-research versus production semantics, technical authorization, category transition where relevant, and reassessment',
    'including equivalent ownership of technical viability analysis, Organizational business/basis authority, assessment-versus-specific-research authority, bounded-research versus production semantics, Business-Authorization coverage for Project-only production reauthorization where applicable, technical authorization, category transition where relevant, and reassessment',
    'Program 6 BA coverage',
)

# §5 acceptance: the canonical mapping must carry the same authority relationship.
b = replace_exact(
    b,
    'the mapping has a stable ID/version, controlled-object/lifecycle baseline, source/Organizational-business/Project-authorization baseline, scope, assumptions, materiality decision rule, guarantee semantics where applicable, and materiality rationales for inclusion/exclusion.',
    'the mapping has a stable ID/version, controlled-object/lifecycle baseline, source/Organizational-business/Project-authorization baseline—including applicable Organizational Business Authorization coverage for production reauthorization where relevant—scope, assumptions, materiality decision rule, guarantee semantics where applicable, and materiality rationales for inclusion/exclusion.',
    '§5 acceptance BA coverage',
)

# §6 acceptance: require the same semantic property in substitute comparisons.
b = replace_exact(
    b,
    'For material viability/economic/research relationships, the frozen semantics include equivalent ownership of technical viability analysis, Organizational business/basis authority, assessment-versus-specific-research authority, scoped technical authorization, Project-selected-design category transition where relevant, and reassessment—not the numerical control burden.',
    'For material viability/economic/research relationships, the frozen semantics include equivalent ownership of technical viability analysis, Organizational business/basis authority, assessment-versus-specific-research authority, applicable Organizational Business Authorization coverage for Project-only production reauthorization where relevant, scoped technical authorization, Project-selected-design category transition where relevant, and reassessment—not the numerical control burden.',
    '§6 acceptance BA coverage',
)

# Changelog: preserve the new authority invariant in the merge-facing record.
old_change = '- Reopened lifecycle-ownership research in the synthesis article and framework traceability. The paper now tests a sharper distinction between initial Organizational **assessment eligibility**; Project-owned Model-Judgment necessity, technical/design selection inside the standing Organizational business/authority basis, bounded-control/economics analysis, category confirmation, and **Project viability conclusion**; Organization-owned business outcome/basis plus **specific Bounded Research Authorization**, production Business Authorization, changed-basis, and initiative-level proceed/reshape/defer/stop decisions; and scoped technical **research-only** versus **production-capable Project Authorization**. A simpler design that still satisfies the standing Organizational basis may be selected and category-tested at Project without a second Organizational architecture approval; Organization is reactivated only when an Organizationally owned premise or initiative-level decision must change. Exogenous Organizational authoritative/business changes are treated as direct Organization inputs rather than as Runtime/Delivery evidence. The paper also tests whether multiple scoped Project Authorizations may coexist for disjoint or explicitly overlapping/nested scopes when precedence/interaction is explicit and material evidence can reconstruct the applicable authorization set. These semantics remain research under validation and do not change status-bearing doctrine or patterns by implication.'
new_change = '- Reopened lifecycle-ownership research in the synthesis article and framework traceability. The paper now tests a sharper distinction between initial Organizational **assessment eligibility**; Project-owned Model-Judgment necessity, technical/design selection inside the standing Organizational business/authority basis, bounded-control/economics analysis, category confirmation, and **Project viability conclusion**; Organization-owned business outcome/basis plus **specific Bounded Research Authorization**, production Business Authorization, changed-basis, and initiative-level proceed/reshape/defer/stop decisions; and scoped technical **research-only** versus **production-capable Project Authorization**. A simpler design that still satisfies the standing Organizational basis may be selected and category-tested at Project without a second Organizational architecture approval; Organization is reactivated only when an Organizationally owned premise or initiative-level decision must change. Exogenous Organizational authoritative/business changes are treated as direct Organization inputs rather than as Runtime/Delivery evidence. Project-only production reauthorization is tested as valid only while the resulting production scope remains covered by the applicable existing Organizational Business Authorization; otherwise renewed/reshaped Organizational authorization is required before the corresponding production-capable technical baseline is issued. The paper also tests whether multiple scoped Project Authorizations may coexist for disjoint or explicitly overlapping/nested scopes when precedence/interaction is explicit and material evidence can reconstruct the applicable authorization set. These semantics remain research under validation and do not change status-bearing doctrine or patterns by implication.'
c = replace_exact(c, old_change, new_change, 'CHANGELOG BA coverage')

joined = b + '\n' + c
required = [
    'Business-Authorization coverage → Project production-reauthorization boundary',
    'Business-Authorization coverage boundary for Project-only production reauthorization where applicable',
    'legitimate equivalent authority boundary',
    'Business-Authorization coverage for Project-only production reauthorization where applicable',
    'including applicable Organizational Business Authorization coverage for production reauthorization where relevant',
    'Project-only production reauthorization is tested as valid only while the resulting production scope remains covered by the applicable existing Organizational Business Authorization',
]
for phrase in required:
    if phrase not in joined:
        raise SystemExit('required wording missing: ' + phrase)

bp.write_text(b)
cl.write_text(c)
