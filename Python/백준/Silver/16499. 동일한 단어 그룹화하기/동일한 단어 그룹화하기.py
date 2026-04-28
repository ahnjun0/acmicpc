import sys
input = lambda: sys.stdin.readline().rstrip()

group = set()
for _ in range(int(input())):
    group.add(tuple(sorted(input())))

print(len(group))