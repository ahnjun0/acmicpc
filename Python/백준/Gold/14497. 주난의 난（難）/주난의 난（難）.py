import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def bfs_0_1(graph, start, M, N, to):
    dxdy = [1, -1, 0, 0]
    deq = deque()
    deq.append(start)
    cost = [[-1 for _ in range(M)] for _ in range(N)]
    cost[start[1]][start[0]] = 0
    
    while deq:
        px, py = deq.popleft()
        for i, j in zip(dxdy, dxdy[::-1]):
            nx = i + px
            ny = j + py
            
            if 0 <= nx < M and 0 <= ny < N:
                if cost[ny][nx] == -1 or graph[ny][nx] + cost[py][px] < cost[ny][nx]:
                    cost[ny][nx] = graph[ny][nx] + cost[py][px]
                
                    if graph[ny][nx] == 0:
                        deq.appendleft((nx, ny))
                    else: # graph[ny][nx] == 1
                        deq.append((nx, ny))
    return cost[to[1]][to[0]]


N, M = map(int, input().split())
y1, x1, y2, x2 = map(int, input().split())
graph = [[*input()] for _ in range(N)]
graph[y2-1][x2-1] = "1"
graph[y1-1][x1-1] = "0"
graph = [[*map(int, row)] for row in graph]

print(bfs_0_1(graph, (x1-1, y1-1), M, N, (x2-1, y2-1)))