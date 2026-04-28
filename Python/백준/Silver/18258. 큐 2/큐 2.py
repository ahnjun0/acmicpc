import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

queue = deque()

for _ in range(int(input())):
    order = input().split()
    
    match order[0]:
        case "push":
            queue.append(order[1])
        case "pop":
            print(queue.popleft() if len(queue) != 0 else -1)
        case "size":
            print(len(queue))
        case "empty":
            print(1 if len(queue) == 0 else 0)
        case "front":
            print(queue[0] if len(queue) != 0 else -1)
        case "back":
            print(queue[-1] if len(queue) != 0 else -1)