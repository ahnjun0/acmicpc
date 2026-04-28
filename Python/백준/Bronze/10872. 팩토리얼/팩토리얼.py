import sys

def factorical(num):
    if num == 1:
        return 1
    elif num == 0:
        return 1
    else:
        return num * factorical(num-1)

N = int(sys.stdin.readline().rstrip())
print(factorical(N))