#!/usr/bin/python3
"""Serialize and deserialize custom objects using pickle."""

import pickle


class CustomObject:
    """Represent a person with a name, age, and student status."""

    def __init__(self, name, age, is_student):
        """Initialize the object's public attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Save the object to a binary file, returning None on failure."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError, TypeError, AttributeError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load an instance, returning None for missing or invalid files."""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            if isinstance(obj, cls):
                return obj
            return None
        except (OSError, pickle.PickleError, EOFError, AttributeError,
                ImportError, IndexError, TypeError, ValueError):
            return None
