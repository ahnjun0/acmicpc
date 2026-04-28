import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

cnt = 0
odd_li = ''
for val, i in (count := Counter(inp := input())).items():
    if i & 1 == 1:
        odd_li = val
        cnt += 1
        
    if cnt > 1 or (cnt == 1 and len(inp)&1 == 0):
        print("I'm Sorry Hansoo")
        sys.exit(0)

result = ''
for k, v in sorted(count.items()):
    result += (k * (v//2))

print(result + odd_li + result[::-1])