import sys
input = lambda: sys.stdin.readline().rstrip()

cnt = 0
for i in range(4):
    for p, q in zip(input(), "F^F^F^F^"):
        if p == q: cnt += 1
    for p, q in zip(input(), "^F^F^F^F"):
        if p == q: cnt += 1

print(cnt)