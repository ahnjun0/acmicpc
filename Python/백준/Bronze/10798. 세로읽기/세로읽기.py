import sys
input = lambda: sys.stdin.readline().rstrip()

arr = [['' for _ in range(5)] for _ in range(15)]

for i in range(5):
    for j, val in enumerate(input()):
        arr[j][i] = val

for i in arr:
    print(*i, end='', sep='')