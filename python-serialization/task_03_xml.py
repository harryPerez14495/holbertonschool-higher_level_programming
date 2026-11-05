#!/usr/bin/python3
"""Serialize dictionaries to XML and deserialize XML files."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Save dictionary entries as child elements of a data root."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Read an XML file and return a dictionary of string values."""
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
