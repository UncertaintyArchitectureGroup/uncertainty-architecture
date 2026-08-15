from pathlib import Path
p=Path('content/research/notes/open-engineering-specification-article-blueprint.md')
s=p.read_text()
repls={
"Project viability conclusion → Organizational selected-path/research/business decision → scoped Project Authorization where applicable":"Project technical/design selection and viability → Organizational business/basis/research/continuation decision only where required → scoped Project Authorization where applicable",
"technical viability versus business/design authority":"Project-owned technical/design viability versus Organization-owned business/basis authority",
"selected-path/business/research authorization":"business/basis/research authorization where required",
"Organizational selected-path/specific-research/business authorization":"Organizational specific-research/business/basis authority where required",
"Organizational selected-path/business/research-decision consumer/options":"Organizational business/basis/research/continuation-decision consumer/options where required",
"Organizational selected-path/business/research decision":"Organizational business/basis/research/continuation decision where required",
"Organizational selected-path/research/business decision":"Organizational business/basis/research/continuation decision where required",
"Organizational selected-path/specific-research/business authorization":"Organizational specific-research/business/basis authority where required",
"Organizational selected-path":"Organizational business/basis decision where required",
"selected-path/business/research-authorization semantics":"technical-design/business-basis/research-authorization semantics",
"assessment/viability/path/research/business decision":"assessment/technical-viability/business-basis/research decision",
}
for old,new in repls.items():
    if old in s:
        s=s.replace(old,new)
# Strengthen §5 callback exact phrase.
old="Article §4 has already established that if Project selects such a path inside the standing Organizational basis, Project confirms the selected design's negative category result and it exits the Thinking-System lifecycle"
new="Article §4 has already established that if Project selects such a path inside the standing Organizational basis, Project confirms the selected design's negative category result and it exits the Thinking-System-specific lifecycle by handing off to ordinary product/software governance; that exit is not business authorization and otherwise applicable funding, initiative, delivery, and release decision rights remain in force"
if old not in s: raise SystemExit('missing section5 category callback')
s=s.replace(old,new)
# Fix §6 pure-source bullet if old composite wording remains.
s=s.replace("Project selects the technical path and category within the standing Organizational basis; Organization makes the specific-research/business/basis decision on the Project viability conclusion; Project then issues", "Project selects the technical path and category within the standing Organizational basis; Organization makes a specific-research/business/basis or continuation decision only when the Project finding implicates that reserved authority; Project then issues")
# Clean duplication-risk shorthand if present.
s=s.replace("Organization↔Project assessment/viability/path/research/business-authorization handshake", "Organization↔Project assessment/technical-design-and-viability/business-basis/research-authorization handshake")
p.write_text(s)
