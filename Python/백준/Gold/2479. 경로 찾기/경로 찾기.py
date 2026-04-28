import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
code = [[0] * K] + [[*map(int, [*input()])] for _ in range(N)]
A, B = map(int, input().split())
def bfs(x):
    visited = [False for _ in range(N+1)]
    visited[A] = True
    queue = deque([(x, [x])])
    
    while queue:
        now, course = queue.popleft()
        if now == B: return course
        
        for i in range(1, N+1):
            cnt = 0
            if visited[i]: continue
            for j in range(K):
                if code[now][j] != code[i][j]:
                    cnt += 1
                if cnt > 1:
                    break
                
            if cnt == 1:
                visited[i] = True
                queue.append((i, course + [i]))
                
    return [-1]

print(*bfs(A))