import sys

N = int(sys.stdin.readline().rstrip())

n_list = list(range(666, 3000000, 1))
cnt = 0

for j in n_list:
    j_list = list(str(j))
    for k in range(len(j_list)-2):
        if j_list[k] == '6' and j_list[k+1] == '6' and j_list[k+2] == '6':
            cnt += 1
            break
    if cnt == N:
        print(j)
        break