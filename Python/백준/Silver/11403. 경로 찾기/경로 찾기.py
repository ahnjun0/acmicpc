import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
floyd = []

for _ in range(N):
    inp = [*map(int, input().split())]
    floyd.append([102 if x == 0 else x for x in inp])

for k in range(N):
    for i in range(N):
        for j in range(N):
            floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j])

for val in floyd:
    print(*[1 if x < 102 else 0 for x in val])