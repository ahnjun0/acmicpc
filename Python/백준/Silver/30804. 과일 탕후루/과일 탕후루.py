import sys
input = lambda: sys.stdin.readline()

N = int(input())
tanghulu = [*map(int, input().split())]

lptr = 0
max_len = 0
count = [0] * 10
kind_count = 0

for rptr, val in enumerate(tanghulu):
    count[val] += 1
    if count[val] == 1:
        kind_count += 1
    
    while kind_count > 2:
        count[tanghulu[lptr]] -= 1
        if count[tanghulu[lptr]] == 0:
            kind_count -= 1
        lptr += 1
    
    max_len = max(max_len, rptr - lptr + 1)
    
print(max_len)