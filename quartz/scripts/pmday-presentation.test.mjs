import assert from "node:assert/strict"
import { execFileSync, spawnSync } from "node:child_process"
import { mkdtemp, readFile, rm, writeFile } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import test from "node:test"
import { fileURLToPath } from "node:url"
import { renderIndependentPreview, verifyRenderedText, verifyPng } from "./preview-pmday-pptx.mjs"
import { parseDeck } from "./pmday-presentation.mjs"
import { verifyPptxPair, runtimeEnvironment } from "./build-pmday-pptx.mjs"

const root = path.resolve(fileURLToPath(new URL("../..", import.meta.url)))
const folder = path.join(root, "assets/presentations/pmday-2026")
const source = await readFile(path.join(folder, "README.md"), "utf8")
const validator = path.join(root, "quartz/scripts/validate-pmday-pptx.py")

test("authoring maps supplied runtime paths for finalizer subprocesses", () => {
  const env = runtimeEnvironment({
    CODEX_PRIMARY_RUNTIME_ROOT: "/runtime",
    CODEX_PRIMARY_RUNTIME_NODE: "/runtime/node",
    CODEX_PRIMARY_RUNTIME_NODE_MODULES: "/runtime/modules",
    CODEX_PRIMARY_RUNTIME_PYTHON: "/runtime/python",
  })
  assert.equal(env.RUNTIME_NODE_MODULES, "/runtime/modules")
  assert.equal(env.RUNTIME_BIN_DIR, "/runtime/dependencies/bin/override")
})

test("approved 14-slide source has its original narrative order and complete notes", () => {
  const slides = parseDeck(source)
  assert.equal(slides.length, 14)
  assert.equal(slides[4].title, "The New Scarcity Is Human Comprehension")
  assert.equal(slides[5].title, "The Team Is the Last Line of Defense")
  assert.equal(slides[6].title, "We Are Searching for a New SDLC Equilibrium")
  assert.equal(slides[13].title, "Engineering Rigor Moves — It Doesn’t Disappear")
  assert.ok(slides.every((slide) => slide.notes.length > 80))
})

test("source refuses missing slide, reordered layout and unapproved image exception", () => {
  assert.throws(() => parseDeck(source.replace("## 14. ", "## Removed. ")), /14 approved/)
  assert.throws(() => parseDeck(source.replace('"layout": "cover"', '"layout": "sdlc"')), /order/)
  assert.throws(
    () =>
      parseDeck(
        source.replace('"layout": "cover"', '"images": ["background.png"], "layout": "cover"'),
      ),
    /exceptions/,
  )
})

test("committed PPTX is fresh, editable and follows the dark-background contract", () => {
  const result = JSON.parse(execFileSync("python3", [validator], { encoding: "utf8" }))
  assert.equal(result.slides, 14)
  assert.equal(result.pictures, 1)
  assert.equal(result.tables, 2)
})

