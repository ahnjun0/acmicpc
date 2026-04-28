import sys
input = lambda: map(int, sys.stdin.readline().split())

N, M = input()
A = [[*input()] for _ in range(N)]
_, K = input()
B = [[*input()] for _ in range(M)]

AB = [[0] * K for _ in range(N)]
for r in range(N):
    for c in range(K):
        for i in range(M):
            AB[r][c] += A[r][i] * B[i][c]

for i in AB:
    print(*i)