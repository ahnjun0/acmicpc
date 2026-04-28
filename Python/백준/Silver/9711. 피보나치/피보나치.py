import sys
input = lambda: sys.stdin.readline()


def fibo(P):
    dp = [0] * 10000
    n, m = 0, 1

    for i in range(P):
        n, m = m, (n+m)
        dp[i] = n
    return dp

dp = fibo(10000)

for i in range(1, int(input())+1):
    P, Q = map(int, input().split())
    print(f"Case #{i}: {dp[P-1]%Q}")