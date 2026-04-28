import sys
input = lambda: sys.stdin.readline().rstrip()

arr = []
inp = input()
for i in range(len(inp)):
    arr.append(inp[i:])
arr.sort()
for v in arr:
    print(v)