import sys
input = lambda : sys.stdin.readline().rstrip()

listen = set()
result = set()
N, M = map(int, input().split())

for _ in range(N):
    listen.add(input())

for _ in range(M):
    name = input()
    if name in listen:
        result.add(name)

print(len(result))
tmp = list(result)
tmp.sort()
print(*tmp, sep="\n")