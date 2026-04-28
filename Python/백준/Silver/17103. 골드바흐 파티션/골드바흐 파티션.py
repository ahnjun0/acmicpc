import sys
input = lambda: int(sys.stdin.readline())

prime = [False, False] + [True] * 999999

for i in range(3, 1001, 2):
    if prime[i]:
        prime[i+i::i] = [False] * len(prime[i+i::i])

for i in range(input()):
    n = input()
    cnt = 0
    
    if n == 4:
        print(1)
        continue

    for i in range(3, n//2+1, 2):
        if prime[i] and prime[n-i]:
            cnt += 1
    print(cnt)