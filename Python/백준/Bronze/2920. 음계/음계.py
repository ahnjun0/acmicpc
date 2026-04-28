import sys

li = list(map(int, sys.stdin.readline().rstrip().split(" ")))
ascend = 0
descend = 0

for k in range(7):
    if li[k] < li[k+1]:
        ascend += 1
    else:
        descend += 1

if ascend != 0 and descend == 0:
    print('ascending')

elif ascend == 0 and descend != 0:
    print('descending')

else:
    print('mixed')