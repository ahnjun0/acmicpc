import sys, heapq
from collections import defaultdict, deque
input = lambda: map(int, sys.stdin.readline().rstrip().split())

def dijkstra(graph, start, except_path=set()):
    dist = {node: -1 for node in graph}

    dist[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        now_dist, now_where = heapq.heappop(queue)
        
        if dist[now_where] != -1 and dist[now_where] < now_dist:
            continue
        
        for new_where, new_dist in graph[now_where].items():
            far = now_dist + new_dist
            if (now_where, new_where) not in except_path and (dist[new_where] == -1 or (far < dist[new_where])):
                dist[new_where] = far
                heapq.heappush(queue, (far, new_where))
                
    return dist

def tracking(graph, start, end, dijk):
    ret = set()
    queue = deque()
    queue.append(end)
    
    while queue:
        now = queue.popleft()
        
        if now == start:
            continue
        
        for new_where, new_dist in graph[now].items():
            if dijk[new_where] + new_dist == dijk[now] and (new_where, now) not in ret:
                ret.add((new_where, now))
                queue.append(new_where)
    
    return ret

while True:
    graph = defaultdict(lambda: defaultdict(lambda: 1001))
    tracking_graph = defaultdict(lambda: defaultdict(lambda: 1001))

    N, M = input()
    if N == 0 and M == 0: break
    
    S, D = input()


    for _ in range(M):
        u, v, w = input()
        # if w < graph[u][v]:
        graph[u][v] = w
        graph[v]
        tracking_graph[v][u] = w
    
    if D not in graph:
        print(-1)
        
    else:
        leng = dijkstra(graph, S)
        print(dijkstra(graph, S, tracking(tracking_graph, S, D, leng))[D])
        
    # print(dijkstra(graph, S)[D])