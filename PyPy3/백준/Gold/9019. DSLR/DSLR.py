from collections import deque, defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()


for _ in range(int(input())):
    A, B = map(int, input().split())
    
    visited = defaultdict(bool)
    queue = deque()
    queue.append((A, []))
    visited[A] = True
    
    while queue:
        (num, cmd) = queue.popleft()
        if num == B:
            print(*cmd, sep="")
            break
        
        # D
        D = num * 2 if num * 2 < 10000 else num * 2 - 10000
        if not visited[D]:
            visited[D] = True
            cmpTmp = cmd[:]
            cmpTmp.append("D")
            queue.append((D, cmpTmp))
            
        # S
        S = num - 1 if num != 0 else 9999
        if not visited[S]:
            visited[S] = True
            cmpTmp = cmd[:]
            cmpTmp.append("S")
            queue.append((S, cmpTmp))
        
        # L
        L = num // 1000 + (num % 1000) * 10
        if not visited[L]:
            visited[L] = True
            cmpTmp = cmd[:]
            cmpTmp.append("L")
            queue.append((L, cmpTmp))
            
        # R
        R = num // 10 + (num % 10) * 1000
        if not visited[R]:
            visited[R] = True
            cmpTmp = cmd
            cmpTmp.append("R")
            queue.append((R, cmpTmp))