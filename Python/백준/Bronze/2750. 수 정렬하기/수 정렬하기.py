import sys

N = int(sys.stdin.readline().rstrip())
temp = 0
arr = []

for _ in range(N):
    T = int(sys.stdin.readline().rstrip())
    arr.append(T)

for _ in range(N-1):
    for j in range(N-1):
        if arr[j] > arr[j+1]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp

for k in range(len(arr)):
    print(arr[k])