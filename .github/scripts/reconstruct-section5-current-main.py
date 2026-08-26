from pathlib import Path
import json, re, subprocess

ROOT = Path('.')
OLD = '1d1d1c3e074e17032172ee3b0fe7ed7ddb9437ad'
TODAY = '2026-08-26'

def git_show(path):
    return subprocess.check_output(['git','show',f'{OLD}:{path}'], text=True)

def read(path): return (ROOT/path).read_text()
def write(path, text): (ROOT/path).write_text(text)

def replace_once(s, old, new, label):
    n=s.count(old)
    assert n==1, f'{label}: expected exactly 1 occurrence, found {n}'
    return s.replace(old,new,1)

# 1) Manuscript: append only final Article §5 from PR82 to current-main §4 ending.
manuscript_path='content/research/notes/open-engineering-specification-article-draft.md'
cur=read(manuscript_path)
assert '## 5. Applying the Map Without Overbuilding' not in cur, 'Section 5 already present'
old=git_show(manuscript_path)
marker='## 5. Applying the Map Without Overbuilding'
assert marker in old
section5=old[old.index(marker):].rstrip()+"\n"
cur=re.sub(r'^updated: \d{4}-\d{2}-\d{2}$', f'updated: {TODAY}', cur, count=1, flags=re.M)
cur=cur.rstrip()+"\n\n"+section5
write(manuscript_path,cur)

# 2) Blueprint: import only v12 canonical map block and accepted §5 drafting decisions.
bp_path='content/research/notes/open-engineering-specification-article-blueprint.md'
cur=read(bp_path)
old=git_show(bp_path)
map_start='**Blueprint-owned canonical working mapping — `support-resolution-canonical-material-map / v12`.**'
map_end='**Reverse-mapping closure rule:**'
assert map_start not in cur, 'v12 map already present'
assert map_start in old and map_end in old
map_block=old[old.index(map_start):old.index(map_end)].rstrip()+"\n\n"
assert map_end in cur
cur=replace_once(cur,map_end,map_block+map_end,'insert v12 map')

dec_start='**Accepted drafting decisions from the 2026-08-16 Article §5 first-draft iteration:**'
dec_end='**Minimum publication-facing output:**'
assert dec_start not in cur, 'accepted decisions already present'
assert dec_start in old and dec_end in old
dec_block=old[old.index(dec_start):old.index(dec_end)].rstrip()+"\n\n"
assert dec_end in cur
cur=replace_once(cur,dec_end,dec_block+dec_end,'insert accepted decisions')
cur=re.sub(r'^updated: \d{4}-\d{2}-\d{2}$', f'updated: {TODAY}', cur, count=1, flags=re.M)
# Make the active research item explicit at the imported §5 handoff.
cur=replace_once(cur,
    'Define carrier sufficiency as a paper-level research hypothesis: every pre-declared material relationship must remain operable and traceable somewhere, but no framework-specific artifact is required when existing mechanisms preserve the semantics.',
    'Define carrier sufficiency as a paper-level research hypothesis tracked as `TS-CARRIER-001`: every pre-declared material relationship must remain operable and traceable somewhere, but no framework-specific artifact is required when existing mechanisms preserve the semantics.',
    'TS-CARRIER link')
write(bp_path,cur)

# 3) Research State Register: §5 is now a concrete hypothesis under validation, not merely open drafting work.
reg_path='content/research/research-register.md'
cur=read(reg_path)
cur=re.sub(r'^updated: \d{4}-\d{2}-\d{2}$', f'updated: {TODAY}', cur, count=1, flags=re.M)
old_row='| `TS-CARRIER-001` | Material-relationship carrier sufficiency and proportional application | Artifact / process hypothesis | Article §5 blueprint synthesis | Open | [`open-engineering-specification-article-blueprint.md`](notes/open-engineering-specification-article-blueprint.md) | Complete Article §5 mapping and test whether existing records/tools can carry each material relationship without UA-specific duplicate artifacts or semantic loss |'
new_row='| `TS-CARRIER-001` | Material-relationship carrier sufficiency and proportional application | Artifact / process hypothesis | Article §5 blueprint synthesis | Under Validation | [`open-engineering-specification-article-blueprint.md`](notes/open-engineering-specification-article-blueprint.md) and Article §5 in the living manuscript | Test the integrated carrier-sufficiency hypothesis and `support-resolution-canonical-material-map / v12` against serious existing carrier compositions and Article §6 reverse mapping; revise the map before any whole-object substitution verdict if material semantics are missing or distorted |'
cur=replace_once(cur,old_row,new_row,'register human row')
# Machine block parse/update without touching other items.
m=re.search(r'<!-- ua-research-register\n(\{.*?\})\n-->',cur,re.S)
assert m, 'machine register block missing'
data=json.loads(m.group(1))
items=[i for i in data['items'] if i['id']=='TS-CARRIER-001']
assert len(items)==1
item=items[0]
assert item['status']=='open'
item['status']='under-validation'
item['next_step']='Test the integrated Article 5 carrier-sufficiency hypothesis and support-resolution-canonical-material-map / v12 against serious existing carrier compositions and Article 6 reverse mapping; revise the map before any whole-object substitution verdict if material semantics are missing or distorted.'
new_json=json.dumps(data,indent=2,ensure_ascii=False)
cur=cur[:m.start(1)]+new_json+cur[m.end(1):]
write(reg_path,cur)

# 4) Notes index: manuscript now genuinely includes Article §5.
idx_path='content/research/notes/README.md'
cur=read(idx_path)
cur=re.sub(r'^updated: \d{4}-\d{2}-\d{2}$', f'updated: {TODAY}', cur, count=1, flags=re.M)
old_desc='- [`open-engineering-specification-article-draft.md`](open-engineering-specification-article-draft.md) — active long-form target manuscript governed by the blueprint. The current merged paper establishes the core argument through Article §4 while later research remains intentionally open; Draft PRs may continue the long-form work independently of publication adaptations.'
new_desc='- [`open-engineering-specification-article-draft.md`](open-engineering-specification-article-draft.md) — active long-form target manuscript governed by the blueprint. The current draft establishes the core argument through Article §4 and adds Article §5 as the paper-level carrier-sufficiency/proportional-application hypothesis; the complete `support-resolution-canonical-material-map / v12` remains an unfrozen research object owned by the blueprint for later Article §6 reverse-mapping and substitution tests.'
cur=replace_once(cur,old_desc,new_desc,'notes manuscript description')
write(idx_path,cur)

# 5) Changelog: add only the Section 5/v12 work, not obsolete PR98 review reconciliation.
cl_path='CHANGELOG.md'
cur=read(cl_path)
entry='- Integrated Article §5, **Applying the Map Without Overbuilding**, as the paper-level `TS-CARRIER-001` carrier-sufficiency and proportional-application hypothesis: compares lower- and higher-authority candidate designs at the same Project / Architecture maturity point, requires materiality to be established before carrier choice, treats records and operating mechanisms as many-to-many carriers, and adds the blueprint-owned `support-resolution-canonical-material-map / v12` with explicit guarantee, authority, evidence, correction, reconstructability, conditional-research, exclusion-inventory, and reverse-mapping semantics. The map remains unfrozen research and cannot support a whole-controlled-object substitution verdict until Article §6 freezes an exact snapshot/digest and tests it bidirectionally.\n'
assert entry.strip() not in cur
changed='### Changed\n\n'
assert changed in cur
cur=cur.replace(changed,changed+entry+'\n',1)
write(cl_path,cur)

print('bounded Section 5 reconstruction complete')
