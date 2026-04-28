import sys, heapq
input = lambda: sys.stdin.readline()

pq = []
table = []
for _ in range(int(input())):
    _, s, e = map(int, input().split())
    table.append((s, e))

for start, end in sorted(table):
    if pq and pq[0] <= start:
        heapq.heappop(pq)
    heapq.heappush(pq, end)

print(len(pq))