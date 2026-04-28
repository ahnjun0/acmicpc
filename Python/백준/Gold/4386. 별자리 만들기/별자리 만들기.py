import sys
input = lambda: sys.stdin.readline()

N = int(input())
arr = [(*map(float, input().split()), i) for i in range(N)]

edges = [(((arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2)**.5, i, j) for i in range(N-1) for j in range(i+1, N) ]
edges.sort()

# Union-find Algorithm
ancestor = [i for i in range(N)]
def find_ancestor(node):
    if ancestor[node] == node: return node
    return find_ancestor(ancestor[node])

def union_ancestor(nodeA, nodeB):
    ancestorA, ancestorB = find_ancestor(nodeA), find_ancestor(nodeB)
    if ancestorA < ancestorB: ancestor[ancestorB] = ancestorA
    else: ancestor[ancestorA] = ancestorB

# Kruskal Algorithm
total_cost = 0
for cost, a, b in edges:
    if find_ancestor(a) != find_ancestor(b):
        union_ancestor(a, b)
        total_cost += cost

print(total_cost)