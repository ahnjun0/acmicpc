import sys, heapq
input = lambda: sys.stdin.readline()

pq = []

for _ in range(int(input())):
    now = input()
    if now == '0\n':
        if len(pq) == 0: print(-1)
        else:
            print(-heapq.heappop(pq))
    else:
        _, *arr = now.split()
        for i in map(int, arr): heapq.heappush(pq, -i)