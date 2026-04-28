import sys
from collections import deque
input = lambda: int(sys.stdin.readline())

arr = [-1] * ((N := input()) + 1)
arr[N] = 0
queue = deque()
queue.append(N)

while arr[1] == -1:
    now = queue.popleft()
    
    if now % 3 == 0 and arr[now//3] == -1:
        arr[now//3] = now
        queue.append(now//3)
    
    if now % 2 == 0 and arr[now//2] == -1:
        arr[now//2] = now
        queue.append(now//2)
    
    if arr[now-1] == -1:
        arr[now-1] = now
        queue.append(now-1)

tmp = 0
result = [1]
while result[-1] != N:
    result.append(arr[result[-1]])

print(len(result)-1)
print(*result[::-1])