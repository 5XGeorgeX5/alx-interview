#!/usr/bin/python3
"""prints pascal triangle with hight n"""

def pascal_triangle(n):
    """prints pascal triangle with hight n"""
    if (n <= 0):
        return []
    ans = [[1]]
    for i in range(n-1):
        lst = [1]
        for j in range (i):
            lst.append(ans[i][j] + ans[i][j+1])
        lst.append(1)
        ans.append(lst)
    return ans