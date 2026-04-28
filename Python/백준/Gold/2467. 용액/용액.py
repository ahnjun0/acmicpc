import sys
input = lambda: sys.stdin.readline()

L = 0
R = int(input())-1
arr = [*map(int, input().split())]

ans = abs(arr[L] + arr[R])
ansL, ansR = L, R

while L < R:
    val = arr[L] + arr[R]
    
    if abs(val) < ans:
        ansL = L
        ansR = R
        if (ans := abs(val)) == 0:
            break
    
    if val < 0: L += 1
    else: R -= 1

print(arr[ansL], arr[ansR])