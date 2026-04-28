N = int(input())
M = int(input())
S = input()
ioi, cnt, idx = 0, 0, 0

while idx < M-1:
    if S[idx:idx+3] == "IOI":
        cnt += 1
        idx += 2
        if cnt == N:
            ioi += 1
            cnt -= 1
    else:
        cnt = 0
        idx += 1

print(ioi)