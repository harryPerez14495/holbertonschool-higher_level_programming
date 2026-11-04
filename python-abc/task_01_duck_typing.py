#!/usr/bin/python3
"""Define abstract shapes and display their measurements."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Define the methods required for geometric shapes."""

    @abstractmethod
    def area(self):
        """Return the shape's area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the shape's perimeter."""
        pass


class Circle(Shape):
    """Represent a circle with a radius."""

    def __init__(self, radius):
        """Initialize the circle's radius."""
        self.radius = radius

    def area(self):
        """Return the circle's area."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the circle's circumference."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represent a rectangle with width and height."""

    def __init__(self, width, height):
        """Initialize the rectangle's dimensions."""
        self.width = width
        self.height = height

    def area(self):
        """Return the rectangle's area."""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle's perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print an object's area and perimeter using its methods."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
