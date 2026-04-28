import sys
input = lambda: sys.stdin.readline().rstrip()

first = input()
second = input()
third = input()
arr = [[[0] * (len(third) + 1) for _ in range(len(second) + 1)] for _ in range(len(first) + 1)]

for i in range(1, len(first)+1):
    for j in range(1, len(second)+1):
        for k in range(1, len(third)+1):
            if first[i-1] == second[j-1] == third[k-1]:
                arr[i][j][k] = arr[i-1][j-1][k-1] + 1
            else:
                arr[i][j][k] = max(arr[i-1][j][k], arr[i][j-1][k], arr[i][j][k-1])

print(arr[-1][-1][-1])