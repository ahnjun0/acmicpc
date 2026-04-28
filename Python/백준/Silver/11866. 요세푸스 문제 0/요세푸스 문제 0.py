import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
dq = deque(range(1, N + 1))
print("<", end="")

while dq:
    for _ in range(K-1):
        dq.append(dq.popleft())
    print("{}{}".format(dq.popleft(), ", " if dq else ">"), end="")
