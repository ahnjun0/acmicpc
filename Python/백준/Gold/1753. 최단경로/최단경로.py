import sys, heapq
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

def dijkstra(graph, start, V):
    dist = {node: -1 for node in range(1, V+1)}

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
    return dist

graph = defaultdict(lambda: defaultdict(lambda: 11))

V, E = map(int, input().split())
K = int(input())

for _ in range(E):
    u, v, w = map(int, input().split())
    if w < graph[u][v]:
        graph[u][v] = w

ret = dijkstra(graph, K, V)

for i in range(1, V+1):
    print(ret[i] if ret[i] != -1 else "INF")