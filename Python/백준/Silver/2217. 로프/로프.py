import sys
input = lambda: int(sys.stdin.readline())

maxi = 0
inp = []
for _ in range(N := input()): inp.append(input())

for i, val in enumerate(sorted(inp, reverse=True)):
    tmp = (i+1) * val
    if tmp > maxi:
        maxi = tmp

print(maxi)