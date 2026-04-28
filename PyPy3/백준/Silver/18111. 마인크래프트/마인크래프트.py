import sys

input = lambda: sys.stdin.readline()

N, M, B = map(int, input().split())
arr = []
floor = 0
lowest_time = N * M * 256 * 2

for _ in range(N):
    arr.append(list(map(int, input().split())))

for k in range(257):
    removal = creation = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > k:
                removal += arr[i][j] - k
            else:
                creation += k - arr[i][j]

    if creation - removal > B:
        break

    time = removal * 2 + creation * 1
    if time <= lowest_time:
        lowest_time = time

        if floor < k:
            floor = k

print(lowest_time, floor)