import sys
input = sys.stdin.readline


T = int(input().rstrip())


for _ in range(T):
    testnum = 0
    decision = False
    tmp = list(input().rstrip())

    for k in tmp:
        if k == '(':
            testnum += 1
        else:
            testnum -= 1
        
        if testnum < 0:
            print("NO")
            decision = True
            break
    
    if decision:
        continue

    if testnum == 0:
        print("YES")
    else:
        print("NO")