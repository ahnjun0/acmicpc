import sys
input = lambda: sys.stdin.readline().rstrip()

N = input()

if len(N)//10 > 0:
    for i in range(len(N)//10):
        print(N[10*i:10*(i+1)])

    print(N[10*(i+1):])
else:
    print(N)