import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dxdy = [1, -1, 0, 0]

N = int(input())
house = [list(map(int, [*input()])) for _ in range(N)]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    house[a][b] = 0
    house_cnt = 1
    
    while queue:
        px, py = queue.popleft()
        
        for i, j in zip(dxdy, dxdy[::-1]):
            nx = i + px
            ny = j + py

            if 0 <= nx < N and 0 <= ny < N and house[nx][ny] == 1:
                house[nx][ny] = 0
                house_cnt += 1
                queue.append((nx, ny))
    return house_cnt

cnt = []
for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            cnt.append(bfs(i, j))

print(len(cnt))
print(*sorted(cnt), sep="\n")