import sys
input = lambda: int(sys.stdin.readline())

n, m = 0, 1
for _ in range(int(input())):
    n, m = m, n+m
print(n)