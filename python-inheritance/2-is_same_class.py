#!/usr/bin/python3
"""Check whether an object has exactly the specified class."""


def is_same_class(obj, a_class):
    """Return True when the object's type matches a_class exactly."""
    return type(obj) is a_class
