import sys
input = lambda: sys.stdin.readline().rstrip()

dp = [(1,0),(0,1)]
input_arr = []

for _ in range(int(input())):
    input_arr.append(int(input()))

max_val = max(input_arr)

for i in range(2, max_val+1):
    dp.append((dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1]))
    
for val in input_arr:
    print(*dp[val])