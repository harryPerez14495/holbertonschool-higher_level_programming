#!/usr/bin/python3
"""Module for dividing all elements of a matrix."""


def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by div."""
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if (not isinstance(matrix, list) or not matrix or
            any(not isinstance(row, list) or not row for row in matrix)):
        raise TypeError(error)

    size = len(matrix[0])

    for row in matrix:
        if any(type(value) not in (int, float) for value in row):
            raise TypeError(error)
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(value / div, 2) for value in row]
            for row in matrix]
