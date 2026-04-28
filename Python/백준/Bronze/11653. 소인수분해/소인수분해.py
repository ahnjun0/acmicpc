import sys

N = int(sys.stdin.readline().rstrip())

k = []

for i in range(2, N+1):
    while N%i == 0:
        k.append(i)
        N = N//i
    if N == 0:
        break

print(*k, sep='\n')