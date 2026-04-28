import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = input().split()
for _ in range(int(N)):
    print(input()[::-1])