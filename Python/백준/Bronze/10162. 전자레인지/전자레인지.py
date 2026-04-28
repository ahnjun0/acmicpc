import sys
input = lambda: sys.stdin.readline()

T = int(input())

if T % 10 != 0:
    print(-1)
    sys.exit(0)

first = T // 300
T %= 300

second = T // 60
T %= 60

third = T // 10

print(first, second, third)