import sys

li = list(map(int, sys.stdin.readline().rstrip().split(" ")))
li = [x ** 2 for x in li]
print(sum(li)%10)