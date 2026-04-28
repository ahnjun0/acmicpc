import sys
input = lambda: sys.stdin.readline().rstrip()

arr = []
plus = minus = 0
for _ in range(int(input())):
    arr.append([*map(int, input().split())])
arr.append(arr[0])

for i in range(len(arr)-1):
    plus += arr[i][0] * arr[i+1][1]
    minus += arr[i][1] * arr[i+1][0]

print(f"{(0.5 * abs(plus - minus)):.1f}")