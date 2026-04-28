import sys
input = lambda : sys.stdin.readline().rstrip()

def between(a, b):
    dist = 0
    for i in range(4):
        if a[i] != b[i]: dist += 1
    return dist

for _ in range(int(input())):
    N = int(input())
    if N > 32:
        print(0)
        input()
    
    else:
        min_dist = 100
        mbti = list(input().split())

        for i in range(N-2):
            for j in range(i+1, N-1):
                for k in range(j+1, N):
                    min_dist = min(min_dist, between(mbti[i], mbti[j]) + between(mbti[j], mbti[k]) + between(mbti[k], mbti[i]))
                    
        print(min_dist)