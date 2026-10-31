#!/usr/bin/python3
"""Define a square with controlled access to its size."""


class Square:
    """Represent a square with a validated size property."""

    def __init__(self, size=0):
        """Initialize the square using the size setter."""
        self.size = size

    @property
    def size(self):
        """Return the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Validate and update the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
