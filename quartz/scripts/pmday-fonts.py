"""Set the requested standard Arial family in every PPTX text/theme font reference.

No proprietary font binaries are redistributed. Applications resolve Arial from
installed/platform fonts; independent previews must report any substitution.
"""
import argparse
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

A = "http://schemas.openxmlformats.org/drawingml/2006/main"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
ET.register_namespace("p", P)
ET.register_namespace("a", A)
ET.register_namespace("r", "http://schemas.openxmlformats.org/officeDocument/2006/relationships")


def standardize(source, target):
    with zipfile.ZipFile(source) as package:
        parts = {name: package.read(name) for name in package.namelist()}
    assert not any(name.startswith("ppt/fonts/") for name in parts), "Unexpected embedded font data"
    for name, data in list(parts.items()):
        if not name.startswith("ppt/") or not name.endswith(".xml"):
            continue
        tree = ET.fromstring(data)
        assert tree.find(f"{{{P}}}embeddedFontLst") is None, "Unexpected embedded font list"
        changed = False
        for element in tree.iter():
            if "typeface" in element.attrib and element.get("typeface") != "Arial":
                element.set("typeface", "Arial")
                changed = True
        if changed:
            parts[name] = ET.tostring(tree, encoding="utf-8", xml_declaration=True)
    with zipfile.ZipFile(target, "x", zipfile.ZIP_DEFLATED) as package:
        for name, data in parts.items():
            package.writestr(name, data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    args = parser.parse_args()
    standardize(args.source, args.target)
