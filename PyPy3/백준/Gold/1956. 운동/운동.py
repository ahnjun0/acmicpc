import sys
input = lambda: map(int, sys.stdin.readline().rstrip().split())

N, M = input()
floyd = [[1e7 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b, c = input()
    floyd[a-1][b-1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            floyd[i][j] = min(floyd[i][j], floyd[i][k]+floyd[k][j])

ans = 1e7

for i in range(N):
    ans = min(ans, floyd[i][i])

print(ans if ans != 1e7 else -1)