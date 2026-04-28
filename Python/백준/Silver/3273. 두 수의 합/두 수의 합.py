import sys
input = lambda: sys.stdin.readline()
_ = int(input())
arr = sorted([*map(int, input().split())])
x = int(input())

seen = set()
cnt = 0

for n in arr:
    if x - n in seen:
        cnt += 1
    seen.add(n)

print(cnt)