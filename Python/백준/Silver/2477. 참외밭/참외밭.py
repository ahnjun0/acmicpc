import sys
input = lambda : sys.stdin.readline().rstrip()

K = int(input())
w, w_idx, h, h_idx = 0, 0, 0, 0

arr = [list(map(int, input().split())) for _ in range(6)]

for i, (dest, val) in enumerate(arr):
    if dest <= 2:
        if w < val:
            w, w_idx = val, i
    else:
        if h < val:
            h, h_idx = val, i
                    
print(((w*h) - abs(arr[w_idx-1][1] - arr[(w_idx+1)%6][1]) * abs(arr[h_idx-1][1] - arr[(h_idx+1)%6][1]))*K)