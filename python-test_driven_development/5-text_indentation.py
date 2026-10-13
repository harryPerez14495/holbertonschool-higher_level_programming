#!/usr/bin/python3
"""Module for printing text with indentation."""


def text_indentation(text):
    """Print text with two newlines after '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""

    for char in text:
        if char in ".?:":
            print(line.strip() + char)
            print()
            line = ""
        else:
            line += char

    if line.strip():
        print(line.strip(), end="")
