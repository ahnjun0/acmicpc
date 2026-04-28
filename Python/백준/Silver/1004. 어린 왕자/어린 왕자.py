import sys
input = lambda: sys.stdin.readline()

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    cnt_start = 0
    cnt_end = 0
    for _ in range(int(input())):
        x, y, a = map(int, input().split())
        flag_start, flag_end = False, False
        
        if (x1-x)**2 + (y1-y)**2 < a**2:
            cnt_start += 1
            flag_start = True
            
        if (x2-x)**2 + (y2-y)**2 < a**2:
            cnt_end += 1
            flag_end = True
        
        if flag_start and flag_end:
            cnt_start -= 1
            cnt_end -= 1

    print(cnt_start + cnt_end)