import sys
from queue import PriorityQueue
input = lambda : sys.stdin.readline().rstrip()

que = PriorityQueue()

for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if que.empty():
            print(0)
        else:
            print(que.get())
    
    else:
        que.put(x)