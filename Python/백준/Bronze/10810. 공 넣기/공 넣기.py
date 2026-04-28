import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

arr = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    
    for m in range(i-1, j):
        arr[m] = k

print(*arr)