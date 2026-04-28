import sys

input = sys.stdin.readline

N = int(input())
A = set(map(int, input().rstrip().split()))

M = int(input())
arr = list(map(int, list(input().rstrip().split())))

for i in arr:
    if i in A:
        print(1)
    else:
        print(0)
