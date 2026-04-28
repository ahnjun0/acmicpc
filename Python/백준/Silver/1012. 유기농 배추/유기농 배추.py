import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

def dfs(x, y, field, M, N):
    move = [0, 0, -1, 1]
    
    for a, b in zip(move, move[::-1]):
        dx = x + a
        dy = y + b

        if (0 <= dx < M) and (0 <= dy < N):
            if field[dy][dx]:
                field[dy][dx] = not field[dy][dx]
                dfs(dx, dy, field, M, N)
        
for _ in range(int(input())):
    cnt = 0
    
    M, N, K = map(int, input().split())

    field = [[False for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = True


    for x in range(M):
        for y in range(N):
            if field[y][x] == 1:
                dfs(x, y, field, M, N)
                cnt += 1

    print(cnt)