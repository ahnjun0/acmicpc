import sys
input = lambda: sys.stdin.readline()

N = int(input())
arr = [*input().split()]

dp = [['0' for _ in range(N)] for _ in range(N)]

dp[0][0] = '1'
for i in range(1, N):
    dp[i][i] = '1'
    
    if arr[i-1] == arr[i]:
        dp[i-1][i] = '1'


for i in range(1, N):
    for j in range(1, min(i+1, N-i)):
        if arr[i-j] == arr[i+j]:
            dp[i-j][i+j] = '1'
        else:
            break
        
    if dp[i-1][i] == '1':
        for j in range(1, min(i+1, N-i)):
            if arr[i-j-1] == arr[i+j]:
                dp[i-j-1][i+j] = '1'
            else:
                break


for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])