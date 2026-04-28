import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

arr = list(range(1, N+1))
for _ in range(M):
    i, j = map(int, input().split())
    arr = arr[:(i-1)] + list(reversed(arr[(i-1):j])) + arr[j:]

print(*arr)