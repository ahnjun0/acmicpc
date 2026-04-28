import sys
input = lambda : sys.stdin.readline().rstrip()

def r_round(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)

N = int(input())

if N:
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    
    arr.sort()
    delete = r_round(N*0.15)
    print(r_round(sum(arr[delete:-delete] if delete else arr) / (N-2*delete)))

else:
    print(0)