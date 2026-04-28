import sys, heapq
input = lambda: sys.stdin.readline()

for _ in range(int(input())):
    pq = []
    for _ in range(int(input())):
        heapq.heappush(pq, [*map(int, input().split())])
    
    cnt = 0
    maxi = len(pq)+1
    while pq:
        _, score = heapq.heappop(pq)
        if score < maxi:
            cnt += 1
            maxi = score
    
    print(cnt)