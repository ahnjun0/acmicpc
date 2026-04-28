import sys

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

if M == 1:
    M = 2


k = list(range(M, N+1))

a = [False,False] + [True]*(N-1)
primes=[] #1부터 N까지 소수 list

for i in range(2,N+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, N+1, i):
        a[j] = False

prime = []

for i in range(len(k)):
    if k[i] in primes:
        prime.append(k[i])

if len(prime) != 0:
    print(sum(prime))
    print(prime[0])

else:
    print(-1)