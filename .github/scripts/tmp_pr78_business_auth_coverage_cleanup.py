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

# 1) Production Project Reauthorization must stay inside the applicable existing Organizational Business Authorization.
m = replace_exact(
    m,
    'Project Reauthorization follows the same distinction. If Delivery or Runtime evidence changes the technical design but the proposal remains viable inside the standing Organizational business and authority basis, Project may reassess, select a different technical architecture, apply the category test, and—where the system remains a Thinking System—issue a new production-capable technical baseline without a new business decision.',
    'Project Reauthorization follows the same distinction. If Delivery or Runtime evidence changes the technical design but the proposal remains viable inside the standing Organizational business and authority basis **and the resulting production scope remains covered by the applicable existing Organizational Business Authorization**, Project may reassess, select a different technical architecture, apply the category test, and—where the system remains a Thinking System—issue or update the production-capable technical baseline without a new business decision. If the resulting production scope is no longer covered by that Business Authorization, Organization must renew, reshape, or otherwise explicitly change the business authorization before Project can issue the corresponding production-capable technical baseline.',
    'manuscript Project Reauthorization business-authorization coverage',
)

m = replace_exact(
    m,
    'PR -->|still production-viable inside standing Organizational basis| PA',
    'PR -->|still production-viable and covered by applicable<br/>Organizational Business Authorization| PA',
    'manuscript production reauthorization edge',
    expected=2,
)

# 2) Figure 11 must make clear that research/production branches are scoped members, not mutually exclusive system states.
m = replace_exact(
    m,
    '**Figure 11 — Project technical/design selection, viability conclusion, Organizational business/research decision, category exit, and authorization handshake.** Project / Architecture owns Model-Judgment necessity, alternative-design selection within the standing Organizational business/authority basis, category confirmation, architectural feasibility, control economics, and the Project viability conclusion. A simpler architecture that still satisfies that standing basis may be selected at Project and can exit the Thinking-System-specific lifecycle immediately after a negative category test; that exit is a handoff to ordinary product/software governance, not an Organizational funding, initiative, delivery, or release authorization, and it does not require an Organizational architecture-selection ceremony. Organization is reactivated when a Project conclusion requires a changed business/authority/investment premise, when proposed research crosses an Organizationally reserved boundary, or when the business decision is to proceed, reshape, defer, or stop. Research that stays inside the standing assessment envelope may remain Project-local; research that crosses an Organizationally reserved boundary follows the two-step authorization path: Project defines a controllable experiment, Organization issues a specific Bounded Research Authorization, and Project then issues the research-only technical baseline. Architectural Veto is a Project conclusion; “do not proceed” is an Organizational business decision.',
    '**Figure 11 — Project technical/design selection, viability conclusion, Organizational business/research decision, category exit, and authorization handshake.** Project / Architecture owns Model-Judgment necessity, alternative-design selection within the standing Organizational business/authority basis, category confirmation, architectural feasibility, control economics, and the Project viability conclusion. A simpler architecture that still satisfies that standing basis may be selected at Project and can exit the Thinking-System-specific lifecycle immediately after a negative category test; that exit is a handoff to ordinary product/software governance, not an Organizational funding, initiative, delivery, or release authorization, and it does not require an Organizational architecture-selection ceremony. Organization is reactivated when a Project conclusion requires a changed business/authority/investment premise, when proposed research crosses an Organizationally reserved boundary, or when the business decision is to proceed, reshape, defer, or stop. Research that stays inside the standing assessment envelope may remain Project-local; research that crosses an Organizationally reserved boundary follows the two-step authorization path: Project defines a controllable experiment, Organization issues a specific Bounded Research Authorization, and Project then issues the research-only technical baseline. The research-only and production-capable branches distinguish authorization sources and scoped member types; they are not mutually exclusive full-system states, and such members may coexist only with explicit scope separation or overlap/nesting/precedence semantics. Architectural Veto is a Project conclusion; “do not proceed” is an Organizational business decision.',
    'manuscript Figure 11 caption concurrency',
)

# Keep blueprint operating/acceptance contracts aligned with the same production-coverage invariant.
b = replace_exact(
    b,
    '   → production remains viable inside standing Organizational business/authority basis: production Project Reauthorization',
    '   → production remains viable inside standing Organizational business/authority basis **and remains covered by the applicable existing Organizational Business Authorization**: production Project Reauthorization',
    'blueprint routing production reauthorization coverage',
)

b = replace_exact(
    b,
    '- [ ] Figure 12 distinguishes Release Gate **rework**, **terminal stop/defer/reject**, and **Project viability reassessment**; it releases only inside the applicable Project Authorization scope or explicitly defined authorization set, never promotes research-only authorization into production, and does not bypass Project / Architecture to Organization. Project may reauthorize locally when the basis remains viable inside standing Organizational authorization; Organization is reached when an Organizational business/authority/investment basis or continuation decision is implicated, Architectural Veto requires a changed proposal, new specific research permission is needed, or wider Organizational change is implicated.',
    '- [ ] Figure 12 distinguishes Release Gate **rework**, **terminal stop/defer/reject**, and **Project viability reassessment**; it releases only inside the applicable Project Authorization scope or explicitly defined authorization set, never promotes research-only authorization into production, and does not bypass Project / Architecture to Organization. Project may reauthorize a production-capable technical baseline locally only when the resulting production scope remains technically viable inside the standing Organizational basis **and remains covered by the applicable existing Organizational Business Authorization**; otherwise Organization must renew, reshape, or explicitly change the relevant business authorization before Project issues the corresponding production-capable baseline. Organization is also reached when an Organizational business/authority/investment basis or continuation decision is implicated, Architectural Veto requires a changed proposal, new specific research permission is needed, or wider Organizational change is implicated.',
    'blueprint Figure 12 acceptance business-authorization coverage',
)

# Figure 11 blueprint contract should also teach scoped-member coexistence.
b = replace_exact(
    b,
    '           ├→ specific Bounded Research Authorization → research-only Project Authorization → Delivery experiment → evidence → Project viability reassessment\n           ├→ changed basis → Project / Architecture reassessment\n           └→ positive Business Authorization on viable production basis → production-capable Project Authorization → Delivery',
    '           ├→ specific Bounded Research Authorization → research-only Project Authorization → Delivery experiment → evidence → Project viability reassessment\n           ├→ changed basis → Project / Architecture reassessment\n           └→ positive Business Authorization on viable production basis → production-capable Project Authorization → Delivery\n           (research-only and production-capable branches are scoped member types, not mutually exclusive full-system states; coexistence requires explicit scope/overlap/nesting/precedence semantics)',
    'blueprint Figure 11 scoped-member coexistence',
)

joined = b + '\n' + m
for obsolete in [
    'issue a new production-capable technical baseline without a new business decision',
    'PR -->|still production-viable inside standing Organizational basis| PA',
    'Project may reauthorize locally when the basis remains viable inside standing Organizational authorization',
]:
    if obsolete in joined:
        raise SystemExit('obsolete wording remains: ' + obsolete)

required = [
    'resulting production scope remains covered by the applicable existing Organizational Business Authorization',
    'still production-viable and covered by applicable<br/>Organizational Business Authorization',
    'not mutually exclusive full-system states',
    'coexistence requires explicit scope/overlap/nesting/precedence semantics',
]
for phrase in required:
    if phrase not in joined:
        raise SystemExit('required wording missing: ' + phrase)

bp.write_text(b)
ms.write_text(m)
