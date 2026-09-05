#!/usr/bin/env python3
"""Build and query the deterministic UA Agent Context Surface.

The projection is read-only orientation evidence. It preserves repository paths,
explicit relationships, and source provenance, but never creates semantic
authority. Live Git/GitHub and the owning source documents remain authoritative.
"""

import argparse
import hashlib
import json
import posixpath
import re
import sys
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
DEFAULT_SURFACE = ROOT / ".github/agent-context.json"
SCHEMA_VERSION = 1
PRODUCER_VERSION = 1
SOURCE_ALGORITHM = "sha256-path-content-v1"

TERM_HEADING = re.compile(r"^###\s+(.+?)\s*$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
BOLD_TEXT = re.compile(r"\*\*([^*]+)\*\*")
TOKEN = re.compile(r"[0-9A-Za-zА-Яа-яІіЇїЄєҐґ]+", re.UNICODE)
RESEARCH_REGISTER_BLOCK = re.compile(
    r"<!--\s*ua-research-register\s*(\{.*?\})\s*-->", re.DOTALL
)
MARKDOWN_TITLE = re.compile(r"^(.*?)(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))$")

RELATION_FIELDS = {
    "related": "RELATED_TO",
    "supersedes": "SUPERSEDES",
    "superseded_by": "SUPERSEDED_BY",
    "source_basis": "SOURCE_BASIS",
}
SEMANTIC_EDGE_TYPES = {
    "DEFINES",
    "LINKS_TO",
    "RELATED_TO",
    "SUPERSEDES",
    "SUPERSEDED_BY",
    "SOURCE_BASIS",
    "CANONICAL_FOR",
    "RESEARCH_OWNER",
    "FRAMEWORK_DESTINATION",
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


def repository_path(root: Path, relative: str) -> Optional[Path]:
    root_resolved = root.resolve()
    candidate = (root_resolved / relative).resolve()
    try:
        candidate.relative_to(root_resolved)
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
    text = path.read_text(encoding="utf-8")
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


def discover_artifacts(root: Path, contract: Dict[str, object]) -> List[Dict[str, object]]:
    artifacts: Dict[str, Dict[str, object]] = {}
    for path in discover_maintained_documents(root, contract):
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

    # Some repository-process owners are deliberately frontmatter-free. They are
    # structural sources that the architecture itself requires the shared
    # projection to expose. Preserve missing metadata as missing rather than
    # inventing canonical_for/status/module values for graph convenience.
    for relative, projection_role in STRUCTURAL_ARTIFACTS.items():
        if relative in artifacts:
            continue
        path = repository_path(root, relative)
        if path is None or not path.is_file():
            continue
        metadata, title, text = parse_document(path)
        artifacts[relative] = artifact_record(
            relative,
            metadata,
            title,
            text,
            projection_role,
        )

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
    if match:
        return match.group(1).strip()
    return raw


def resolve_local_target(source: str, target: str, repository_files: Set[str]) -> Tuple[Optional[str], bool]:
    raw = target.strip().strip("<>")
    raw = strip_optional_markdown_title(raw)
    if not raw or raw.startswith(("#", "http://", "https://", "mailto:", "data:")):
        return None, False
    without_fragment = unquote(raw.split("#", 1)[0].split("?", 1)[0])
    if not without_fragment:
        return None, False
    normalized = posixpath.normpath(posixpath.join(posixpath.dirname(source), without_fragment))
    candidates = [normalized]
    if PurePosixPath(normalized).suffix == "":
        candidates.extend(
            [
                normalized.rstrip("/") + "/README.md",
                normalized + ".md",
            ]
        )
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
        "projection_role": artifact.get(
            "projection_role", "maintained-conceptual-process-artifact"
        ),
    }


def support_document_node(root: Path, path: str) -> Dict[str, object]:
    title = PurePosixPath(path).stem
    absolute = root / path
    if absolute.is_file() and absolute.suffix.lower() == ".md":
        try:
            metadata, parsed_title, _ = parse_document(absolute)
            title = parsed_title
            return {
                "id": node_id("document", path),
                "family": "Document",
                "identity": path,
                "path": path,
                "title": title,
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


def edge(
    source: str,
    relation: str,
    target: str,
    provenance_path: str,
    provenance_kind: str,
    detail: str,
) -> Dict[str, object]:
    return {
        "id": hashlib.sha256(
            "\0".join([source, relation, target, provenance_path, provenance_kind, detail]).encode("utf-8")
        ).hexdigest()[:20],
        "source": source,
        "relation": relation,
        "target": target,
        "provenance": {
            "path": provenance_path,
            "kind": provenance_kind,
            "detail": detail,
        },
    }


def signal(
    signal_class: str,
    subjects: Sequence[str],
    origin: str,
    evidence: str,
    severity: str,
    disposition: str,
) -> Dict[str, object]:
    stable = "\0".join([signal_class, *sorted(subjects), origin, evidence, severity, disposition])
    return {
        "id": hashlib.sha256(stable.encode("utf-8")).hexdigest()[:20],
        "class": signal_class,
        "subjects": sorted(subjects),
        "origin": origin,
        "evidence": evidence,
        "severity": severity,
        "disposition": disposition,
    }


def build_graph(
    root: Path,
    artifacts: Sequence[Dict[str, object]],
    terms: Sequence[Dict[str, object]],
    instructions: Sequence[Dict[str, str]],
    research_items: Sequence[Dict[str, object]],
    validation: Dict[str, object],
) -> Tuple[List[Dict[str, object]], List[Dict[str, object]], List[Dict[str, object]]]:
    nodes: Dict[str, Dict[str, object]] = {}
    edges: Dict[str, Dict[str, object]] = {}
    signals: Dict[str, Dict[str, object]] = {}
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
                    document_identifier,
                    "CANONICAL_FOR",
                    responsibility_identifier,
                    str(artifact["path"]),
                    "frontmatter",
                    "canonical_for: {}".format(claim),
                )
            )
            responsibility_claimants.setdefault(claim, []).append(document_identifier)

    for claim, claimants in sorted(responsibility_claimants.items()):
        if len(claimants) > 1:
            add_signal(
                signal(
                    "duplicate-active-canonical-claim",
                    claimants,
                    "deterministic",
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
                            "deterministic",
                            "{} declares {}={!r}, but no repository target resolves".format(
                                source_path, field, raw_target
                            ),
                            "error",
                            "blocking",
                        )
                    )
                    continue
                target_identifier = node_id("document", resolved)
                if target_identifier not in nodes:
                    add_node(support_document_node(root, resolved))
                add_edge(
                    edge(
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
            target_identifier = node_id("document", resolved)
            if target_identifier not in nodes and resolved in artifact_by_path:
                add_node(document_node(artifact_by_path[resolved]))
            if target_identifier not in nodes:
                continue
            if target_identifier == source_identifier:
                continue
            add_edge(
                edge(
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
                        "deterministic",
                        "research item {} declares {}={!r}, but the path is missing".format(
                            item["id"], field, target_path
                        ),
                        "error",
                        "blocking",
                    )
                )
                continue
            target_identifier = node_id("document", target_path)
            if target_identifier not in nodes:
                add_node(support_document_node(root, target_path))
            add_edge(
                edge(
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
                    node_id("document", str(artifact["path"])),
                    "VALIDATED_BY",
                    metadata_validator,
                    ".github/policy/metadata-contract.json",
                    "metadata-scan-contract",
                    "maintained document is included in the repository-intelligence metadata scan",
                )
            )

    semantic_degree: Dict[str, int] = {
        node_id("document", str(artifact["path"])): 0 for artifact in artifacts
    }
    for value in edges.values():
        if value["relation"] not in SEMANTIC_EDGE_TYPES:
            continue
        if value["source"] in semantic_degree:
            semantic_degree[str(value["source"])] += 1
        if value["target"] in semantic_degree:
            semantic_degree[str(value["target"])] += 1
    for identifier, degree in sorted(semantic_degree.items()):
        if degree == 0:
            add_signal(
                signal(
                    "weak-explicit-connectivity",
                    [identifier],
                    "deterministic",
                    "projected maintained artifact has no explicit semantic relation in the baseline projection",
                    "warning",
                    "advisory",
                )
            )

    return (
        sorted(nodes.values(), key=lambda item: str(item["id"])),
        sorted(edges.values(), key=lambda item: str(item["id"])),
        sorted(signals.values(), key=lambda item: str(item["id"])),
    )


def source_input_paths(
    root: Path,
    artifacts: Sequence[Dict[str, object]],
    instructions: Sequence[Dict[str, str]],
    research_items: Sequence[Dict[str, object]],
    validation: Dict[str, object],
) -> List[str]:
    del research_items  # research-register path is added explicitly below
    paths: Set[str] = {str(item["path"]) for item in artifacts}
    paths.update(str(item["path"]) for item in instructions)
    for category in ("policies", "validators", "workflows", "tests"):
        paths.update(str(item) for item in validation.get(category, []))
    for fixed in (
        ".github/REPOSITORY-INTELLIGENCE.md",
        "00-doctrine/glossary.md",
        "content/research/research-register.md",
        "DOCUMENT-METADATA.md",
        "package.json",
    ):
        if (root / fixed).is_file():
            paths.add(fixed)
    paths.discard(".github/agent-context.json")
    return sorted(paths)


def compute_source_identity(root: Path, paths: Sequence[str]) -> Dict[str, object]:
    aggregate = hashlib.sha256()
    aggregate.update((SOURCE_ALGORITHM + "\0").encode("utf-8"))
    for relative in paths:
        path = repository_path(root, relative)
        if path is None or not path.is_file():
            raise ValueError("Indexed input is missing or unsafe: {}".format(relative))
        content_digest = hashlib.sha256(path.read_bytes()).hexdigest()
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(content_digest.encode("ascii"))
        aggregate.update(b"\n")
    return {
        "algorithm": SOURCE_ALGORITHM,
        "digest": aggregate.hexdigest(),
        "file_count": len(paths),
        "inputs": list(paths),
        "excluded_outputs": [".github/agent-context.json"],
    }


def build_surface(root: Path) -> Dict[str, object]:
    contract = load_metadata_contract(root)
    artifacts = discover_artifacts(root, contract)
    terms = discover_terms(root)
    instructions = discover_instructions(root)
    research_items = parse_research_items(root)
    validation = discover_validation_surfaces(root)
    nodes, edges, signals = build_graph(
        root, artifacts, terms, instructions, research_items, validation
    )
    inputs = source_input_paths(root, artifacts, instructions, research_items, validation)
    return {
        "schema_version": SCHEMA_VERSION,
        "producer": {
            "implementation": ".github/scripts/repository_intelligence.py",
            "version": PRODUCER_VERSION,
        },
        "source_identity": compute_source_identity(root, inputs),
        "inventories": {
            "instructions": instructions,
            "terms": terms,
            "artifacts": artifacts,
            "research_items": research_items,
        },
        "graph": {
            "nodes": nodes,
            "edges": edges,
            "signals": signals,
        },
        "validation_surfaces": validation,
    }


def serialize_surface(surface: Dict[str, object]) -> str:
    return json.dumps(surface, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


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


def claim_candidates(surface: Dict[str, object], query: str) -> List[Dict[str, object]]:
    candidates: List[Dict[str, object]] = []
    for artifact in inventories(surface).get("artifacts", []):
        for claim in artifact.get("canonical_for", []):
            score, reasons = score_fields(query, [("canonical_for", str(claim))])
            if not score:
                continue
            candidates.append(
                {
                    "path": artifact["path"],
                    "title": artifact["title"],
                    "role": "machine_responsibility_claim",
                    "responsibility": claim,
                    "score": score,
                    "reasons": reasons,
                }
            )
    return candidates


def research_owner_candidates(surface: Dict[str, object], query: str) -> List[Dict[str, object]]:
    candidates: List[Dict[str, object]] = []
    for item in inventories(surface).get("research_items", []):
        fields = [
            ("research_id", str(item.get("id", ""))),
            ("title", str(item.get("title", ""))),
            ("next_step", str(item.get("next_step", ""))),
        ]
        score, reasons = score_fields(query, fields)
        if not score:
            continue
        candidates.append(
            {
                "path": "content/research/research-register.md",
                "title": str(item.get("title") or item.get("id")),
                "role": "research_state_owner",
                "research_id": item.get("id"),
                "score": score,
                "reasons": reasons,
            }
        )
        owning_record = item.get("owning_record")
        if owning_record:
            candidates.append(
                {
                    "path": str(owning_record),
                    "title": str(item.get("title") or item.get("id")),
                    "role": "research_record_owner",
                    "research_id": item.get("id"),
                    "score": max(score - 1, 1),
                    "reasons": reasons,
                }
            )
    return candidates


def implementation_candidates(surface: Dict[str, object], query: str) -> List[Dict[str, object]]:
    candidates: List[Dict[str, object]] = []
    for node in surface.get("graph", {}).get("nodes", []):
        if node.get("family") != "PolicyOrValidator":
            continue
        path = str(node.get("path", ""))
        score, reasons = score_fields(query, [("implementation_path", path)])
        if not score:
            continue
        candidates.append(
            {
                "path": path,
                "title": PurePosixPath(path).name,
                "role": "implementation_surface",
                "kind": node.get("kind", ""),
                "score": score,
                "reasons": reasons,
            }
        )
    return candidates


def find_owner(surface: Dict[str, object], query: str) -> Dict[str, object]:
    owners: List[Dict[str, object]] = []
    owners.extend(claim_candidates(surface, query))
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
    owners.extend(research_owner_candidates(surface, query))
    owners.extend(implementation_candidates(surface, query))
    owners.sort(key=lambda item: (-int(item["score"]), str(item["path"]), str(item["role"])))
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


def likely_instruction_paths(surface: Dict[str, object], query: str) -> List[Dict[str, str]]:
    selected: List[Dict[str, str]] = []
    query_tokens = token_set(query)
    for item in inventories(surface).get("instructions", []):
        scope = str(item.get("scope_root", "."))
        path = str(item.get("path", ""))
        if path == "AGENTS.md":
            selected.append(item)
            continue
        scope_tokens = token_set(scope.replace("/", " "))
        if scope != "." and (scope in query or scope_tokens & query_tokens):
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

    for value in (
        ".github/scripts/validate_change_coupling.py",
        ".github/scripts/validate_code_quality.py",
    ):
        add(validators, value, available_validators)

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
        companion_candidates.add("CHANGELOG.md")

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


def graph_neighborhood(surface: Dict[str, object], paths: Iterable[str]) -> Dict[str, object]:
    identifiers = {node_id("document", path) for path in paths}
    edges = surface.get("graph", {}).get("edges", [])
    selected_edges = [
        value for value in edges if value.get("source") in identifiers or value.get("target") in identifiers
    ]
    neighbor_ids = set(identifiers)
    for value in selected_edges:
        neighbor_ids.add(str(value["source"]))
        neighbor_ids.add(str(value["target"]))
    nodes = [
        value
        for value in surface.get("graph", {}).get("nodes", [])
        if value.get("id") in neighbor_ids
    ]
    signals = [
        value
        for value in surface.get("graph", {}).get("signals", [])
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
        "instructions": likely_instruction_paths(surface, query),
        "owner_candidates": owner_candidates,
        "term_candidates": term_preflight(surface, query)["candidates"][:10],
        "artifact_candidates": artifact_preflight(surface, query)["candidates"][:10],
        "research_items": inventories(surface).get("research_items", []) if include_research else [],
        "graph_context": graph_neighborhood(surface, candidate_paths),
        "validation_plan": validation_plan(surface, query),
        "fallback": "If the surface is stale, unavailable, or ambiguous, use live GitHub and read the owning sources directly.",
    }


def parse_surface(path: Path) -> Dict[str, object]:
    payload = load_json(path, "Agent Context Surface")
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(
            "Unsupported Agent Context Surface schema_version: {!r}".format(
                payload.get("schema_version")
            )
        )
    return payload


def verify_surface(root: Path, surface_path: Path, candidate_path: Optional[Path] = None) -> List[str]:
    expected = serialize_surface(build_surface(root))
    errors: List[str] = []
    if candidate_path is not None:
        try:
            candidate = candidate_path.read_text(encoding="utf-8")
        except FileNotFoundError:
            errors.append("Generated candidate is missing: {}".format(candidate_path))
        else:
            if candidate != expected:
                errors.append("Generated candidate does not match the deterministic current projection")
    try:
        committed = surface_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(
            "Committed Agent Context Surface is missing: {}. Use the CI-generated candidate artifact or run the build command.".format(
                surface_path
            )
        )
        return errors
    if committed != expected:
        errors.append(
            "Committed Agent Context Surface is stale. Regenerate it from the current repository state before relying on it."
        )
    return errors


def load_fresh_surface(root: Path, surface_path: Path) -> Dict[str, object]:
    surface = parse_surface(surface_path)
    current = build_surface(root)
    expected_digest = str(current["source_identity"]["digest"])
    actual_digest = str(surface.get("source_identity", {}).get("digest", ""))
    if actual_digest != expected_digest:
        raise ValueError(
            "Agent Context Surface is stale (surface {}, current {}). Fall back to live repository reading or regenerate it.".format(
                actual_digest or "<missing>", expected_digest
            )
        )
    return surface


def write_json(value: Dict[str, object]) -> None:
    sys.stdout.write(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root")
    parser.add_argument("--surface", type=Path, default=DEFAULT_SURFACE, help="Committed context surface")
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build", help="Build deterministic context JSON")
    build.add_argument("--output", type=Path, required=True)

    verify = subparsers.add_parser("verify", help="Verify committed context JSON is fresh")
    verify.add_argument("--candidate", type=Path)

    for command in (
        "context-for-task",
        "find-owner",
        "term-preflight",
        "artifact-preflight",
        "validation-plan",
    ):
        query = subparsers.add_parser(command)
        query.add_argument("query")

    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = args.root.resolve()
    surface_path = args.surface
    if not surface_path.is_absolute():
        surface_path = root / surface_path

    try:
        if args.command == "build":
            output = args.output
            if not output.is_absolute():
                output = root / output
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(serialize_surface(build_surface(root)), encoding="utf-8")
            print("Built Agent Context Surface: {}".format(output))
            return 0
        if args.command == "verify":
            candidate = args.candidate
            if candidate is not None and not candidate.is_absolute():
                candidate = root / candidate
            errors = verify_surface(root, surface_path, candidate)
            if errors:
                print("Repository intelligence verification failed:")
                for error in errors:
                    print("- {}".format(error))
                return 1
            print("Repository intelligence verification passed.")
            return 0

        surface = load_fresh_surface(root, surface_path)
        query = str(args.query)
        if args.command == "context-for-task":
            write_json(context_for_task(surface, query))
        elif args.command == "find-owner":
            write_json(find_owner(surface, query))
        elif args.command == "term-preflight":
            write_json(term_preflight(surface, query))
        elif args.command == "artifact-preflight":
            write_json(artifact_preflight(surface, query))
        elif args.command == "validation-plan":
            write_json(validation_plan(surface, query))
        else:  # pragma: no cover
            parser.error("Unsupported command: {}".format(args.command))
        return 0
    except (OSError, ValueError) as exc:
        print("Repository intelligence error: {}".format(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
