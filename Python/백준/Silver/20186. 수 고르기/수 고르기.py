import sys
input = lambda: map(int, sys.stdin.readline().split())

N, K = input()
arr = sorted([*input()], reverse=True)
cnt = 0
for i in range(K):
    cnt += arr[i] - i

print(cnt)