import sys
input = lambda: sys.stdin.readline()

N = int(input())
A = sorted([*map(int, input().split())]) 
B = sorted([*map(int, input().split())], reverse=True)

val = 0
for i in range(N):
    val += A[i] * B[i]

print(val)