import sys
input = lambda: sys.stdin.readline()

dp = [0] * int(input())
table = [*map(int, input().split())]
dp[0] = table[0]
maxi = dp[0]

for i in range(1, len(dp)):
    dp[i] = max(table[i], dp[i-1]+  table[i])
    if dp[i] > maxi: maxi = dp[i]
print(maxi)