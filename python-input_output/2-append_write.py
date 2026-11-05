#!/usr/bin/python3
"""Provide a function to append text to a UTF-8 file."""


def append_write(filename="", text=""):
    """Append text and return the number of characters written."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
