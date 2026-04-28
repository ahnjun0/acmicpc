import sys
from collections import defaultdict
input = lambda: int(sys.stdin.readline())
MOD = 1000000007

arr = defaultdict(lambda: -1); arr[0] = 0; arr[1] = 1; arr[2] = 1;

def fibo(N):
    if arr[N] >= 0: return arr[N]
    
    if N % 2 == 0:
        result = (fibo(N//2) * (fibo(N//2 + 1) + fibo(N//2 - 1))) % MOD
    else:
        result = ((fibo((N+1)//2) * fibo((N+1)//2)) % MOD) + ((fibo((N-1)//2) * fibo((N-1)//2)) % MOD) % MOD
    
    arr[N] = result % MOD
    return arr[N]

print(fibo(input()))