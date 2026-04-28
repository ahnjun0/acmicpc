import sys
input = lambda: sys.stdin.readline()

K = int(input())
D1, D2 = map(int, input().split())

print(K**2 - (.5*(D1-D2))**2)