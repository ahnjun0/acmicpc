import sys
input = lambda: sys.stdin.readline()

N = int(input())
sol = ""
N2 = N//2

for i in range(N2):
    sol += f"{N2 - i} {(N2)*2 - i} "

print((sol + str(N) if N & 1 else sol).rstrip())