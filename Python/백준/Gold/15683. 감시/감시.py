import sys
from itertools import permutations
input = lambda: sys.stdin.readline()

dxdy = [(-1,0),(0,1),(1,0),(0,-1)]

cctv_dxdy = {
    1: [[0], [1], [2], [3]],
    2: [[0,2], [1,3]],
    3: [[0,1], [1,2], [2,3], [3,0]],
    4: [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
    5: [[0,1,2,3]]
}

def watch(board, x, y, direct):
    changed = []
    dx, dy = dxdy[direct]
    nx, ny = x+dx, y+dy
    while 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6:
        if board[nx][ny] == 0:
            board[nx][ny] = '#'
            changed.append((nx, ny))
        nx += dx
        ny += dy
    return changed

def dfs(idx):
    global blind
    if idx == len(cctvs):
        tmp_blind = sum(row.count(0) for row in board)
        blind = min(tmp_blind, blind)
        return

    x, y, t = cctvs[idx]
    for dset in cctv_dxdy[t]:
        changes = []
        for d in dset:
            changes.extend(watch(board, x, y, d))
        dfs(idx+1)
        
        # Original State
        for cx, cy in changes:
            board[cx][cy] = 0

N, M = map(int, input().split())
blind = N * M
board = []
cctvs = []

for i in range(N):
    board.append(arr := [*map(int, input().split())])
    for j, val in enumerate(arr):
        if 1 <= val <= 5: cctvs.append((i, j, val))

# No.5 CCTV Exception
new_cctvs = []
for (x, y, t) in cctvs:
    if t == 5:
        for d in cctv_dxdy[5][0]:
            watch(board, x, y, d)
    else:
        new_cctvs.append((x, y, t))
cctvs = new_cctvs

dfs(0)
print(blind)