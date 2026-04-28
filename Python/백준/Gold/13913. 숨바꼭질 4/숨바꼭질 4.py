import sys
from collections import deque
input = lambda: map(int, sys.stdin.readline().rstrip().split())

N, K = input()
queue = deque()
queue.append((N, 0))

visited = [False] * 100001
route = [0] * 100001
cnt = 0

def bfs():
    while queue:
        where, now = queue.popleft()
        visited[where] = True
        
        if where == K:
            return now
        
        
        for will_visit in (where-1, where+1, 2*where):
            if 0 <= will_visit <= 100000 and not visited[will_visit] :
                
                visited[will_visit] = True
                queue.append((will_visit, now + 1))
                route[will_visit] = where

print(d := bfs())
re = [K]
for _ in range(d):
    re.append(route[re[-1]])

print(*re[::-1], sep=" ")