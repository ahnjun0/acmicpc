import sys
input = lambda: map(int, sys.stdin.readline().rstrip().split())

N, M = input()
floyd = [[False for _ in range(N)] for _ in range(N)]

for _ in range(M):
    a, b = input()
    floyd[a-1][b-1] = True

for k in range(N):
    for i in range(N):
        for j in range(N):
            if floyd[i][k] and floyd[k][j]:
                floyd[i][j] = True
cnt = 0

for i in range(N):
    for j in range(N):
        if i != j and not (floyd[i][j] or floyd[j][i]):
            known = False
            break
    else:
        cnt += 1

print(cnt)