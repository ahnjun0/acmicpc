import sys, re
input = lambda: sys.stdin.readline().rstrip()

pattern = re.compile('(100+1+|01)+')

for i in range(int(input())):
    if pattern.fullmatch(input()):
        print("YES")
    else:
        print("NO")