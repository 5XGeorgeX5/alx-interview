#!/usr/bin/python3
"""Model for rotating a 2D matrix in place"""


def rotate_2d_matrix(matrix):
    """Rotate a matrix 90 degree in place"""
    SIZE = len(matrix)

    for r in range(SIZE):
        for c in range(r + 1, SIZE):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for r in range(SIZE):
        matrix[r].reverse()
