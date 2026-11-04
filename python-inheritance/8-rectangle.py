#!/usr/bin/python3
"""Define a rectangle with validated private dimensions."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with positive integer dimensions."""

    def __init__(self, width, height):
        """Validate and store the rectangle's width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
