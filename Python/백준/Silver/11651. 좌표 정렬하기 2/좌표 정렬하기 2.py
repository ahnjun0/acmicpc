import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])

for i in arr:
    print(*i)