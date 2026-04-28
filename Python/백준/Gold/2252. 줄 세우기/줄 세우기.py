import sys
from collections import deque
input = lambda: map(int, sys.stdin.readline().split())

N, M = input()
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for _ in range(M):
    A, B = input()
    graph[A].append(B)
    degree[B] += 1

queue = deque()

for i in range(1, N+1):
    if degree[i] == 0: queue.append(i)

ans = []
while queue:
    ans.append(v := queue.popleft())
    
    for adj in graph[v]:
        degree[adj] -= 1
        if degree[adj] == 0: queue.append(adj)

print(*ans)