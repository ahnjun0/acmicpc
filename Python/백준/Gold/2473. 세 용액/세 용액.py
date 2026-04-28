import sys
input = lambda: sys.stdin.readline()

N = int(input())
arr = sorted([*map(int, input().split())])

ans = abs(arr[0] + arr[1] + arr[N-1])
ansL, ansR, ansI = 1, N-1, 0

for i in range(N-2):
    L = i+1
    R = N-1
    while L < R:
        val = arr[L] + arr[R] + arr[i]
        
        if abs(val) < ans:
            ansL = L
            ansR = R
            ansI = i
            if (ans := abs(val)) == 0:
                break
        
        if val < 0: L += 1
        else: R -= 1

print(arr[ansI], arr[ansL], arr[ansR])