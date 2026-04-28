import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    x1, y1, r1, x2, y2, r2= map(int, sys.stdin.readline().rstrip().split(" "))
    d = (x2-x1)**2 + (y2-y1)**2
    if x1 == x2 and y1== y2 and r1 == r2:
        print(-1)
    elif (r1-r2)**2 < d < (r1+r2)**2:
        print(2)
    elif d == (r1+r2)**2:
        print(1)
    elif d == (r1-r2)**2:
        print(1)

    elif d < (r1-r2)**2:
        print(0)
    elif d > (r1+r2)**2:
        print(0)