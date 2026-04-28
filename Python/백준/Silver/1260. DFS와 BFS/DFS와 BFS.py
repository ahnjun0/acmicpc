import sys
from collections import defaultdict, deque
input = lambda: map(int, sys.stdin.readline().rstrip().split())

def dfs(graph, v, visited):
    visited.append(v)
    for node in sorted(graph[v]):
        if node not in visited:
            dfs(graph, node, visited)
    return visited

def bfs(graph, v, visited):
    visited = []
    queue = deque()
    queue.append(v)
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))
    return visited

inp = defaultdict(list)
N, M, V = input()
for _ in range(M):
    a, b = input()
    inp[a].append(b)
    inp[b].append(a)
    
visited = []
print(*dfs(inp, V, visited))

visited = []
print(*bfs(inp, V, visited))
