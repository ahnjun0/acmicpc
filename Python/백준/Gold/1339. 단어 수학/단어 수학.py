import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

alpha = Counter()

for _ in range(int(input())):
    for i, val in enumerate(inp := input()):
        alpha[val] += 10 ** (len(inp) - i - 1)

cnt = 0

for i, j in zip(alpha.most_common(), range(9, -1, -1)):
    cnt += i[1] * j

print(cnt)