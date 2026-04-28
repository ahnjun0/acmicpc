import sys
input = sys.stdin.readline

weight = [1, 3] * 6
isbn = [*input().rstrip()]
missing = isbn.index('*')
checksum = int(isbn[-1])

total = sum(int(check) * weight[i] for i, check in enumerate(isbn[:12]) if check != '*')
print(next(x for x in range(10) if (total + x * weight[missing] + checksum) % 10 == 0))