"""Portable OOXML acceptance checks; no rendering or authoring dependency required."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
SOURCE = "assets/presentations/pmday-2026/README.md"
INPUTS = [SOURCE, "quartz/scripts/pmday-presentation.mjs", "quartz/scripts/build-pmday-pptx.mjs", "quartz/scripts/validate-pmday-pptx.py"]
NS = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main", "a": "http://schemas.openxmlformats.org/drawingml/2006/main"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def validate(pptx, manifest_path):
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest.get("schema_version") == 1, "Unsupported manifest"
    assert manifest["pptx_sha256"] == digest(pptx.read_bytes()), "PPTX checksum mismatch"
    assert set(manifest["inputs"]) == set(INPUTS), "Missing or extra provenance input"
    for name in INPUTS:
        assert manifest["inputs"][name] == digest((ROOT / name).read_bytes()), f"Stale input: {name}"
    source = (ROOT / SOURCE).read_text(encoding="utf-8")
    titles = [m[1] for m in re.findall(r"^## (\d+)\. (.+)$", source, re.M)]
    assert len(titles) == 14, "Source must contain 14 slides"
    counts = {"slides": 0, "pictures": 0, "tables": 0, "text_runs": 0}
    with zipfile.ZipFile(pptx) as package:
        assert len(package.namelist()) == len(set(package.namelist())), "Duplicate package members"
        slides = sorted((n for n in package.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)), key=lambda n: int(re.search(r"slide(\d+)", n)[1]))
        assert len(slides) == 14, "PPTX must contain 14 slides"
        presentation = ET.fromstring(package.read("ppt/presentation.xml"))
        size = presentation.find("p:sldSz", NS)
        assert (size.get("cx"), size.get("cy")) == ("12192000", "6858000"), "Expected 16:9 design canvas"
        for number, name in enumerate(slides, 1):
            slide = ET.fromstring(package.read(name))
            bg = slide.find("p:cSld/p:bg/p:bgPr/a:solidFill/a:srgbClr", NS)
            assert bg is not None and bg.get("val").upper() == "0B0F14", f"Slide {number}: dark solid background missing"
            assert not slide.findall(".//a:blipFill", NS), f"Slide {number}: image fill forbidden"
            assert not slide.findall(".//p:pic", NS), f"Slide {number}: image exceptions not approved"
            assert not slide.findall(".//p:oleObj", NS), f"Slide {number}: OLE object forbidden"
            runs = [e.text or "" for e in slide.findall(".//a:t", NS)]
            normalized = " ".join(" ".join(runs).split())
            assert titles[number - 1] in normalized, f"Slide {number}: wrong/missing title"
            assert len(runs) >= 4, f"Slide {number}: insufficient native text"
            notes = ET.fromstring(package.read(f"ppt/notesSlides/notesSlide{number}.xml"))
            assert sum(len(e.text or "") for e in notes.findall(".//a:t", NS)) > 80, f"Slide {number}: notes missing"
            tables = slide.findall(".//a:tbl", NS)
            if number in (11, 13):
                assert len(tables) == 1, f"Slide {number}: native table required"
            if number == 4:
                for required in ("17.3×", "2.8×", "1.3×", "79% → 86%", "18% → 31%", "2025", "2026"):
                    assert required in normalized, f"Evidence slide missing {required}"
            counts["slides"] += 1
            counts["tables"] += len(tables)
            counts["text_runs"] += len(runs)
        # Master/layout image backgrounds can hide outside the slide XML.
        for name in package.namelist():
            if re.match(r"ppt/(slideMasters|slideLayouts)/.*\.xml$", name):
                root = ET.fromstring(package.read(name))
                assert not root.findall(".//a:blipFill", NS), f"Image fill in {name}"
                assert not root.findall(".//p:pic", NS), f"Picture in {name}"
    return counts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pptx", type=Path, default=ROOT / "assets/presentations/pmday-2026/ai-changes-both-sides.pptx")
    parser.add_argument("--manifest", type=Path, default=ROOT / "assets/presentations/pmday-2026/ai-changes-both-sides.manifest.json")
    args = parser.parse_args()
    try:
        print(json.dumps(validate(args.pptx, args.manifest), indent=2))
    except (AssertionError, KeyError, OSError, ValueError, zipfile.BadZipFile, ET.ParseError) as error:
        print(f"PPTX validation failed: {error}", file=sys.stderr)
        sys.exit(1)
