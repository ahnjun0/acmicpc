import sys, itertools
input = lambda: sys.stdin.readline()

_, M = map(int, input().split())
s = set()

for i in itertools.combinations(sorted([*map(int, input().split())]), M):
    if i not in s:
        print(*i)
        s.add(i)