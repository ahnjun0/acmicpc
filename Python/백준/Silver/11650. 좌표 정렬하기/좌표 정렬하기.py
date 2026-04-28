import sys

input = sys.stdin.readline
arr = []

for _ in range(int(input())):
    arr.append(list(map(int, input().rstrip().split())))
arr.sort()

for k in arr:
    print(*k)