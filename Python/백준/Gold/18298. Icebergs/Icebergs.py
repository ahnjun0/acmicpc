import sys
input = lambda: sys.stdin.readline()

def area(polygon):
    plus = minus = 0
    polygon.append(polygon[0])
    
    for i in range(len(polygon)-1):
        plus += polygon[i][0] * polygon[i+1][1]
        minus += polygon[i][1] * polygon[i+1][0]

    return abs(plus-minus)

ret = 0
for _ in range(int(input())):
    ret += area([[*map(int, input().split())] for _ in range(int(input()))])

print(int(.5*ret))