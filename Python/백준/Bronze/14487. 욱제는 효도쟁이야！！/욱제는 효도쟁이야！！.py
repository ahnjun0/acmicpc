import sys
input = lambda: [*map(int, sys.stdin.readline().split())]

input()
arr = input()
print(sum(arr)-max(arr))