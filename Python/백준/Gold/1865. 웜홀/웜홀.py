import sys
from collections import defaultdict
input = lambda: sys.stdin.readline()

def bellman_ford(graph, N):
    dist = [100001] * (N+1)
    dist[1] = 0
    
    for ck in range(N):
        for ver in range(1, N+1):
            for n_ver, n_cost in graph[ver]:
                if dist[n_ver] > dist[ver] + n_cost:
                    dist[n_ver] = dist[ver] + n_cost
                    if ck == N-1:
                        return False
    return True

for _ in range(int(input())):
    N, M, W = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((E, T))
        graph[E].append((S, T))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        graph[S].append((E, -T))

    print("NO" if bellman_ford(graph, N) else "YES")
        