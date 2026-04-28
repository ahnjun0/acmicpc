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

graph = defaultdict(lambda: defaultdict(lambda: 1001))

N, E = map(int, input().split())

for _ in range(E):
    u, v, w = map(int, input().split())
    if w < graph[u][v]:
        graph[u][v] = w
        graph[v][u] = w

v1, v2 = map(int, input().split())

from_one = dijkstra(graph, 1, N)
from_v1 = dijkstra(graph, v1, N)
from_v2 = dijkstra(graph, v2, N)

if from_v1[v2] == -1:
    print(-1)
    sys.exit(0)

match (from_one[v1], from_v2[N], from_one[v2], from_v1[N]):
    case (-1, _, -1, _) | (-1, _, _, -1) | (_, -1, _, -1) | (_, -1, _, -1):
        print(-1)
        sys.exit(0)

    case (-1, _, _, _) | (_, -1, _, _):
        print(from_one[v2] + from_v1[N] + from_v1[v2])
    
    case (_, _, -1, _) | (_, _, _, -1):
        print(from_one[v1] + from_v2[N] + from_v1[v2])
    
    case _:
        print(min(from_one[v1] + from_v2[N], from_one[v2] + from_v1[N]) + from_v1[v2])

