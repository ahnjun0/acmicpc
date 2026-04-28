import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


for _ in range(int(input())):
    N, M = map(int, input().split())
    file = list(map(int, input().split()))
    deq = deque(file, maxlen=N)

    cnt = 0

    while deq:
        quickly = max(deq)
        printer = deq.popleft()
        M -= 1

        if printer >= quickly:
            cnt += 1
            if M < 0:
                print(cnt)
                break

        else:
            deq.append(printer)
            if M < 0:
                M = len(deq) - 1