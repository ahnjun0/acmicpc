import sys

L = int(sys.stdin.readline().rstrip())
ans = list(map(ord, sys.stdin.readline().rstrip()))
answer = 0
m = 0

for i in range(L):
    ans[i] -= 96

for k in ans:
    answer += k*(31**m)
    m += 1

print(answer%1234567891)