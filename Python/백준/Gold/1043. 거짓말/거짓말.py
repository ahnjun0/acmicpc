import sys
input = lambda: map(int, sys.stdin.readline().split())

N, M = input()
truth_num, *truth_person = input()
party = [(num, person) for _ in range(M) for num, *person in [input()]]

# Union-find Algorithm
ancestor = [i for i in range(N+1)]

def find_ancestor(node):
    if ancestor[node] == node: return node
    ancestor[node] = find_ancestor(ancestor[node])
    return ancestor[node]

def union_ancestor(nodeA, nodeB):
    ancestorA, ancestorB = find_ancestor(nodeA), find_ancestor(nodeB)
    if ancestorA < ancestorB: ancestor[ancestorB] = ancestorA
    else: ancestor[ancestorA] = ancestorB

if truth_num == 0:
    print(len(party))
    sys.exit(0)

for person in truth_person:
    union_ancestor(0, person)

for num, persons in party:
    root_person = persons[0]
    for person in persons[1:]:
        union_ancestor(root_person, person)

exaggerate_count = 0
for num, persons in party:
    if all(find_ancestor(person) != find_ancestor(0) for person in persons):
        exaggerate_count += 1

print(exaggerate_count)