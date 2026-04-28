import sys
inputs = lambda: map(int, sys.stdin.readline().split())

N = int(input())
X, S = inputs()

for _ in range(N):
    c, p = inputs()
    if c <= X and p > S:
        print("YES")
        sys.exit(0)
print("NO")