import sys
from collections import deque
inputs = lambda: map(int, sys.stdin.readline().split())

for _ in range(int(input())):
    N, K = inputs()
    time = [*inputs()]
    graph = [[] for _ in range(N+1)]
    degree = [0] * (N+1)
    dp = [0] * (N+1)

    for _ in range(K):
        A, B = inputs()
        graph[A].append(B)
        degree[B] += 1

    queue = deque()

    W = int(input())
    
    for i in range(1, N+1):
        if degree[i] == 0:
            queue.append(i)
            dp[i] = time[i-1]

    ans = []
    while queue:
        ans.append(v := queue.popleft())
        
        for adj in graph[v]:
            degree[adj] -= 1
            dp[adj] = max(dp[adj], dp[v] + time[adj-1])
            if degree[adj] == 0: queue.append(adj)

    print(dp[W])