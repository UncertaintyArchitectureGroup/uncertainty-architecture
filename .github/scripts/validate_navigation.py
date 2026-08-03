#!/usr/bin/env python3
"""Validate UA navigation coverage, order, and route ownership."""

from pathlib import Path
import re
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
NAVIGATION_MARKER = "> **UA navigation**"
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

Route = Tuple[Path, Optional[str]]

FRAMEWORK_ENTRY_PAGES: Set[Path] = {
    Path("README.md"),
    Path("SPECIFICATION.md"),
    Path("00-doctrine/README.md"),
    Path("01-patterns/README.md"),
    Path("02-ai-control-plane/README.md"),
    Path("03-reference-architectures/README.md"),
    Path("04-failure-modes/README.md"),
    Path("content/research/index.md"),
}

EXPECTED_NAVIGATION_ROUTES: Dict[str, Route] = {
    "UA Home": (Path("README.md"), None),
    "Specification": (Path("SPECIFICATION.md"), None),
    "Organization / boundaries": (
        Path("00-doctrine/nested-control-lifecycle.md"),
        "1-organizational-control-context",
    ),
    "Project / architecture": (
        Path("01-patterns/project-control-architecture-and-viability-review.md"),
        None,
    ),
    "Delivery / release": (
        Path("01-patterns/thinking-system-review.md"),
        None,
    ),
    "Runtime / reassessment": (
        Path("00-doctrine/nested-control-lifecycle.md"),
        "4-runtime-operation-and-reassessment",
    ),
    "Doctrine": (Path("00-doctrine/README.md"), None),
    "Patterns": (Path("01-patterns/README.md"), None),
    "Control capabilities": (Path("02-ai-control-plane/README.md"), None),
    "Reference architectures": (Path("03-reference-architectures/README.md"), None),
    "Failure modes": (Path("04-failure-modes/README.md"), None),
    "Research": (Path("content/research/index.md"), None),
}

COMPACT_BREADCRUMBS: Dict[Path, Dict[str, Route]] = {
    Path("01-patterns/project-control-architecture-and-viability-review-template.md"): {
        "← Owning pattern": (
            Path("01-patterns/project-control-architecture-and-viability-review.md"),
            None,
        ),
        "↑ Patterns index": (Path("01-patterns/README.md"), None),
        "UA Home": (Path("README.md"), None),
    },
    Path("01-patterns/thinking-system-review-template.md"): {
        "← Owning pattern": (Path("01-patterns/thinking-system-review.md"), None),
        "↑ Patterns index": (Path("01-patterns/README.md"), None),
        "UA Home": (Path("README.md"), None),
    },
    Path("03-reference-architectures/judgment-placement-examples.md"): {
        "← Reference Architectures": (
            Path("03-reference-architectures/README.md"),
            None,
        ),
        "Judgment Node Boundary": (
            Path("01-patterns/judgment-node-boundary.md"),
            None,
        ),
        "UA Home": (Path("README.md"), None),
    },
}


def repository_file(path: Path) -> Path:
    """Return an absolute path for a repository-relative path."""
    return ROOT / path


def blockquotes(text: str) -> List[str]:
    """Return contiguous Markdown blockquote regions."""
    blocks: List[str] = []
    current: List[str] = []

    for line in text.splitlines():
        if line.startswith(">"):
            current.append(line)
        elif current:
            blocks.append("\n".join(current))
            current = []

    if current:
        blocks.append("\n".join(current))

    return blocks


def parse_links(
    block: str,
    source: Path,
    errors: List[str],
) -> List[Tuple[str, str]]:
    """Parse Markdown links in display order and report duplicate labels."""
    parsed = LINK_PATTERN.findall(block)
    seen: Set[str] = set()

    for label, _ in parsed:
        if label in seen:
            errors.append(f"{source}: duplicate navigation label {label!r}")
        seen.add(label)

    return parsed


def resolve_target(source: Path, target: str) -> Tuple[Optional[Path], Optional[str]]:
    """Resolve a repository-relative Markdown target and optional fragment."""
    path_text, separator, fragment = target.partition("#")
    candidate = (ROOT / source.parent / unquote(path_text)).resolve()

    if candidate.is_dir():
        index_candidates = (candidate / "README.md", candidate / "index.md")
        candidate = next((item for item in index_candidates if item.is_file()), candidate)

    try:
        repository_path = candidate.relative_to(ROOT)
    except ValueError:
        return None, unquote(fragment) if separator else None

    return repository_path, unquote(fragment) if separator else None


