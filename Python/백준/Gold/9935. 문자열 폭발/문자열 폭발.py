import sys
input = lambda: sys.stdin.readline().rstrip()

inp = input()
bomb = input()
stack = []

for i in inp:
    stack.append(i)
    if bomb[-1] == stack[-1] and stack[-len(bomb):] == [*bomb]:
        del stack[-len(bomb):]

print(''.join(stack) if stack else "FRULA")