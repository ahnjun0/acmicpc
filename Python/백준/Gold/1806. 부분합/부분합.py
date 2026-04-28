import sys
input = lambda: map(int, sys.stdin.readline().split())

N, S = input()
arr = [*input()]
pt1, pt2 = 0, 0
minSize = N+1
subTotal = arr[0]

while pt1 < N:
    while pt2 < N - 1 and subTotal < S:
        pt2 += 1
        subTotal += arr[pt2]

    if subTotal >= S:
        minSize = min(minSize, pt2 - pt1 + 1)
    
    subTotal -= arr[pt1]
    pt1 += 1

print(0 if minSize == N + 1 else minSize)
