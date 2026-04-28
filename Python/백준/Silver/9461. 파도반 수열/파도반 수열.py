import sys
input = lambda : sys.stdin.readline().rstrip()

def pad(n):
    pPrevPrev, pPrev, pCurr, pNext = 1, 1, 1, 1
    for _ in range(3, n+1):
        pNext = pPrevPrev + pPrev
        pPrevPrev = pPrev
        pPrev = pCurr
        pCurr = pNext
    return pNext

for _ in range(int(input())):
    print(pad(int(input())-1))