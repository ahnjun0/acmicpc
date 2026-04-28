import sys
input = lambda: sys.stdin.readline()

N = int(input())
graph = [[*map(int, input().split())] for _ in range(N)]

dp = {}

def dfs(now, visited):
    if visited == (1 << N)-1:
        return graph[now][0] if graph[now][0] else int(1e9)
    
    if (now, visited) in dp:
        return dp[(now, visited)]
    
    mini = int(1e9)
    
    for n in range(1, N):
        if not graph[now][n] or visited & (1<<n): continue
        
        mini = min(((dfs(n, visited | (1<<n))) + graph[now][n]), mini)
    dp[(now, visited)] = mini
    return mini

print(dfs(0, 1))