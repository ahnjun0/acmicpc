import sys
input = lambda: sys.stdin.readline().rstrip()

regex = []
for i in range(int(input())):
    if regex == []:
        regex = [*input()]
        continue
    
    for idx, (p, q) in enumerate(zip(input(), regex)):
        if q != '?' and p != q:
            regex[idx] = '?'

print(*regex, sep='')