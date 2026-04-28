import sys
input = lambda: sys.stdin.readline().rstrip().split()

dp_before = []
dp_now = []

for i in range(N := int(*input())):
    dp_now = [*map(int, input())]

    if i != 0:
        for j in range(0, i+1):
            if j == 0: dp_now[0] += dp_before[0]
            elif j == i: dp_now[j] += dp_before[j-1]
            else: dp_now[j] += max(dp_before[j-1], dp_before[j])

    dp_before = dp_now


print(max(dp_before))
