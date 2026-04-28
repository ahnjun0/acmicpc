import sys
input = lambda: int(sys.stdin.readline())

if (N := input()) == 1:
    print(1)

else:
    dp = [1, 1] + [0] * (N-2)
    for i in range(2, N): dp[i] = dp[i-1] + dp[i-2]
    print(dp[N-1])