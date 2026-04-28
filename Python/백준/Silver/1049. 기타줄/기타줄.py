import sys
input = lambda: map(int, sys.stdin.readline().split())

N, M = input()
min_pack, min_each = 1001, 1001

for _ in range(M):
    pack, each = input()
    if pack < min_pack: min_pack = pack
    if each < min_each: min_each = each

if min_each * 6 < min_pack:
    print(N * min_each)

else:
    fit = ((N // 6) * min_pack + (N % 6) * min_each)
    over = ((N // 6) + 1) * min_pack
    
    print(min(over, fit))