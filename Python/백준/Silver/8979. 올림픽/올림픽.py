import sys
input = lambda: map(int, sys.stdin.readline().split())

N, K = input()
arr = []

for _ in range(N):
    name, gold, silver, bronze = input()
    arr.append(tuple([gold, silver, bronze]))
    if name == K:
        know = (gold, silver, bronze)

arr.sort(reverse=True)
print(arr.index(know) + 1)