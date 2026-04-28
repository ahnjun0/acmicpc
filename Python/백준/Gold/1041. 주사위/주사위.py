import sys
from itertools import combinations
input = lambda: sys.stdin.readline()
opposite = [(0, 5), (1, 4), (2, 3)]

N = int(input())
arr = [*map(int, input().split())]

if N == 1:
    print(sum(arr) - max(arr))
    sys.exit(0)

one = min(arr)
two = min([arr[a] + arr[b] for a, b in [x for x in [*combinations(range(6), 2)] if x not in opposite]])
three = min([arr[a] + arr[b] + arr[c] for a, b, c in [x for x in [*combinations(range(6), 3)] if ((x[0], x[1]) not in opposite and (x[0], x[2]) not in opposite and (x[1], x[2]) not in opposite)]])

print(three * 4 + two * (8 * N - 12) + one * (5 * (N ** 2) - 16 * N + 12))