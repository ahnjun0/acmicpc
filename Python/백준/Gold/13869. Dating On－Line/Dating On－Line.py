import sys, math
input = lambda: sys.stdin.readline()

N = int(input())
rad = math.radians(360/N)
scores = sorted(map(int, input().split()), reverse=True)
coordi = [(val * math.cos(rad * i), val * math.sin(rad * i)) for i, val in enumerate(scores[1::2][::-1] + scores[::2])]
coordi.append(coordi[0])

plus = minus = 0
for i in range(len(coordi)-1):
    plus += coordi[i][0] * coordi[i+1][1]
    minus += coordi[i][1] * coordi[i+1][0]

print(f"{(.5 * abs(plus - minus)):.3f}")