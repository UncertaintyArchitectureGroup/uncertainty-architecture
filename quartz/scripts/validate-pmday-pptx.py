"""Portable OOXML acceptance checks; no rendering or authoring dependency required."""
import argparse
import hashlib
import json
import posixpath
from pathlib import Path
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
SOURCE = "assets/presentations/pmday-2026/README.md"
COVER = "assets/presentations/pmday-2026/artwork/ai-two-roles.png"
FONTS = "assets/presentations/pmday-2026/artwork/roboto-fonts.zip"
INPUTS = [SOURCE, COVER, FONTS, "assets/presentations/pmday-2026/frozen-slides.json", "quartz/scripts/pmday-presentation.mjs", "quartz/scripts/build-pmday-pptx.mjs", "quartz/scripts/validate-pmday-pptx.py", "quartz/scripts/pmday-fonts.py"]
NS = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main", "a": "http://schemas.openxmlformats.org/drawingml/2006/main"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


FREEZE = "assets/presentations/pmday-2026/frozen-slides.json"
REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
CREATION_ID = "{http://schemas.microsoft.com/office/drawing/2014/main}creationId"


def frozen_source_hashes(source):
    sections = re.findall(r"^## (\d+)\. [^\n]+\n[\s\S]*?(?=^## \d+\. |\Z)", source, re.M)
    assert sections == [str(i) for i in range(1, 15)], "Frozen source: invalid slide order"
    blocks = re.finditer(r"^## (\d+)\. [^\n]+\n[\s\S]*?(?=^## \d+\. |\Z)", source, re.M)
    return {m[1]: digest(m[0].encode()) for m in blocks if int(m[1]) <= 8}


def frozen_package_hashes(package):
    """Hash slides 1–8 and their dependency closure, ignoring only generated IDs.

    Relationships are resolved to their semantic type/target, not UUIDs. Shared
    presentation settings are included; its slide list is restricted to 1–8.
    Notes, layout/master/theme, cover bytes and relationship rewiring are covered.
    This is an accidental-change guard, not independent authorization evidence.
    """
    result = {}
    pending = ["ppt/presentation.xml"]
    while pending:
        name = pending.pop()
        if name in result:
            continue
        data = package.read(name)
        directory, filename = posixpath.split(name)
        relname = posixpath.join(directory, "_rels", filename + ".rels")
        rels = {}
        if relname in package.namelist():
            for rel in ET.fromstring(package.read(relname)):
                target = rel.get("Target")
                mode = rel.get("TargetMode", "Internal")
                target = target if mode == "External" else posixpath.normpath(posixpath.join(directory, target)).lstrip("/")
                if name == "ppt/presentation.xml" and rel.get("Type").endswith("/slide"):
                    match = re.fullmatch(r"ppt/slides/slide(\d+)\.xml", target)
                    assert match is not None, "Frozen presentation: unexpected slide target"
                    if int(match[1]) > 8:
                        continue
                rels[rel.get("Id")] = [rel.get("Type"), mode, target]
                if mode != "External":
                    pending.append(target)
            result[relname] = digest(json.dumps(sorted(rels.values()), ensure_ascii=False).encode())
        if name.endswith(".xml"):
            tree = ET.fromstring(data)
            if name == "ppt/presentation.xml":
                slide_ids = tree.find("p:sldIdLst", NS)
                assert slide_ids is not None and len(slide_ids) == 14, "Frozen presentation: invalid slide list"
                for child in list(slide_ids)[8:]:
                    slide_ids.remove(child)
            for element in tree.iter():
                if element.tag == CREATION_ID:
                    element.set("id", "generated")
                if element.tag == "{http://schemas.microsoft.com/office/powerpoint/2010/main}creationId":
                    element.set("val", "generated")
                for key, value in list(element.attrib.items()):
                    if key.startswith("{" + REL_NS + "}"):
                        assert value in rels, f"Frozen package: unresolved relationship in {name}"
                        element.set(key, json.dumps(rels[value], ensure_ascii=False))
            data = ET.tostring(tree, encoding="utf-8")
        result[name] = digest(data)
    return dict(sorted(result.items()))


def validate_frozen(source, package):
    record = json.loads((ROOT / FREEZE).read_text(encoding="utf-8"))
    assert record.get("schema_version") == 1 and record.get("slides") == list(range(1, 9)), "Invalid frozen-slide record"
    assert record["source_sections"] == frozen_source_hashes(source), "Frozen slides 1–8: source changed; explicit maintainer request required"
    actual = frozen_package_hashes(package)
    changed = sorted(set(actual) ^ set(record["package_parts"]) | {name for name in actual if actual[name] != record["package_parts"].get(name)})
    assert not changed, f"Frozen slides 1–8: rendered content/dependency changed: {', '.join(changed)}"


