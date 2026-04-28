import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
card = set(map(int, input().split()))
M = int(input())
for i in map(int, input().split()):
    print('{}'.format(1 if i in card else 0), end=" ")