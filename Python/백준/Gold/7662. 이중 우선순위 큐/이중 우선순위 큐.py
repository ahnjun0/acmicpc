import sys, heapq
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    
    max_pq = []
    min_pq = []
    rm = [False] * (K := int(input()))
    for i in range(K):
        
        ID, val = input().split()
        val = int(val)
        
        if ID == "I":
            heapq.heappush(max_pq, (-val, i))
            heapq.heappush(min_pq, (val, i))
        
        elif len(max_pq) != 0:
            if val == -1:
                rm[heapq.heappop(min_pq)[1]] = True
            else:
                rm[heapq.heappop(max_pq)[1]] = True

        while len(max_pq) != 0 and rm[max_pq[0][1]]: heapq.heappop(max_pq)
        while len(min_pq) != 0 and rm[min_pq[0][1]]: heapq.heappop(min_pq)

    if len(max_pq) == 0:
        print("EMPTY")
    else:
        print(-max_pq[0][0], min_pq[0][0])