for (const mutation of [
  "background",
  "picture",
  "table",
  "stale",
  "text-outside",
  "cover-missing",
  "cover-size",
  "evidence-number",
  "nber-obsolete",
  "agarwal-rounded",
  "toc-missing",
  "block-edge",
  "dora-interval",
  "sdlc-arrow",
  "curve-kink",
  "recovery-owner",
  "equilibrium-drill",
]) {
  test(`portable validator rejects ${mutation} regression`, async (t) => {
    const temporary = await mkdtemp(path.join(os.tmpdir(), "ua-pptx-test-"))
    t.after(() => rm(temporary, { recursive: true, force: true }))
    const fixture = path.join(temporary, "fixture.pptx")
    const manifest = path.join(temporary, "fixture.json")
    execFileSync("python3", [
      "-c",
      `
import hashlib,json,sys,zipfile,xml.etree.ElementTree as E
source,target,record,mutation=sys.argv[1:]
ns={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
with zipfile.ZipFile(source) as old, zipfile.ZipFile(target,'w') as new:
 for item in old.infolist():
  data=old.read(item.filename)
  if item.filename=='ppt/slides/slide1.xml' and mutation.startswith('cover-'):
   tree=E.fromstring(data)
   pic=tree.find('.//p:pic',ns)
   if mutation=='cover-size': pic.find('p:spPr/a:xfrm/a:ext',ns).set('cx','12192000')
   if mutation=='cover-missing': tree.find('p:cSld/p:spTree',ns).remove(pic)
   data=E.tostring(tree)
  if item.filename=='ppt/slides/slide4.xml' and mutation=='evidence-number': data=data.replace(b'59%',b'99%')
  if item.filename=='ppt/slides/slide4.xml' and mutation=='nber-obsolete': data=data.replace('25.5×'.encode(),'17.3×'.encode())
  if item.filename=='ppt/slides/slide4.xml' and mutation=='agarwal-rounded': data=data.replace(b'+34.85% / +42.87%',b'+35% / +43%')
  if item.filename=='ppt/slides/slide4.xml' and mutation=='dora-interval': data=data.replace(b'+0.07 to +0.13',b'+0.77 to +0.83')
  if item.filename=='ppt/slides/slide2.xml' and mutation=='block-edge':
   tree=E.fromstring(data)
   for shape in tree.findall('.//p:sp',ns):
    geom=shape.find('p:spPr/a:prstGeom',ns)
    if geom is not None and geom.get('prst')=='rect' and shape.find('p:spPr/a:solidFill',ns) is not None:
     shape.find('p:spPr/a:xfrm/a:off',ns).set('x','0')
     break
   data=E.tostring(tree)
  if item.filename=='ppt/slides/slide3.xml' and mutation=='toc-missing': data=data.replace(b'THEORY OF CONSTRAINTS',b'MISSING')
  if item.filename=='ppt/slides/slide3.xml' and mutation=='sdlc-arrow':
   tree=E.fromstring(data)
   E.SubElement(tree.find('.//a:ln',ns),'{'+ns['a']+'}tailEnd',{'type':'triangle'})
   data=E.tostring(tree)
  if item.filename=='ppt/slides/slide5.xml' and mutation=='curve-kink':
   tree=E.fromstring(data)
   for path in tree.findall('.//a:custGeom/a:pathLst/a:path',ns):
    for vertex in path.findall('a:lnTo',ns)[3:]: path.remove(vertex)
   data=E.tostring(tree)
  if item.filename=='ppt/slides/slide6.xml' and mutation=='recovery-owner': data=data.replace(b'proposes fix',b'waits for AI')
  if item.filename=='ppt/slides/slide7.xml' and mutation=='equilibrium-drill': data=data.replace(b'Human recovery drills',b'Just trust the agent')
  if item.filename=='ppt/slides/slide11.xml':
   tree=E.fromstring(data)
   if mutation=='text-outside': tree.find('.//p:sp/p:spPr/a:xfrm/a:off',ns).set('x','12192000')
   if mutation=='background': tree.find('p:cSld/p:bg/p:bgPr/a:solidFill/a:srgbClr',ns).set('val','FFFFFF')
   if mutation=='picture': E.SubElement(tree.find('p:cSld/p:spTree',ns),'{'+ns['p']+'}pic')
   if mutation=='table':
    for parent in tree.iter():
     for child in list(parent):
      if child.tag=='{'+ns['a']+'}tbl': parent.remove(child)
   data=E.tostring(tree)
  new.writestr(item,data)
with open(source.replace('.pptx','.manifest.json')) as f: m=json.load(f)
with open(target,'rb') as f: m['pptx_sha256']=hashlib.sha256(f.read()).hexdigest()
if mutation=='stale': m['inputs']['assets/presentations/pmday-2026/README.md']='0'*64
with open(record,'w') as f: json.dump(m,f)
`,
      path.join(folder, "ai-changes-both-sides.pptx"),
      fixture,
      manifest,
      mutation,
    ])
    const result = spawnSync("python3", [validator, "--pptx", fixture, "--manifest", manifest], {
      encoding: "utf8",
    })
    assert.equal(result.status, 1, result.stdout + result.stderr)
    assert.match(
      result.stderr,
      /background|exceptions|native table|Stale input|outside canvas|safe margins|foreground boundary|Evidence slide missing|SDLC slide missing|must not contain arrowheads|Comprehension curve|Recovery slide missing|Equilibrium slide missing/,
    )
  })
}

test("PPTX pair verification refuses a checksum mismatch", async (t) => {
  const temporary = await mkdtemp(path.join(os.tmpdir(), "ua-pptx-pair-"))
  t.after(() => rm(temporary, { recursive: true, force: true }))
  await writeFile(path.join(temporary, "deck.pptx"), "not-the-declared-file")
  await writeFile(
    path.join(temporary, "manifest.json"),
    JSON.stringify({ pptx_sha256: "0".repeat(64) }),
  )
  await assert.rejects(
    verifyPptxPair(path.join(temporary, "deck.pptx"), path.join(temporary, "manifest.json")),
    /checksum/,
  )
})

