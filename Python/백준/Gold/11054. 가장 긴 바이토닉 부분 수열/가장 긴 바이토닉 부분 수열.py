import sys
input = lambda: sys.stdin.readline()

N = int(input())
A = [*map(int, input().split())]

lis = [1] * N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            lis[i] = max(lis[i], lis[j] + 1)

lds = [1] * N
for i in reversed(range(N)):
    for j in reversed(range(i, N)):
        if A[i] > A[j]:
            lds[i] = max(lds[i], lds[j] + 1)

max_length = 0
for i in range(N):
    max_length = max(max_length, lis[i] + lds[i] - 1)

print(max_length)