from pathlib import Path
bp=Path('content/research/notes/open-engineering-specification-article-blueprint.md')
tr=Path('content/research/framework-traceability.md')
b=bp.read_text()
t=tr.read_text()

# Ownership-language sweep.
for old,new in [
('Organizational-selected-path-or-specific-research-or-business-decision','Project technical/design selection plus Organizational business/basis/specific-research/continuation decisions where required'),
('Organization ↔ Project / Architecture viability/path/business/research-authorization handshake','Organization ↔ Project / Architecture technical-design-and-viability / business-basis-and-research-authorization handshake'),
('Organizationally selected deterministic/manual redesign','Project-selected deterministic/manual redesign'),
('changing assessment eligibility, specific research permission, business permission, selected path, exception, vendor approval, shared capability, or business assumptions','changing assessment eligibility, specific research permission, business/basis permission, exception, vendor approval, shared capability, or business assumptions'),
('assessment-eligibility / Project-viability / Organizational-path-specific-research-business / research-only-versus-production-capable-Project-Authorization handshake','assessment-eligibility / Project-technical-design-and-viability / Organizational-business-basis-specific-research-continuation-where-required / research-only-versus-production-capable-Project-Authorization handshake'),
('Project viability conclusion ↔ Organizational path/research/business decision ↔ scoped Project Authorization handshake','Project technical/design selection and viability ↔ Organizational business/basis/research/continuation decision where required ↔ scoped Project Authorization handshake'),
('assessment/viability/path/business/research-authorization handshake','assessment/technical-design-and-viability/business-basis/research-authorization handshake'),
('selected-path category-exit rule','Project-selected-design category-exit rule'),
('selected-path category confirmation/exit','Project-selected-design category confirmation/exit'),
('the Organization ↔ Project / Architecture viability/path/business/research-authorization handshake','the Organization ↔ Project / Architecture technical-design-and-viability / business-basis-and-research-authorization handshake'),
]: b=b.replace(old,new)

# §6 worksheet item 11.
b=b.replace('which Organization-level path/business/research decision consumes that conclusion, which outcomes can follow, what technical authorization scope results, and what triggers reassessment?',
'which Organization-level business/basis/research/continuation decision, if any, consumes a Project finding that implicates reserved authority, which outcomes can follow, what technical authorization scope results, and what triggers reassessment?')

# Research proportionality in the unresolved-risk wording.
b=b.replace('initial eligibility lets Project analyze candidates and design a research proposal; it does **not** authorize exposure of a concrete experiment. A specific Bounded Research Authorization follows only after Project defines the experiment\'s purpose, control envelope, scope, data/tools, reachable authority, stopping conditions, and evidence obligations.',
'initial eligibility lets Project analyze candidates and conduct local simulation, offline/synthetic evaluation, or other engineering evidence generation inside the standing assessment envelope when no Organizationally reserved exposure or commitment is consumed or created. It does **not** authorize an experiment that crosses a reserved Organizational boundary. A specific Bounded Research Authorization follows only after Project defines such an experiment\'s purpose, control envelope, scope, data/tools, reachable authority, stopping conditions, and evidence obligations.')

# Traceability: replace the single Needs Resolution row robustly by its first cell.
newrow="| Project technical/design selection and viability versus Organizational business/research authority | Current status-bearing Project pattern combines project viability, authorization, deferral, and No-Go inside the Project decision surface and does not yet express the paper's explicit assessment-eligibility versus specific bounded-research distinction | Article research hypothesis assigns Model-Judgment necessity, technical/design selection inside the standing Organizational business/authority basis, category confirmation, and viability to Project / Architecture; initial Organizational assessment eligibility permits Project-local analysis and evidence generation inside the standing envelope but does not authorize reserved exposure; a specific Bounded Research Authorization is required when a Project-defined experiment crosses an Organizationally owned exposure/authority/data/material-commitment boundary; Organization also owns the business outcome/basis plus proceed/continue/reshape/defer/do-not-proceed decisions; scoped Project Authorization is research-only for specifically authorized bounded research before production viability is established or production-capable after positive Organizational Business Authorization on a viable basis | Needs Resolution | Do not change doctrine/pattern ownership by implication. Validate the boundary—including Project-owned simpler-design selection inside the standing basis, assessment eligibility versus specific reserved-exposure research authorization, and research-only versus production-capable Project Authorization—then deliberately accept, narrow, reject, or otherwise reconcile it through framework review before status-bearing sources change. |"
lines=t.splitlines()
idx=[i for i,x in enumerate(lines) if x.startswith('| Project technical/design selection and viability versus Organizational business/research authority |')]
if len(idx)!=1: raise SystemExit(f'traceability row count {len(idx)}')
lines[idx[0]]=newrow
t='\n'.join(lines)+'\n'

# Exact guards for the rejected ownership semantics.
for bad in ['Organizational-selected-path','Organizationally selected deterministic/manual redesign','Organization-level path/business/research decision','Organizational path/research/business decision','Organizational-path-specific-research-business','viability/path/business/research-authorization handshake','assessment/viability/path/business/research-authorization handshake']:
    if bad in b: raise SystemExit('obsolete phrase remains: '+bad)
if 'which Organization-level business/basis/research/continuation decision, if any' not in b: raise SystemExit('worksheet update missing')
if 'assessment eligibility versus specific reserved-exposure research authorization' not in t: raise SystemExit('traceability update missing')
bp.write_text(b)
tr.write_text(t)
