import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
sortli = list(set(li))
sortli.sort()

di = {string : i for i, string in enumerate(sortli)}

for k in range(N):
    print(di[li[k]], end=' ')