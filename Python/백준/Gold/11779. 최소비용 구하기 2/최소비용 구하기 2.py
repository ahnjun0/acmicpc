import sys, heapq
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

def dijkstra(graph, start, N):
    dist = {node: -1 for node in graph}
    path = {node: 0 for node in graph}

    dist[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    
    while queue:
        now_dist, now_where = heapq.heappop(queue)
        
        if dist[now_where] != -1 and dist[now_where] < now_dist:
            continue
        
        for new_where, new_dist in graph[now_where].items():
            far = now_dist + new_dist
            if dist[new_where] == -1 or (far < dist[new_where]):
                dist[new_where] = far
                heapq.heappush(queue, [far, new_where])
                
                path[new_where] = now_where
                
    return dist, path

graph = defaultdict(lambda: defaultdict(lambda: 100001))

N = int(input())
M = int(input())

path = {node: 0 for node in range(1, N+1)}

for _ in range(M):
    u, v, w = map(int, input().split())
    if w < graph[u][v]:
        graph[u][v] = w
        graph[v]

start, stop = map(int, input().split())
leng, pathto = dijkstra(graph, start, N)

how_can = [stop]

while how_can[-1] != start:
    now_tmp = pathto[how_can[-1]]
    how_can.append(now_tmp)

print(leng[stop])
print(len(how_can))
print(*how_can[::-1])