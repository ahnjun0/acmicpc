import sys
input = lambda: sys.stdin.readline().rstrip()

chairman = "ZZZ"

for _ in range(int(input())):
    name = input()
    if len(name) == 3 and name < chairman:
        chairman = name

print(chairman)