import sys
input = lambda: sys.stdin.readline()

dp = [1] * int(input())
arr = [*map(int, input().split())]

for i in range(1, len(dp)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(find := max(dp))
out = []

for i in range(len(dp)-1, -1, -1):
    if dp[i] == find:
        out.append(arr[i])
        find -= 1

print(*out[::-1])