import sys
input = sys.stdin.readline

N = int(input().rstrip())
judge_list = []
for _ in range(N):
    p, q = input().rstrip().split(" ")
    p = int(p)
    judge_list.append([p,q])


judge_list.sort(key=lambda x:x[0])

for i in range(N):
    print(judge_list[i][0], judge_list[i][1])