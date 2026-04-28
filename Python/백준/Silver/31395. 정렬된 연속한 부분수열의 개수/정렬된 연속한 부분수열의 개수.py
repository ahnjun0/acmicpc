import sys
input = lambda: sys.stdin.readline()

N = int(input())
arr = [*map(int, input().split())]
ret, cnt = 0, 0

for i in range(1, N):
    if arr[i-1] < arr[i]:
        cnt += 1
    else:
        ret += ((cnt) * (cnt+1)) // 2
        cnt = 0

ret += (((cnt) * (cnt+1)) // 2) + N

print(ret)