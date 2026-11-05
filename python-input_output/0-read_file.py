#!/usr/bin/python3
"""Provide a function to display a UTF-8 text file."""


def read_file(filename=""):
    """Print the file contents without adding extra newlines."""
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
