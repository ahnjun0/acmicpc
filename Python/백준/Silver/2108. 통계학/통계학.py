import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
k = []
min_list = [0] * 4001

for _ in range(N):
    k.append(int(sys.stdin.readline().rstrip()))

k.sort()
        
k_s = Counter(k).most_common()

modee = k_s[0][0]

if len(k_s) > 1 and k_s[0][1] == k_s[1][1]:
    modee = k_s[1][0]

print(round(sum(k)/N))
print(k[int(N//2)])
print(modee)
print(int(k[-1]-k[0]))