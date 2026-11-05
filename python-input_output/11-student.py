#!/usr/bin/python3
"""Define a student with dictionary conversion and reloading."""


class Student:
    """Represent a student with public name and age attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student's name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return all attributes or those selected by string names."""
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace or add instance attributes using a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
