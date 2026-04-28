import sys
from collections import deque
input = lambda: map(int, sys.stdin.readline().rstrip().split())

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(i, j):
    dist[i][j] = 0
    
    deq = deque()
    deq.append((i, j))
    
    while deq:
        x, y = deq.popleft()
        
        for px, py in zip(dx, dy):
            nx, ny = px + x, py + y
            
            if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    dist[nx][ny] = 0
                elif arr[nx][ny] == 1:
                    dist[nx][ny] = dist[x][y] + 1
                    deq.append((nx, ny))

N, M = input()
dist = [[-1] * M for _ in range(N)]
arr = [[*input()] for _ in range(N)]
bfs(*[(i, j) for i in range(N) for j in range(M) if arr[i][j] == 2][0])

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()