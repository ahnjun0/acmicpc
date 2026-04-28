import sys
input = lambda: map(int, sys.stdin.readline().split())

K, N, M = input()
re = K*N-M
print(re if re > 0 else 0)