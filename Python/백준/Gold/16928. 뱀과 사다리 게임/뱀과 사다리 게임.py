import sys
from collections import deque
input = lambda: map(int, sys.stdin.readline().rstrip().split())

snake = {}
ladder = {}
board = {i: [0, False] for i in range(1, 101)}

N, M = input()
for _ in range(N):
    orig, dest = input()
    snake[orig] = dest

for _ in range(M):
    orig, dest = input()
    ladder[orig] = dest

queue = deque([1])

while queue:
    now = queue.popleft()
    
    if now == 100:
        print(board[100][0])
        sys.exit(0)
    
    for i in range(1, 7):
        ne_xt = now + i
        
        if ne_xt <= 100 and not board[ne_xt][1]:
            if ne_xt in ladder:
                ne_xt = ladder[ne_xt]
            elif ne_xt in snake:
                ne_xt = snake[ne_xt]
            
            if not board[ne_xt][1]:
                board[ne_xt] = [board[now][0] + 1, True]
                queue.append(ne_xt)