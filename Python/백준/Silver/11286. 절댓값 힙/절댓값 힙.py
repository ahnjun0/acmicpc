import sys
import heapq
input = lambda : sys.stdin.readline().rstrip()

heap = []

for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    
    else:
        heapq.heappush(heap, (abs(x), x))