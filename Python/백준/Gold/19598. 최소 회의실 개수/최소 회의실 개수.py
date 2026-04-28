import sys, heapq
input = lambda: sys.stdin.readline()

pq = []
for start, end in sorted([[*map(int, input().split())] for _ in range(int(input()))]):
    if pq and pq[0] <= start:
        heapq.heappop(pq)
    heapq.heappush(pq, end)

print(len(pq))