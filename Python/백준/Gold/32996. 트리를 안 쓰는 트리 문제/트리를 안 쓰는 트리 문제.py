N = int(input())
print(N*2-1)

for i in range(N-1):
    print(i*N+i+1, (i+1)*N+i, i+1, 1)

print(N*N, N*N, N, 1)

for i in range(1, N):
    print(i*(N+1), i*(N+1), N, i+1)