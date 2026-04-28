import sys, heapq
input = lambda: sys.stdin.readline()

N, K = map(int, input().split())
jew = []
for _ in range(N): heapq.heappush(jew, tuple([*map(int, input().split())]))
bag = [int(input()) for _ in range(K)]
bag.sort()

cnt = 0
pq = []

for i in bag:
    while jew and i >= jew[0][0]:
        heapq.heappush(pq, -heapq.heappop(jew)[1])
    if pq:
        cnt -= heapq.heappop(pq)

print(cnt)