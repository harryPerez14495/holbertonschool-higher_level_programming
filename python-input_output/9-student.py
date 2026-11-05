#!/usr/bin/python3
"""Define a student with a dictionary representation."""


class Student:
    """Represent a student by first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student's public attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary containing the student's attributes."""
        return self.__dict__
