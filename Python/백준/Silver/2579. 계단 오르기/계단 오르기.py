import sys
input = lambda: int(sys.stdin.readline().rstrip())

N = input()
point = [input() for _ in range(N)]
dp = [point[0], sum(point[:2])] + [0] * (N-2)

if N == 1:
    print(point[0])
    sys.exit(0)

elif N == 2:
    print(sum(point))
    sys.exit(0)

for i in range(2, N):
    dp[i] = max(dp[i-2] + point[i], dp[i-3] + point[i-1] + point[i])

print(dp[-1])