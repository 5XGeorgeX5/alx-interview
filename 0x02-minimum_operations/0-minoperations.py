#!/usr/bin/python3
"""
calculates the fewest number of operations
needed to result in exactly n H characters
"""


def minOperations(n):
    """
    calculates the fewest number of operations
    needed to result in exactly n H characters
    """
    if n < 2:
        return 0
    h = paste = op = 1
    while h < n:
        if (h/2 > paste and n % h == 0):
            paste = h
            h *= 2
            op += 2
        else:
            h += paste
            op += 1
    return op
