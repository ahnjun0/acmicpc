import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().rstrip().split(" "))
    a = a%10


    if a == 1 or a == 5 or a == 6:
        print(a)

    elif a == 0:
        print('10')

    elif a == 2 or a == 3 or a == 7 or a == 8:
        b = b%4
        if b != 0:
            print((a**b)%10)
        else:
            print((a**4)%10)

    else:
        b = b%2
        if b != 0:
            print((a**b)%10)
        else:
            print((a**2)%10)