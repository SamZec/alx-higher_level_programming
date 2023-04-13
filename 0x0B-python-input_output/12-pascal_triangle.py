#!/usr/bin/python3
# 12-pascal_triangle.py
"""A module for pascal_triangl function that returns pascal triangle"""


def pascal_triangle(n):
    """a function def pascal_triangle(n): that returns a list of
        lists of integers representing the Pascal’s triangle of n:

        n: integer for height of triangle
    """
    if n <= 0:
        return []
    triangle = []
    hld = []

    for i in range(n):
        level = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                level.append(1)
            else:
                level.append(hld[j] + hld[j - 1])
        hld = level
        triangle.append(level)
    return triangle
