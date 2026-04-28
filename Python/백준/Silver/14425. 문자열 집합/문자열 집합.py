import sys
input = lambda: sys.stdin.readline()

N, M = map(int, input().split())
string = set()
cnt = 0

for _ in range(N):
    string.add(input())

for _ in range(M):
    if input() in string:
        cnt += 1

print(cnt)