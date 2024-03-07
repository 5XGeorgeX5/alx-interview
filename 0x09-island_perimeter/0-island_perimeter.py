#!/usr/bin/python3
"""Defines an island perimeter measuring function."""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid."""
    rows, cols, perimeter = len(grid), len(grid[0]), 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0:
                    perimeter -= 2 * grid[i - 1][j]
                if j > 0:
                    perimeter -= 2 * grid[i][j - 1]
    return perimeter
