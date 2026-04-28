# Similar to 7576

import sys
from collections import deque
input = lambda: map(int, sys.stdin.readline().rstrip().split())

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
cnt_zero = 0

M, N, H = input()
queue = deque(tuple())
tomatoes = [[[*input()] for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        for k in range(M):
            tmp_to = tomatoes[i][j][k]
            if tmp_to == 1:
                queue.append((i, j, k)) # Start Position
            elif tmp_to == 0:
                cnt_zero += 1

def bfs():
    global cnt_zero
    while queue:
        px, py, pz = queue.popleft()
        for i, j, k in zip(dx, dy, dz):
            nx = i + px
            ny = j + py
            nz = k + pz

            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and tomatoes[nx][ny][nz] == 0:
                tomatoes[nx][ny][nz] = tomatoes[px][py][pz] + 1
                queue.append((nx, ny, nz))
                cnt_zero -= 1

bfs()

if cnt_zero != 0:
    print(-1)

else:
    print(max(max(max(sublist) for sublist in matrix) for matrix in tomatoes) - 1)