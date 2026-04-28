from collections import deque
import sys
sys.setrecursionlimit(10000)

input = lambda: sys.stdin.readline().rstrip()

dxdy = [0,0,-1,1]


N = int(input())
arr = [[*input()] for _ in range(N)]
arr_blind = [[x if x != "G" else "R" for x in item] for item in arr]

# BFS
def bfs(a, b, array):
    queue = deque()
    queue.append((a, b))
    
    while queue:
        (nowX, nowY) = queue.popleft()
        nowColor = array[nowY][nowX]
        array[nowY][nowX] = "@"
        
        for dx, dy in zip(dxdy, dxdy[::-1]):
            nextX, nextY = nowX + dx, nowY + dy
            if not (0 <= nextX < N) or not (0 <= nextY < N) or array[nextY][nextX] == "@":
                continue
            elif array[nextY][nextX] == nowColor:
                queue.append((nextX, nextY))

cnt = 0
cnt_blind = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] != "@":
            bfs(j, i, arr)
            cnt += 1
        
        if arr_blind[i][j] != "@":
            bfs(j, i, arr_blind)
            cnt_blind += 1

print(cnt, cnt_blind)