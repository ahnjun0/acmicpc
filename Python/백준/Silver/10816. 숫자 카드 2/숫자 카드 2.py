import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip().split()))
max_arr, min_arr = max(arr), min(arr)
arr_cnt = [0] * 20000001

for k in arr:
    arr_cnt[k+10000000] += 1

M = int(input())
arr_m = list(map(int, input().rstrip().split()))

for i in arr_m:
    print(arr_cnt[i+10000000], end=' ')