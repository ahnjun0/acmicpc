import sys
from collections import deque
input = lambda: map(int, sys.stdin.readline().rstrip().split())

# KnapSack Problem


N, K = input()

stuff = [[0, 0]]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
    stuff.append([*input()])

for i in range(1, N+1):
    for j in range(1, K+1):
        W, V = stuff[i]
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V) if W <= j else dp[i-1][j]

print(dp[-1][-1])