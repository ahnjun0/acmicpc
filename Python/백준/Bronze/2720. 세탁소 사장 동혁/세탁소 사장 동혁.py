import sys
input = lambda: int(sys.stdin.readline())

for _ in range(input()):
    coin = [0]*4
    change = input()
    
    for i, val in enumerate([25, 10, 5, 1]):
        coin[i] = change // val
        change %= val
    
    print(*coin)