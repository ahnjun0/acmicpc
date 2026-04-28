import sys, math
input = lambda: map(int, sys.stdin.readline().split())

D, H, W = input()
l = (H**2 + W**2)**0.5

print(math.floor(H*D/l), math.floor(W*D/l))