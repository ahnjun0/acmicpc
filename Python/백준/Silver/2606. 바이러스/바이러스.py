import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

visited = []
graph = {}
need = deque()

comp = int(input())
pair = int(input())

for _ in range(pair):
    a, b = map(int, input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
        
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

if 1 in graph:
    need.append(1)
    while need:
        node = need.pop()
        if node not in visited:
            visited.append(node)
            need.extend(graph[node])

    print(len(visited)-1)

else:
    print(0)