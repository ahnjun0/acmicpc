import sys
input = lambda: int(sys.stdin.readline())

N = input()
F = input()
tmp = (N // 100) * 100
for i in range(100):
    if (tmp + i) % F == 0:
        print(f"{i:>02}")
        break