import sys
input = lambda : sys.stdin.readline().rstrip()

valid = False

N = int(input())
M = int(input())

ans = abs(100-N)

if M != 0:
    broken_button = set(input().split())

else:  # M == 0
    broken_button = set()
    

if not valid and N == 100:  # N == 100
    print(0)
    valid = True
    
elif not valid:
    for num in range(1000001):
        for i in str(num):
            if i in broken_button:
                break
        else:
            ans = min(ans, len(str(num)) + abs(num-N))
    
    print(ans)