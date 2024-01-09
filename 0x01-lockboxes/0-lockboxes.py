#!/usr/bin/python3
"""determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    n = len(boxes)
    locked = [True] * n
    locked[0] = False
    queue = [0]
    count = 1

    while queue and (count != n):
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and locked[key]:
                locked[key] = False
                queue.append(key)
                count += 1
    return (n == count)
