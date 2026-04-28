import sys
input = lambda: sys.stdin.readline()

arr = [0] * int(input())
build = [*map(int, input().split())]
for i, val in enumerate(build):
    cnt = 0
    
    mini = 1000000001
    for p in range(i-1, -1, -1):
        left = (val - build[p]) / (i - p)
        if left < mini:
            cnt += 1
            mini = left

    maxi = -1000000001
    for q in range(i+1, len(build)):
        right = (build[q] - val) / (q - i)
        if right > maxi:
            cnt += 1
            maxi = right
    
    arr[i] = cnt

print(max(arr))