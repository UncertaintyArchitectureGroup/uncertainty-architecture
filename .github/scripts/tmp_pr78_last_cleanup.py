from pathlib import Path
p=Path('content/research/notes/open-engineering-specification-article-blueprint.md')
s=p.read_text()

# Sweep obsolete §5–§6 ownership labels without depending on one exact prior wording.
for old,new in [
("Organizational selected-path/research/business decision", "Organizational business/basis/research/continuation decision where required"),
("Organizational selected-path/business/research-decision consumer/options", "Organizational business/basis/research/continuation-decision consumer/options where required"),
("Organizational selected-path/specific-research/business authorization", "Organizational specific-research/business/basis authority where required"),
("technical viability versus business/design authority", "Project-owned technical/design viability versus Organization-owned business/basis authority"),
("selected-path/business/research authorization", "business/basis/research authorization where required"),
("selected-path/business/research-authorization semantics", "technical-design/business-basis/research-authorization semantics"),
("assessment/viability/path/research/business decision", "assessment/technical-viability/business-basis/research decision"),
("Organization↔Project assessment/viability/path/research/business-authorization handshake", "Organization↔Project assessment/technical-design-and-viability/business-basis/research-authorization handshake"),
("Project viability conclusion → Organizational business/basis/research/continuation decision where required → scoped Project Authorization where applicable", "Project technical/design selection and viability → Organizational business/basis/research/continuation decision only where required → scoped Project Authorization where applicable"),
("Organization makes the specific-research/business/basis decision on the Project viability conclusion", "Organization makes a specific-research/business/basis or continuation decision only when the Project finding implicates that reserved authority"),
]:
    s=s.replace(old,new)

# Strengthen category-exit semantics wherever the old §5/§4 callback still exists.
s=s.replace(
"Article §4 has already established that if Project selects such a path inside the standing Organizational basis, Project confirms the selected design's negative category result and it exits the Thinking-System lifecycle",
"Article §4 has already established that if Project selects such a path inside the standing Organizational basis, Project confirms the selected design's negative category result and it exits the Thinking-System-specific lifecycle by handing off to ordinary product/software governance; that exit is not business authorization and otherwise applicable funding, initiative, delivery, and release decision rights remain in force")
s=s.replace(
"Project confirms the category of its selected design; a negative category result exits the Thinking-System lifecycle, while a selected narrower model-assisted path is reassessed as a Thinking System.",
"Project confirms the category of its selected design; a negative category result exits the Thinking-System-specific lifecycle and hands off to ordinary product/software governance without granting business, funding, delivery, or release authorization, while a selected narrower model-assisted path is reassessed as a Thinking System.")
s=s.replace(
"→ exit Thinking-System lifecycle → ordinary product/software lifecycle",
"→ exit Thinking-System-specific lifecycle → handoff to ordinary product/software governance; normal funding / initiative / delivery / release authority still applies")
s=s.replace(
"A simpler design that satisfies the standing Organizational basis may exit the Thinking-System lifecycle at Project after category confirmation; a changed Organizational premise must return to Organization before Project reassesses.",
"A simpler design that satisfies the standing Organizational basis may, after Project category confirmation, exit the Thinking-System-specific lifecycle and hand off to ordinary product/software governance; that exit is not business authorization and normal funding, initiative, delivery, and release decision rights still apply. A changed Organizational premise must return to Organization before Project reassesses.")

# Delivery escalation: Model-Judgment-necessity changes are local unless an Organizational premise/continuation decision is implicated.
s=s.replace(
"If Project concludes that the architecture is no longer viable, that economics/Model-Judgment necessity or an Organizationally owned business assumption is invalid, that Architectural Veto now applies, that a new specific Bounded Research Authorization is required, or that a changed Organizational boundary/exception/business/continuation decision is required, Project routes the conclusion/proposal to Organization before a new scoped technical baseline can be issued. If Project instead prefers a simpler technical path that still satisfies the standing Organizational business/authority basis, Project may select that path, confirm its category, and either reauthorize the resulting narrower Thinking System or exit this Thinking-System-specific lifecycle and hand off to ordinary product/software governance when the selected design is no longer a Thinking System; no Organizational architecture-selection step is required.",
"If Project concludes that the architecture is no longer viable, that economics or another Organizationally owned business/basis assumption is invalid, that Architectural Veto now applies, that a new specific Bounded Research Authorization is required, or that a changed Organizational boundary/exception/business/continuation decision is required, Project routes the conclusion/proposal to Organization before a new scoped technical baseline can be issued. A changed Model-Judgment-necessity finding remains Project-local when a simpler technical path still satisfies the standing Organizational business/authority basis: Project may select that path, confirm its category, and either reauthorize the resulting narrower Thinking System or exit this Thinking-System-specific lifecycle and hand off to ordinary product/software governance when the selected design is no longer a Thinking System. Organization is reactivated only when that finding requires changing an Organizationally owned premise or continuation decision; no Organizational architecture-selection step is required.")

# Guard only the contradictions this cleanup is supposed to remove.
for bad in ['Organizational selected-path','technical viability versus business/design authority','selected-path/business/research authorization','economics/Model-Judgment necessity','exit Thinking-System lifecycle → ordinary product/software lifecycle']:
    if bad in s:
        raise SystemExit(f'obsolete phrase remains: {bad}')
p.write_text(s)