def validate_fonts(package):
    presentation = ET.fromstring(package.read("ppt/presentation.xml"))
    assert presentation.get("embedTrueTypeFonts") == "1" and presentation.get("saveSubsetFonts") == "0", "Roboto: full font embedding must be enabled"
    fonts = presentation.findall("p:embeddedFontLst/p:embeddedFont", NS)
    assert len(fonts) == 1 and fonts[0].find("p:font", NS).get("typeface") == "Roboto", "Roboto: embedded family missing"
    types = ET.fromstring(package.read("[Content_Types].xml"))
    assert any(e.get("Extension") == "fntdata" and e.get("ContentType") == "application/x-fontdata" for e in types), "Roboto: font content type missing"
    rels = ET.fromstring(package.read("ppt/_rels/presentation.xml.rels"))
    with zipfile.ZipFile(ROOT / FONTS) as archive:
        provenance = json.loads(archive.read("PROVENANCE.json"))
        for name, expected in provenance["sha256"].items():
            assert digest(archive.read(name)) == expected, f"Roboto: stale archived asset {name}"
        for style in ("Regular", "Bold"):
            reference = fonts[0].find(f"p:{style.lower()}", NS)
            assert reference is not None, f"Roboto: {style} reference missing"
            matches = [r for r in rels if r.get("Id") == reference.get(f"{{{REL_NS}}}id")]
            assert len(matches) == 1, f"Roboto: {style} relationship missing or duplicated"
            rel = matches[0]
            assert rel.get("Type") == f"{REL_NS}/font" and rel.get("TargetMode", "Internal") == "Internal", f"Roboto: {style} font relationship invalid"
            target = posixpath.normpath(posixpath.join("ppt", rel.get("Target"))).lstrip("/")
            assert target == f"ppt/fonts/Roboto-{style}.fntdata", f"Roboto: {style} font target invalid"
            assert target in package.namelist() and package.read(target) == archive.read(f"Roboto-{style}.fntdata"), f"Roboto: {style} embedded bytes missing or corrupted"
    for name in package.namelist():
        if re.fullmatch(r"ppt/(slides|notesSlides)/[^/]+\.xml", name):
            faces = [e.get("typeface") for e in ET.fromstring(package.read(name)).iter() if "typeface" in e.attrib]
            assert (faces or name.startswith("ppt/notesSlides/")) and set(faces) <= {"Roboto"}, f"Roboto: unexpected text font in {name}"


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
                offset = pic.find("p:spPr/a:xfrm/a:off", NS)
                assert extent is not None and offset is not None, "Cover image geometry missing"
                px, py = int(offset.get("x")), int(offset.get("y"))
                pw, ph = int(extent.get("cx")), int(extent.get("cy"))
                assert px >= 96*9525 and py >= 225*9525 and 0 < pw <= 1088*9525 and 0 < ph <= 370*9525 and px+pw <= 1184*9525 and py+ph <= 602*9525, "Cover image exceeds foreground boundary"
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
            # The requested block rows have symmetric outer margins. Check their
            # exported geometry, not only the source layout constants.
            if number in (2, 3):
                for shape in slide.findall(".//p:sp", NS):
                    geom = shape.find("p:spPr/a:prstGeom", NS)
                    if geom is None or geom.get("prst") != "rect" or shape.find("p:spPr/a:solidFill", NS) is None:
                        continue
                    transform = shape.find("p:spPr/a:xfrm", NS)
                    if transform is None:
                        continue
                    offset, extent = transform.find("a:off", NS), transform.find("a:ext", NS)
                    x, w = int(offset.get("x")), int(extent.get("cx"))
                    assert x >= 96*9525 and x+w <= 1184*9525, f"Slide {number}: block outside safe margins"
            notes = ET.fromstring(package.read(f"ppt/notesSlides/notesSlide{number}.xml"))
            assert sum(len(e.text or "") for e in notes.findall(".//a:t", NS)) > 80, f"Slide {number}: notes missing"
            tables = slide.findall(".//a:tbl", NS)
            if number in (11, 13):
                assert len(tables) == 1, f"Slide {number}: native table required"
            if number == 4:
                for required in ("SEP 2026 REVISION", "25.5×", "3.4×", "1.3×", "≈78% → 87%", "19% → 33%", "Jan 2025 → Apr 2026", "first 3 months", ">80%", "59%", "≈ +0.10 SD", "89% credible interval", "+0.07 to +0.13", "Survey model", "Moved-code share", "13% → 3.8%", "Calls / 1k changed lines", "343 → 223", "−9.2 pp (−70.8%)", "−120 (≈−35%)", "not a quality verdict", "≈+81%", "+15%", "1.4–2×", "3 questions", "+34.85% / +42.87%", "Agent-first / IDE-first", "Higher throughput", "Lower delivery stability", "2025", "2026"):
                    assert required in normalized, f"Evidence slide missing {required}"
            if number == 3:
                assert not any(e.get("type", "none") != "none" for e in slide.findall(".//a:tailEnd", NS) + slide.findall(".//a:headEnd", NS)), "SDLC slide must not contain arrowheads"
                for required in ("THEORY OF CONSTRAINTS", "BEFORE", "AFTER AI", "+92", "Illustrative", "AI can affect every stage", "not sped up"):
                    assert required in normalized, f"SDLC slide missing {required}"
            if number == 5:
                paths = slide.findall(".//a:custGeom/a:pathLst/a:path", NS)
                assert any(len(p.findall("a:lnTo", NS)) >= 80 for p in paths), "Comprehension curve missing smooth native path"
                for required in ("YES", "NOT AT THIS RATE", "5 years?", "?"):
                    assert required in normalized, f"Comprehension slide missing {required}"
            if number == 6:
                assert "WATCH" not in normalized.upper() and "EXPLORE" not in normalized.upper(), "Recovery slide still contains Watch / Explore"
                for required in ("technical systems with limits", "Team diagnoses", "proposes fix", "Validate fix"):
                    assert required in normalized, f"Recovery slide missing {required}"
            if number == 7:
                for required in ("WATCH", "EXPLORE", "WIP limits", "Repository intelligence", "Human recovery drills"):
                    assert required in normalized, f"Equilibrium slide missing {required}"
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
        validate_fonts(package)
        validate_frozen(source, package)
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
