#!/usr/bin/python3
"""Define a list subclass with sorted printing."""


class MyList(list):
    """Represent a list with a sorted display method."""

    def print_sorted(self):
        """Print values in ascending order without changing the list."""
        print(sorted(self))
