import sys
from itertools import combinations
input = lambda: map(int, sys.stdin.readline().split())

while True:
    arr = [*input()]
    if arr[0] == 0: break
    
    for i in combinations(arr[1:], 6):
        print(*i)
    print()