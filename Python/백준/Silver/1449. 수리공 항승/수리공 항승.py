import sys
input = lambda: map(int, sys.stdin.readline().split())

N, L = input()
leak = [*input()]
leak.sort()

cnt = 1
scope = leak[0] + (L - 0.5)

for i in leak[1:]:
    if scope < i + 0.5:
        scope = i + (L - 0.5)
        cnt += 1
    else:
        continue

print(cnt)