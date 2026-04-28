import sys
input = lambda: map(int, sys.stdin.readline().split())

T, S = input()
if S == 1:
    print(280)
else: # S == 0
    if 12 <= T <= 16:
        print(320)
    else:
        print(280)