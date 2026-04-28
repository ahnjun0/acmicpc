import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

matrix_f = []

for _ in range(N):
    matrix_f.append(list(map(int, input().rstrip().split())))

for i in range(N):
    temp_m = list(map(int, input().rstrip().split()))

    for j in range(M):
        matrix_f[i][j] += temp_m[j]

for i in matrix_f:
    print(' '.join(map(str, i)))