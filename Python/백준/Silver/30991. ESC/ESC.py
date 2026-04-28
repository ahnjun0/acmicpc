import sys
input = lambda: int(sys.stdin.readline())

# (a, b, c) -> (a-c, b+c, c-4b)
a, b, c = -1, 1, 1
for _ in range(input()-1):
    a, b, c = a-c, b+c, c-(4*b)

print(a+b+c)