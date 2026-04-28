import sys
from bisect import bisect_left
input = lambda: sys.stdin.readline()

N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
arr.sort()

stack = []
lis = []

for _, i in arr:
    if not stack or stack[-1] < i:
        stack.append(i)
        lis.append((len(stack)-1, i))
    else:
        stack[bisect_left(stack, i)] = i
        lis.append((bisect_left(stack, i), i))

ret = set()
idx = len(stack)-1
for val in lis[::-1]:
    if val[0] == idx:
        ret.add(val[1])
        idx -= 1

print(N - len(stack))

for a, b in arr:
    if b not in ret:
        print(a)