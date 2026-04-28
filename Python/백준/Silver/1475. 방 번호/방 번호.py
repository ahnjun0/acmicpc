import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

num = Counter(input())
num['9'] += num['6']
num['6'] = 0

if num['9'] % 2 == 0: num['9'] //= 2
else: num['9'] = (num['9'] // 2) + 1

print(max(num.values()))