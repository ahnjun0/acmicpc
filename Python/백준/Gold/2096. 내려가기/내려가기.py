import sys
input = lambda: sys.stdin.readline()

N = int(input())
startArr = [*map(int, input().split())]
maxDP = [startArr, [0,0,0]]
minDP = [startArr, [0,0,0]]

for i in range(1, N):
    tmpArr = [*map(int, input().split())] 
    maxDP[1][0] = tmpArr[0] + max(maxDP[0][0], maxDP[0][1])
    maxDP[1][1] = tmpArr[1] + max(maxDP[0])
    maxDP[1][2] = tmpArr[2] + max(maxDP[0][1], maxDP[0][2])
    
    
    minDP[1][0] = tmpArr[0] + min(minDP[0][0], minDP[0][1])
    minDP[1][1] = tmpArr[1] + min(minDP[0])
    minDP[1][2] = tmpArr[2] + min(minDP[0][1], minDP[0][2])

    maxDP[0] = maxDP[1][:]
    minDP[0] = minDP[1][:]
    
print(max(maxDP[0]), min(minDP[0]))