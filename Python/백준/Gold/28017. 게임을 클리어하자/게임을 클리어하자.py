r,k=range,input
N,M=map(int,k().split())
a=[]
for _ in r(N):
    a.append(list(map(int,k().split())))
for i in r(N-1):
    for j in r(M):
        a[i+1][j]+=min(a[i][:j]+a[i][j+1:])
print(min(a[-1]))