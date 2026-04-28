from heapq import heappush, heappop
import sys

input = lambda: map(int, sys.stdin.readline().split())

N, L = input()
arr = [*input()]
pq = []

for i in range(N):
    heappush(pq, (arr[i], i))
    val, idx = pq[0]
    
    while idx < i - L + 1:
        heappop(pq)
        val, idx = pq[0]
    
    print(val, end=' ')