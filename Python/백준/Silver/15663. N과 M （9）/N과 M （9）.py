from itertools import permutations
import sys
input = lambda: map(int, sys.stdin.readline().rstrip().split())

_, M = input()
result = set()

for i in permutations(sorted(input()), M):
    result.add(i)

for i in sorted(result):
    print(*i)