#!/usr/bin/python3
"""Module that prints a square using the # character."""


def print_square(size):
    """Print a square of # characters of the given size."""
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if type(size) not in (int, float):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        print("#" * int(size))
