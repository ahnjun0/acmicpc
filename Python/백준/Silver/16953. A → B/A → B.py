import sys
from collections import deque
input = lambda: map(int, sys.stdin.readline().rstrip().split())

A, B = input()
queue = deque()
queue.append((A, 0))

# visited = [False] * (10)**9
cnt = 0

while queue:
    where, now = queue.popleft()
    # visited[where] = True
    
    if where == B:
        print(now+1)
        sys.exit(0)
    
    for will_visit in (2*where, int(str(where)+"1")):
        if 0 <= will_visit <= 1e9 :
            # visited[will_visit] = True
            queue.append((will_visit, now + 1))

print(-1)