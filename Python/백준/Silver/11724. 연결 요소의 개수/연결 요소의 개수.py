import sys
input = lambda: map(int, sys.stdin.readline().split())
sys.setrecursionlimit(10**6)

def dfs(v):
    if visited[v]:
        return
    
    visited[v] = True
    for i in arr[v]:
        dfs(i)

N, M = input()
arr = [[] for _ in range(N)]

visited = [False] * N

for _ in range(M):
    u, v = input()
    arr[u-1].append(v-1)
    arr[v-1].append(u-1)

result = 0
for i in range(N):
    if not visited[i]:
        result += 1
        dfs(i)

print(result)