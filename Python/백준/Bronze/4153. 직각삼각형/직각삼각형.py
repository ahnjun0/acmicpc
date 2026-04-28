import sys

while True:
    triangle = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    if triangle[0] != 0:
        triangle.sort()
        if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
            print('right')
        else:
            print('wrong')
    else:
        break