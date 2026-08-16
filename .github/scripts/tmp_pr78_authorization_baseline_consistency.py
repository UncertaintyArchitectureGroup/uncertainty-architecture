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

# Finish publication-facing Runtime/Delivery baseline propagation.
m = replace_exact(
    m,
    '**Question owned:** Does active operation remain inside the authorized Requirement, Constraint baseline, authority, capacity, economics, **and Project Authorization scope**—and what response is authorized when it does not?',
    '**Question owned:** Does active operation remain inside the authorized Requirement, Constraint baseline, authority, capacity, economics, **and the applicable Project Authorization scope or authorization-set semantics**—and what response is authorized when it does not?',
    'manuscript Runtime owned question authorization set',
)

m = replace_exact(
    m,
    'Relevant correlation may span authoritative-source, Organizational assessment/research/business basis, Project Authorization type and scope, Delivery baseline, Constraint Realization, model, prompt/instruction, context/retrieval, tool/routing, evaluator, policy/configuration, deployment scope, and fallback state.',
    'Relevant correlation may span authoritative-source, Organizational assessment/research/business basis, the applicable Project Authorization set (including type/scope and any overlap/nesting/precedence relationship), Delivery baseline, Constraint Realization, model, prompt/instruction, context/retrieval, tool/routing, evaluator, policy/configuration, deployment scope, and fallback state.',
    'manuscript Delivery baseline correlation authorization set',
)

m = replace_exact(
    m,
    '**Figure 12 — Delivery realization, bounded exposure, and release loop.** Delivery translates the scoped Project Authorization into a bounded operating contract and realization.',
    '**Figure 12 — Delivery realization, bounded exposure, and release loop.** Delivery translates the applicable scoped Project Authorization or explicitly defined authorization set into a bounded operating contract and realization.',
    'Figure 12 caption authorization set',
)

# Finish blueprint runtime/delivery evidence and validation propagation.
b = replace_exact(
    b,
    '- Can material release, experiment, incident, and correction evidence be correlated to the active authoritative-source, Organizational-assessment/research/business, Project-Authorization-type/scope, Delivery, realization, model/configuration, evaluator, deployment, and fallback baseline rather than to an ambiguous list of independent versions?',
    '- Can material release, experiment, incident, and correction evidence be correlated to the active authoritative-source, Organizational-assessment/research/business, applicable Project-Authorization-set/type/scope/precedence, Delivery, realization, model/configuration, evaluator, deployment, and fallback baseline rather than to an ambiguous list of independent versions?',
    'blueprint Delivery evidence baseline authorization set',
)

b = replace_exact(
    b,
    '- enough correlated baseline identity to reconstruct relevant authoritative-source, Organizational-assessment/research/business, Project-Authorization-type/scope, Delivery, realization, model/prompt/context/retrieval/tool/routing/evaluator/policy/deployment/fallback state for material evidence;',
    '- enough correlated baseline identity to reconstruct relevant authoritative-source, Organizational-assessment/research/business, applicable Project-Authorization-set/type/scope/precedence, Delivery, realization, model/prompt/context/retrieval/tool/routing/evaluator/policy/deployment/fallback state for material evidence;',
    'blueprint Runtime input baseline authorization set',
)

b = replace_exact(
    b,
    '- correlated active source/Organizational-assessment-research-business/Project-Authorization-type/project/delivery/configuration/version traceability sufficient to reconstruct the material behavioral/control baseline;',
    '- correlated active source/Organizational-assessment-research-business/applicable-Project-Authorization-set-and-scope-precedence/Project/Delivery/configuration/version traceability sufficient to reconstruct the material behavioral/control baseline;',
    'blueprint Runtime output baseline authorization set',
)

b = replace_exact(
    b,
    '- **Behavioral/control baseline correlation:** Material evidence, incidents, release decisions, experiment results, and Actuator actions need enough correlation across authoritative-source, Organizational-assessment/research/business, Project-Authorization-type/scope, Delivery, realization, model/prompt/context/retrieval/tool/routing/evaluator/policy/deployment/fallback state to reconstruct what was actually active.',
    '- **Behavioral/control baseline correlation:** Material evidence, incidents, release decisions, experiment results, and Actuator actions need enough correlation across authoritative-source, Organizational-assessment/research/business, applicable Project-Authorization-set/type/scope/precedence, Delivery, realization, model/prompt/context/retrieval/tool/routing/evaluator/policy/deployment/fallback state to reconstruct what was actually active.',
    'blueprint known-risk baseline authorization set',
)

b = replace_exact(
    b,
    '- release/runtime/incident/research records showing whether material source, Organizational-assessment/research/business, Project-Authorization-type/scope, Delivery, realization, model/prompt-instruction/context-retrieval/tool-routing/evaluator-policy/deployment/fallback state could be correlated well enough to reconstruct the active behavioral/control baseline without relying on a new mandatory registry;',
    '- release/runtime/incident/research records showing whether material source, Organizational-assessment/research/business, applicable Project-Authorization-set/type/scope/precedence, Delivery, realization, model/prompt-instruction/context-retrieval/tool-routing/evaluator-policy/deployment/fallback state could be correlated well enough to reconstruct the active behavioral/control baseline without relying on a new mandatory registry;',
    'blueprint validation evidence baseline authorization set',
)

b = replace_exact(
    b,
    '- [ ] **Article §5** revisits implementation depth and carrier choice when authoritative sources, Organizational assessment/research/business authorization, Project Authorization type/scope, Project assumptions, Delivery realization evidence, Runtime operation evidence, or evidence-instrument validity change;',
    '- [ ] **Article §5** revisits implementation depth and carrier choice when authoritative sources, Organizational assessment/research/business authorization, the applicable Project Authorization set/scope/precedence relationship, Project assumptions, Delivery realization evidence, Runtime operation evidence, or evidence-instrument validity change;',
    'blueprint Article 5 acceptance authorization set',
)

joined = b + '\n' + m
for obsolete in [
    '**and Project Authorization scope**—and what response',
    'Project Authorization type and scope, Delivery baseline',
    'Delivery translates the scoped Project Authorization into a bounded operating contract',
    'Project-Authorization-type/scope, Delivery, realization',
    'Project Authorization type/scope, Project assumptions',
]:
    if obsolete in joined:
        raise SystemExit('obsolete wording remains: ' + obsolete)

required = [
    'applicable Project Authorization scope or authorization-set semantics',
    'applicable Project Authorization set (including type/scope and any overlap/nesting/precedence relationship)',
    'applicable scoped Project Authorization or explicitly defined authorization set',
    'applicable Project-Authorization-set/type/scope/precedence',
    'applicable Project Authorization set/scope/precedence relationship',
]
for phrase in required:
    if phrase not in joined:
        raise SystemExit('required wording missing: ' + phrase)

bp.write_text(b)
ms.write_text(m)
