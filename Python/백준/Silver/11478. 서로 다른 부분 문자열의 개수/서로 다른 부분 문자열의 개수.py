import sys
input = lambda: sys.stdin.readline().rstrip()

check = set()
inp = input()

for i in range(len(inp)):
    for j in range(i+1, len(inp)+1):
        if inp[i:j] not in check:
            check.add(inp[i:j])
print(len(check))