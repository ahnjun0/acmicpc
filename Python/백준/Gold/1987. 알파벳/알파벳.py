import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
arr = [[*input()] for _ in range(R)]
dxdy = [0,0,1,-1]
cnt = 1

def bfs():
    global cnt
    queue = set([(0, 0, arr[0][0])])
    
    while queue:
        px, py, now = queue.pop()
        for i, j in zip(dxdy, dxdy[::-1]):
            nx = i + px
            ny = j + py

            if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] not in now:
                queue.add((nx, ny, now + arr[nx][ny]))
                cnt = max(cnt, len(now)+1)

bfs()
print(cnt)