import sys
input = sys.stdin.readline


def factorical(n):
    if n > 0:
        return n * factorical(n-1)
    else:
        return 1

def permutation(n, r): # n >= r
    return factorical(n)//factorical(n-r)

def combination(n, r): # n >= r
    return permutation(n, r)//factorical(r)

for _ in range(int(input())): # N <= M
    N, M = map(int, input().rstrip().split(" "))

    print(combination(M, N))