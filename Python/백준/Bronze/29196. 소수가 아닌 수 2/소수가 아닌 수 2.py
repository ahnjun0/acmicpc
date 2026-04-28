import sys
input = lambda: sys.stdin.readline().rstrip()

k = input()
print("YES")
print(int(k[2:]), 10 ** len(k[2:]))
