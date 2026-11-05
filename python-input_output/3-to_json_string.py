#!/usr/bin/python3
"""Provide a function to convert a Python object to JSON."""

import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object."""
    return json.dumps(my_obj)
