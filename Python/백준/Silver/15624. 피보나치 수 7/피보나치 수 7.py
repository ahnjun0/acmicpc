import sys
input = lambda: int(sys.stdin.readline())
MOD = 1000000007

n, m = 0, 1
for _ in range(input()):
    n, m = m, (n+m) % MOD
print(n)