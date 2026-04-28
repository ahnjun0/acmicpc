import sys
input = lambda: sys.stdin.readline()

input()
flag = [False, False, False]
cnt = 0
for i in input().split():
    if i == '0' and not flag[0]:
        flag[0] = True
        cnt += 1
    
    elif i == '1' and flag[0] and not flag[1]:
        flag[1] = True
        cnt += 1
    
    elif i == '2' and flag[0] and flag[1] and not flag[2]:
        flag[2] = True
        cnt += 1
    
    if flag[0] and flag[1] and flag[2]:
        flag = [False, False, False]

print(cnt)