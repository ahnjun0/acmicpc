import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
arr = [*map(int, [*input()])]
deq = deque()
cnt = K

for i in arr:
    if len(deq) == 0:
        deq.append(i)
    
    elif deq[-1] < i and cnt > 0:
        while deq and deq[-1] < i and cnt > 0:
            deq.pop()
            cnt -= 1
        deq.append(i)
    else:
        deq.append(i)

print(*[*deq][:N-K], sep='')