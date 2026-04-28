import sys
input = lambda: int(sys.stdin.readline())

prime = [False, False] + [True] * 999999

for i in range(3, 1001, 2):
    if prime[i]:
        prime[i+i::i] = [False] * len(prime[i+i::i])

while True:
    n = input()
    if n == 0:
        break

    for i in range(3, n//2+1, 2):
        if prime[i] and prime[n-i]:
            print(f"{n} = {i} + {n-i}")
            break