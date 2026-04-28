import sys
input = lambda: sys.stdin.readline()

N = int(input())
cost = [*map(int, input().split())]
city = [*map(int, input().split())]
ptr = 0
next_ptr = 1
cnt = 0

now_city = city[ptr]

while ptr < N-1 and next_ptr < N-1:
    next_city = city[next_ptr]
    
    if now_city > next_city:
        cnt += sum(cost[ptr:next_ptr]) * city[ptr]
        ptr = next_ptr
        now_city = city[ptr]
    
    next_ptr += 1

print(cnt + sum(cost[ptr:next_ptr]) * city[ptr] )