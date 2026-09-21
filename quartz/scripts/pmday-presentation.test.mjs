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
  assert.equal(result.pictures, 0)
  assert.equal(result.tables, 2)
})

for (const mutation of ["background", "picture", "table", "stale", "text-outside"]) {
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
    assert.match(result.stderr, /background|exceptions|native table|Stale input|outside canvas/)
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

// Line breaks may change layout, but must never silently rename a slide.
test("title line breaks preserve the approved wording", () => {
  assert.throws(
    () => parseDeck(source.replace('"We Are Searching for a New",', '"Changed title",')),
    /approved title/,
  )
})

test("independent renderer rejects an exported word split", () => {
  assert.doesNotThrow(() => verifyRenderedText("Test Integrate Deploy"))
  assert.throws(() => verifyRenderedText("Test Integrat\ne Deploy"), /missing or split/)
})

test("independent preview rejects an external source", async () => {
  await assert.rejects(renderIndependentPreview("../outside.pptx"), /inside/)
})

test("independent preview failure preserves the last committed pair", async () => {
  const pptx = path.join(folder, "ai-changes-both-sides.pptx")
  const manifest = path.join(folder, "ai-changes-both-sides.manifest.json")
  const before = [await readFile(pptx), await readFile(manifest)]
  await assert.rejects(
    renderIndependentPreview(pptx, { UA_SOFFICE: "/missing-ua-renderer/soffice" }),
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
