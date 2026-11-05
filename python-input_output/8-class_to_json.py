#!/usr/bin/python3
"""Provide a dictionary representation of an object's attributes."""


def class_to_json(obj):
    """Return the object's instance attribute dictionary."""
    return obj.__dict__
