from itertools import permutations
import sys
input = lambda: map(int, sys.stdin.readline().rstrip().split())

N, M = input()
for i in permutations(sorted(frozenset(input())), M):
    print(*i)