import sys, math
input = lambda: map(int, sys.stdin.readline().split())

N, A, B, C = input()
print(math.factorial(N) // (math.factorial(A)*math.factorial(B)*math.factorial(C)))