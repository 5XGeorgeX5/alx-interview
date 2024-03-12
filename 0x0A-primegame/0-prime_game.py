#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Determines if a player is the winner"""
    if x is None or nums is None or len(nums) == 0:
        return None
    if x < 1:
        return None
    if x < len(nums):
        return None
    b_win, m_win = 0, 0

    for n in nums:
        prime = [True for i in range(n+1)]
        p = 2
        count = 0
        while p * p <= n:
            if prime[p] is True:
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1

        for p in range(2, n+1):
            if prime[p]:
                count += 1
        if count % 2 == 0:
            b_win += 1
        else:
            m_win += 1
    if b_win > m_win:
        return "Ben"
    if b_win < m_win:
        return "Maria"
    return None
