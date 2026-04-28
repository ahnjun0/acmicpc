import sys

while True:
    N = list(sys.stdin.readline().rstrip())
    if N != ['0']:
        N_rev = list(N)
        N_rev.reverse()
        if N_rev == N:
            print('yes')
        else:
            print('no')
    else:
        break