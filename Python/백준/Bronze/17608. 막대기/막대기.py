import sys
input = lambda: int(sys.stdin.readline().rstrip())

stack = []
for _ in range(input()):
    stack.append(input())

maxi = stack.pop()
cnt = 1

for i in stack[::-1]:
    if i > maxi:
        maxi = i
        cnt += 1

print(cnt)