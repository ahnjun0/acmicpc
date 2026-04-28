import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()

N, k = map(int, input().split())
waiting = [(0, idx, []) for idx in range(k)]

for _ in range(N):
    distinct, w = map(int, input().split())
    total_waiting, idx, waiting_list = heapq.heappop(waiting)
    new_wait = total_waiting + w
    waiting_list.append([new_wait, distinct])
    heapq.heappush(waiting, (new_wait, idx, waiting_list))

result = sorted([(idx, M[0], M[1]) for _, idx, M_list in waiting for M in M_list], key=lambda x: (x[1], -x[0]))
cnt = 0

for i, val in enumerate(result):
    cnt += (i + 1) * val[2]
print(cnt)

# for item in result:
#     print(item)
