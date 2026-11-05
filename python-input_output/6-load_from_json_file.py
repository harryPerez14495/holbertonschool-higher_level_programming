#!/usr/bin/python3
"""Provide a function to load a Python object from a JSON file."""

import json


def load_from_json_file(filename):
    """Read a JSON file and return the represented Python object."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