test("portable font checks reject mixed faces, stale themes and embedded font data", () => {
  execFileSync("python3", [
    "-c",
    `
import importlib.util,io,zipfile,xml.etree.ElementTree as E
spec=importlib.util.spec_from_file_location('pptx_validator',${JSON.stringify(validator)})
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
with zipfile.ZipFile(v.ROOT/'assets/presentations/pmday-2026/ai-changes-both-sides.pptx') as z:
 original={n:z.read(n) for n in z.namelist()}
def check(parts):
 stream=io.BytesIO()
 with zipfile.ZipFile(stream,'w') as z:
  for name,data in parts.items(): z.writestr(name,data)
 with zipfile.ZipFile(stream) as z: v.validate_fonts(z)
check(original)
mutations=[]
for name in ('ppt/slides/slide14.xml','ppt/notesMasters/theme/theme3.xml','ppt/slideMasters/theme/theme2.xml','ppt/slides/charts/chart1.xml'):
 parts=original.copy();assert b'typeface="Arial"' in parts[name];parts[name]=parts[name].replace(b'typeface="Arial"',b'typeface="Roboto"');mutations.append(parts)
parts=original.copy();parts['ppt/fonts/unapproved.fntdata']=b'unapproved';mutations.append(parts)
parts=original.copy();name='ppt/slides/slide14.xml';tree=E.fromstring(parts[name])
for e in tree.iter(): e.attrib.pop('typeface',None)
parts[name]=E.tostring(tree);mutations.append(parts)
for parts in mutations:
 try: check(parts)
 except AssertionError as error: assert 'Arial:' in str(error)
 else: raise AssertionError('Invalid standard font contract passed')
print('Arial font mutation checks passed')
`,
  ])
})

// Line breaks may change layout, but must never silently rename a slide.
test("title line breaks preserve the approved wording", () => {
  assert.throws(
    () => parseDeck(source.replace('"We Are Searching for a New",', '"Changed title",')),
    /approved title/,
  )
})

test("independent renderer rejects an exported word split", () => {
  assert.doesNotThrow(() => verifyRenderedText("Test Integrate Deploy Button A Window B"))
  assert.throws(() => verifyRenderedText("Test Integrat\ne Deploy"), /missing or split/)
  assert.throws(() => verifyRenderedText("Integrate Button\nA Window B"), /Button A/)
  assert.throws(() => verifyRenderedText("Integrate Button A Window\nB"), /Window B/)
})

