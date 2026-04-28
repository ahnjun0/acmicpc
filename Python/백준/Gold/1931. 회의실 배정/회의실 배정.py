import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

heap = []

for _ in range(int(input())):
    heappush(heap, (lambda x, y: (y, x))(*map(int, input().split())))


cnt = 1
end = heap[0][0]
heappop(heap)

while len(heap) != 0:
    k = heap[0]
    if k[1] >= end:
        cnt += 1
        end = k[0]
    heappop(heap)
        
print(cnt)