#!/usr/bin/python3
"""
Module for pascal triangle
"""


def pascal_triangle(n):
    """
    Creates a lists of pascal triangle
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        triangle.append([a+b for a, b
                         in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
