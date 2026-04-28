import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
for _ in range(n):
    cloth = {}
    k = int(input())
    for _ in range(k):
        a, b = input().split()
        
        if b in cloth:
            cloth[b].append(a)
        else:
            cloth[b] = [a]
    
    cnt = 1
    valid = False
    
    for value in cloth.values():
        cnt *= len(value) + 1
        valid = True
        
    print(cnt-1)