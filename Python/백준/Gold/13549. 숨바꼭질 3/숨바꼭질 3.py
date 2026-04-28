import sys
from collections import deque
input = lambda: map(int, sys.stdin.readline().rstrip().split())

N, K = input()
queue = deque()
queue.append((N, 0))

visited = [False] * 100001
cnt = 0

while queue:
    where, now = queue.popleft()
    visited[where] = True
    
    if where == K:
        print(now)
        sys.exit(0)
    
    will_warp = 2*where
    if 0 <= will_warp <= 100000 and not visited[will_warp] :
        visited[will_warp] = True
        queue.append((will_warp, now))
    
    
    for will_visit in (where-1, where+1):
        if 0 <= will_visit <= 100000 and not visited[will_visit] :
            visited[will_visit] = True
            queue.append((will_visit, now + 1))