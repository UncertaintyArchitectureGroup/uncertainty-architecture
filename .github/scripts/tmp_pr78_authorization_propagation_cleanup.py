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

# 1) Keep the high-level blueprint argument scoped: research may answer a local
# experiment/change question even when another production scope remains viable.
b = replace_exact(
    b,
    '→ when production viability remains unresolved, Project may conduct evidence generation locally when the work remains inside the standing assessment envelope; when the needed experiment crosses an Organizationally reserved boundary, Project defines the research question, scope, reachable authority, stopping conditions, and evidence obligations, Organization may then issue a specific Bounded Research Authorization, and Project issues a research-only technical authorization that cannot silently become production permission',
    '→ when viability for a proposed experiment or change scope remains unresolved, Project may conduct evidence generation locally when the work remains inside the standing assessment envelope; when the needed experiment crosses an Organizationally reserved boundary, Project defines the research question, scope, reachable authority, stopping conditions, and evidence obligations, Organization may then issue a specific Bounded Research Authorization, and Project issues a research-only technical authorization for that declared scope that cannot silently become production permission',
    'blueprint connected argument scoped research viability',
)

b = replace_exact(
    b,
    '- If production viability remains open, Project may generate evidence locally while the work remains inside the standing assessment envelope. If the needed credibly bounded experiment crosses an Organizationally reserved boundary, initial assessment eligibility is insufficient for that reserved exposure: Organization must issue a **specific Bounded Research Authorization**, after which Project issues a research-only Project Authorization. Its Delivery/Runtime evidence returns to Project and cannot self-promote into production.',
    '- If viability for a proposed experiment or change scope remains open, Project may generate evidence locally while the work remains inside the standing assessment envelope. If the needed credibly bounded experiment crosses an Organizationally reserved boundary, initial assessment eligibility is insufficient for that reserved exposure: Organization must issue a **specific Bounded Research Authorization**, after which Project issues a research-only Project Authorization for that declared scope. Its Delivery/Runtime evidence returns to Project and cannot self-promote into production.',
    'blueprint Article 4 plan scoped research viability',
)

# 2) Propagate authorization-set semantics into publication-facing Delivery and Runtime.
m = replace_exact(
    m,
    '**Question owned:** Is this bounded realization complete, evidence-bearing, operationally supportable, and acceptable for the specific exposure permitted by its Project Authorization?',
    '**Question owned:** Is this bounded realization complete, evidence-bearing, operationally supportable, and acceptable for the specific exposure permitted by the Project Authorization scope or authorization set applicable to it?',
    'manuscript Delivery owned question authorization set',
)

m = replace_exact(
    m,
    'Delivery begins from a **scoped Project Authorization**, not from the Project viability conclusion alone and not from any Organizational decision alone. For research, Project Authorization exists only after a specific Bounded Research Authorization and permits only the defined experiment. For production, it carries the production-capable technical scope covered by Organizational Business Authorization.',
    'Delivery begins from the **scoped Project Authorization or explicitly defined authorization set applicable to the exposure being realized**, not from the Project viability conclusion alone and not from any Organizational decision alone. For research exposure, the applicable research-only Project Authorization exists only after a specific Bounded Research Authorization and permits only the defined experiment. For production exposure, the applicable production-capable Project Authorization carries the technical scope covered by Organizational Business Authorization. Where research-only and production-capable authorizations coexist, Delivery must preserve their explicit scope separation or overlap/nesting/precedence semantics rather than flatten them into one undifferentiated baseline.',
    'manuscript Delivery authorization-set basis',
)

m = replace_exact(
    m,
    'Delivery receives the current Project Constraint Architecture, intended Judgment landscape and placement assumptions, required operating-contract properties, evidence obligations, shared-capability dependencies, delegated authority, reauthorization triggers, baseline-correlation obligations, control economics, and the Organizational business/research assumptions on which the authorization depends. Within that baseline, Delivery owns the implementation-level Judgment Nodes, approves the Requirement and Operating Envelope for the bounded scope, turns inherited decisions into a concrete realization, and proves enough about that realization for the next decision.',
    'Delivery receives the current Project Constraint Architecture, intended Judgment landscape and placement assumptions, required operating-contract properties, evidence obligations, shared-capability dependencies, delegated authority, reauthorization triggers, baseline-correlation obligations, control economics, and the Organizational business/research assumptions on which the applicable authorization scope or authorization set depends. Within those applicable baseline semantics, Delivery owns the implementation-level Judgment Nodes, approves the Requirement and Operating Envelope for the bounded scope, turns inherited decisions into a concrete realization, and proves enough about that realization for the next decision.',
    'manuscript Delivery baseline semantics',
)

m = replace_exact(
    m,
    'Material runtime evidence must be attributable to the baseline under which the system actually acted. Runtime therefore needs enough correlated authoritative-source, Organizational assessment/research/business basis, Project, Delivery, realization, model/prompt/context/retrieval/tool/routing/evaluator/policy/deployment/fallback identity—including whether the active Project Authorization was research-only or production-capable—to reconstruct what was active for a material decision, incident, experiment result, or corrective action. The objective is reconstructability, not a mandatory universal registry.',
    'Material runtime evidence must be attributable to the baseline under which the system actually acted. Runtime therefore needs enough correlated authoritative-source, Organizational assessment/research/business basis, Project, Delivery, realization, model/prompt/context/retrieval/tool/routing/evaluator/policy/deployment/fallback identity—including the applicable Project Authorization set, each relevant authorization type/scope, and any overlap/nesting/precedence or interaction relationship—to reconstruct what was active for a material decision, incident, experiment result, or corrective action. The objective is reconstructability, not a mandatory universal registry.',
    'manuscript Runtime authorization-set reconstructability',
)

