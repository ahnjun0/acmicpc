import sys

N = int(sys.stdin.readline().rstrip())
temp = 0
arr = []

for _ in range(N):
    T = int(sys.stdin.readline().rstrip())
    arr.append(T)

arr.sort()

for k in range(len(arr)):
    print(arr[k])