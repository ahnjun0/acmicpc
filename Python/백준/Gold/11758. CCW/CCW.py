import sys
input = lambda: sys.stdin.readline().rstrip()

def ccw(a,b,c):
    return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - (b[0]*a[1] + c[0]*b[1] + a[0]*c[1]))

arr = []
for _ in range(3):
    arr.append(tuple(map(int,input().split())))

re = ccw(arr[0], arr[1], arr[2])

if re > 0: print(1)
elif re == 0: print(0)
else: print(-1)
