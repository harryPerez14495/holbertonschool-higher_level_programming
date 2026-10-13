#!/usr/bin/python3
"""Module for adding two integers."""


def add_integer(a, b=98):
    """Return the sum of two integers after converting floats."""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
