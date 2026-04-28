import sys, re
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
pattern = re.compile(input().replace('*', '.*'))

for _ in range(n):
    if pattern.fullmatch(input()):
        print("DA")
    else:
        print("NE")