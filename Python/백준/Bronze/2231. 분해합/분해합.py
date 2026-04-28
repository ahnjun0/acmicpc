import sys

try:
    N = int(sys.stdin.readline().rstrip())
    all_list = []
    for i in range(N):
        all_list.append(sum(map(int, list(str(i))))+i)

    print(int(all_list.index(N)))

except:
    print(0)