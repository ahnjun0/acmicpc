import sys
from collections import defaultdict, deque
input = lambda: sys.stdin.readline().rstrip()

tree = defaultdict(list)
result = set()

for _ in range(int(input())-1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)

def bfs():
    result = set()
    
    queue = deque()
    queue.append(1)
    
    while queue:
        now = queue.popleft()
        
        for i in tree[now]:
            if (now, i) not in result:
                result.add((i, now))
                queue.append(i)
                
    return sorted(result)

for i in bfs():
    print(i[-1])

