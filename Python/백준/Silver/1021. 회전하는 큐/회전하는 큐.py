import sys
from collections import deque
input = lambda: map(int, sys.stdin.readline().split())

N, _ = input()

dq = deque([i for i in range(1, N+1)])
cnt = 0

for i in [*input()]:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        
        if dq.index(i) < len(dq)/2:
            while dq[0] != i:
                dq.rotate(-1)
                cnt += 1
        else:
            while dq[0] != i:
                dq.rotate(1)
                cnt += 1

print(cnt)