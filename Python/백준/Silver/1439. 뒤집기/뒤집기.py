import sys
input = lambda: sys.stdin.readline().rstrip()

cnt = 0
before = ''
for i in input():
    if i != before:
        cnt += 1
        before = i

print(cnt//2)