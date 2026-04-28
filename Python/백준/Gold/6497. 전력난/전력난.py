import sys
input = lambda: map(int, sys.stdin.readline().split())

while True:
    V, E = input()
    
    if V == 0 and E == 0:
        break
    
    edge = [[*input()] for _ in range(E)]
    edge.sort(key=lambda x: x[2])
    total = sum(x[2] for x in edge)

    # Union-find Algorithm
    ancestor = [i for i in range(V)]

    def find_ancestor(node):
        if ancestor[node] == node: return node
        ancestor[node] = find_ancestor(ancestor[node])
        return ancestor[node]

    def union_ancestor(nodeA, nodeB):
        ancestorA, ancestorB = find_ancestor(nodeA), find_ancestor(nodeB)
        if ancestorA < ancestorB: ancestor[ancestorB] = ancestorA
        else: ancestor[ancestorA] = ancestorB

    ret = 0
    for A, B, C in edge:
        if find_ancestor(A) != find_ancestor(B):
            union_ancestor(A, B)
            ret += C

    print(total-ret)