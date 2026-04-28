import sys
input = lambda : sys.stdin.readline().rstrip()

A, B = map(int, input().split())

def xor(n):
    ans = 0
    for i in range(n//4*4, n+1):
        ans ^= i
    return ans

print(xor(A-1) ^ xor(B))