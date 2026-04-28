import sys
input = lambda: sys.stdin.readline()

ans = 0

for _ in range(int(input())):
    N, S = map(int, input().split())
    ans += S * pow(N, 1000000005, 1000000007)
print(ans%1000000007)