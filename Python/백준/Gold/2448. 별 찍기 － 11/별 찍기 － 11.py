import sys
input = lambda: int(sys.stdin.readline().rstrip())
N = input()

arr = [[" "]*(2*N-1) for _ in range(N)] # 전부 공백으로 된 배열 생성 여기에 별을 그림

def recursive(n, x, y):
    if n == 3:
        arr[ y ][   x   ] =   "*"
        arr[y+1][x-1:x+2] =  "* *"
        arr[y+2][x-2:x+3] = "*****"
        return
    else:
        recursive(n//2, x, y)
        recursive(n//2, x - (n // 2), y + (n // 2))
        recursive(n//2, x + (n // 2), y + (n // 2))

recursive(N, N-1, 0)

for i in arr:
    print(''.join(i)) 