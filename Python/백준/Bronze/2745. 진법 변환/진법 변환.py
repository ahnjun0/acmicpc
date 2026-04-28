N, B = input().split()
N = [int(char, 36) for char in N]
B = int(B)
result = 0

for i, val in enumerate(N[::-1]):
    result += val * (B ** i)

print(result)