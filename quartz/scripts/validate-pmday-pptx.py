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
COVER = "assets/presentations/pmday-2026/artwork/ai-two-roles.png"
INPUTS = [SOURCE, COVER, "quartz/scripts/pmday-presentation.mjs", "quartz/scripts/build-pmday-pptx.mjs", "quartz/scripts/validate-pmday-pptx.py"]
NS = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main", "a": "http://schemas.openxmlformats.org/drawingml/2006/main"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def validate(pptx, manifest_path):
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest.get("schema_version") == 1, "Unsupported manifest"
    assert manifest["pptx_sha256"] == digest(pptx.read_bytes()), "PPTX checksum mismatch"
    assert manifest.get("image_exceptions") == [{"slide": 1, "asset": COVER, "purpose": "Requested conceptual cover illustration"}], "Unapproved image exceptions"
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
            pictures = slide.findall(".//p:pic", NS)
            assert len(pictures) == (1 if number == 1 else 0), f"Slide {number}: image exceptions violated"
            # One requested foreground illustration is allowed; no background or native-shape image fills.
            assert not slide.findall(".//p:bg//a:blipFill", NS), f"Slide {number}: image background forbidden"
            assert not slide.findall(".//p:sp//a:blipFill", NS), f"Slide {number}: image fill forbidden"
            if pictures:
                pic = pictures[0]
                extent = pic.find("p:spPr/a:xfrm/a:ext", NS)
                assert extent is not None and int(extent.get("cx")) <= 640*9525 and int(extent.get("cy")) <= 440*9525, "Cover image exceeds foreground boundary"
                blip = pic.find("p:blipFill/a:blip", NS)
                rid = blip.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed") if blip is not None else None
                rels = ET.fromstring(package.read("ppt/slides/_rels/slide1.xml.rels"))
                targets = [r.get("Target") for r in rels if r.get("Id") == rid and r.get("TargetMode") in (None, "Internal") and r.get("Type", "").endswith("/image")]
                assert len(targets) == 1 and re.fullmatch(r"(?:/ppt|\.\.)/media/[^/]+", targets[0]), "Cover image relationship invalid"
                # OOXML permits package-absolute and slide-relative internal part names.
                media = targets[0].lstrip("/") if targets[0].startswith("/") else "ppt/" + targets[0][3:]
                assert digest(package.read(media)) == manifest["inputs"][COVER], "Cover image bytes differ from approved asset"
            assert not slide.findall(".//p:oleObj", NS), f"Slide {number}: OLE object forbidden"
            runs = [e.text or "" for e in slide.findall(".//a:t", NS)]
            normalized = " ".join(" ".join(runs).split())
            assert titles[number - 1] in normalized, f"Slide {number}: wrong/missing title"
            assert len(runs) >= 4, f"Slide {number}: insufficient native text"
            # Native editable text must stay inside the declared page. This is
            # a geometry guard only; line wrapping still needs a rendered review.
            for shape in slide.findall(".//p:sp", NS):
                if not shape.findall(".//a:t", NS):
                    continue
                transform = shape.find("p:spPr/a:xfrm", NS)
                assert transform is not None, f"Slide {number}: text geometry missing"
                offset, extent = transform.find("a:off", NS), transform.find("a:ext", NS)
                x, y = int(offset.get("x")), int(offset.get("y"))
                w, h = int(extent.get("cx")), int(extent.get("cy"))
                assert x >= 0 and y >= 0 and w > 0 and h > 0 and x+w <= 12192000 and y+h <= 6858000, f"Slide {number}: text outside canvas"
            notes = ET.fromstring(package.read(f"ppt/notesSlides/notesSlide{number}.xml"))
            assert sum(len(e.text or "") for e in notes.findall(".//a:t", NS)) > 80, f"Slide {number}: notes missing"
            tables = slide.findall(".//a:tbl", NS)
            if number in (11, 13):
                assert len(tables) == 1, f"Slide {number}: native table required"
            if number == 4:
                for required in ("17.3×", "2.8×", "1.3×", "79% → 86%", "18% → 31%", ">80%", "59%", "Moved-code share", "+81%", "2025", "2026"):
                    assert required in normalized, f"Evidence slide missing {required}"
            if number == 3:
                for required in ("THEORY OF CONSTRAINTS", "+92 / week", "Illustrative", "AI can affect every stage"):
                    assert required in normalized, f"SDLC slide missing {required}"
            counts["slides"] += 1
            counts["pictures"] += len(pictures)
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
