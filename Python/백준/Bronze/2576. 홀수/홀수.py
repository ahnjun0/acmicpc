import sys
input = lambda : sys.stdin.readline().rstrip()

re, mini = 0, 100
for _ in range(7):
    tmp = int(input())
    if tmp & 1 == 1:
        re += tmp
        if tmp < mini:
            mini = tmp

print("{}\n{}".format(re, mini) if re != 0 else -1)