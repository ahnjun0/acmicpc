import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
time = list(map(int, input().split()))
time.sort()

mini = 0
for i, value in enumerate(time):
    mini += (N-i) * value
    
print(mini)