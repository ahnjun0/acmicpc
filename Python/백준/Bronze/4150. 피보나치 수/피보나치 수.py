import sys
input = lambda: int(sys.stdin.readline())

n, m = 1, 1
for _ in range(input()-1):
    n, m = m, (n+m)
print(n)