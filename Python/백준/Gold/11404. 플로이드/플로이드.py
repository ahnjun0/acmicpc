import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = [[1e9] * n for _ in range(n)]

for a in range(n):
    for b in range(n):
        if a == b: graph[a][b] = 0

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(c, graph[a-1][b-1])


for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for dist in graph:
    for num in dist:
        print("0" if num == 1e9 else num, end=" ")
    print()