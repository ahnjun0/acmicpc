import sys

N = list(sys.stdin.readline().rstrip())
N.sort(reverse=True)
print(int(''.join(N)))