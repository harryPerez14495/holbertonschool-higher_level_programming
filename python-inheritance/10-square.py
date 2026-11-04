#!/usr/bin/python3
"""Define a square using the Rectangle class."""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represent a square with a positive integer size."""

    def __init__(self, size):
        """Validate and store the size, then initialize the rectangle."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
