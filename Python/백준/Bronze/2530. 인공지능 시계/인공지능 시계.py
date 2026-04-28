import sys
input = lambda: sys.stdin.readline()

A, B, C = map(int, input().split())
D = int(input())

A += D // 3600
D %= 3600
B += D // 60
D %= 60
C += D

if C >= 60:
    C -= 60
    B += 1

if B >= 60:
    B -= 60
    A += 1

if A >= 24:
    A %= 24

print(A, B, C)