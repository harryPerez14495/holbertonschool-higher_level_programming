#!/usr/bin/python3
"""Provide a function to write text to a UTF-8 file."""


def write_file(filename="", text=""):
    """Write text to a file and return the character count."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
