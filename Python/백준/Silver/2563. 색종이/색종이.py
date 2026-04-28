import sys
input = sys.stdin.readline

arr = [[0]*101 for i in range(101)]
cnt = 0


for _ in range(int(input())):
    a, b = map(int, input().split())
    for p in range(10):
        for q in range(10):
            arr[a+p][b+q] = 1

for r in arr:
    for s in range(101):
       if r[s] == 1:
            cnt += 1 

print(cnt)