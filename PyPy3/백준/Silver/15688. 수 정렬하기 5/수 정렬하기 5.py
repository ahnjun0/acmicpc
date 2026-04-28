import sys, heapq
input = lambda: int(sys.stdin.readline())

pq = []

for i in range(input()):
    heapq.heappush(pq, input())

while pq:
    print(heapq.heappop(pq))