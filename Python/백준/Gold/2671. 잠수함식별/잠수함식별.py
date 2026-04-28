import sys, re
input = lambda: sys.stdin.readline().rstrip()

pattern = re.compile('(100+1+|01)+')

if pattern.fullmatch(input()):
    print("SUBMARINE")
else:
    print("NOISE")