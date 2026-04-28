import sys

N = int(sys.stdin.readline().rstrip())

a = [False,False] + [True]*(246911)
primes=[] #1부터 N까지 소수 list

for i in range(2,246912,1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, 246912, i):
        a[j] = False

while N != 0:
    cnt = 0
    for i in primes:
        if N<i<=2*N:
            cnt += 1
    print(cnt)
    N = int(sys.stdin.readline().rstrip())