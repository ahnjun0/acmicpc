import sys
input = lambda: map(int, sys.stdin.readline().split())

N, K = input()
arr = [*input()]
maxi = now = sum(arr[:K])

for i in range(0, N-K):
    now = now - arr[i] + arr[i+K]
    maxi = max(maxi, now)
    
print(maxi)