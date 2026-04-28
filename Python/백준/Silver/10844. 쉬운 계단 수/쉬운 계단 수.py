dp = [9,17,32,61,116]
for i in range(5,N:=int(input())):
    dp.append(dp[i-1]+4*dp[i-2]-3*dp[i-3]-3*dp[i-4]+dp[i-5])
print(dp[N-1]%1000000000)