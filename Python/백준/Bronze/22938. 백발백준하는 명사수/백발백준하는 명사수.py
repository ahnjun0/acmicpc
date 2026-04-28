import sys
input = lambda: map(int, sys.stdin.readline().split())

x1, y1, r1 = input()
x2, y2, r2 = input()

if (x2-x1)**2 + (y2-y1)**2 < (r1+r2)**2: print("YES")
else: print("NO")