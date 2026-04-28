import sys
input = lambda: int(sys.stdin.readline())

score = [input() for _ in range(input())]
score.reverse()
cnt = 0

for i in range(0, len(score)-1):
    if score[i] <= score[i+1]:
        cnt += score[i+1] - score[i] + 1
        score[i+1] = score[i] - 1

print(cnt)