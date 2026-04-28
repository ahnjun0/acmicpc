import sys
from bisect import bisect_left
input = lambda: sys.stdin.readline()

N = int(input())

stack = []
lis = []

for i in map(int, input().split()):
    if not stack or stack[-1] < i:
        stack.append(i)
        lis.append((len(stack)-1, i))
    else:
        stack[bisect_left(stack, i)] = i
        lis.append((bisect_left(stack, i), i))

ret = []
idx = len(stack)-1
for val in lis[::-1]:
    if val[0] == idx:
        ret.append(val[1])
        idx -= 1

print(len(stack))
print(*ret[::-1])