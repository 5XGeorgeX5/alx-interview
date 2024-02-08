#!/usr/bin/python3
"""solves the N queens problem"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if N < 4:
    print("N must be at least 4")
    exit(1)

board = [[0 for _ in range(N)] for _ in range(N)]


def isSafe(row, col):
    """checks if a sqaur is save for queen"""
    for i in range(row):
        if board[i][col]:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j]:
            return False
        i -= 1
        j += 1
    return True


ans = []


def SolveNQueens(row):
    """solves the N queens problem"""
    if (row == N):
        print(ans)
        return
    for i in range(N):
        if isSafe(row, i):
            board[row][i] = 1
            ans.append([row, i])
            SolveNQueens(row + 1)
            ans.pop()
            board[row][i] = 0


SolveNQueens(0)
