import sys
input = lambda: map(int, sys.stdin.readline().split())

N, M = input()
N %= 2*M
if N==0: N=2*M

arr = []
for i in range(1, M+1):
    l, r = input()
    arr.extend([(l, i), (r, i)])

arr.sort()
print(arr[N-1][1])