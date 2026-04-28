import sys
input = sys.stdin.readline

X = int(input())

for _ in range(int(input())):
    a, b = map(int, input().split())
    X -= a*b

print("Yes" if not X else "No")