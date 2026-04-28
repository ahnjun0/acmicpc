t=lambda:map(int,input().split());N,M=t();r=range(N+1);f=[[N]*(N+1)for _ in r];exec("a,b=t();f[a][b]=f[b][a]=1;"*M)
for k in r:
 for i in r:
  for j in r:f[i][j]=min(f[i][j],f[i][k]+f[k][j])
print(min(r,key=lambda i:sum(f[i])))