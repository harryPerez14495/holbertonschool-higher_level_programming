#!/usr/bin/python3
"""Build Pascal's triangle as a list of integer lists."""


def pascal_triangle(n):
    """Return n rows of Pascal's triangle, or [] when n <= 0."""
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
