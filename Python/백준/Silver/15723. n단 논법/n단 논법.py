import sys
input = lambda: sys.stdin.readline().rstrip()

graph = [[27] * 26 for _ in range(26)]

for _ in range(int(input())):
    a, b = map(lambda x: ord(x)-97, input().rstrip().split(" is "))
    graph[a][b] = 1

for k in range(26):
    for i in range(26):
        for j in range(26):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(int(input())):
    x, y = map(lambda x: ord(x)-97, input().rstrip().split(" is "))
    print("T" if graph[x][y] != 27 else "F")