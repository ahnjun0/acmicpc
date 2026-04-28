import sys
input = lambda: sys.stdin.readline()

N = int(input())
arr = [(*map(int, input().split()), i) for i in range(N)]

edges = []
for k in range(3):
    arr.sort(key=lambda x: x[k])
    for i in range(N - 1):
        cost = abs(arr[i][k] - arr[i + 1][k])
        edges.append((cost, arr[i][3], arr[i + 1][3]))

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