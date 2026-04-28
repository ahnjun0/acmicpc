import sys
input = lambda: map(int, sys.stdin.readline().split())

x1, x2 = input()
a, b, c, d, e = input()

print(int((1/3)*a*(x2**3-x1**3) + (1/2)*(b-d)*(x2**2-x1**2) + (c-e)*(x2-x1)))