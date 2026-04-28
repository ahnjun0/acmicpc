# 21736

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dxdy = [0, 0, 1, -1]
queue = deque()

N, M = map(int, input().split())
campus = [[*input()] for _ in range(N)]

for i, val in enumerate(campus):
    for j, inV in enumerate(val):
        if inV == "I":
            queue.append((i, j))
            break



def bfs():
    cnt = 0
    
    while queue:
        px, py = queue.popleft()
        for i, j in zip(dxdy, dxdy[::-1]):
            nx = i + px
            ny = j + py
            
            if 0 <= nx < N and 0 <= ny < M:
                val = campus[nx][ny]
            
            else:
                continue

            if val == "P":
                campus[nx][ny] = "C"
                cnt += 1
                queue.append((nx, ny))

            elif val == "O":
                campus[nx][ny] = "C"
                queue.append((nx, ny))

    return cnt

result = bfs()
print(result if result != 0 else "TT")