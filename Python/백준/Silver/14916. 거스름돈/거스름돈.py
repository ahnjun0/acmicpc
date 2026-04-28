import sys
input = lambda: sys.stdin.readline()

n = int(input())

if n == 1 or n == 3:
    print(-1)

else:
    a, b = n//5, n%5
    match b:
        case 0:
            print(a)
        case 1 | 4:
            print(a+2)
        case 2:
            print(a+1)
        case 3:
            print(a+3)