import sys
input = lambda: sys.stdin.readline().rstrip()


N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
col = {"white" : 0, "blue" : 0}

def recursive(x, y, N):
    if N == 0:
        return
    
    color = arr[x][y]
    half = N // 2
    
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != arr[i][j]:
                # case 1 : left, top
                recursive(x, y, half)
                # case 2 : right, top
                recursive(x+half, y, half)
                # case 3 : left, bottom
                recursive(x, y+half, half)
                # case 4 : right, bottom
                recursive(x+half, y+half, half)
                return
            

    if color == 0:
        col["white"] += 1
    else:
        col["blue"] += 1


recursive(0, 0, N)
print(col["white"])
print(col["blue"])