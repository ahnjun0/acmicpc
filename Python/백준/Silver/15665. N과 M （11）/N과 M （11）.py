import sys, itertools
input = lambda: sys.stdin.readline()

_, M = map(int, input().split())
s = set()

for i in itertools.product(sorted([*map(int, input().split())]), repeat=M):
    if i not in s:
        print(*i)
        s.add(i)