import sys
from collections import deque
input = lambda: sys.stdin.readline()

N = int(input())
arr = [*map(int, input().split())]

ans = [-1] * N
deq = deque()

for i, val in enumerate(arr):
    while deq and arr[deq[-1]] < val:
        ans[deq.pop()] = val
    deq.append(i)

print(*ans)