test("slide freeze protects 1–11, chart/workbook and table while permitting 12–14", () => {
  execFileSync("python3", [
    "-c",
    `
import copy,importlib.util,io,json,zipfile,xml.etree.ElementTree as E
from pathlib import Path
spec=importlib.util.spec_from_file_location('pptx_validator',${JSON.stringify(validator)})
v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
source=(v.ROOT/v.SOURCE).read_text()
record=json.loads((v.ROOT/v.FREEZE).read_text())
assert v.frozen_source_hashes(source)==record['source_sections']
assert v.frozen_source_hashes(source.replace('## 2. This Is a Real Phase Transition','## 2. Accidental edit'))!=record['source_sections']
assert v.frozen_source_hashes(source.replace('Button A','Other button'))!=record['source_sections']
assert v.frozen_source_hashes(source.replace('Production Needs a Control Loop','Changed editable title'))==record['source_sections']
assert record['slides']==list(range(1,12))
with zipfile.ZipFile(v.ROOT/'assets/presentations/pmday-2026/ai-changes-both-sides.pptx') as z:
 original={n:z.read(n) for n in z.namelist()}
def check(parts):
 stream=io.BytesIO()
 with zipfile.ZipFile(stream,'w') as z:
  for name,data in parts.items(): z.writestr(name,data)
 with zipfile.ZipFile(stream) as z: v.validate_frozen(source,z)
check(original)
mutations=[]
parts=original.copy(); tree=E.fromstring(parts['ppt/slides/slide2.xml'])
off=tree.find('.//p:sp/p:spPr/a:xfrm/a:off',v.NS); off.set('x',str(int(off.get('x'))+9525))
parts['ppt/slides/slide2.xml']=E.tostring(tree); mutations.append(parts)
parts=original.copy(); tree=E.fromstring(parts['ppt/notesSlides/notesSlide4.xml']); tree.find('.//a:t',v.NS).text='Accidentally rewritten notes'
parts['ppt/notesSlides/notesSlide4.xml']=E.tostring(tree); mutations.append(parts)
parts=original.copy(); tree=E.fromstring(parts['ppt/theme/theme1.xml']); tree.find('.//a:srgbClr',v.NS).set('val','123456')
parts['ppt/theme/theme1.xml']=E.tostring(tree); mutations.append(parts)
parts=original.copy(); name='ppt/slides/_rels/slide2.xml.rels'; parts[name]=parts[name].replace(b'notesSlide2.xml',b'notesSlide3.xml'); mutations.append(parts)
for number in (9,10,11):
 parts=original.copy();name=f'ppt/slides/slide{number}.xml';tree=E.fromstring(parts[name]);tree.find('.//a:t',v.NS).text='Unapproved protected text';parts[name]=E.tostring(tree);mutations.append(parts)
 parts=original.copy();name=f'ppt/notesSlides/notesSlide{number}.xml';tree=E.fromstring(parts[name]);tree.find('.//a:t',v.NS).text='Unapproved protected notes';parts[name]=E.tostring(tree);mutations.append(parts)
parts=original.copy();name='ppt/slides/slide11.xml';tree=E.fromstring(parts[name]);tree.find('.//a:tbl//a:t',v.NS).text='Unapproved table cell';parts[name]=E.tostring(tree);mutations.append(parts)
parts=original.copy();name='ppt/slides/charts/chart1.xml';assert b'>196<' in parts[name];parts[name]=parts[name].replace(b'>196<',b'>195<');mutations.append(parts)
parts=original.copy();name='ppt/embeddings/chart-data-snapshot-001.xlsx'
with zipfile.ZipFile(io.BytesIO(parts[name])) as w: members={n:w.read(n) for n in w.namelist()}
assert b'>196<' in members['xl/worksheets/sheet1.xml']
def pack_workbook(files):
 stream=io.BytesIO()
 with zipfile.ZipFile(stream,'w',zipfile.ZIP_STORED) as w:
  for n in sorted(files,reverse=True): w.writestr(zipfile.ZipInfo(n,(2020,1,1,0,0,0)),files[n])
 return stream.getvalue()
parts[name]=pack_workbook(members);assert parts[name]!=original[name];check(parts)
changed=members.copy();changed['xl/worksheets/sheet1.xml']=changed['xl/worksheets/sheet1.xml'].replace(b'>196<',b'>195<');parts[name]=pack_workbook(changed);mutations.append(parts)
for parts in mutations:
 try: check(parts)
 except AssertionError as error: assert 'Frozen slides' in str(error)
 else: raise AssertionError('Protected mutation passed')
for number in (12,13,14):
 parts=original.copy();name=f'ppt/slides/slide{number}.xml';tree=E.fromstring(parts[name]);tree.find('.//a:t',v.NS).text='Editable slide';parts[name]=E.tostring(tree);check(parts)
print('Freeze checks passed')
`,
  ])
})

test("independent preview rejects an external source", async () => {
  await assert.rejects(renderIndependentPreview("../outside.pptx"), /inside/)
})

test("independent preview failure preserves the last committed pair", async () => {
  const pptx = path.join(folder, "ai-changes-both-sides.pptx")
  const manifest = path.join(folder, "ai-changes-both-sides.manifest.json")
  const before = [await readFile(pptx), await readFile(manifest)]
  await assert.rejects(
    renderIndependentPreview(pptx, {
      UA_SOFFICE: "/missing-ua-renderer/soffice",
    }),
    /ENOENT/,
  )
  assert.deepEqual([await readFile(pptx), await readFile(manifest)], before)
})

test("independent preview rejects truncated image output", async () => {
  const png = Buffer.from(
    "89504e470d0a1a0a0000000d4948445200000001000000010802000000907753de0000000c49444154789c63606060000000040001f61738550000000049454e44ae426082",
    "hex",
  )
  assert.doesNotThrow(() => verifyPng(png))
  assert.throws(() => verifyPng(png.subarray(0, -5)), /Truncated/)
})
