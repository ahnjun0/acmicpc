import sys
input = lambda: sys.stdin.readline().split()

_, _ = input()
A = set(input())
B = set(input())
print(len(A^B))