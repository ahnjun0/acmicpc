import sys, math
input = lambda: map(int, sys.stdin.readline().rstrip().split())

A, B = input()
Bsqrt = int(math.sqrt(B))
prime = [False, False] + [True] * (Bsqrt - 1)

for i in range(2, Bsqrt + 1):
    if prime[i]:
        if i**2 >= len(prime): break
        for j in range(i**2, Bsqrt + 1, i):
            prime[j] = False

cnt = 0
for i in range(1, len(prime)):
    if prime[i]:
        tmp = i**2
        while True:
            if tmp < A: tmp *= i
            elif tmp > B: break
            else:
                cnt += 1
                tmp *= i

print(cnt)