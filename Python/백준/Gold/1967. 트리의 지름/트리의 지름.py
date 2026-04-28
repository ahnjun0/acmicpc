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

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))
print(bfs_tree(graph, bfs_tree(graph, 0)[0])[1])