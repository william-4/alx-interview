#!/usr/bin/python3
"""
Module defining a function that rotates a 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    Function that rotates a 2d n * n matrix 90 degrees clockwise
    """
    # First Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    # Second Reverse the matrix
    for i in range(n):
        for j in range(int(n / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-1-j] = 
