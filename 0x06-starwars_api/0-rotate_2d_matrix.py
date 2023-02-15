#!/usr/bin/env python3
"""
Module defining a function that rotates a 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    Function that rotates a 2d n * n matrix 90 degrees clockwise
    """
    # First Transpose the matrix
    i = 0
    while i < len(matrix):
        j = i
        while j < len(matrix[0]):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            j += 1
        i += 1
    # Second Reverse each row
    for row in matrix:
        i = 0  # start index pointer
        j = len(row) - 1  # last index pointer
        while i < j//2:
            temp = row[i]
            row[i] = row[j]
            row[j] = temp
            i += 1
            j -= 1
