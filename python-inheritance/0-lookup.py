#!/usr/bin/python3
"""Define a function to list available object attributes."""


def lookup(obj):
    """Return the list of available attributes and methods."""
    return dir(obj)
