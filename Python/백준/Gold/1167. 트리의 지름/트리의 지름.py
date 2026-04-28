import sys
from collections import deque
input = lambda: sys.stdin.readline()

def bfs_tree(graph, start):
    visited = [-1] * len(graph)
    visited[start] = 0
    queue = deque()
    queue.append(start)
    maxi = (0,0)
    
    while queue:
        node = queue.popleft()
        
        for where, dist in graph[node]:
            if visited[where] == -1:
                visited[where] = visited[node] + dist
                queue.append(where)
                if maxi[1] < visited[where]:
                    maxi = (where, visited[where])
    return maxi


N = int(input())
graph = [[] for _ in range(N)]

for _ in range(N):
    a, *b, _ = input().split()
    a, b = int(a), [*map(int, b)]
    for i in range(0, len(b), 2):
        graph[a-1].append((b[i]-1, b[i+1]))

print(bfs_tree(graph, bfs_tree(graph, 0)[0])[1])