#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

changelog_path = ROOT / "CHANGELOG.md"
changelog = changelog_path.read_text(encoding="utf-8")
old_changelog = "- Added a deployment-independent publication pipeline that keeps Markdown canonical while providing generic Quartz-to-PDF export, explicit standalone-article and long-form working-paper commands, publication title/metadata pages, page numbering, automatic TOC for long PDFs, manifests and checksums, visual PDF verification, readability-preserving Figure 8 rendition splitting, and reusable SVG/PNG/Medium/LinkedIn publication assets."
new_changelog = "- Added a deployment-independent PDF publication pipeline that keeps Markdown canonical while providing generic Quartz-to-PDF export, explicit standalone-article and long-form working-paper commands, publication title/metadata pages, page numbering, automatic TOC for long PDFs, rollback-protected PDF/manifest bundles, provenance checksums, visual verification, readability-preserving Figure 8 rendition splitting, and path-aware end-to-end publication validation."
if changelog.count(old_changelog) != 1:
    raise SystemExit("Expected publication changelog entry was not found exactly once")
changelog_path.write_text(changelog.replace(old_changelog, new_changelog), encoding="utf-8")

roadmap_path = ROOT / "ROADMAP.md"
roadmap = roadmap_path.read_text(encoding="utf-8")
old_roadmap = "- deployment-independent publication rendering from canonical Markdown to PDF and reusable platform assets, with draft-only temporary builds, provenance manifests, visual verification, and explicit standalone-publication versus working-paper outputs;"
new_roadmap = "- deployment-independent publication rendering from canonical Markdown to PDF, with draft-only temporary builds, rollback-protected provenance manifests, visual verification, path-aware end-to-end validation, and explicit standalone-publication versus working-paper outputs;"
if roadmap.count(old_roadmap) != 1:
    raise SystemExit("Expected publication roadmap entry was not found exactly once")
roadmap_path.write_text(roadmap.replace(old_roadmap, new_roadmap), encoding="utf-8")

contract_path = ROOT / ".github/policy/repository-contract-change-coupling.json"
contract = json.loads(contract_path.read_text(encoding="utf-8"))
removed_required = {
    "quartz/scripts/render-publication-assets.mjs",
    "quartz/scripts/run-publication-assets.mjs",
}
contract["required_paths"] = [
    entry for entry in contract["required_paths"] if entry["path"] not in removed_required
]
publication_workflow = ".github/workflows/publication-render.yml"
if not any(entry["path"] == publication_workflow for entry in contract["required_paths"]):
    insert_at = next(
        (
            index + 1
            for index, entry in enumerate(contract["required_paths"])
            if entry["path"] == ".github/workflows/build-integrity.yml"
        ),
        len(contract["required_paths"]),
    )
    contract["required_paths"].insert(
        insert_at,
        {"path": publication_workflow, "type": "file"},
    )

critical = []
for entry in contract["critical_files"]:
    path = entry["path"]
    if path in removed_required:
        continue
    if path == ".github/workflows/build-integrity.yml":
        entry["required_text"] = [
            "name: Build integrity",
            "Build / Quartz production site",
            "PDF export / regression tests",
            "Content / render Mermaid diagrams",
            "Supply chain / workflows and pins",
            "Run supply-chain regression fixtures",
            "zizmor --pedantic",
        ]
    elif path == ".github/workflows/export-research-pdf.yml":
        entry["required_text"] = [
            "name: Export research PDF",
            "workflow_dispatch:",
            "content/research/notes/thinking-systems-publication-draft.md",
            "npm run pdf:article",
            "npm run pdf:verify",
            "actions/upload-artifact@",
            "fetch-depth: 0",
            "UA_PDF_REPOSITORY_REF: ${{ github.sha }}",
        ]
    elif path == "quartz/scripts/render-publication-pdf.mjs":
        entry["required_text"] = [
            "finalizePublicationBundle",
            "source_state",
            "requireFigure8Split",
            "stagedManifestPath",
        ]
    critical.append(entry)
contract["critical_files"] = critical
publication_critical = {
    "path": publication_workflow,
    "required_text": [
        "name: Publication render",
        "pull_request:",
        "paths:",
        "Publication / article and working paper",
        "Install Chromium and PDF inspection tools",
        "Render current publication PDF",
        "Visual verify current publication PDF",
        "Render living working paper PDF",
        "Visual verify living working paper PDF",
        "Upload publication validation artifact",
        "fetch-depth: 0",
        "UA_PDF_REPOSITORY_REF: ${{ github.sha }}",
    ],
}
if not any(entry["path"] == publication_workflow for entry in contract["critical_files"]):
    build_index = next(
        (
            index + 1
            for index, entry in enumerate(contract["critical_files"])
            if entry["path"] == ".github/workflows/build-integrity.yml"
        ),
        len(contract["critical_files"]),
    )
    contract["critical_files"].insert(build_index, publication_critical)
else:
    for index, entry in enumerate(contract["critical_files"]):
        if entry["path"] == publication_workflow:
            contract["critical_files"][index] = publication_critical
            break
contract_path.write_text(json.dumps(contract, indent=2) + "\n", encoding="utf-8")

cases_path = ROOT / ".github/tests/repository_contract/cases.json"
case_manifest = json.loads(cases_path.read_text(encoding="utf-8"))
cases = case_manifest["cases"]
case_name = "publication render workflow deletion is rejected"
if not any(case.get("name") == case_name for case in cases):
    new_case = {
        "name": case_name,
        "mutation": {
            "type": "delete_path",
            "path": publication_workflow,
        },
        "expected_error": f"Missing required file: {publication_workflow}",
    }
    insert_at = next(
        (
            index + 1
            for index, case in enumerate(cases)
            if case.get("name") == "manual publication export workflow deletion is rejected"
        ),
        len(cases),
    )
    cases.insert(insert_at, new_case)

for case in cases:
    if case.get("name") == "publication integration provenance ref deletion is rejected":
        case["mutation"]["path"] = publication_workflow
        case["expected_error"] = f"{publication_workflow}: missing protected text"
        break
else:
    raise SystemExit("Publication provenance fixture was not found")
cases_path.write_text(json.dumps(case_manifest, indent=2) + "\n", encoding="utf-8")

test_path = ROOT / ".github/tests/repository_contract/test_repository_contract.py"
test_text = test_path.read_text(encoding="utf-8")
required_case = '    "publication render workflow deletion is rejected",\n'
if required_case not in test_text:
    insertion = '    "manual publication export workflow deletion is rejected",\n'
    if insertion not in test_text:
        raise SystemExit("Repository contract case insertion point not found")
    test_text = test_text.replace(insertion, insertion + required_case, 1)
test_path.write_text(test_text, encoding="utf-8")

for relative in [
    ".github/scripts/finalize_pr79_metadata.py",
    ".github/workflows/finalize-pr79-metadata.yml",
]:
    path = ROOT / relative
    if path.exists():
        path.unlink()
