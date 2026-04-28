import sys

x, y, w, h = map(int, sys.stdin.readline().rstrip().split(" "))
if w-x >= x and h-y >= y:
    if x<y:
        print(x)
    else:
        print(y)
elif w-x >= x and h-y < y:
    if x<h-y:
        print(x)
    else:
        print(h-y)
elif w-x < x and h-y >= y:
    if w-x<y:
        print(w-x)
    else:
        print(y)
elif w-x < x and h-y < y:
    if w-x<h-y:
        print(w-x)
    else:
        print(h-y)
