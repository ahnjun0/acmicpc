import sys
input = lambda: map(int, sys.stdin.readline().split())

W, H = input()
print(f"{W*H*0.5:.1f}")
