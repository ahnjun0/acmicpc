import sys

x1 , y1 = map(int, sys.stdin.readline().rstrip().split(" "))
x2 , y2 = map(int, sys.stdin.readline().rstrip().split(" "))
x3 , y3 = map(int, sys.stdin.readline().rstrip().split(" "))

if (x2-x1)**2 + (y2-y1)**2 + (x3-x1)**2 + (y3-y1)**2 == (x3-x2)**2 + (y3-y2)**2:
    x4 = x2 + (x3-x1)
    y4 = y2 + (y3-y1)
elif (x3-x2)**2 + (y3-y2)**2 + (x3-x1)**2 + (y3-y1)**2 == (x2-x1)**2 + (y2-y1)**2:
    x4 = x1 + (x2-x3)
    y4 = y1 + (y2-y3)
else:
    x4 = x1 + (x3-x2)
    y4 = y1 + (y3-y2)

print(x4, y4)