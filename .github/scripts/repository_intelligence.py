#!/usr/bin/env python3
"""Build and query deterministic UA repository-intelligence materializations.

The producer creates one logical Repository Intelligence Projection and two
consumer-specific deterministic views:

* a compact root-level Agent Context Surface for connector/iPad orientation;
* a fuller Graph View for CI/Quartz consumers.

The projection is read-only orientation evidence. Git/GitHub and the owning
repository files remain authoritative. Trusted accepted/proposed comparison is
implemented as a target-owned capability: candidate repository content is read
as bounded Git tree/blob data and candidate producer/schema changes are reported
as unsupported rather than executed or silently trusted.
"""

import argparse
import hashlib
import json
import os
import posixpath
import re
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple, Union
from urllib.parse import unquote

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

try:
    import validate_metadata as metadata_tools
except ImportError as exc:  # pragma: no cover - actionable CLI boundary
    raise SystemExit("Unable to import sibling validate_metadata.py: {}".format(exc))

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONTRACT = ROOT / ".github/policy/repository-intelligence-contract.json"
DEFAULT_SURFACE = ROOT / "assets/repository-intelligence/agent-context.json"
SOURCE_ALGORITHM = "sha256-path-content-v2"

TERM_HEADING = re.compile(r"^###\s+(.+?)\s*$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
BOLD_TEXT = re.compile(r"\*\*([^*]+)\*\*")
TOKEN = re.compile(r"[0-9A-Za-zА-Яа-яІіЇїЄєҐґ]+", re.UNICODE)
RESEARCH_REGISTER_BLOCK = re.compile(
    r"<!--\s*ua-research-register\s*(\{.*?\})\s*-->", re.DOTALL
)
MARKDOWN_TITLE = re.compile(r"^(.*?)(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))$")
GIT_TREE_ENTRY = re.compile(rb"^([0-9]{6}) ([^ ]+) ([0-9a-f]{40})\t(.*)$", re.DOTALL)

RELATION_FIELDS = {
    "related": "RELATED_TO",
    "supersedes": "SUPERSEDES",
    "superseded_by": "SUPERSEDED_BY",
    "source_basis": "SOURCE_BASIS",
}
ARTIFACT_TYPES = {
    "repository-index",
    "repository-guide",
    "repository-process",
    "specification-index",
    "doctrine",
    "glossary",
    "pattern-index",
    "pattern",
    "control-plane-index",
    "control-capability",
    "reference-index",
    "reference-architecture",
    "failure-mode-index",
    "failure-mode",
    "research-index",
    "research-process",
    "research-template",
    "research-traceability",
    "publishing-index",
    "roadmap",
}
STRUCTURAL_ARTIFACTS = {
    ".github/REPOSITORY-INTELLIGENCE.md": "repository-process-owner",
}
MetadataValue = Union[str, bool, int, float, None, List[object]]


class SnapshotBoundaryError(ValueError):
    """Candidate snapshot cannot be interpreted completely inside the trust boundary."""


class ComparisonUnsupported(ValueError):
    """Trusted target producer cannot safely interpret the proposed semantics."""


def repository_path(root: Path, relative: str) -> Optional[Path]:
    if not relative or relative.startswith("/"):
        return None
    pure = PurePosixPath(relative)
    if any(part in ("", ".", "..") for part in pure.parts):
        return None
    root_resolved = root.resolve()
    candidate = root_resolved.joinpath(*pure.parts)
    try:
        candidate.resolve().relative_to(root_resolved)
    except ValueError:
        return None
    return candidate


def relpath(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def as_list(value: MetadataValue) -> List[str]:
    if isinstance(value, list):
        return [str(item) for item in value if item is not None and str(item)]
    if value is None or value == "":
        return []
    return [str(value)]


def load_json(path: Path, label: str) -> Dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError("{} does not exist: {}".format(label, path))
    except json.JSONDecodeError as exc:
        raise ValueError("{} JSON is invalid: {}".format(label, exc))
    if not isinstance(value, dict):
        raise ValueError("{} must be a JSON object: {}".format(label, path))
    return value


def load_contract(path: Path) -> Dict[str, object]:
    contract = load_json(path, "Repository-intelligence contract")
    if contract.get("contract_version") != 1:
        raise ValueError("Unsupported repository-intelligence contract_version")
    relation_semantics = contract.get("relation_semantics")
    if not isinstance(relation_semantics, dict):
        raise ValueError("repository-intelligence contract relation_semantics must be an object")
    for relation, semantics in relation_semantics.items():
        if not isinstance(semantics, dict):
            raise ValueError("relation semantics must be objects: {}".format(relation))
        if semantics.get("edge_class") not in {
            "semantic-evolution", "repository-control", "navigation"
        }:
            raise ValueError("uncontrolled edge_class for {}".format(relation))
        if semantics.get("impact_role") not in {
            "dependency", "ownership", "provenance", "association", "navigation", "control"
        }:
            raise ValueError("uncontrolled impact_role for {}".format(relation))
        if semantics.get("impact_direction") not in {
            "source-to-target", "target-to-source", "both", "none"
        }:
            raise ValueError("uncontrolled impact_direction for {}".format(relation))
    return contract


def load_metadata_contract(root: Path) -> Dict[str, object]:
    return load_json(root / ".github/policy/metadata-contract.json", "Metadata contract")


def is_excluded(relative: str, contract: Dict[str, object]) -> bool:
    return any(
        relative.startswith(str(prefix))
        for prefix in contract.get("frontmatter_exclude_prefixes", [])
    )


def discover_maintained_documents(root: Path, contract: Dict[str, object]) -> List[Path]:
    discovered: Set[Path] = set()
    for relative in contract.get("frontmatter_scan_files", []):
        path = repository_path(root, str(relative))
        if path is not None and path.is_file():
            discovered.add(path)
    for relative in contract.get("required_frontmatter_paths", []):
        path = repository_path(root, str(relative))
        if path is not None and path.is_file():
            discovered.add(path)
    for relative in contract.get("frontmatter_scan_roots", []):
        directory = repository_path(root, str(relative))
        if directory is None or not directory.is_dir():
            continue
        discovered.update(path for path in directory.rglob("*.md") if path.is_file())
    return sorted(
        [path for path in discovered if not is_excluded(relpath(root, path), contract)],
        key=lambda path: relpath(root, path),
    )


def parse_document(path: Path) -> Tuple[Dict[str, MetadataValue], str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeError as exc:
        raise ValueError("{} is not valid UTF-8: {}".format(path, exc))
    frontmatter, _, error = metadata_tools.extract_frontmatter(text)
    if error:
        raise ValueError("{}: {}".format(path, error))
    metadata: Dict[str, MetadataValue] = {}
    if frontmatter is not None:
        metadata, errors = metadata_tools.parse_frontmatter(frontmatter)
        if errors:
            raise ValueError("{}: {}".format(path, "; ".join(errors)))
    title = str(metadata.get("title") or metadata_tools.first_h1(text) or path.stem)
    return metadata, title, text


def artifact_record(
    relative: str,
    metadata: Dict[str, MetadataValue],
    title: str,
    text: str,
    projection_role: str,
) -> Dict[str, object]:
    return {
        "path": relative,
        "title": title,
        "h1": metadata_tools.first_h1(text) or title,
        "module": str(metadata.get("module") or ""),
        "artifact_type": str(metadata.get("artifact_type") or ""),
        "status": str(metadata.get("status") or ""),
        "maturity": str(metadata.get("maturity") or ""),
        "topics": sorted(as_list(metadata.get("topics"))),
        "canonical_for": sorted(as_list(metadata.get("canonical_for"))),
        "relations": {
            field: sorted(as_list(metadata.get(field)))
            for field in RELATION_FIELDS
            if as_list(metadata.get(field))
        },
        "projection_role": projection_role,
    }


def discover_artifacts(root: Path, metadata_contract: Dict[str, object]) -> List[Dict[str, object]]:
    artifacts: Dict[str, Dict[str, object]] = {}
    for path in discover_maintained_documents(root, metadata_contract):
        relative = relpath(root, path)
        metadata, title, text = parse_document(path)
        artifact_type = str(metadata.get("artifact_type") or "")
        if artifact_type not in ARTIFACT_TYPES:
            continue
        artifacts[relative] = artifact_record(
            relative,
            metadata,
            title,
            text,
            "maintained-conceptual-process-artifact",
        )
    for relative, projection_role in STRUCTURAL_ARTIFACTS.items():
        if relative in artifacts:
            continue
        path = repository_path(root, relative)
        if path is None or not path.is_file():
            continue
        metadata, title, text = parse_document(path)
        artifacts[relative] = artifact_record(
            relative, metadata, title, text, projection_role
        )
    inactive = set(metadata_contract["canonical_ownership"]["inactive_maturities"])
    for artifact in artifacts.values():
        # Preserve historical declarations for inspection, without presenting
        # retired claims as current owners or active uniqueness violations.
        artifact["canonical_owner_active"] = artifact["maturity"] not in inactive
    return [artifacts[path] for path in sorted(artifacts)]


def split_glossary_sections(text: str) -> List[Tuple[str, str]]:
    matches = list(TERM_HEADING.finditer(text))
    sections: List[Tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match.group(1).strip(), text[start:end].strip()))
    return sections


def normalize_text(value: str) -> str:
    return " ".join(TOKEN.findall(value.casefold().replace("-", " ")))


def token_set(value: str) -> Set[str]:
    return set(normalize_text(value).split())


def slugify(value: str) -> str:
    normalized = normalize_text(value).replace(" ", "-")
    return normalized or hashlib.sha256(value.encode("utf-8")).hexdigest()[:12]


def explicit_predecessors(term: str, body: str) -> List[str]:
    predecessors: Set[str] = set()
    sentences = re.split(r"(?<=[.!?])\s+", body)
    for sentence in sentences:
        lower = sentence.casefold()
        if "historical predecessor" not in lower and not (
            "earlier" in lower and " used " in " {} ".format(lower)
        ):
            continue
        for candidate in BOLD_TEXT.findall(sentence):
            label = candidate.strip()
            if label and normalize_text(label) != normalize_text(term):
                predecessors.add(label)
    return sorted(predecessors, key=str.casefold)


def discover_terms(root: Path) -> List[Dict[str, object]]:
    glossary = root / "00-doctrine/glossary.md"
    if not glossary.is_file():
        raise ValueError("Canonical glossary does not exist: {}".format(glossary))
    text = glossary.read_text(encoding="utf-8")
    return [
        {
            "term": term,
            "path": "00-doctrine/glossary.md",
            "anchor": slugify(term),
            "predecessors": explicit_predecessors(term, body),
        }
        for term, body in split_glossary_sections(text)
    ]


def discover_instructions(root: Path) -> List[Dict[str, str]]:
    instructions: List[Dict[str, str]] = []
    for path in sorted(root.rglob("AGENTS.md"), key=lambda item: relpath(root, item)):
        if any(part in {"node_modules", ".git", "dist"} for part in path.parts):
            continue
        relative = relpath(root, path)
        parent = PurePosixPath(relative).parent.as_posix()
        instructions.append(
            {
                "path": relative,
                "scope_root": "." if parent == "." else parent,
            }
        )
    return instructions


def parse_research_items(root: Path) -> List[Dict[str, object]]:
    path = root / "content/research/research-register.md"
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8")
    match = RESEARCH_REGISTER_BLOCK.search(text)
    if not match:
        return []
    try:
        block = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise ValueError("Research register machine block is invalid JSON: {}".format(exc))
    items = block.get("items", [])
    if not isinstance(items, list):
        raise ValueError("Research register machine block items must be a list")
    normalized: List[Dict[str, object]] = []
    for item in items:
        if not isinstance(item, dict) or not item.get("id"):
            continue
        normalized.append({str(key): value for key, value in item.items()})
    return sorted(normalized, key=lambda item: str(item["id"]))


def discover_validation_surfaces(root: Path) -> Dict[str, object]:
    policies = sorted(
        relpath(root, path)
        for path in (root / ".github/policy").glob("*.json")
        if path.is_file()
    )
    validators = sorted(
        relpath(root, path)
        for path in (root / ".github/scripts").glob("validate_*.py")
        if path.is_file()
    )
    workflows = sorted(
        relpath(root, path)
        for path in (root / ".github/workflows").glob("*.yml")
        if path.is_file()
    )
    tests = sorted(
        relpath(root, path)
        for path in (root / ".github/tests").rglob("test_*.py")
        if path.is_file()
    )
    package_scripts: List[str] = []
    package_path = root / "package.json"
    if package_path.is_file():
        package = load_json(package_path, "package.json")
        scripts = package.get("scripts", {})
        if isinstance(scripts, dict):
            package_scripts = sorted(str(key) for key in scripts)
    return {
        "policies": policies,
        "validators": validators,
        "workflows": workflows,
        "tests": tests,
        "package_scripts": package_scripts,
    }


def all_repository_files(root: Path) -> Set[str]:
    result: Set[str] = set()
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in {".git", "node_modules", "dist"} for part in path.parts):
            continue
        result.add(relpath(root, path))
    return result


def strip_optional_markdown_title(raw: str) -> str:
    match = MARKDOWN_TITLE.match(raw)
    return match.group(1).strip() if match else raw


def resolve_local_target(source: str, target: str, repository_files: Set[str]) -> Tuple[Optional[str], bool]:
    raw = target.strip().strip("<>")
    raw = strip_optional_markdown_title(raw)
    if not raw or raw.startswith(("#", "http://", "https://", "mailto:", "data:")):
        return None, False
    without_fragment = unquote(raw.split("#", 1)[0].split("?", 1)[0])
    if not without_fragment:
        return None, False
    normalized = posixpath.normpath(posixpath.join(posixpath.dirname(source), without_fragment))
    if normalized == ".." or normalized.startswith("../") or normalized.startswith("/"):
        return normalized, True
    candidates = [normalized]
    if PurePosixPath(normalized).suffix == "":
        candidates.extend([normalized.rstrip("/") + "/README.md", normalized + ".md"])
    for candidate in candidates:
        if candidate in repository_files:
            return candidate, True
    return normalized, True


def node_id(kind: str, identity: str) -> str:
    return "{}:{}".format(kind, identity)


def document_node(artifact: Dict[str, object]) -> Dict[str, object]:
    return {
        "id": node_id("document", str(artifact["path"])),
        "family": "Document",
        "identity": str(artifact["path"]),
        "path": artifact["path"],
        "title": artifact["title"],
        "module": artifact.get("module", ""),
        "artifact_type": artifact.get("artifact_type", ""),
        "status": artifact.get("status", ""),
        "maturity": artifact.get("maturity", ""),
        "topics": artifact.get("topics", []),
        "canonical_for": artifact.get("canonical_for", []),
        "canonical_owner_active": artifact.get("canonical_owner_active", True),
        "projection_role": artifact.get(
            "projection_role", "maintained-conceptual-process-artifact"
        ),
    }


def support_document_node(root: Path, path: str) -> Dict[str, object]:
    title = PurePosixPath(path).stem
    absolute = repository_path(root, path)
    if absolute is not None and absolute.is_file() and absolute.suffix.lower() == ".md":
        try:
            metadata, parsed_title, _ = parse_document(absolute)
            return {
                "id": node_id("document", path),
                "family": "Document",
                "identity": path,
                "path": path,
                "title": parsed_title,
                "module": str(metadata.get("module") or ""),
                "artifact_type": str(metadata.get("artifact_type") or ""),
                "status": str(metadata.get("status") or ""),
                "projection_role": "explicit-relation-target",
            }
        except ValueError:
            pass
    return {
        "id": node_id("document", path),
        "family": "Document",
        "identity": path,
        "path": path,
        "title": title,
        "projection_role": "explicit-relation-target",
    }


def relation_semantics(contract: Dict[str, object], relation: str) -> Dict[str, str]:
    raw = contract.get("relation_semantics", {}).get(relation)
    if not isinstance(raw, dict):
        raise ValueError("No impact semantics declared for relation {}".format(relation))
    return {
        "edge_class": str(raw["edge_class"]),
        "impact_role": str(raw["impact_role"]),
        "impact_direction": str(raw["impact_direction"]),
    }


def edge(
    contract: Dict[str, object],
    source: str,
    relation: str,
    target: str,
    provenance_path: str,
    provenance_kind: str,
    detail: str,
) -> Dict[str, object]:
    semantics = relation_semantics(contract, relation)
    stable = "\0".join([source, relation, target, provenance_path, provenance_kind, detail])
    return {
        "id": hashlib.sha256(stable.encode("utf-8")).hexdigest()[:20],
        "source": source,
        "relation": relation,
        "target": target,
        "edge_class": semantics["edge_class"],
        "impact_role": semantics["impact_role"],
        "impact_direction": semantics["impact_direction"],
        "provenance": {
            "path": provenance_path,
            "kind": provenance_kind,
            "detail": detail,
        },
    }


def signal(
    signal_class: str,
    subjects: Sequence[str],
    evidence_path: str,
    evidence: str,
    severity: str,
    disposition: str,
) -> Dict[str, object]:
    stable = "\0".join(
        [signal_class, *sorted(subjects), evidence_path, evidence, severity, disposition]
    )
    return {
        "id": hashlib.sha256(stable.encode("utf-8")).hexdigest()[:20],
        "class": signal_class,
        "subjects": sorted(subjects),
        "origin": "deterministic",
        "evidence": {"path": evidence_path, "detail": evidence},
        "severity": severity,
        "disposition": disposition,
    }


def build_graph(
    root: Path,
    contract: Dict[str, object],
    artifacts: Sequence[Dict[str, object]],
    terms: Sequence[Dict[str, object]],
    instructions: Sequence[Dict[str, str]],
    research_items: Sequence[Dict[str, object]],
    validation: Dict[str, object],
    metadata_contract: Dict[str, object],
) -> Tuple[List[Dict[str, object]], List[Dict[str, object]], List[Dict[str, object]], Set[str]]:
    nodes: Dict[str, Dict[str, object]] = {}
    edges: Dict[str, Dict[str, object]] = {}
    signals: Dict[str, Dict[str, object]] = {}
    relation_targets: Set[str] = set()
    repository_files = all_repository_files(root)

    def add_node(value: Dict[str, object]) -> str:
        identifier = str(value["id"])
        nodes.setdefault(identifier, value)
        return identifier

    def add_edge(value: Dict[str, object]) -> None:
        edges[str(value["id"])] = value

    def add_signal(value: Dict[str, object]) -> None:
        signals[str(value["id"])] = value

    artifact_by_path = {str(item["path"]): item for item in artifacts}
    for artifact in artifacts:
        add_node(document_node(artifact))

    glossary_id = node_id("document", "00-doctrine/glossary.md")
    for term in terms:
        term_identifier = add_node(
            {
                "id": node_id("term", str(term["term"])),
                "family": "Term",
                "identity": str(term["term"]),
                "term": term["term"],
                "path": term["path"],
                "anchor": term["anchor"],
                "predecessors": term.get("predecessors", []),
            }
        )
        if glossary_id in nodes:
            add_edge(
                edge(
                    contract,
                    glossary_id,
                    "DEFINES",
                    term_identifier,
                    "00-doctrine/glossary.md",
                    "heading",
                    "### {}".format(term["term"]),
                )
            )

    instruction_ids: Dict[str, str] = {}
    for instruction in instructions:
        identifier = add_node(
            {
                "id": node_id("agent-scope", str(instruction["path"])),
                "family": "AgentScope",
                "identity": instruction["path"],
                "path": instruction["path"],
                "scope_root": instruction["scope_root"],
            }
        )
        instruction_ids[str(instruction["path"])] = identifier

    for artifact in artifacts:
        document_identifier = node_id("document", str(artifact["path"]))
        path = str(artifact["path"])
        for instruction in instructions:
            scope = str(instruction["scope_root"])
            if scope == "." or path == scope or path.startswith(scope.rstrip("/") + "/"):
                add_edge(
                    edge(
                        contract,
                        document_identifier,
                        "SCOPED_BY",
                        instruction_ids[str(instruction["path"])],
                        str(instruction["path"]),
                        "structural-scope",
                        scope,
                    )
                )

    responsibility_claimants: Dict[str, List[str]] = {}
    for artifact in artifacts:
        document_identifier = node_id("document", str(artifact["path"]))
        for claim in artifact.get("canonical_for", []):
            claim = str(claim)
            responsibility_identifier = add_node(
                {
                    "id": node_id("responsibility", claim),
                    "family": "Responsibility",
                    "identity": claim,
                    "responsibility": claim,
                }
            )
            add_edge(
                edge(
                    contract,
                    document_identifier,
                    "CANONICAL_FOR",
                    responsibility_identifier,
                    str(artifact["path"]),
                    "frontmatter",
                    "canonical_for: {}".format(claim),
                )
            )
            if artifact["canonical_owner_active"]:
                responsibility_claimants.setdefault(claim, []).append(document_identifier)

    allowed_duplicates = set(metadata_contract["canonical_ownership"]["allow_duplicate_values"])
    for claim, claimants in sorted(responsibility_claimants.items()):
        if len(claimants) > 1 and claim not in allowed_duplicates:
            add_signal(
                signal(
                    "duplicate-active-canonical-claim",
                    claimants,
                    ".github/policy/metadata-contract.json",
                    "canonical_for {!r} is claimed by {} active projected artifacts".format(
                        claim, len(claimants)
                    ),
                    "error",
                    "blocking",
                )
            )

    for artifact in artifacts:
        source_path = str(artifact["path"])
        source_identifier = node_id("document", source_path)
        for field, relation in RELATION_FIELDS.items():
            for raw_target in artifact.get("relations", {}).get(field, []):
                resolved, local = resolve_local_target(source_path, str(raw_target), repository_files)
                if not local:
                    continue
                if resolved is None or resolved not in repository_files:
                    add_signal(
                        signal(
                            "missing-explicit-relation-target",
                            [source_identifier],
                            source_path,
                            "{} declares {}={!r}, but no repository target resolves".format(
                                source_path, field, raw_target
                            ),
                            "error",
                            "blocking",
                        )
                    )
                    continue
                relation_targets.add(resolved)
                target_identifier = node_id("document", resolved)
                if target_identifier not in nodes:
                    add_node(support_document_node(root, resolved))
                add_edge(
                    edge(
                        contract,
                        source_identifier,
                        relation,
                        target_identifier,
                        source_path,
                        "frontmatter",
                        "{}: {}".format(field, raw_target),
                    )
                )

        text = (root / source_path).read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            resolved, local = resolve_local_target(source_path, raw_target, repository_files)
            if not local or resolved is None or resolved not in repository_files:
                continue
            relation_targets.add(resolved)
            target_identifier = node_id("document", resolved)
            if target_identifier not in nodes and resolved in artifact_by_path:
                add_node(document_node(artifact_by_path[resolved]))
            if target_identifier not in nodes:
                add_node(support_document_node(root, resolved))
            if target_identifier == source_identifier:
                continue
            add_edge(
                edge(
                    contract,
                    source_identifier,
                    "LINKS_TO",
                    target_identifier,
                    source_path,
                    "markdown-link",
                    raw_target,
                )
            )

    for item in research_items:
        research_id = add_node(
            {
                "id": node_id("research", str(item["id"])),
                "family": "ResearchItem",
                "identity": item["id"],
                "research_id": item["id"],
                "title": item.get("title", ""),
                "item_class": item.get("item_class", ""),
                "status": item.get("status", ""),
                "origin_kind": item.get("origin_kind", ""),
                "provenance_record": item.get("provenance_record"),
                "next_step": item.get("next_step", ""),
            }
        )
        for field, relation in (
            ("owning_record", "RESEARCH_OWNER"),
            ("framework_destination", "FRAMEWORK_DESTINATION"),
        ):
            raw_target = item.get(field)
            if not raw_target:
                continue
            target_path = str(raw_target)
            if target_path not in repository_files:
                add_signal(
                    signal(
                        "missing-research-route-target",
                        [research_id],
                        "content/research/research-register.md",
                        "research item {} declares {}={!r}, but the path is missing".format(
                            item["id"], field, target_path
                        ),
                        "error",
                        "blocking",
                    )
                )
                continue
            relation_targets.add(target_path)
            target_identifier = node_id("document", target_path)
            if target_identifier not in nodes:
                add_node(support_document_node(root, target_path))
            add_edge(
                edge(
                    contract,
                    research_id,
                    relation,
                    target_identifier,
                    "content/research/research-register.md",
                    "research-register",
                    "{}: {}".format(field, target_path),
                )
            )

    validation_node_ids: Dict[str, str] = {}
    for category in ("policies", "validators", "workflows"):
        for path in validation.get(category, []):
            identifier = add_node(
                {
                    "id": node_id("policy", str(path)),
                    "family": "PolicyOrValidator",
                    "identity": path,
                    "path": path,
                    "kind": category[:-1] if category.endswith("s") else category,
                }
            )
            validation_node_ids[str(path)] = identifier

    metadata_validator = validation_node_ids.get(".github/scripts/validate_metadata.py")
    if metadata_validator:
        for artifact in artifacts:
            if artifact.get("projection_role") != "maintained-conceptual-process-artifact":
                continue
            add_edge(
                edge(
                    contract,
                    node_id("document", str(artifact["path"])),
                    "VALIDATED_BY",
                    metadata_validator,
                    ".github/policy/metadata-contract.json",
                    "metadata-scan-contract",
                    "maintained document is included in the metadata scan",
                )
            )

    return (
        sorted(nodes.values(), key=lambda item: str(item["id"])),
        sorted(edges.values(), key=lambda item: str(item["id"])),
        sorted(signals.values(), key=lambda item: str(item["id"])),
        relation_targets,
    )


def source_input_records(
    root: Path,
    contract: Dict[str, object],
    artifacts: Sequence[Dict[str, object]],
    instructions: Sequence[Dict[str, str]],
    validation: Dict[str, object],
    relation_targets: Iterable[str],
) -> List[Dict[str, str]]:
    records: Dict[str, str] = {}
    for item in artifacts:
        records[str(item["path"])] = "content"
    for item in instructions:
        records[str(item["path"])] = "content"
    for fixed in (
        ".github/REPOSITORY-INTELLIGENCE.md",
        ".github/policy/metadata-contract.json",
        ".github/policy/repository-intelligence-contract.json",
        "00-doctrine/glossary.md",
        "content/research/research-register.md",
        "DOCUMENT-METADATA.md",
        "package.json",
    ):
        if (root / fixed).is_file():
            records[fixed] = "content"
    for path in relation_targets:
        # Support Markdown nodes expose parsed titles/classification too. Their
        # bytes affect both views even when the document is outside preflight.
        mode = "content" if PurePosixPath(str(path)).suffix.lower() == ".md" else "existence"
        records.setdefault(str(path), mode)
    # Validation surfaces are projected as paths only. Their existence changes the
    # projection, while their executable content remains owned by the repository.
    for category in ("policies", "validators", "workflows", "tests"):
        for path in validation.get(category, []):
            records.setdefault(str(path), "existence")
    records.pop(str(contract.get("compact_surface_path", "assets/repository-intelligence/agent-context.json")), None)
    return [
        {"path": path, "identity_mode": records[path]}
        for path in sorted(records)
    ]


def compute_source_identity(root: Path, records: Sequence[Dict[str, str]]) -> Dict[str, object]:
    aggregate = hashlib.sha256()
    aggregate.update((SOURCE_ALGORITHM + "\0").encode("utf-8"))
    for record in records:
        relative = str(record["path"])
        mode = str(record["identity_mode"])
        path = repository_path(root, relative)
        if path is None or not path.is_file():
            raise ValueError("Indexed input is missing or unsafe: {}".format(relative))
        if mode == "content":
            content_digest = hashlib.sha256(path.read_bytes()).hexdigest()
            identity = "content:" + content_digest
        elif mode == "existence":
            identity = "exists"
        else:
            raise ValueError("Unsupported source identity mode: {}".format(mode))
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(identity.encode("ascii"))
        aggregate.update(b"\n")
    return {
        "algorithm": SOURCE_ALGORITHM,
        "digest": aggregate.hexdigest(),
        "input_count": len(records),
        "inputs": list(records),
        "excluded_outputs": ["assets/repository-intelligence/agent-context.json"],
    }


def producer_identity(root: Path, contract: Dict[str, object]) -> Dict[str, object]:
    paths = [str(item) for item in contract.get("interpretation_paths", [])]
    values: List[Dict[str, str]] = []
    aggregate = hashlib.sha256()
    for relative in paths:
        path = repository_path(root, relative)
        if path is None or not path.is_file():
            digest = "missing"
        else:
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
        values.append({"path": relative, "sha256": digest})
        aggregate.update(relative.encode("utf-8") + b"\0" + digest.encode("ascii") + b"\n")
    return {
        "implementation": ".github/scripts/repository_intelligence.py",
        "contract": ".github/policy/repository-intelligence-contract.json",
        "producer_version": int(contract["producer_version"]),
        "schema_version": int(contract["schema_version"]),
        "interpretation_digest": aggregate.hexdigest(),
        "interpretation_paths": values,
    }


def build_projection(root: Path, contract_path: Optional[Path] = None) -> Dict[str, object]:
    contract_path = contract_path or root / ".github/policy/repository-intelligence-contract.json"
    contract = load_contract(contract_path)
    metadata_contract = load_metadata_contract(root)
    artifacts = discover_artifacts(root, metadata_contract)
    terms = discover_terms(root)
    instructions = discover_instructions(root)
    research_items = parse_research_items(root)
    validation = discover_validation_surfaces(root)
    nodes, edges, signals, relation_targets = build_graph(
        root, contract, artifacts, terms, instructions, research_items, validation, metadata_contract
    )
    records = source_input_records(
        root, contract, artifacts, instructions, validation, relation_targets
    )
    return {
        "schema_version": int(contract["schema_version"]),
        "producer": producer_identity(root, contract),
        "source_identity": compute_source_identity(root, records),
        "inventories": {
            "instructions": instructions,
            "terms": terms,
            "artifacts": artifacts,
            "research_items": research_items,
        },
        "graph": {"nodes": nodes, "edges": edges, "signals": signals},
        "validation_surfaces": validation,
    }


def materialize_agent_surface(projection: Dict[str, object], contract: Dict[str, object]) -> Dict[str, object]:
    compact_relations = set(str(item) for item in contract.get("compact_relation_types", []))
    compact_edges = [
        item for item in projection["graph"]["edges"]
        if str(item.get("relation")) in compact_relations
    ]
    compact_node_ids: Set[str] = set()
    for item in compact_edges:
        compact_node_ids.add(str(item["source"]))
        compact_node_ids.add(str(item["target"]))
    compact_nodes = [
        node for node in projection["graph"]["nodes"]
        if str(node["id"]) in compact_node_ids
    ]
    return {
        "schema_version": projection["schema_version"],
        "view": "agent-context",
        "producer": projection["producer"],
        "source_identity": projection["source_identity"],
        "inventories": projection["inventories"],
        "high_value_graph": {
            "nodes": compact_nodes,
            "edges": compact_edges,
            "signals": projection["graph"]["signals"],
        },
        "validation_surfaces": projection["validation_surfaces"],
    }


def materialize_graph_view(projection: Dict[str, object]) -> Dict[str, object]:
    return {
        "schema_version": projection["schema_version"],
        "view": "graph",
        "producer": projection["producer"],
        "source_identity": projection["source_identity"],
        "graph": projection["graph"],
    }


def serialize_json(value: Dict[str, object]) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def score_fields(query: str, fields: Sequence[Tuple[str, str]]) -> Tuple[int, List[str]]:
    query_normal = normalize_text(query)
    query_tokens = token_set(query)
    score = 0
    reasons: List[str] = []
    for label, value in fields:
        normalized = normalize_text(value)
        if not normalized:
            continue
        if query_normal and query_normal == normalized:
            score += 100
            reasons.append("exact {}".format(label))
            continue
        if query_normal and query_normal in normalized:
            score += 25
            reasons.append("phrase in {}".format(label))
        elif normalized in query_normal:
            score += 20
            reasons.append("{} in task".format(label))
        overlap = query_tokens & token_set(value)
        if overlap:
            score += 5 * len(overlap)
            reasons.append("{} token overlap: {}".format(label, ", ".join(sorted(overlap))))
    return score, reasons


def inventories(surface: Dict[str, object]) -> Dict[str, object]:
    value = surface.get("inventories", {})
    return value if isinstance(value, dict) else {}


def term_preflight(surface: Dict[str, object], query: str) -> Dict[str, object]:
    term_inventory = inventories(surface).get("terms", [])
    candidates: List[Dict[str, object]] = []
    for term in term_inventory:
        fields: List[Tuple[str, str]] = [("term", str(term["term"]))]
        fields.extend(("predecessor", str(item)) for item in term.get("predecessors", []))
        score, reasons = score_fields(query, fields)
        if score:
            candidates.append(
                {
                    "term": term["term"],
                    "path": term["path"],
                    "anchor": term["anchor"],
                    "predecessors": term.get("predecessors", []),
                    "score": score,
                    "reasons": reasons,
                }
            )
    candidates.sort(key=lambda item: (-int(item["score"]), str(item["term"]).casefold()))
    return {
        "operation": "term_preflight",
        "query": query,
        "inventory": term_inventory,
        "candidates": candidates,
        "decision_boundary": "Candidates are orientation only; read the owning glossary/doctrine before creating or renaming a term.",
    }


def artifact_role(artifact: Dict[str, object]) -> str:
    if not artifact.get("canonical_owner_active", True):
        return "inactive_artifact"
    path = str(artifact.get("path", ""))
    artifact_type = str(artifact.get("artifact_type", ""))
    module = str(artifact.get("module", ""))
    if path == ".github/REPOSITORY-INTELLIGENCE.md":
        return "repository_process_owner"
    if path == "content/research/research-register.md":
        return "research_state_owner"
    if artifact_type == "glossary":
        return "definition_owner"
    if artifact_type.startswith("repository-") or artifact_type in {"roadmap", "publishing-index"}:
        return "repository_process_owner"
    if artifact_type == "research-traceability":
        return "research_disposition_owner"
    if artifact_type.startswith("research-"):
        return "research_surface"
    if module in {"doctrine", "patterns", "control-plane"} or artifact_type == "specification-index":
        return "semantic_owner_candidate"
    if module in {"reference-architectures", "failure-modes"}:
        return "supporting_semantic_surface"
    return "maintained_artifact"


def artifact_preflight(surface: Dict[str, object], query: str) -> Dict[str, object]:
    artifact_inventory = inventories(surface).get("artifacts", [])
    candidates: List[Dict[str, object]] = []
    for artifact in artifact_inventory:
        fields: List[Tuple[str, str]] = [
            ("title", str(artifact.get("title", ""))),
            ("path", str(artifact.get("path", ""))),
            ("module", str(artifact.get("module", ""))),
            ("artifact_type", str(artifact.get("artifact_type", ""))),
        ]
        fields.extend(("topic", str(item)) for item in artifact.get("topics", []))
        fields.extend(("canonical_for", str(item)) for item in artifact.get("canonical_for", []))
        score, reasons = score_fields(query, fields)
        if score:
            candidates.append(
                {
                    "path": artifact["path"],
                    "title": artifact["title"],
                    "role": artifact_role(artifact),
                    "module": artifact.get("module", ""),
                    "artifact_type": artifact.get("artifact_type", ""),
                    "status": artifact.get("status", ""),
                    "canonical_for": artifact.get("canonical_for", []),
                    "canonical_owner_active": artifact.get("canonical_owner_active", True),
                    "score": score,
                    "reasons": reasons,
                }
            )
    candidates.sort(key=lambda item: (-int(item["score"]), str(item["path"])))
    return {
        "operation": "artifact_preflight",
        "query": query,
        "inventory": artifact_inventory,
        "candidates": candidates,
        "decision_boundary": "Candidates are orientation only; establish why an existing owner cannot be refined before creating a maintained conceptual/process artifact.",
    }


def find_owner(surface: Dict[str, object], query: str) -> Dict[str, object]:
    owners: List[Dict[str, object]] = []
    for artifact in inventories(surface).get("artifacts", []):
        if not artifact.get("canonical_owner_active", True):
            continue
        for claim in artifact.get("canonical_for", []):
            score, reasons = score_fields(query, [("canonical_for", str(claim))])
            if score:
                owners.append(
                    {
                        "path": artifact["path"],
                        "title": artifact["title"],
                        "role": "machine_responsibility_claim",
                        "responsibility": claim,
                        "score": score,
                        "reasons": reasons,
                    }
                )
    for item in term_preflight(surface, query)["candidates"][:10]:
        owners.append(
            {
                "path": item["path"],
                "title": item["term"],
                "role": "definition_owner",
                "score": item["score"],
                "reasons": item["reasons"],
            }
        )
    for item in artifact_preflight(surface, query)["candidates"][:20]:
        owners.append(
            {
                "path": item["path"],
                "title": item["title"],
                "role": item["role"],
                "score": item["score"],
                "reasons": item["reasons"],
                "canonical_for": item.get("canonical_for", []),
            }
        )
    for item in inventories(surface).get("research_items", []):
        fields = [
            ("research_id", str(item.get("id", ""))),
            ("title", str(item.get("title", ""))),
            ("next_step", str(item.get("next_step", ""))),
        ]
        score, reasons = score_fields(query, fields)
        if not score:
            continue
        owners.append(
            {
                "path": "content/research/research-register.md",
                "title": str(item.get("title") or item.get("id")),
                "role": "research_state_owner",
                "research_id": item.get("id"),
                "score": score,
                "reasons": reasons,
            }
        )
    for path in surface.get("validation_surfaces", {}).get("validators", []):
        score, reasons = score_fields(query, [("implementation_path", str(path))])
        if score:
            owners.append(
                {
                    "path": path,
                    "title": PurePosixPath(str(path)).name,
                    "role": "implementation_surface",
                    "score": score,
                    "reasons": reasons,
                }
            )
    # Exact source evidence precedes aggregate lexical overlap. This orders
    # retrieval candidates; it never grants authority or resolves conflicts.
    exact_evidence = {"exact canonical_for", "exact term", "exact path", "exact research_id", "exact implementation_path"}
    owners.sort(key=lambda item: (
        item["role"] == "inactive_artifact",
        not bool(exact_evidence.intersection(item["reasons"])),
        -int(item["score"]), str(item["path"]), str(item["role"]),
    ))
    deduped: List[Dict[str, object]] = []
    seen: Set[Tuple[str, str, str]] = set()
    for owner in owners:
        key = (
            str(owner["path"]),
            str(owner["role"]),
            str(owner.get("responsibility") or owner.get("research_id") or ""),
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(owner)
    return {
        "operation": "find_owner",
        "query": query,
        "candidates": deduped[:20],
        "authority_boundary": "Retrieval discovers typed candidates and evidence roles; semantic authority remains in the owning source and must be read before decision.",
    }


def likely_instruction_paths(
    surface: Dict[str, object], query: str, paths: Sequence[str] = ()
) -> List[Dict[str, str]]:
    selected: List[Dict[str, str]] = []
    query_tokens = token_set(query)
    for item in inventories(surface).get("instructions", []):
        scope = str(item.get("scope_root", "."))
        path = str(item.get("path", ""))
        if path == "AGENTS.md":
            selected.append(item)
            continue
        scope_tokens = token_set(scope.replace("/", " "))
        covers_candidate = any(path == scope or path.startswith(scope.rstrip("/") + "/") for path in paths)
        if scope != "." and (covers_candidate or scope in query or scope_tokens & query_tokens):
            selected.append(item)
    return selected


def validation_plan(surface: Dict[str, object], query: str) -> Dict[str, object]:
    normalized = normalize_text(query)
    tokens = token_set(query)
    validators: Set[str] = set()
    workflows: Set[str] = set()
    tests: Set[str] = set()
    package_scripts: Set[str] = set()
    companion_candidates: Set[str] = set()
    available = surface.get("validation_surfaces", {})
    available_validators = set(str(item) for item in available.get("validators", []))
    available_workflows = set(str(item) for item in available.get("workflows", []))
    available_tests = set(str(item) for item in available.get("tests", []))
    available_package = set(str(item) for item in available.get("package_scripts", []))

    def add(target: Set[str], value: str, available_values: Set[str]) -> None:
        if value in available_values:
            target.add(value)

    add(validators, ".github/scripts/validate_change_coupling.py", available_validators)
    add(validators, ".github/scripts/validate_code_quality.py", available_validators)
    if tokens & {"markdown", "document", "docs", "doctrine", "pattern", "term", "glossary", "metadata"}:
        add(validators, ".github/scripts/validate_metadata.py", available_validators)
        add(workflows, ".github/workflows/metadata-integrity.yml", available_workflows)
        add(workflows, ".github/workflows/link-integrity.yml", available_workflows)
        companion_candidates.add("CHANGELOG.md")
    if ".github" in query or tokens & {"repository", "policy", "workflow", "validator", "agent", "context", "intelligence"}:
        add(validators, ".github/scripts/validate_repository_contract.py", available_validators)
        add(workflows, ".github/workflows/repository-contract.yml", available_workflows)
        add(workflows, ".github/workflows/change-coupling.yml", available_workflows)
        add(workflows, ".github/workflows/metadata-integrity.yml", available_workflows)
        companion_candidates.update({"CHANGELOG.md", "ROADMAP.md"})
    if "research" in normalized or "дослідж" in normalized:
        add(validators, ".github/scripts/validate_research_register.py", available_validators)
        add(workflows, ".github/workflows/metadata-integrity.yml", available_workflows)
        companion_candidates.add("content/research/framework-traceability.md")
    if tokens & {"quartz", "pdf", "publishing", "publication", "typescript", "code"}:
        add(workflows, ".github/workflows/build-integrity.yml", available_workflows)
        for script in ("check:types", "test", "build"):
            if script in available_package:
                package_scripts.add(script)
    if tokens & {"context", "repository", "intelligence", "preflight", "graph", "map"}:
        for test in available_tests:
            if "/repository_intelligence/" in test:
                tests.add(test)
    return {
        "operation": "validation_plan",
        "query": query,
        "validators": sorted(validators),
        "tests": sorted(tests),
        "workflows": sorted(workflows),
        "package_scripts": sorted(package_scripts),
        "companion_candidates": sorted(companion_candidates),
        "note": "Orientation only. Execute applicable checks explicitly under CONTRIBUTING.md and scoped AGENTS.md guidance.",
    }


def compact_graph_context(surface: Dict[str, object], paths: Iterable[str]) -> Dict[str, object]:
    identifiers = {node_id("document", path) for path in paths}
    graph = surface.get("high_value_graph", {})
    selected_edges = [
        value for value in graph.get("edges", [])
        if value.get("source") in identifiers or value.get("target") in identifiers
    ]
    neighbor_ids = set(identifiers)
    for value in selected_edges:
        neighbor_ids.add(str(value["source"]))
        neighbor_ids.add(str(value["target"]))
    nodes = [value for value in graph.get("nodes", []) if value.get("id") in neighbor_ids]
    signals = [
        value for value in graph.get("signals", [])
        if set(str(item) for item in value.get("subjects", [])) & neighbor_ids
    ]
    return {"nodes": nodes, "edges": selected_edges, "signals": signals}


def context_for_task(surface: Dict[str, object], query: str) -> Dict[str, object]:
    owner_candidates = find_owner(surface, query)["candidates"][:8]
    candidate_paths = [str(item["path"]) for item in owner_candidates]
    include_research = "research" in normalize_text(query) or "дослідж" in normalize_text(query)
    return {
        "operation": "context_for_task",
        "query": query,
        "source_identity": surface.get("source_identity", {}),
        "instructions": likely_instruction_paths(surface, query, candidate_paths),
        "owner_candidates": owner_candidates,
        "term_candidates": term_preflight(surface, query)["candidates"][:10],
        "artifact_candidates": artifact_preflight(surface, query)["candidates"][:10],
        "research_items": inventories(surface).get("research_items", []) if include_research else [],
        "graph_context": compact_graph_context(surface, candidate_paths),
        "validation_plan": validation_plan(surface, query),
        "fallback": "If the surface is stale, unavailable, or ambiguous, use live GitHub and read the owning sources directly.",
    }


def impact_for_paths(graph_view: Dict[str, object], paths: Sequence[str]) -> Dict[str, object]:
    graph = graph_view.get("graph", {})
    path_set = set(paths)
    # One repository path can have document, scope, and policy projections.
    # Seed every represented family so control-side edits reach their coverage.
    changed = {str(node["id"]) for node in graph.get("nodes", []) if node.get("path") in path_set}
    represented = {str(node["path"]) for node in graph.get("nodes", []) if node.get("path") in path_set}
    changed.update(node_id("document", path) for path in path_set - represented)
    impacted: Dict[str, Dict[str, object]] = {}
    traversed: List[Dict[str, object]] = []
    for edge_record in graph.get("edges", []):
        role = edge_record.get("impact_role")
        direction = edge_record.get("impact_direction")
        source = str(edge_record.get("source"))
        target = str(edge_record.get("target"))
        destination: Optional[str] = None
        origin: Optional[str] = None
        if source in changed and direction in {"source-to-target", "both"}:
            origin, destination = source, target
        elif target in changed and direction in {"target-to-source", "both"}:
            origin, destination = target, source
        if origin is None or destination is None:
            continue
        if role not in {"dependency", "control"}:
            continue
        traversed.append(edge_record)
        impacted[destination] = {
            "id": destination,
            "via": edge_record["id"],
            "impact_role": role,
            "first_order_terminal": role == "control",
        }
    # Deliberately no BFS through returned control nodes: shared scopes/validators
    # provide first-order review relevance, not transitive sibling fan-out.
    return {
        "operation": "impact_for_paths",
        "changed": sorted(changed),
        "impacted": [impacted[key] for key in sorted(impacted)],
        "traversed_edges": sorted(traversed, key=lambda item: str(item["id"])),
        "traversal_boundary": "repository-control edges are endpoint-sensitive, first-order, and terminal by default",
    }


def git_bytes(root: Path, args: Sequence[str], check: bool = True) -> bytes:
    completed = subprocess.run(
        ["git", *args], cwd=str(root), check=False,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if check and completed.returncode != 0:
        raise ValueError(
            "git {} failed: {}".format(" ".join(args), os.fsdecode(completed.stderr).strip())
        )
    return completed.stdout


def git_text(root: Path, args: Sequence[str], check: bool = True) -> str:
    return os.fsdecode(git_bytes(root, args, check=check)).strip()


def git_blob_optional(root: Path, ref: str, path: str) -> Optional[bytes]:
    spec = "{}:{}".format(ref, path)
    exists = subprocess.run(
        ["git", "cat-file", "-e", spec], cwd=str(root), check=False,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    if exists.returncode != 0:
        return None
    return git_bytes(root, ["show", spec])


def interpretation_changes(root: Path, accepted_ref: str, proposed_ref: str, contract: Dict[str, object]) -> List[str]:
    changes: List[str] = []
    for path in contract.get("interpretation_paths", []):
        relative = str(path)
        accepted = git_blob_optional(root, accepted_ref, relative)
        proposed = git_blob_optional(root, proposed_ref, relative)
        if accepted != proposed:
            changes.append(relative)
    return sorted(changes)


def local_interpretation_matches_ref(root: Path, accepted_ref: str, contract: Dict[str, object]) -> Tuple[bool, List[str]]:
    mismatches: List[str] = []
    for path in contract.get("interpretation_paths", []):
        relative = str(path)
        accepted = git_blob_optional(root, accepted_ref, relative)
        local_path = repository_path(root, relative)
        local = local_path.read_bytes() if local_path is not None and local_path.is_file() else None
        if accepted != local:
            mismatches.append(relative)
    return not mismatches, sorted(mismatches)


def is_ancestor(root: Path, ancestor: str, descendant: str) -> bool:
    completed = subprocess.run(
        ["git", "merge-base", "--is-ancestor", ancestor, descendant],
        cwd=str(root), check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    return completed.returncode == 0


def validate_git_path(raw: bytes) -> str:
    path = os.fsdecode(raw)
    pure = PurePosixPath(path)
    if not path or path.startswith("/") or any(part in ("", ".", "..") for part in pure.parts):
        raise SnapshotBoundaryError("candidate path escapes or is ambiguous: {!r}".format(path))
    return pure.as_posix()


def snapshot_requires_content(path: str, contract: Dict[str, object]) -> bool:
    suffixes = set(str(item).lower() for item in contract.get("text_suffixes", []))
    names = set(str(item) for item in contract.get("text_files", []))
    pure = PurePosixPath(path)
    return pure.name in names or pure.suffix.lower() in suffixes


def materialize_git_snapshot(repo_root: Path, ref: str, destination: Path, contract: Dict[str, object]) -> Dict[str, object]:
    bounds = contract.get("snapshot_bounds", {})
    max_files = int(bounds.get("max_files", 5000))
    max_file_bytes = int(bounds.get("max_text_file_bytes", 2000000))
    max_total_bytes = int(bounds.get("max_total_text_bytes", 50000000))
    raw = git_bytes(repo_root, ["ls-tree", "-r", "-z", "--full-tree", ref])
    entries = [item for item in raw.split(b"\0") if item]
    if len(entries) > max_files:
        raise SnapshotBoundaryError(
            "candidate snapshot has {} files, exceeding declared max_files {}".format(
                len(entries), max_files
            )
        )
    total_text_bytes = 0
    existence_only = 0
    written = 0
    for raw_entry in entries:
        match = GIT_TREE_ENTRY.match(raw_entry)
        if not match:
            raise SnapshotBoundaryError("unsupported git tree entry")
        mode = os.fsdecode(match.group(1))
        object_type = os.fsdecode(match.group(2))
        sha = os.fsdecode(match.group(3))
        path = validate_git_path(match.group(4))
        if object_type != "blob" or mode not in {"100644", "100755"}:
            raise SnapshotBoundaryError(
                "unsupported candidate file kind at {}: mode {}, type {}".format(
                    path, mode, object_type
                )
            )
        target = destination.joinpath(*PurePosixPath(path).parts)
        target.parent.mkdir(parents=True, exist_ok=True)
        if snapshot_requires_content(path, contract):
            size = int(git_text(repo_root, ["cat-file", "-s", sha]))
            if size > max_file_bytes:
                raise SnapshotBoundaryError(
                    "candidate text input {} is {} bytes, exceeding max_text_file_bytes {}".format(
                        path, size, max_file_bytes
                    )
                )
            total_text_bytes += size
            if total_text_bytes > max_total_bytes:
                raise SnapshotBoundaryError(
                    "candidate text inputs exceed max_total_text_bytes {}".format(max_total_bytes)
                )
            target.write_bytes(git_bytes(repo_root, ["cat-file", "blob", sha]))
        else:
            # The deterministic projection needs only existence for unsupported
            # binary/media paths. A regular-file placeholder prevents candidate
            # content from becoming an execution or parser input.
            target.write_bytes(b"")
            existence_only += 1
        written += 1
    return {
        "ref": ref,
        "file_count": written,
        "text_bytes": total_text_bytes,
        "existence_only_files": existence_only,
        "bounds": {
            "max_files": max_files,
            "max_text_file_bytes": max_file_bytes,
            "max_total_text_bytes": max_total_bytes,
        },
    }


def projection_from_git_ref(repo_root: Path, ref: str, contract: Dict[str, object]) -> Tuple[Dict[str, object], Dict[str, object]]:
    with tempfile.TemporaryDirectory(prefix="ua-ri-snapshot-") as temporary:
        destination = Path(temporary)
        boundary = materialize_git_snapshot(repo_root, ref, destination, contract)
        projection = build_projection(
            destination,
            contract_path=destination / ".github/policy/repository-intelligence-contract.json",
        )
        return projection, boundary


def diff_projection(accepted: Dict[str, object], proposed: Dict[str, object]) -> Dict[str, object]:
    def diff_records(a: Sequence[Dict[str, object]], b: Sequence[Dict[str, object]]) -> Dict[str, object]:
        left = {str(item["id"]): item for item in a}
        right = {str(item["id"]): item for item in b}
        added = sorted(set(right) - set(left))
        removed = sorted(set(left) - set(right))
        changed = sorted(
            key for key in set(left) & set(right) if left[key] != right[key]
        )
        return {"added": added, "removed": removed, "changed": changed}
    return {
        "nodes": diff_records(accepted["graph"]["nodes"], proposed["graph"]["nodes"]),
        "edges": diff_records(accepted["graph"]["edges"], proposed["graph"]["edges"]),
        "signals": diff_records(accepted["graph"]["signals"], proposed["graph"]["signals"]),
    }


def compare_refs(
    repo_root: Path,
    accepted_ref: str,
    proposed_ref: str,
    proposed_kind: str,
    contract: Dict[str, object],
) -> Dict[str, object]:
    if proposed_kind not in {"tested-merge", "head"}:
        raise ValueError("proposed_kind must be tested-merge or head")
    contains_target = is_ancestor(repo_root, accepted_ref, proposed_ref)
    if proposed_kind == "tested-merge" and not contains_target:
        return {
            "comparison_state": "incomplete",
            "reason": "proposed tested-merge ref does not contain the current accepted target",
            "accepted_ref": accepted_ref,
            "proposed_ref": proposed_ref,
        }
    view_state = "merge-state" if proposed_kind == "tested-merge" else (
        "head-contained-target" if contains_target else "head-only"
    )
    changed_interpretation = interpretation_changes(repo_root, accepted_ref, proposed_ref, contract)
    if changed_interpretation:
        return {
            "comparison_state": "unsupported",
            "reason": "candidate changes repository-intelligence interpretation semantics",
            "changed_interpretation_paths": changed_interpretation,
            "accepted_ref": accepted_ref,
            "proposed_ref": proposed_ref,
            "view_state": view_state,
        }
    local_matches, mismatches = local_interpretation_matches_ref(repo_root, accepted_ref, contract)
    if not local_matches:
        return {
            "comparison_state": "unsupported",
            "reason": "executing producer/schema does not match accepted target interpretation boundary",
            "mismatched_interpretation_paths": mismatches,
            "accepted_ref": accepted_ref,
            "proposed_ref": proposed_ref,
            "view_state": view_state,
        }
    try:
        accepted, accepted_boundary = projection_from_git_ref(repo_root, accepted_ref, contract)
        proposed, proposed_boundary = projection_from_git_ref(repo_root, proposed_ref, contract)
    except SnapshotBoundaryError as exc:
        return {
            "comparison_state": "incomplete",
            "reason": str(exc),
            "accepted_ref": accepted_ref,
            "proposed_ref": proposed_ref,
            "view_state": view_state,
        }
    return {
        "comparison_state": "complete" if view_state != "head-only" else "head-only",
        "view_state": view_state,
        "accepted_ref": accepted_ref,
        "proposed_ref": proposed_ref,
        "producer": accepted["producer"],
        "accepted_source_identity": accepted["source_identity"],
        "proposed_source_identity": proposed["source_identity"],
        "accepted_snapshot_boundary": accepted_boundary,
        "proposed_snapshot_boundary": proposed_boundary,
        "diff": diff_projection(accepted, proposed),
    }


def parse_surface(path: Path, expected_schema: int) -> Dict[str, object]:
    payload = load_json(path, "Agent Context Surface")
    if payload.get("schema_version") != expected_schema or payload.get("view") != "agent-context":
        raise ValueError("Unsupported Agent Context Surface schema/view")
    return payload


def verify_surface(
    root: Path,
    contract: Dict[str, object],
    surface_path: Path,
    candidate_path: Optional[Path] = None,
) -> List[str]:
    projection = build_projection(root)
    expected = serialize_json(materialize_agent_surface(projection, contract))
    errors: List[str] = []
    blocking = [
        item for item in projection.get("graph", {}).get("signals", [])
        if item.get("disposition") == "blocking"
    ]
    if blocking:
        errors.append(
            "Repository Intelligence Projection contains {} blocking deterministic signal(s): {}".format(
                len(blocking), ", ".join(str(item.get("class")) for item in blocking)
            )
        )
    if candidate_path is not None:
        try:
            candidate = candidate_path.read_text(encoding="utf-8")
        except FileNotFoundError:
            errors.append("Generated candidate is missing: {}".format(candidate_path))
        else:
            if candidate != expected:
                errors.append("Generated candidate does not match the deterministic compact materialization")
    try:
        committed = surface_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(
            "Committed Agent Context Surface is missing: {}. Use the CI candidate artifact or build it explicitly.".format(
                surface_path
            )
        )
        return errors
    if committed != expected:
        errors.append("Committed Agent Context Surface is stale; regenerate before relying on it")
    return errors


def load_fresh_surface(root: Path, contract: Dict[str, object], surface_path: Path) -> Dict[str, object]:
    surface = parse_surface(surface_path, int(contract["schema_version"]))
    current = materialize_agent_surface(build_projection(root), contract)
    expected_digest = str(current["source_identity"]["digest"])
    actual_digest = str(surface.get("source_identity", {}).get("digest", ""))
    if actual_digest != expected_digest:
        raise ValueError(
            "Agent Context Surface is stale (surface {}, current {}). Fall back to live repository reading or regenerate it.".format(
                actual_digest or "<missing>", expected_digest
            )
        )
    if surface != current:
        raise ValueError(
            "Agent Context Surface is stale or invalid: producer identity or generated facts differ. "
            "Fall back to live repository reading or regenerate it."
        )
    return surface


def write_json(value: Dict[str, object]) -> None:
    sys.stdout.write(serialize_json(value))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root")
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--surface", type=Path, default=DEFAULT_SURFACE)
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build", help="Build deterministic materialization")
    build.add_argument("--view", choices=("agent", "graph"), required=True)
    build.add_argument("--output", type=Path, required=True)

    verify = subparsers.add_parser("verify", help="Verify committed compact view is fresh")
    verify.add_argument("--candidate", type=Path)

    for command in (
        "context-for-task", "find-owner", "term-preflight", "artifact-preflight", "validation-plan"
    ):
        query = subparsers.add_parser(command)
        query.add_argument("query")

    impact = subparsers.add_parser("impact-for-paths")
    impact.add_argument("paths", nargs="+")

    compare_parser = subparsers.add_parser("compare-refs")
    compare_parser.add_argument("--accepted-ref", required=True)
    compare_parser.add_argument("--proposed-ref", required=True)
    compare_parser.add_argument("--proposed-kind", choices=("tested-merge", "head"), required=True)

    bounds = subparsers.add_parser("snapshot-ref")
    bounds.add_argument("--ref", required=True)
    bounds.add_argument("--output", type=Path, required=True)

    stats = subparsers.add_parser("stats")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = args.root.resolve()
    contract_path = args.contract
    if not contract_path.is_absolute():
        contract_path = root / contract_path
    try:
        contract = load_contract(contract_path)
        surface_path = args.surface
        if not surface_path.is_absolute():
            surface_path = root / surface_path
        if args.command == "build":
            projection = build_projection(root, contract_path=contract_path)
            value = materialize_agent_surface(projection, contract) if args.view == "agent" else materialize_graph_view(projection)
            output = args.output
            if not output.is_absolute():
                output = root / output
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(serialize_json(value), encoding="utf-8")
            print(
                "Built {} materialization: {} ({} bytes)".format(
                    args.view, output, output.stat().st_size
                )
            )
            return 0
        if args.command == "verify":
            candidate = args.candidate
            if candidate is not None and not candidate.is_absolute():
                candidate = root / candidate
            errors = verify_surface(root, contract, surface_path, candidate)
            if errors:
                print("Repository intelligence verification failed:")
                for error in errors:
                    print("- {}".format(error))
                return 1
            print("Repository intelligence verification passed.")
            return 0
        if args.command == "compare-refs":
            write_json(
                compare_refs(
                    root, args.accepted_ref, args.proposed_ref, args.proposed_kind, contract
                )
            )
            return 0
        if args.command == "snapshot-ref":
            output = args.output
            if not output.is_absolute():
                output = root / output
            output.mkdir(parents=True, exist_ok=True)
            write_json(materialize_git_snapshot(root, args.ref, output, contract))
            return 0
        if args.command == "stats":
            surface = load_fresh_surface(root, contract, surface_path)
            write_json(
                {
                    "surface_path": relpath(root, surface_path),
                    "surface_bytes": surface_path.stat().st_size,
                    "term_count": len(inventories(surface).get("terms", [])),
                    "artifact_count": len(inventories(surface).get("artifacts", [])),
                    "high_value_edge_count": len(surface.get("high_value_graph", {}).get("edges", [])),
                    "deterministic_signal_count": len(surface.get("high_value_graph", {}).get("signals", [])),
                }
            )
            return 0

        surface = load_fresh_surface(root, contract, surface_path)
        if args.command == "context-for-task":
            write_json(context_for_task(surface, str(args.query)))
        elif args.command == "find-owner":
            write_json(find_owner(surface, str(args.query)))
        elif args.command == "term-preflight":
            write_json(term_preflight(surface, str(args.query)))
        elif args.command == "artifact-preflight":
            write_json(artifact_preflight(surface, str(args.query)))
        elif args.command == "validation-plan":
            write_json(validation_plan(surface, str(args.query)))
        elif args.command == "impact-for-paths":
            write_json(impact_for_paths(materialize_graph_view(build_projection(root)), args.paths))
        else:  # pragma: no cover
            parser.error("Unsupported command: {}".format(args.command))
        return 0
    except (OSError, ValueError) as exc:
        print("Repository intelligence error: {}".format(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
