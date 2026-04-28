import sys
from itertools import combinations
input = lambda: sys.stdin.readline().split()

N, M = map(int, input())
city = [[*input()] for _ in range(N)]

result = int(1e6)
house = []
chick = []

for i in range(N):
    for j in range(N):
        match city[i][j]:
            case '1': house.append([i, j])
            case '2': chick.append([i, j])

for chi in combinations(chick, M):  # m개의 치킨집 선택
    tmp = 0
    for hou in house: 
        chi_len = 200   # 각 집마다 치킨 거리
        for j in range(M):
            chi_len = min(chi_len, abs(hou[0] - chi[j][0]) + abs(hou[1] - chi[j][1]))
        tmp += chi_len
    result = min(result, tmp)

print(result)