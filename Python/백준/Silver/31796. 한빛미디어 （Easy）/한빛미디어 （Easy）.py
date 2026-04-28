import sys
input = lambda: sys.stdin.readline()

N = int(input())
arr = sorted(map(int, input().split()))

page = 0
idx = 0

while idx < N:
    page += 1
    start_price = arr[idx]
    while idx < N and arr[idx] < start_price * 2:
        idx += 1

print(page)