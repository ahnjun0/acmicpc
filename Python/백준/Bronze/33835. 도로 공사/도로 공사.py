import sys
input = lambda: sys.stdin.readline()

N = int(input())
x1, y1 = map(int, input().split())
for _ in range(N-2): _ = input()
xn, yn = map(int, input().split())

print(((xn-x1)**2 + (yn-y1)**2)**0.5)