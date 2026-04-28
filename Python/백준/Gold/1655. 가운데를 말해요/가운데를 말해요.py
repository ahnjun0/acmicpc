import sys, heapq
input = lambda: int(sys.stdin.readline())

left_queue = []
right_queue = []
for _ in range(input()):
    num = int(input())
    
    if len(left_queue) == 0 and len(right_queue) == 0:
        heapq.heappush(left_queue, -num)

        print(-left_queue[0])
        continue
    
    elif len(left_queue) == 1 and len(right_queue) == 0:
        if -left_queue[0] < num:
            heapq.heappush(right_queue, num)
        
        else:
            heapq.heappush(right_queue, -heapq.heappop(left_queue))
            heapq.heappush(left_queue, -num)

        print(-left_queue[0])
        continue

    if -left_queue[0] < num:
        heapq.heappush(right_queue, num)
        
        if len(right_queue) > len(left_queue):
            heapq.heappush(left_queue, -heapq.heappop(right_queue))
    else:
        heapq.heappush(left_queue, -num)
        
        if len(left_queue) > len(right_queue) + 1:
            heapq.heappush(right_queue, -heapq.heappop(left_queue))

    print(-left_queue[0])
