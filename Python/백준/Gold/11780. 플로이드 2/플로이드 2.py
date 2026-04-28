# 11780

import sys
from collections import defaultdict
inputs = lambda: map(int, sys.stdin.readline().rstrip().split())

N = int(input())
M = int(input())

floyd = [[1e8 for _ in range(N)] for _ in range(N)]
road = defaultdict(dict)

for _ in range(M):
    a, b, c = inputs()
    
    if c < floyd[a-1][b-1]:
        floyd[a-1][b-1] = c
        road[a][b] = [a,b]


for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j and floyd[i][j] > floyd[i][k]+floyd[k][j]:
                floyd[i][j] = floyd[i][k]+floyd[k][j]
                road[i+1][j+1] = [i+1,k+1,j+1]

for val in floyd:
    print(*[x if x != 1e8 else 0 for x in val])


def recursive(a, b):
    result = []
    path = road[a][b]
    
    if len(path) == 2:
        return [b]
    
    for i in range(1, len(path)):
        result.extend(recursive(path[i-1], path[i]))
    
    return result

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j or j not in road[i]:
            print(0)
            continue
        
        if len(road[i][j]) == 2:
            print(2, *road[i][j])
            
        else:
            path = [i] + recursive(i, j)
            print(len(path), *path)