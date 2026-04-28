import sys
input = lambda: sys.stdin.readline()

sheet = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

for i in range(int(input())):
    if [*map(int, input().split())] == sheet:
        print(i+1)