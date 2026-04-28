import sys
from collections import deque
input = lambda: map(int, sys.stdin.readline().rstrip().split())

N, K = input()

if N == K:
    print(0)
    print(1)
    sys.exit(0)

queue = deque()
queue.append((N, 0))

visited = [0] * 100001
cnt = 0
now_time = 0


while queue:
    where, now = queue.popleft()
    # visited[where] = now
    
    if now_time > 0 and now > now_time:
        break
    
    if where == K:
        cnt += 1
        now_time = now
        continue
    
    for will_visit in (where-1, where+1, 2*where):
        if 0 <= will_visit <= 100000 and (visited[will_visit] == 0 or visited[will_visit] == visited[where] + 1):
            
            visited[will_visit] = now+1
            queue.append((will_visit, now + 1))

print(now_time)
print(cnt)