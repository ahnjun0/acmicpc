import sys
input = lambda: sys.stdin.readline().rstrip()

pw = set()
for _ in range(int(input())):
    inp = input()
    if inp[::-1] in pw or inp == inp[::-1]:
        print(f"{len(inp)} {inp[(len(inp)//2)]}")
        break

    else:
        pw.add(inp)