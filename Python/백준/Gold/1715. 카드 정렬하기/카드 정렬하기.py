import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

heap = []
result = 0

for _ in range(int(input())):
    heapq.heappush(heap, int(input()))
    
while len(heap) > 1:
    prev = heapq.heappop(heap)
    curr = heapq.heappop(heap)
    result += prev + curr
    heapq.heappush(heap, prev+curr)
    
print(result)