# dp = [y][x][sumof] version.

import sys
input = lambda: sys.stdin.readline()

N = int(input())
board = [[i for i in input().split()] for _ in range(N)]

# 0: Horizontal → / 1: Vertical ↓ / 2: Diagonal ↘
dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]

dp[0][1][0] = 1
for i in range(2, N):
    if board[0][i] == '0':
        dp[0][i][0] = 1
    else: break

for y in range(1, N):
    for x in range(1, N):
        if board[y][x] == '0' and board[y-1][x] == '0' and board[y][x-1] == '0':
            dp[y][x][2] = sum([dp[y-1][x-1][i] for i in range(3)])

        if board[y][x] == '0':
            dp[y][x][0] = sum(dp[y][x-1][i] for i in [0,2])
            dp[y][x][1] = sum(dp[y-1][x][i] for i in [1,2])

print(sum(dp[N-1][N-1][i] for i in range(3)))