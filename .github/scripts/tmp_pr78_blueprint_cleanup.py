from pathlib import Path

bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
b = bp.read_text()


def replace_exact(text: str, old: str, new: str, label: str, expected: int = 1) -> str:
    count = text.count(old)
    if count != expected:
        raise SystemExit(f'{label}: expected {expected} occurrences, found {count}')
    return text.replace(old, new)

# 1) Remove remaining pre-production-only wording from general research rules.
b = replace_exact(
    b,
    'If production viability is unresolved, Project may continue evidence generation locally while it remains inside the standing assessment envelope.',
    'If viability for the proposed experiment or change scope remains unresolved, Project may continue evidence generation locally while the work remains inside the standing assessment envelope.',
    'running-example Article 4 general research rule',
)

b = replace_exact(
    b,
    '- whether a bounded experiment can be credibly controlled when production viability is not yet established;',
    '- whether a bounded experiment can be credibly controlled when viability for the proposed experiment or change scope remains unresolved;',
    'Project alternatives research question',
)

b = replace_exact(
    b,
    '- **Further bounded research required:** production viability remains unresolved, but Project can identify the evidence it needs and a credible experiment envelope.',
    '- **Further bounded research required:** viability for the proposed experiment or change scope remains unresolved, but Project can identify the evidence it needs and a credible experiment envelope.',
    'Project conclusion scoped research viability',
)

b = replace_exact(
    b,
    '- If production viability remains unresolved and the needed credibly bounded experiment crosses an Organizationally reserved boundary, is **that specific evidence** worth acquiring, and do the proposed exposure, data/tools, authority, stopping conditions, Human Authority/fallback, and evidence obligations fit Organizational limits?',
    '- If viability for the proposed experiment or change scope remains unresolved and the needed credibly bounded experiment crosses an Organizationally reserved boundary, is **that specific evidence** worth acquiring, and do the proposed exposure, data/tools, authority, stopping conditions, Human Authority/fallback, and evidence obligations fit Organizational limits?',
    'Organization scoped research question',
)

# Keep explicitly illustrative Case D wording intact; it is intentionally pre-production.

# 2) Align future drafting / acceptance contracts with authorization-set semantics.
b = replace_exact(
    b,
    '**Future-section ownership rule after Article §4.** **Article §§1–4** now own the category boundary, whole-system controlled object, capability anatomy, Hard/Soft semantics, substantive Human Authority, four decision horizons, the Project-viability / Organizational-business-and-research-authorization handshake, the meaning of Architectural Veto, **Project Authorization as a scoped technical baseline with research-only and production-capable forms**,',
    '**Future-section ownership rule after Article §4.** **Article §§1–4** now own the category boundary, whole-system controlled object, capability anatomy, Hard/Soft semantics, substantive Human Authority, four decision horizons, the Project-viability / Organizational-business-and-research-authorization handshake, the meaning of Architectural Veto, **Project Authorization as a scoped technical baseline with research-only and production-capable forms, including explicit applicable-authorization-set scope/overlap/nesting/precedence semantics where multiple authorizations coexist**,',
    'future-section ownership authorization-set semantics',
)

b = replace_exact(
    b,
    '- [ ] Material release/runtime evidence can be correlated to the active source/Organizational-assessment-research-business/Project-Authorization-type-and-scope/Delivery/realization/model-config/evaluator/deployment/fallback baseline without requiring one universal registry.',
    '- [ ] Material release/runtime evidence can be correlated to the active source/Organizational-assessment-research-business/applicable-Project-Authorization-set/type/scope/precedence/Delivery/realization/model-config/evaluator/deployment/fallback baseline without requiring one universal registry.',
    'running-example acceptance baseline set',
)

b = replace_exact(
    b,
    '- Preserve enough correlated source/Organizational-assessment-research-business/Project-Authorization-type-and-scope/Delivery/realization/model-config/evaluator/deployment/fallback identity to reconstruct the material active behavioral/control baseline for release, incident, experiment, and corrective evidence; do not create a mandatory universal registry by implication.',
    '- Preserve enough correlated source/Organizational-assessment-research-business/applicable-Project-Authorization-set/type/scope/precedence/Delivery/realization/model-config/evaluator/deployment/fallback identity to reconstruct the material active behavioral/control baseline for release, incident, experiment, and corrective evidence; do not create a mandatory universal registry by implication.',
    'accepted drafting decision baseline set',
)

b = replace_exact(
    b,
    '- [ ] Material evidence can be correlated to the active source/Organizational-assessment-research-business/Project-Authorization-type-and-scope/Delivery/realization/model-config/evaluator/deployment/fallback baseline sufficiently to reconstruct what governed a material release, experiment, incident, or Actuator decision; no universal registry is implied.',
    '- [ ] Material evidence can be correlated to the active source/Organizational-assessment-research-business/applicable-Project-Authorization-set/type/scope/precedence/Delivery/realization/model-config/evaluator/deployment/fallback baseline sufficiently to reconstruct what governed a material release, experiment, incident, or Actuator decision; no universal registry is implied.',
    'Article 4 acceptance baseline set',
)

b = replace_exact(
    b,
    '- [ ] Figure 12 distinguishes Release Gate **rework**, **terminal stop/defer/reject**, and **Project viability reassessment**; it releases only inside the current Project Authorization scope, never promotes research-only authorization into production, and does not bypass Project / Architecture to Organization.',
    '- [ ] Figure 12 distinguishes Release Gate **rework**, **terminal stop/defer/reject**, and **Project viability reassessment**; it releases only inside the applicable Project Authorization scope or explicitly defined authorization set, never promotes research-only authorization into production, and does not bypass Project / Architecture to Organization.',
    'Figure 12 acceptance authorization set',
)

joined = b
for obsolete in [
    'If production viability is unresolved, Project may continue evidence generation locally while it remains inside the standing assessment envelope.',
    'whether a bounded experiment can be credibly controlled when production viability is not yet established',
    '**Further bounded research required:** production viability remains unresolved',
    'If production viability remains unresolved and the needed credibly bounded experiment crosses an Organizationally reserved boundary',
    'Project-Authorization-type-and-scope/Delivery/realization',
    'inside the current Project Authorization scope, never promotes',
]:
    if obsolete in joined:
        raise SystemExit('obsolete wording remains: ' + obsolete)

required = [
    'If viability for the proposed experiment or change scope remains unresolved, Project may continue evidence generation locally',
    'whether a bounded experiment can be credibly controlled when viability for the proposed experiment or change scope remains unresolved',
    '**Further bounded research required:** viability for the proposed experiment or change scope remains unresolved',
    'applicable-authorization-set scope/overlap/nesting/precedence semantics where multiple authorizations coexist',
    'applicable-Project-Authorization-set/type/scope/precedence',
    'applicable Project Authorization scope or explicitly defined authorization set',
]
for phrase in required:
    if phrase not in joined:
        raise SystemExit('required wording missing: ' + phrase)

bp.write_text(b)
