import sys

M, N = map(int, sys.stdin.readline().rstrip().split(" "))

if M == 1:
    M = 2



for i in range(M, N+1):
    k = 0
    for j in range(2, int(i**0.5)+1):
        if i%j ==0:
            k += 1
            break
    if k == 0:
        print(i)