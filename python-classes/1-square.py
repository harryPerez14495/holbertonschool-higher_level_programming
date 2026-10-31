#!/usr/bin/python3
"""Define a square with a private size attribute."""


class Square:
    """Represent a square with a given size."""

    def __init__(self, size):
        """Initialize the square with its private size."""
        self.__size = size
