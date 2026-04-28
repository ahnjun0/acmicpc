import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    for i in input().split():
        print(i[::-1], end=' ')
    print()