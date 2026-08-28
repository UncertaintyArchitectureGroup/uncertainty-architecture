from pathlib import Path

root = Path('.')

# 1) Restore Figure 7 exactly to the pre-PR layout.
p = root / 'content/research/notes/thinking-systems-publication-draft.md'
s = p.read_text()
old = 'Human Authority is substantive only when the person has enough information, time, competence, capacity, independence, and power to change the outcome. An approval button attached to an overloaded queue is not a complete control path.\n\n```mermaid\nflowchart TB\n'
new = 'Human Authority is substantive only when the person has enough information, time, competence, capacity, independence, and power to change the outcome. An approval button attached to an overloaded queue is not a complete control path.\n\n```mermaid\nflowchart LR\n'
if old not in s:
    raise SystemExit('Figure 7 TB marker not found')
p.write_text(s.replace(old, new, 1))

# 2) Revert the publication review baseline because this PR must not redefine Figure 7 visual acceptance.
import subprocess
subprocess.run(['git', 'checkout', 'origin/main', '--', 'quartz/scripts/publication-review-baseline.json'], check=True)

# 3) Make the final verifier platform-only. No PDF production/verification belongs to this PR.
p = root / 'quartz/scripts/verify-publication-package.mjs'
s = p.read_text()
s = s.replace('import { createHash } from "node:crypto";\n', '')
s = s.replace('const pdfPath = path.join(repoRoot, "dist", "pdf", "thinking-systems-when-the-controlled-object-changes.pdf");\nconst pdfManifestPath = path.join(repoRoot, "dist", "pdf", "thinking-systems-when-the-controlled-object-changes.manifest.json");\nconst minimumPlatformLabelPx = 12;\n', '')
start = s.index('function digest(buffer) {')
end = s.index('export function countDataImages', start)
replacement = '''export function assertPlatformFigureInventory(manifest) {\n  assert(Array.isArray(manifest?.figures) && manifest.figures.length === 9, "Expected nine platform figure renditions");\n  const figure8 = manifest.figures.filter((figure) => figure.number === 8).map((figure) => figure.panel);\n  assert(JSON.stringify(figure8) === JSON.stringify(["A", "B"]), "Figure 8A and 8B must travel together");\n}\n\n'''
s = s[:start] + replacement + s[end:]
s = s.replace('  const [platformManifest, assetManifest, pdfManifest, pdfBytes] = await Promise.all([\n    readFile(path.join(renditionRoot, "platform-renditions.manifest.json"), "utf8").then(JSON.parse),\n    readFile(path.join(publicationRoot, "assets.manifest.json"), "utf8").then(JSON.parse),\n    readFile(pdfManifestPath, "utf8").then(JSON.parse),\n    readFile(pdfPath),\n  ]);', '  const [platformManifest, assetManifest] = await Promise.all([\n    readFile(path.join(renditionRoot, "platform-renditions.manifest.json"), "utf8").then(JSON.parse),\n    readFile(path.join(publicationRoot, "assets.manifest.json"), "utf8").then(JSON.parse),\n  ]);')
s = s.replace('  assert(pdfManifest.source_commit_sha === expectedCommit, `PDF provenance ${pdfManifest.source_commit_sha} does not match ${expectedCommit}`);\n  assert(pdfManifest.pdf_sha256 === digest(pdfBytes), "PDF checksum does not match its manifest");\n  assert(Number(pdfManifest.page_count) > 0, "PDF manifest has no page count");\n  assertPlatformFigureReadability(assetManifest);', '  assertPlatformFigureInventory(assetManifest);')
s = s.replace('candidate state, PDF, 9 platform figures, copy-ready HTML, linked-heading fallbacks, and publication furniture are coherent.', 'candidate state, 9 platform figures, copy-ready HTML, linked-heading fallbacks, and publication furniture are coherent.')
p.write_text(s)

# 4) Replace verifier tests with scope-appropriate inventory checks.
p = root / 'quartz/scripts/verify-publication-package.test.mjs'
p.write_text('''import test from "node:test";\nimport assert from "node:assert/strict";\n\nimport { assertPlatformFigureInventory, countDataImages } from "./verify-publication-package.mjs";\n\ntest("platform verifier requires nine figures with Figure 8A and 8B coupled", () => {\n  const figures = Array.from({ length: 7 }, (_, index) => ({ number: index + 1, panel: null }));\n  figures.push({ number: 8, panel: "A" }, { number: 8, panel: "B" });\n  assert.doesNotThrow(() => assertPlatformFigureInventory({ figures }));\n});\n\ntest("platform verifier rejects incomplete Figure 8 coupling", () => {\n  const figures = Array.from({ length: 8 }, (_, index) => ({ number: index + 1, panel: null }));\n  figures.push({ number: 8, panel: "A" });\n  assert.throws(() => assertPlatformFigureInventory({ figures }), /Figure 8A and 8B/);\n});\n\ntest("embedded image counter distinguishes data-URI payloads", () => {\n  assert.equal(countDataImages('<img src="data:image/png;base64,a"><img src="https://example.com/x.png">'), 1);\n});\n''')

# 5) Remove PDF-specific language from publication-facing documentation and release notes.
for rel in [
    'content/research/notes/thinking-systems-platform-renditions.md',
    'quartz/PLATFORM-RENDITIONS.md',
    'CHANGELOG.md',
    'ROADMAP.md',
]:
    p = root / rel
    if not p.exists():
        continue
    lines = p.read_text().splitlines()
    kept = []
    for line in lines:
        low = line.lower()
        if 'standalone publication pdf' in low or 'standalone article pdf' in low:
            continue
        if 'pdf manifest' in low and 'platform' in low:
            continue
        if 'pdf + platform' in low or 'pdf and platform' in low:
            line = line.replace('PDF + platform renditions + ', 'platform renditions + ').replace('PDF and platform renditions', 'platform renditions')
        if 'final package verifier' in low and 'pdf' in low:
            line = line.replace('PDF, ', '').replace('PDF + ', '')
        kept.append(line)
    p.write_text('\n'.join(kept) + '\n')

print('PR93 rescope applied')
