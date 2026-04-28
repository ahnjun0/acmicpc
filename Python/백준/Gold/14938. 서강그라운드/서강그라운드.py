import sys, heapq
from collections import defaultdict
input = lambda: sys.stdin.readline()

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    
    while queue:
        now_dist, now_where = heapq.heappop(queue)
        
        if dist[now_where] < now_dist:
            continue
        
        for new_where, new_dist in graph[now_where].items():
            far = now_dist + new_dist
            if far < dist[new_where]:
                dist[new_where] = far
                heapq.heappush(queue, [far, new_where])
    return dist

# graph = defaultdict(dict)

N, M, R = map(int, input().split())
item = [*map(int, input().split())]
graph = {i:{} for i in range(N)}


for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a-1][b-1] = l
    graph[b-1][a-1] = l

ans = 0
for i in range(N):
    ret = dijkstra(graph, i)
    ans = max(sum(item[j] for j in range(N) if ret[j] <= M and ret[j] != float('inf')), ans)

print(ans)
