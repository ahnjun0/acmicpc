import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
ID2Name = dict()
Name2ID = dict()

for i in range(1, N+1):
    tmp = input()
    ID2Name[i] = tmp
    Name2ID[tmp] = i

for _ in range(M):
    order = input()
    print(ID2Name[int(order)] if order.isdigit() else Name2ID[order])