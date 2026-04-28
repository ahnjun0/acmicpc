import sys, heapq
input = lambda: int(sys.stdin.readline())

pq = []
N = input()
dasom = input()
cnt = 0

if N == 1:
    print(0)
    sys.exit(0)

for i in range(N-1):
    heapq.heappush(pq, -input())

while True:
    val = -heapq.heappop(pq)
    
    if dasom > val:
        break
    
    else:
        cnt += 1
        dasom += 1
        heapq.heappush(pq, -(val-1))

print(cnt)