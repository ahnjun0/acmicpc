import sys
input = lambda: map(int, sys.stdin.readline().split())

_ = input()
print(*sorted(set(input())))
