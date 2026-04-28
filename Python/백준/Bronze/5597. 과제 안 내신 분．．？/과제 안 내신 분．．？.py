import sys

all_list = list(range(1, 31))
li = []

for _ in range(28):
    li.append(int(sys.stdin.readline().rstrip()))

diff_set = [x for x in all_list if x not in li]
diff_set.sort()
print(diff_set[0])
print(diff_set[1])