import sys
input = lambda: int(sys.stdin.readline())

pos = []
neg = []
result = 0

for _ in range(input()):
    if (N := input()) > 1:
        pos.append(N)
    elif N <= 0:
        neg.append(N)
    else:
        result += 1

pos.sort(reverse = True)
neg.sort()

if len(pos) & 1 == 1:
    result += pos.pop()

if len(neg) & 1 == 1:
    result += neg.pop()

result += sum(a*b for a, b, in zip(pos[::2], pos[1::2]))
result += sum(a*b for a, b, in zip(neg[::2], neg[1::2]))

print(result)