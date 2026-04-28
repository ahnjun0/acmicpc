import sys

def factorical(M):
    if M > 1:
        return M * factorical(M-1)
    else:
        return 1

N, K = map(int, sys.stdin.readline().rstrip().split(" "))

print(int(factorical(N) / (factorical(K)*factorical(N-K))))