#!/usr/bin/python3
"""Define a base geometry class with an area method."""


class BaseGeometry:
    """Represent the base class for geometric shapes."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")

