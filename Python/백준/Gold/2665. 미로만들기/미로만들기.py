import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def bfs_0_1(graph, start, M, N):
    dxdy = [1, -1, 0, 0]
    deq = deque()
    deq.append(start)
    cost = [[-1 for _ in range(M)] for _ in range(N)]
    cost[0][0] = 0
    
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
    
    return cost[N-1][M-1]


N = int(input())
graph = [[1 - x for x in row] for row in [[*map(int, [*input()])] for _ in range(N)]]
print(bfs_0_1(graph, (0,0), N, N))