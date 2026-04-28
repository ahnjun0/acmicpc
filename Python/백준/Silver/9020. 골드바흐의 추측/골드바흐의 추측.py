import sys

T = int(sys.stdin.readline().rstrip())

a = [False,False] + [True]*(9999)
primes=[]

for i in range(2,10001):
  if a[i]:
    primes.append(i)
    for j in range(2*i, 10001, i):
        a[j] = False

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    n1 = n2 = n//2
    while n1 not in primes or n2 not in primes:
        n1 -= 1
        n2 += 1
    print(n1, n2)
