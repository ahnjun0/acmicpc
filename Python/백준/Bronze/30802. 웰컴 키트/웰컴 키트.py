import sys
input = lambda: sys.stdin.readline()

N = int(input())
sizes = [*map(int, input().split())]
T, P = map(int, input().split())

bundle = 0

for i in sizes:
    if i == 0: pass
    elif i < T: bundle += 1
    elif i % T == 0: bundle += (i // T)
    else: bundle += ((i // T) + 1)

print(bundle)
print(N//P, N%P)