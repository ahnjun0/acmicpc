import sys
input = lambda: sys.stdin.readline()

for i in range(1, int(input())+1):
    n, *val = map(int, input().split())
    val.sort()
    max_gap = 0
    for j in range(n-2, -1, -1):
        if max_gap < val[j+1]-val[j]:
            max_gap = val[j+1]-val[j]
    print(f"Class {i}\nMax {max(val)}, Min {min(val)}, Largest gap {max_gap}")