import sys

input = sys.stdin.readline
li = []

for _ in range(int(input())):
    li.append(input().rstrip())

li = list(set(li))
li.sort()
li.sort(key = len)

for i in li:
    print(i)