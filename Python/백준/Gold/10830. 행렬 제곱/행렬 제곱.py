import sys
input = lambda: map(int, sys.stdin.readline().split())

def mul(A, B):
    N = len(A)
    AB = [[0] * N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            for i in range(N):
                AB[r][c] += A[r][i] * B[i][c]
            AB[r][c] %= 1000
    
    return AB

def power(a, b):
    if b == 1:
        return a

    else:
        tmp = power(a, b//2)
        if b % 2:
            return mul(mul(tmp, tmp), a)
        else:
            return mul(tmp, tmp)

N, B = input()
A = [[*input()] for _ in range(N)]

if B == 1:
    for r in range(N):
        for c in range(N):
            A[r][c] %= 1000
else:
    A = power(A, B)

for i in A:
    print(*i)
