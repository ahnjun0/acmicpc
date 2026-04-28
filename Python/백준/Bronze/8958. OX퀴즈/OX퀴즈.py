import sys
input = sys.stdin.readline

k = int(input())
for _ in range(k):
    score = 0
    cum = 0
    for value in input().rstrip():
        if value == 'O':
            cum += 1
            score += cum
        else:
            cum = 0
            
    print(score)
