import sys
input = lambda: sys.stdin.readline()

log = set()

for _ in range(int(input())):
    A, B = input().split()
    if B == "enter":
        log.add(A)
    else:
        log.remove(A)

print(*sorted(log, reverse=True), sep='\n')