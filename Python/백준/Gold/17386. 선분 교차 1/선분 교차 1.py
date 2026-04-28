import sys
input = lambda: map(int, sys.stdin.readline().split())

def ccw(a, b, c):
    xa, ya = a
    xb, yb = b
    xc, yc = c
    return (xa*yb + xb*yc + xc*ya) - (xb*ya + xc*yb + xa*yc)

x1, y1, x2, y2 = input()
x3, y3, x4, y4 = input()

a, b, c, d = (x1, y1), (x2, y2), (x3, y3), (x4, y4)

print(1 if ccw(a,b,c)*ccw(a,b,d) <= 0 and ccw(c,d,a)*ccw(c,d,b) <= 0 else 0)