import sys
input = lambda : sys.stdin.readline()

N = int(input())

top = list(map(int, input().split()))
push = 1

for i in range(N-1):
    if top[i] <= top[i+1]:
        push += 1

print(push)