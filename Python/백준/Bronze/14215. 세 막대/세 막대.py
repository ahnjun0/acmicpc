import sys
input = lambda: map(int, sys.stdin.readline().split())

inp = [*input()]
inp.sort(reverse=True)

if inp[0] == inp[1] and inp[1] == inp[2]:
    print(inp[0] * 3)

elif inp[0] >= inp[1] + inp[2]:
    print((inp[1] + inp[2]) * 2 - 1)

else:
    print(sum(inp))