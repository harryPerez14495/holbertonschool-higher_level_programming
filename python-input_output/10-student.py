#!/usr/bin/python3
"""Define a student with optional JSON attribute filtering."""


class Student:
    """Represent a student's name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student's public attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return all attributes or those selected by a list of strings."""
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__
