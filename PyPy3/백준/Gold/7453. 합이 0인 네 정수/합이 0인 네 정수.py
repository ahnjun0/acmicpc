import sys
from collections import defaultdict
from itertools import product
input = lambda: sys.stdin.readline()

A, B, C, D = [], [], [], []

for _ in range(int(input())):
    for val, arr in zip(map(int, input().split()), [A, B, C, D]):
        arr.append(val)

AB = dict()
result = 0

for a, b in product(A, B):
    v = a+b
    if v not in AB.keys():
        AB[v] = 1
    else:
        AB[v] += 1


for c, d in product(C, D):
    v = -1 * (c + d)
    if v in AB.keys():
        result += AB[v]

print(result)