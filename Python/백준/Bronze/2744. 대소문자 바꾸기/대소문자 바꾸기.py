import sys
input = sys.stdin.readline

for k in input().rstrip():
    if k.isupper():
        print(k.lower(), end='')
    else:
        print(k.upper(), end='')