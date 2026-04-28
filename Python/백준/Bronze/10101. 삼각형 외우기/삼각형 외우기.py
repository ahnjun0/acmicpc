import sys
input = lambda: sys.stdin.readline().rstrip()

a = int(input())
b = int(input())
c = int(input())

if a == b and b == c and c == 60:
    print("Equilateral")
    sys.exit(0)

if a + b + c != 180:
    print("Error")
    sys.exit(0)

if a != b and b != c and a != c:
    print("Scalene")
    
else:
    print("Isosceles")