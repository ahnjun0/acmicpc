import sys, copy
from fractions import Fraction
input = lambda : sys.stdin.readline()

N, M = map(int, input().split())
plate = []
for _ in range(N):
    plate.append(list(map(Fraction, input().split())))
    
percent = [Fraction(0)] * M
percent_next = [Fraction(0)] * M
first_ball = plate[0].index(2)
percent[first_ball] = Fraction(1)
percent_next[first_ball] = Fraction(1)

for i in range(N-1):
    for j in range(1, M-1):
        if plate[i+1][j] == Fraction(1):
            if plate[i+1][j-1] != Fraction(1):
                percent_next[j-1] += percent[j] * Fraction(0.5)
                
            if plate[i+1][j+1] != Fraction(1):
                percent_next[j+1] += percent[j] * Fraction(0.5)
            
            percent_next[j] = Fraction(0)
            
            if plate[i][j-1] == Fraction(1):
                percent_next[j-1] = Fraction(0)
            if plate[i][j+1] == Fraction(1):
                percent_next[j+1] = Fraction(0)
    
    percent = copy.deepcopy(percent_next)
    # print("percent : ", *percent)


result = Fraction(0)
index = -1

for i, large_num in enumerate(percent):
    if large_num > result:
        result = large_num
        index = i
        

print(index)