# 3) Propagate the same model through blueprint Runtime and Article 5 application contracts.
b = replace_exact(
    b,
    '→ Delivery may realize and release only the exposure permitted by the active Project Authorization; research evidence returns to Project viability assessment and cannot promote itself into production',
    '→ Delivery may realize and release only the exposure permitted by the applicable active Project Authorization scope or explicitly defined authorization set; research evidence returns to Project viability assessment and cannot promote itself into production',
    'blueprint connected argument Delivery authorization set',
)

b = replace_exact(
    b,
    '→ material evidence remains attributable to the active authorization and behavioral/control baseline well enough to reconstruct which source, Organizational decision, Project Authorization type/scope, Delivery decision, realization, model/configuration, evaluator, deployment, and fallback state actually governed the event',
    '→ material evidence remains attributable to the active authorization and behavioral/control baseline well enough to reconstruct which source, Organizational decision, applicable Project Authorization set and scope/precedence relationship, Delivery decision, realization, model/configuration, evaluator, deployment, and fallback state actually governed the event',
    'blueprint connected argument authorization-set evidence',
)

b = replace_exact(
    b,
    '**Primary question owned:** Does active operation remain inside the authorized Requirement, Constraint baseline, authority, capacity, economics, **Project Authorization type/scope**, and standing Organizational business/research basis with required realizations active and healthy, and what response is authorized when it does not?',
    '**Primary question owned:** Does active operation remain inside the authorized Requirement, Constraint baseline, authority, capacity, economics, **applicable Project Authorization set and scope/precedence relationship**, and standing Organizational business/research basis with required realizations active and healthy, and what response is authorized when it does not?',
    'blueprint Runtime primary question authorization set',
)

b = replace_exact(
    b,
    '- active Project Authorization type/scope (`research-only` or `production-capable`);',
    '- applicable Project Authorization set, including each active authorization type/scope (`research-only` and/or `production-capable`) and any explicit overlap/nesting/precedence or interaction relationship;',
    'blueprint Runtime input authorization set',
)

b = replace_exact(
    b,
    '- where this is reassessment, the current Organizational business/research basis and Project Authorization type/scope.',
    '- where this is reassessment, the current Organizational business/research basis and the applicable Project Authorization set, including scope and precedence/interaction where multiple authorizations coexist.',
    'blueprint Project reassessment input authorization set',
)

b = replace_exact(
    b,
    '→ 8. revisit depth, scope, carrier choice, or evidence-instrument validity when an authoritative source, Organizational assessment/research/business authorization, Project Authorization type/scope, Project assumption, model/population/policy/operating condition, Delivery realization, or Runtime operation changes the materiality judgment',
    '→ 8. revisit depth, scope, carrier choice, or evidence-instrument validity when an authoritative source, Organizational assessment/research/business authorization, applicable Project Authorization set/scope/precedence relationship, Project assumption, model/population/policy/operating condition, Delivery realization, or Runtime operation changes the materiality judgment',
    'blueprint Article 5 reassessment trigger authorization set',
)

b = replace_exact(
    b,
    'The output is not a named template. The authority-variant comparison, canonical relationship-to-carrier mapping, and surrounding prose must together make the active operating contract, Organizational assessment/research/business authorization, Project Authorization type/scope, authorization/source/scope, Model-Judgment rationale, material Constraints and assumptions, realization/evidence path, legitimate Controller and effective Actuation, post-action verification, failure handling, and local/Project/Organizational reassessment routes traceable and operable.',
    'The output is not a named template. The authority-variant comparison, canonical relationship-to-carrier mapping, and surrounding prose must together make the active operating contract, Organizational assessment/research/business authorization, applicable Project Authorization set with type/scope and any overlap/nesting/precedence relationship, authorization/source/scope, Model-Judgment rationale, material Constraints and assumptions, realization/evidence path, legitimate Controller and effective Actuation, post-action verification, failure handling, and local/Project/Organizational reassessment routes traceable and operable.',
    'blueprint Article 5 minimum output authorization set',
)

# Tight guards for the two review findings.
joined = b + '\n' + m
for obsolete in [
    '→ when production viability remains unresolved, Project may conduct evidence generation locally',
    '- If production viability remains open, Project may generate evidence locally',
    'specific exposure permitted by its Project Authorization?',
    'Delivery begins from a **scoped Project Authorization**',
    'including whether the active Project Authorization was research-only or production-capable',
    '**Project Authorization type/scope**, and standing Organizational business/research basis',
    '- active Project Authorization type/scope (`research-only` or `production-capable`);',
    'Project Authorization type/scope, authorization/source/scope',
]:
    if obsolete in joined:
        raise SystemExit('obsolete wording remains: ' + obsolete)

required = [
    'when viability for a proposed experiment or change scope remains unresolved',
    'Project Authorization scope or authorization set applicable to it',
    'explicitly defined authorization set applicable to the exposure being realized',
    'applicable Project Authorization set, each relevant authorization type/scope',
    'applicable Project Authorization set and scope/precedence relationship',
    'applicable Project Authorization set/scope/precedence relationship',
    'applicable Project Authorization set with type/scope and any overlap/nesting/precedence relationship',
]
for phrase in required:
    if phrase not in joined:
        raise SystemExit('required wording missing: ' + phrase)

bp.write_text(b)
ms.write_text(m)
