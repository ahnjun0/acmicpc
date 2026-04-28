import sys
input = lambda : sys.stdin.readline()

N, M = map(int, input().split())

listM = []
cnt = 0

brushOne = False
brushTwo = False

for _ in range(N):
    listM.append(list(map(int, input().split())))
    
for i in range(len(listM)):
    while True:
        
        for j in range(len(listM[i])):
            
            if listM[i][j] == 0 and (brushOne == True or brushTwo == True):
                brushOne = False
                brushTwo = False
        
            if listM[i][j] == 1 and brushOne == False and brushTwo == False:
                brushOne = True
                listM[i][j] -= 1
                cnt += 1
            
            elif listM[i][j] == 2 and brushOne == False and brushTwo == False:
                brushTwo = True
                listM[i][j] -= 2
                cnt += 1
                
                
            elif listM[i][j] == 1 and brushOne == True:
                listM[i][j] -= 1
                
            elif listM[i][j] == 2 and brushTwo == True:
                listM[i][j] -= 2
                

        brushOne = False
        brushTwo = False
        
        if sum(listM[i]) == 0:
            break
        
print(cnt)