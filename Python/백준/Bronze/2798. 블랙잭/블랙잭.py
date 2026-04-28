import sys

N, M= map(int, sys.stdin.readline().rstrip().split(" "))
card = list(map(int, sys.stdin.readline().rstrip().split(" ")))
k = maxi = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            if i!=j and i!=k and j!=k:
                k = card[i]+card[j]+card[k]
                if k <= M:
                    maxi = max(maxi, k)

print(maxi)