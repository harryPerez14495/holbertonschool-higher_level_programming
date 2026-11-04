#!/usr/bin/python3
"""Define a square with area calculation and string display."""


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

    def __str__(self):
        """Return the square's description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
