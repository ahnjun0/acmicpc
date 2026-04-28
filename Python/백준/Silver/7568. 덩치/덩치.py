import sys

N = int(sys.stdin.readline().rstrip())
 
data = []
ans = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    data.append((a, b)) # 몸무계와 키를 묶어서 append 해줌
 
for i in range(N):
    count = 0
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]: # 몸무게와 키 모두 자신보다 큰 사람의 수를 센다
            count += 1 
    ans.append(count + 1) # 덩치 등수는 자신보다 몸무계 키 모두 큰 사람의 수 + 1 이므로 count + 1을 ans에 append한다.
 
for d in ans:
    print(d,end=" ")