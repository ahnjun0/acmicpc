import sys
from queue import PriorityQueue
input = lambda : sys.stdin.readline().rstrip()

que = PriorityQueue()

for _ in range(int(input())):
    x = int(input()) * -1
    if x == 0:
        if que.empty():
            print(0)
        else:
            print((que.get()) * -1)
    
    else:
        que.put(x)