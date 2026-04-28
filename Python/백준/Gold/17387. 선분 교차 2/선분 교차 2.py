import sys
input = lambda: map(int, sys.stdin.readline().split())

def ccw(a, b, c):
    xa, ya = a
    xb, yb = b
    xc, yc = c
    return (xa*yb + xb*yc + xc*ya) - (xb*ya + xc*yb + xa*yc)

def check_same_dot(a, b, c, d):
    if a == c or a == d or b == c or b == d:
        return True
    else:
        return False

def check_on_line(a, b, c, d):
    xa, ya = a
    xb, yb = b
    xc, yc = c
    xd, yd = d
    
    for x, y in [(xc, yc), (xd, yd)]:
        if min(xa, xb) <= x <= max(xa, xb) and min(ya, yb) <= y <= max(ya, yb):
            if (y-min(ya, yb))*abs(xb-xa) == (x-min(xa, xb))*abs(yb-ya):
                return True
    
    for x, y in [(xa, ya), (xb, yb)]:
        if min(xc, xd) <= x <= max(xc, xd) and min(yc, yd) <= y <= max(yc, yd):
            if (y-min(yc, yd))*abs(xd-xc) == (x-min(xc, xd))*abs(yd-yc):
                return True
    
    return False

def check_both_straight(p1, p2, p3, p4):
    return min(p1[0], p2[0])<=max(p3[0],p4[0]) and min(p3[0],p4[0])<=max(p1[0],p2[0]) and min(p1[1],p2[1])<=max(p3[1],p4[1]) and min(p3[1],p4[1])<=max(p1[1],p2[1])


x1, y1, x2, y2 = input()
x3, y3, x4, y4 = input()

a, b, c, d = (x1, y1), (x2, y2), (x3, y3), (x4, y4)
flag = False

if check_same_dot(a, b, c, d) or check_on_line(a, b, c, d):
    print(1)

else:
    p1p2 = ccw(a,b,c)*ccw(a,b,d)
    p3p4 = ccw(c,d,a)*ccw(c,d,b)
    
    if p1p2 == 0 and p3p4 == 0:
        flag = True
        if check_both_straight(a, b, c, d):
            print(1)
            sys.exit(0)
    
    print(1 if p1p2 <= 0 and p3p4 <= 0 and not flag else 0)