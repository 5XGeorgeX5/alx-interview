#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet a given amount total,
given a pile of coins of different values
"""
from typing import List


def makeChange(coins: List[int], amount: int) -> int:
    """
    Determines the fewest number of coins needed to meet a given amount total,
    given a pile of coins of different values
    """
    if amount <= 0:
        return 0
    coins.sort(reverse=True)
    change = 0
    for c in coins:
        if amount <= 0:
            break
        temp = amount // c
        change += temp
        amount -= (temp * c)
    if amount != 0:
        return -1
    return change
