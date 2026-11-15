#!/usr/bin/env python3
"""Define shapes and display their area and perimeter."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter."""
        pass


class Circle(Shape):
    """Represent a circle."""

    def __init__(self, radius):
        """Initialize the radius."""
        self.radius = radius

    def area(self):
        """Return the circle's area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return a nonnegative perimeter."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Represent a rectangle."""

    def __init__(self, width, height):
        """Initialize the width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return a nonnegative area."""
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        """Return a nonnegative perimeter."""
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """Print the area and perimeter using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
