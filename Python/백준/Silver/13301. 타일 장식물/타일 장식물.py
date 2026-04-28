import sys
input = lambda: int(sys.stdin.readline())

n, m = 0, 1
for _ in range(input()-1):
    n, m = m, n+m
print(n * 2 + m * 4)