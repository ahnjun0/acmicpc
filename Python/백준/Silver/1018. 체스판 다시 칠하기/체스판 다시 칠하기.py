import sys

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
# M이 가로, N이 세로 - 예제 2에서 가로 13, 세로 10
chess = []
ans = []

for _ in range(N):
    chess.append(list(sys.stdin.readline().rstrip()))

for i in range(N-7):
    for j in range(M-7):
        cnt_b = 0
        cnt_w = 0
        for p in range(i, i+8):
            for q in range(j, j+8):
                if (p+q)%2==0:
                    if chess[p][q] != 'W':
                        cnt_w += 1
                    elif chess[p][q] != 'B':
                        cnt_b += 1
                else:
                    if chess[p][q] != 'B':
                        cnt_w += 1
                    elif chess[p][q] != 'W':
                        cnt_b += 1

        ans.append(min(cnt_w, cnt_b))

print(min(ans))