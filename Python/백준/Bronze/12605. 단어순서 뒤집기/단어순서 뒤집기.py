import sys
input = lambda: sys.stdin.readline()

for i in range(int(input())):
    print(f"Case #{i+1}: ", end='')
    print(*input().split()[::-1])
