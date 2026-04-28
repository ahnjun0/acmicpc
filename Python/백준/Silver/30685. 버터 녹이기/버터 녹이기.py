import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
fan = []

for _ in range(N):
    fan.append(tuple(map(int, input().split())))
fan.sort(key=lambda x: x[0])

time = 10**100

for i in range(N-1):
    between = (fan[i+1][0] - fan[i][0])
    leftmax, rightmax = fan[i][1]//2, fan[i+1][1]//2
    
    if between / 2 <= min(leftmax, rightmax):
        # case 1
        if between % 2 == 0:
            time = min(time, between // 2)
        # case 2
        else: # between % 2 == 1
            time = min(time, (between + 1) // 2)

    # case 3
    elif (between <= (leftmax + rightmax) ):
        time = min(time, between - min(leftmax, rightmax))

print(time-1 if time < 10**100 else "forever")