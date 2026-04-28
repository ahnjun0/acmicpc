import sys
input = lambda: int(sys.stdin.readline())

N = input()
wine = [input() for _ in range(N)]

if N > 2:
    dp = [wine[0]] + [0] * (N-1)

    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[i] + wine[j] for i, j in [[0, 1], [0, 2], [1, 2]])
    
    for i in range(3, N):
        dp[i] = max(dp[i-1], dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])
    
    print(dp[-1])

else: # N == 1 or N == 2:
    print(sum(wine))