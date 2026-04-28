import sys
input = lambda: map(int, sys.stdin.readline().split())

N, M = input()
cnt = 0

paint = [[0 for _ in range(100)] for _ in range(100)]
for _ in range(N):
    x1, y1, x2, y2 = input()
    
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            paint[i-1][j-1] += 1

for i in range(100):
    for j in range(100):
        if paint[i][j] > M:
            cnt += 1

print(cnt)