import sys
from bisect import bisect_left
input = lambda: sys.stdin.readline()

N = int(input())
arr = [*map(int, input().split())]

lis = [arr[0]]

for i in arr:
    if lis[-1] < i: lis.append(i)
    else:
        lis[bisect_left(lis, i)] = i

print(len(lis))