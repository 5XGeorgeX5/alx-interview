#!/usr/bin/python3
"""determines if all the boxes can be opened"""

def canUnlockAll(boxes):
    """determines if all the boxes can be opened"""
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    queue = [0]

    while queue and (n != 1):
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if not unlocked[key]:
                unlocked[key] = True
                queue.append(key)
                n -= 1
    return (n == 1)
