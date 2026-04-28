import sys, itertools
input = lambda: sys.stdin.readline()

_, M = map(int, input().split())
for i in itertools.combinations(sorted([*map(int, input().split())]), M):
    print(*i)