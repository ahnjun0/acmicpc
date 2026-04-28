import sys
input = lambda: sys.stdin.readline()

def checkOdd(candyArr, N):
    for i in range(N):
        candyArr[i] = candyArr[i] + 1 if candyArr[i] & 1 else candyArr[i]
    return candyArr

def isSame(candyArr):
    return len(set(candyArr)) == 1

def roundCandy(candyArr, N):
    newArr = [0] * N
    for i in range(N):
        newArr[i] = candyArr[i] // 2 + candyArr[(i - 1) % N] // 2
    return newArr

for _ in range(int(input())):
    N = int(input())
    C = [*map(int, input().split())]
    cnt = 0
    while True:
        C = checkOdd(C, N)
        if isSame(C):
            break
        C = roundCandy(C, N)
        cnt += 1
    print(cnt)