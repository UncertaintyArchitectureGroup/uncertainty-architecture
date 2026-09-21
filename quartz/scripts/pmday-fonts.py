"""Embed the licensed, fixed Roboto regular/bold font data in a staged PPTX."""
import argparse
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

P = "http://schemas.openxmlformats.org/presentationml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL = "http://schemas.openxmlformats.org/package/2006/relationships"
CT = "http://schemas.openxmlformats.org/package/2006/content-types"
ET.register_namespace("p", P)
ET.register_namespace("a", "http://schemas.openxmlformats.org/drawingml/2006/main")
ET.register_namespace("r", R)


def embed(source, target, archive):
    with zipfile.ZipFile(source) as package:
        parts = {name: package.read(name) for name in package.namelist()}
    presentation = ET.fromstring(parts["ppt/presentation.xml"])
    assert presentation.find(f"{{{P}}}embeddedFontLst") is None, "Fonts already embedded"
    presentation.set("embedTrueTypeFonts", "1")
    presentation.set("saveSubsetFonts", "0")
    fonts = ET.Element(f"{{{P}}}embeddedFontLst")
    font = ET.SubElement(fonts, f"{{{P}}}embeddedFont")
    ET.SubElement(font, f"{{{P}}}font", {"typeface": "Roboto"})
    rels_name = "ppt/_rels/presentation.xml.rels"
    rels = ET.fromstring(parts[rels_name])
    with zipfile.ZipFile(archive) as licensed:
        for style in ("Regular", "Bold"):
            rid = f"rIdRoboto{style}"
            assert all(rel.get("Id") != rid for rel in rels), "Font relationship collision"
            name = f"ppt/fonts/Roboto-{style}.fntdata"
            assert name not in parts, "Font part collision"
            parts[name] = licensed.read(f"Roboto-{style}.fntdata")
            ET.SubElement(font, f"{{{P}}}{style.lower()}", {f"{{{R}}}id": rid})
            ET.SubElement(rels, f"{{{REL}}}Relationship", {
                "Id": rid, "Type": f"{R}/font", "Target": f"fonts/Roboto-{style}.fntdata",
            })
    # CT_Presentation puts embeddedFontLst before these optional later children.
    later = {"custShowLst", "photoAlbum", "custDataLst", "kinsoku", "defaultTextStyle", "modifyVerifier", "extLst"}
    index = next((i for i, child in enumerate(presentation) if child.tag.split("}")[-1] in later), len(presentation))
    presentation.insert(index, fonts)
    types = ET.fromstring(parts["[Content_Types].xml"])
    existing = [e for e in types if e.get("Extension") == "fntdata"]
    assert not existing or all(e.get("ContentType") == "application/x-fontdata" for e in existing), "Conflicting font content type"
    if not existing:
        ET.SubElement(types, f"{{{CT}}}Default", {"Extension": "fntdata", "ContentType": "application/x-fontdata"})
    for name, tree in (("ppt/presentation.xml", presentation), (rels_name, rels), ("[Content_Types].xml", types)):
        # LibreOffice's OPC reader requires a default content-types namespace.
        if name == "[Content_Types].xml":
            ET.register_namespace("", CT)
        elif name == rels_name:
            ET.register_namespace("", REL)
        parts[name] = ET.tostring(tree, encoding="utf-8", xml_declaration=True)
    # Exclusive output: this helper never overwrites an existing artifact.
    with zipfile.ZipFile(target, "x", zipfile.ZIP_DEFLATED) as package:
        for name, data in parts.items():
            package.writestr(name, data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    parser.add_argument("archive", type=Path)
    args = parser.parse_args()
    embed(args.source, args.target, args.archive)
