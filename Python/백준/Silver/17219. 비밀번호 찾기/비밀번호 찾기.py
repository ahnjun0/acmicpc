import sys
input = lambda : sys.stdin.readline().rstrip()

pw = {}
N, M = map(int, input().split())
for _ in range(N):
    www, password = input().split()
    pw[www] = password
    
for _ in range(M):
    print(pw[input()])