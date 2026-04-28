import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

for _ in range(int(input())):
    error = False
    order = list(input())
    n = int(input())
    arr_ = input()
    
    if arr_ == "[]":
        arr = deque()
    else:
        arr = deque(map(int, arr_.strip('[]').split(',')))
        
    rvalue = False
    

    
    for run in order:
        if run == "R":
            rvalue = not rvalue
            
        else: # run == "D"
            if len(arr) != 0 and not rvalue:
                arr.popleft()
            
            elif len(arr) != 0 and rvalue:
                arr.pop()
                
            else:
                error = True
                break
    
    if not error and not rvalue:
        print('[', end='')
        print(*arr, sep=',', end='')
        print(']')
    
    elif not error and rvalue:
        arr.reverse()
        print('[', end='')
        print(*arr, sep=',', end='')
        print(']')
        
    
    else:
        print("error")