import sys
input = lambda: sys.stdin.readline().rstrip()

stack = []
tag = False
tmp = []

for i in input():
    if i == "<":
        stack.append(tmp[::-1])
        tmp = []
        tag = True
        tmp.append(i)
        continue

    if i == ">":
        tag = False
        tmp.append(i)
        stack.append(tmp)
        tmp = []
        continue
    
    if not tag and i == " ":
        stack.append(tmp[::-1] + [' '])
        tmp = []
        continue
    
    tmp.append(i)

stack.append(tmp[::-1])

for i in stack:
    if len(i) != 0:
        print(''.join(i), end='')