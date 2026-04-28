import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
tree = list(map(int, input().split()))
lo, hi = 0, max(tree)


while lo <= hi:
    mid = (lo + hi) // 2
    value = sum([((i - mid) if i > mid else 0) for i in tree])
    
    if M <= value:
        lo = mid+1
        
    else:
        hi = mid-1

print(hi)