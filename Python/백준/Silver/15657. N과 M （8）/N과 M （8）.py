from itertools import combinations_with_replacement
import sys
input = lambda: map(int, sys.stdin.readline().rstrip().split())

N, M = input()
for i in combinations_with_replacement(sorted(frozenset(input())), M):
    print(*i)