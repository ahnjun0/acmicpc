import sys
input = lambda: map(int, sys.stdin.readline().split())

R, C, T = input()
arr = [[*input()] for _ in range(R)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

purifier = -1
for i in range(R):
    if -1 in arr[i]:
        purifier = i
        break

# 위쪽 공기청정기: purifier, 아래쪽 공기청정기: purifier+1
# 공기청정기의 위치 초기화
arr[purifier][0] = -1
arr[purifier + 1][0] = -1

for _ in range(T):
    # 미세먼지 확산
    spread = [[0] * C for _ in range(R)]  # 확산된 미세먼지 저장
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:  # 미세먼지가 존재하면
                cnt = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        spread[ni][nj] += arr[i][j] // 5
                        cnt += 1
                arr[i][j] -= (arr[i][j] // 5) * cnt  # 자신은 확산된 만큼 감소
    # 확산된 미세먼지를 arr에 반영
    for i in range(R):
        for j in range(C):
            arr[i][j] += spread[i][j]
    
    # 공기청정기 위쪽 순환
    for r in range(purifier-1, 0, -1):
        arr[r][0] = arr[r-1][0]
    for c in range(C-1):
        arr[0][c] = arr[0][c+1]
    for r in range(purifier):
        arr[r][-1] = arr[r+1][-1]
    for c in range(C-1, 0, -1):
        arr[purifier][c] = arr[purifier][c-1]
    arr[purifier][1] = 0  # 공기청정기 위쪽 끝

    # 공기청정기 아래쪽 순환
    for r in range(purifier+2, R-1):
        arr[r][0] = arr[r+1][0]
    for c in range(C-1):
        arr[R-1][c] = arr[R-1][c+1]
    for r in range(R-1, purifier+1, -1):
        arr[r][-1] = arr[r-1][-1]
    for c in range(C-1, 0, -1):
        arr[purifier+1][c] = arr[purifier+1][c-1]
    arr[purifier+1][1] = 0  # 공기청정기 아래쪽 끝

# 결과 계산
result = sum(sum(row) for row in arr) + 2  # 공기청정기 위치의 -1 두 개를 더함
print(result)
