import sys, itertools
input = lambda: sys.stdin.readline()

_, M = map(int, input().split())
for i in itertools.product(sorted([*map(int, input().split())]), repeat=M):
    print(*i)