def validate_routes(
    source: Path,
    block: str,
    expected: Dict[str, Route],
    errors: List[str],
) -> None:
    """Validate ordered labels and their owning repository destinations."""
    parsed_links = parse_links(block, source, errors)
    actual_order = [label for label, _ in parsed_links]
    expected_order = list(expected)

    if actual_order != expected_order:
        errors.append(
            f"{source}: navigation order {actual_order!r}, "
            f"expected {expected_order!r}"
        )

    links = dict(parsed_links)
    actual_labels = set(links)
    expected_labels = set(expected)

    for label in sorted(expected_labels - actual_labels):
        errors.append(f"{source}: missing navigation label {label!r}")
    for label in sorted(actual_labels - expected_labels):
        errors.append(f"{source}: unexpected navigation label {label!r}")

    for label in expected_order:
        if label not in links:
            continue

        actual_path, actual_fragment = resolve_target(source, links[label])
        expected_path, expected_fragment = expected[label]

        if actual_path != expected_path or actual_fragment != expected_fragment:
            errors.append(
                f"{source}: {label!r} resolves to "
                f"{actual_path}#{actual_fragment or ''}, expected "
                f"{expected_path}#{expected_fragment or ''}"
            )
            continue

        if actual_path is not None and not repository_file(actual_path).is_file():
            errors.append(
                f"{source}: {label!r} targets missing file {actual_path}"
            )


def validate_framework_entry_pages(errors: List[str]) -> None:
    """Validate complete navigation blocks on declared framework entry pages."""
    for path in sorted(FRAMEWORK_ENTRY_PAGES):
        absolute_path = repository_file(path)
        if not absolute_path.is_file():
            errors.append(f"Missing framework entry page: {path}")
            continue

        text = absolute_path.read_text(encoding="utf-8")
        navigation_blocks = [
            block for block in blockquotes(text) if NAVIGATION_MARKER in block
        ]

        if len(navigation_blocks) != 1:
            errors.append(
                f"{path}: expected exactly one navigation block, "
                f"found {len(navigation_blocks)}"
            )
            continue

        block = navigation_blocks[0]
        marker_position = block.find(NAVIGATION_MARKER)
        lifecycle_position = block.find("**Lifecycle:**")
        explore_position = block.find("**Explore:**")

        if lifecycle_position < 0:
            errors.append(f"{path}: navigation block lacks Lifecycle section")
        if explore_position < 0:
            errors.append(f"{path}: navigation block lacks Explore section")
        if not (
            marker_position >= 0
            and lifecycle_position > marker_position
            and explore_position > lifecycle_position
        ):
            errors.append(
                f"{path}: expected marker, Lifecycle, and Explore in that order"
            )

        validate_routes(path, block, EXPECTED_NAVIGATION_ROUTES, errors)

    actual_navigation_pages = {
        path.relative_to(ROOT)
        for path in ROOT.rglob("*.md")
        if NAVIGATION_MARKER in path.read_text(encoding="utf-8")
    }

    for path in sorted(actual_navigation_pages - FRAMEWORK_ENTRY_PAGES):
        errors.append(f"Unexpected full navigation block: {path}")
    for path in sorted(FRAMEWORK_ENTRY_PAGES - actual_navigation_pages):
        errors.append(f"Missing full navigation block: {path}")


def validate_compact_breadcrumbs(errors: List[str]) -> None:
    """Validate compact owner/back navigation on selected leaf documents."""
    for path, expected_routes in COMPACT_BREADCRUMBS.items():
        absolute_path = repository_file(path)
        if not absolute_path.is_file():
            errors.append(f"Missing breadcrumb document: {path}")
            continue

        text = absolute_path.read_text(encoding="utf-8")
        expected_labels = set(expected_routes)
        candidates = []

        for block in blockquotes(text):
            labels = {label for label, _ in LINK_PATTERN.findall(block)}
            if expected_labels <= labels:
                candidates.append(block)

        if len(candidates) != 1:
            errors.append(
                f"{path}: expected exactly one compact breadcrumb block, "
                f"found {len(candidates)}"
            )
            continue

        validate_routes(path, candidates[0], expected_routes, errors)


def main() -> int:
    """Run all navigation integrity checks from any working directory."""
    errors: List[str] = []
    validate_framework_entry_pages(errors)
    validate_compact_breadcrumbs(errors)

    if errors:
        print("Navigation coverage and routing validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Navigation coverage, order, and routing valid: "
        f"{len(FRAMEWORK_ENTRY_PAGES)} framework entry pages and "
        f"{len(COMPACT_BREADCRUMBS)} compact breadcrumb documents."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
