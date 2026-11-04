#!/usr/bin/python3
"""Check whether an object belongs to a derived class."""


def inherits_from(obj, a_class):
    """Return True for instances of strict subclasses of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
