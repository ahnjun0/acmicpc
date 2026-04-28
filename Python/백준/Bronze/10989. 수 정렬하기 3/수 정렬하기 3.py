import sys

#Counting Sort : 최댓값과 입력 배열의 원소 값 개수를
#               누적합으로 구성한 배열로 정렬을 수행

N = int(sys.stdin.readline().rstrip())

counting = [0] * (10001)

for _ in range(N):
    num = (int(sys.stdin.readline().rstrip()))
    counting[num] += 1

for j in range(1,10001):
    while counting[j] != 0:
        print(j)
        counting[j] -= 1