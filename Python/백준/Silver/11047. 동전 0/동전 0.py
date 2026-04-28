import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
coin = []
cnt = 0

for _ in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)

for i in coin:
    if K - i >= 0:
        cnt += K // i
        K = K % i
    
    if K == 0:
        break
    
print(cnt)