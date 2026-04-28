import sys
input = sys.stdin.readline

K, N = map(int, input().rstrip().split(" "))
cable = []

for _ in range(K):
    cable.append(int(input()))
lo, hi = 1, max(cable)


while lo <= hi:
    mid = (lo+hi)//2
    cable_cnt = sum([x//mid for x in cable])
    if cable_cnt < N:
        hi = mid-1
    else: # sum(cable_cnt) >= N
        lo = mid+1

print(hi)