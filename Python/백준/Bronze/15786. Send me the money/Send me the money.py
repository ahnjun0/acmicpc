import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
S = input()

for _ in range(M):
    i = 0
    
    for c in input():
        tmp = S[i]
        
        if c != tmp: continue
        
        i += 1
        
        if N <= i: break

    print('true') if N == i else print('false')