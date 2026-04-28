import sys, math
input = lambda: map(int, sys.stdin.readline().split())

A, P1 = input()
R, P2 = input()

print("Slice of pizza" if A / P1 > (R ** 2) * math.pi / P2 else "Whole pizza")