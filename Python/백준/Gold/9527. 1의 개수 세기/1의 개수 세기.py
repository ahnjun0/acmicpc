import sys
input = lambda: map(int, sys.stdin.readline().split())

def recur(x, memo):
    if x == 0:
        return 0
    if x in memo:
        return memo[x]
    
    half = x//2
    if x % 2 == 0:
        res =  recur(half, memo) + recur((half) - 1, memo) + half
    else:
        res = 2 * recur(half, memo) + half + 1
    memo[x] = res
    return res

memo = {}
A, B = input()
print(recur(B, memo)-recur(A-1, memo))