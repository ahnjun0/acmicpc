import sys
input = lambda: sys.stdin.readline()

for i in range(int(input())):
    V, E = map(int, input().split())
    print(2-V+E)