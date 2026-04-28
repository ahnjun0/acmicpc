import sys
from collections import deque
input = lambda: sys.stdin.readline()

N, M = map(int, input().split())
tomatoes = [[*map(int, [*input().rstrip()])] for _ in range(N)]

if N == 1 and M == 1:
    print(1)
    sys.exit(0)

queue = deque(tuple())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue.append((0, 0, False))

def bfs():
    result = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    
    while queue:
        px, py, broken = queue.popleft()
        if px == N-1 and py == M-1:            
            return result[N-1][M-1]
        
        for i, j in zip(dx, dy):
            nx = i + px
            ny = j + py
            
            if 0 <= nx < N and 0 <= ny < M: #  and (result[nx][ny][0] == 0 and result[nx][ny][1] == 0)
                if not broken:
                    if tomatoes[nx][ny] == 0 and result[nx][ny][0] == 0:
                        result[nx][ny][0] = result[px][py][0] + 1
                        queue.append((nx, ny, False))    

                    elif tomatoes[nx][ny] == 1 and result[nx][ny][1] == 0:
                        result[nx][ny][1] = result[px][py][0] + 1
                        queue.append((nx, ny, True))    
                
                else:
                    if tomatoes[nx][ny] == 0 and result[nx][ny][1] == 0 and (result[nx][ny][0] == 0 or (result[nx][ny][0] > result[px][py][1] + 1)):
                        result[nx][ny][1] = result[px][py][1] + 1
                        queue.append((nx, ny, True))
    
    return result[N-1][M-1]

match ret := bfs():
    case (0,0):
        print(-1)
    
    case (0,_) | (_,0):
        print(max(ret)+1)
    
    case _:
        print(min(ret)+1)

