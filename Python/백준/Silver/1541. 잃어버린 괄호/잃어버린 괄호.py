import sys
input = lambda : sys.stdin.readline().rstrip()

N = input().split("-")
ans = 0
for i in N[0].split("+"): ans += int(i)
for i in N[1:]:
    for j in i.split("+"): ans -= int(j)
print(ans)