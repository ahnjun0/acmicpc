import sys
from collections import defaultdict
input = lambda: map(int, sys.stdin.readline().split())

def find_fastest_times(N, bus_routes):
    # Define the graph
    graph = defaultdict(list)
    for A, B, C in bus_routes:
        graph[A].append((B, C))

    def bellman_ford(graph, N):
        dist = [float('inf')] * (N + 1)
        dist[1] = 0

        for _ in range(N):
            updated = False
            for ver in range(1, N + 1):
                for n_ver, n_cost in graph[ver]:
                    if dist[n_ver] > dist[ver] + n_cost:
                        dist[n_ver] = dist[ver] + n_cost
                        updated = True
            if not updated:
                break

        # Check for negative weight cycles
        for ver in range(1, N + 1):
            for n_ver, n_cost in graph[ver]:
                if dist[n_ver] > dist[ver] + n_cost:
                    return [-1]

        return dist

    result = bellman_ford(graph, N)
    if result[0] == -1:
        return [-1]
    else:
        return [result[i] if result[i] != float('inf') else -1 for i in range(2, N + 1)]


N, M = input()
bus_routes = [[*input()] for _ in range(M)]
print(*find_fastest_times(N, bus_routes), sep='\n')