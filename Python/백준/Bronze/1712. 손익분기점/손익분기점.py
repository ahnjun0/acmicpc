import sys
a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))

if b < c:
    k = c-b
    sell = (a//k) +1
    print(sell)

else:
    print(-1)