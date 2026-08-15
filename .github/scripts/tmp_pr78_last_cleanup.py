from pathlib import Path
p=Path('content/research/notes/open-engineering-specification-article-blueprint.md')
s=p.read_text()

def rep(old,new,label,min_count=1):
    global s
    n=s.count(old)
    if n<min_count:
        raise SystemExit(f'{label}: expected >= {min_count}, got {n}')
    s=s.replace(old,new)

# Remaining old ownership semantics in §§5–6 / substitution basis.
replacements=[
("Organizational selected-path/research/business decision", "Organizational business/basis/research/continuation decision where required"),
("Organizational selected-path/business/research-decision consumer/options", "Organizational business/basis/research/continuation-decision consumer/options where required"),
("Organizational selected-path/specific-research/business authorization", "Organizational specific-research/business/basis authority where required"),
("technical viability versus business/design authority", "Project-owned technical/design viability versus Organization-owned business/basis authority"),
("selected-path/business/research authorization", "business/basis/research authorization where required"),
("selected-path/business/research-authorization semantics", "technical-design/business-basis/research-authorization semantics"),
("assessment/viability/path/research/business decision", "assessment/technical-viability/business-basis/research decision"),
("Organization↔Project assessment/viability/path/research/business-authorization handshake", "Organization↔Project assessment/technical-design-and-viability/business-basis/research-authorization handshake"),
]
for old,new in replacements:
    if old in s:
        s=s.replace(old,new)

# §5 category-exit callback: explicit governance handoff, not authorization.
old="Article §4 has already established that if Project selects such a path inside the standing Organizational basis, Project confirms the selected design's negative category result and it exits the Thinking-System lifecycle"
new="Article §4 has already established that if Project selects such a path inside the standing Organizational basis, Project confirms the selected design's negative category result and it exits the Thinking-System-specific lifecycle by handing off to ordinary product/software governance; that exit is not business authorization and otherwise applicable funding, initiative, delivery, and release decision rights remain in force"
rep(old,new,'section5 category-exit callback')

# §5 viability relationship semantics.
old="Project viability conclusion → Organizational business/basis decision where required/research/business decision → scoped Project Authorization where applicable"
if old in s:
    s=s.replace(old,"Project technical/design selection and viability → Organizational business/basis/research/continuation decision only where required → scoped Project Authorization where applicable")
old2="Project viability conclusion → Organizational business/basis/research/continuation decision where required → scoped Project Authorization where applicable"
if old2 in s:
    s=s.replace(old2,"Project technical/design selection and viability → Organizational business/basis/research/continuation decision only where required → scoped Project Authorization where applicable")

# Figure 11: make negative category exit full handoff semantics.
old="→ exit Thinking-System lifecycle → ordinary product/software lifecycle"
new="→ exit Thinking-System-specific lifecycle → handoff to ordinary product/software governance; normal funding / initiative / delivery / release authority still applies"
rep(old,new,'figure11 exit')
old="A simpler design that satisfies the standing Organizational basis may exit the Thinking-System lifecycle at Project after category confirmation; a changed Organizational premise must return to Organization before Project reassesses."
new="A simpler design that satisfies the standing Organizational basis may, after Project category confirmation, exit the Thinking-System-specific lifecycle and hand off to ordinary product/software governance; that exit is not business authorization and normal funding, initiative, delivery, and release decision rights still apply. A changed Organizational premise must return to Organization before Project reassesses."
rep(old,new,'figure11 caption exit')

# Project local action bullet also uses weak exit wording.
old="Project confirms the category of its selected design; a negative category result exits the Thinking-System lifecycle, while a selected narrower model-assisted path is reassessed as a Thinking System."
new="Project confirms the category of its selected design; a negative category result exits the Thinking-System-specific lifecycle and hands off to ordinary product/software governance without granting business, funding, delivery, or release authorization, while a selected narrower model-assisted path is reassessed as a Thinking System."
rep(old,new,'project local exit bullet')

# Delivery escalation: do not route Model-Judgment-necessity change to Organization unless basis/continuation is implicated.
old="If Project concludes that the architecture is no longer viable, that economics/Model-Judgment necessity or an Organizationally owned business assumption is invalid, that Architectural Veto now applies, that a new specific Bounded Research Authorization is required, or that a changed Organizational boundary/exception/business/continuation decision is required, Project routes the conclusion/proposal to Organization before a new scoped technical baseline can be issued. If Project instead prefers a simpler technical path that still satisfies the standing Organizational business/authority basis, Project may select that path, confirm its category, and either reauthorize the resulting narrower Thinking System or exit this Thinking-System-specific lifecycle and hand off to ordinary product/software governance when the selected design is no longer a Thinking System; no Organizational architecture-selection step is required."
new="If Project concludes that the architecture is no longer viable, that economics or another Organizationally owned business/basis assumption is invalid, that Architectural Veto now applies, that a new specific Bounded Research Authorization is required, or that a changed Organizational boundary/exception/business/continuation decision is required, Project routes the conclusion/proposal to Organization before a new scoped technical baseline can be issued. A changed Model-Judgment-necessity finding remains Project-local when a simpler technical path still satisfies the standing Organizational business/authority basis: Project may select that path, confirm its category, and either reauthorize the resulting narrower Thinking System or exit this Thinking-System-specific lifecycle and hand off to ordinary product/software governance when the selected design is no longer a Thinking System. Organization is reactivated only when that finding requires changing an Organizationally owned premise or continuation decision; no Organizational architecture-selection step is required."
rep(old,new,'delivery escalation')

# Pure authority source sentence, if still old.
s=s.replace("Organization makes the specific-research/business/basis decision on the Project viability conclusion", "Organization makes a specific-research/business/basis or continuation decision only when the Project finding implicates that reserved authority")

# Final guard: obsolete phrases must be absent.
for bad in [
    'Organizational selected-path',
    'technical viability versus business/design authority',
    'selected-path/business/research authorization',
    'economics/Model-Judgment necessity',
    'exit Thinking-System lifecycle → ordinary product/software lifecycle',
]:
    if bad in s:
        raise SystemExit(f'obsolete phrase remains: {bad}')
p.write_text(s)
