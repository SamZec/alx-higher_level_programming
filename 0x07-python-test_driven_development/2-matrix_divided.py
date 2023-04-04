#!/usr/bin/python3
# 2-matrix_divided.py
"""
    A module for matrix_divided funtion

"""


def matrix_divided(matrix, div):
    """
        a function that divides all elements of a matrix.

        matrix: list of lists of integers or float
        div: number to divide matrix by and should no be 0

        Return: New matrix with the results of the divition

    """
    divided_matrix = []
    if ((not matrix or matrix is None) or
            not all(isinstance(elem, list) for elem in matrix)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    for elem in matrix:
        if (not all(isinstance(row, int) for row in elem) and
                not all(isinstance(row, float) for row in elem)):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if len(elem) != len(matrix[0]):
            raise TypeError("Each row of the matrix must"
                            " have the same size")
        divided_matrix.append(list(map(lambda x: round(x / div, 2), elem)))
    return divided_matrix
