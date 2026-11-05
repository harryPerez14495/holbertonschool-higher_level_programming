#!/usr/bin/python3
"""Provide a function to save a Python object as JSON."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object's JSON representation to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
