import sys

N, W, H = map(int, sys.stdin.readline().rstrip().split(" "))
K = (W**2 + H**2)**0.5

for _ in range(N):
    match = int(sys.stdin.readline().rstrip())
    if match <= K:
        print("DA")
    else:
        print("NE")