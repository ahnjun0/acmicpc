import sys
a = int(input())
b = list(map(int, input().split(" ")))
k = []

for i in range(len(b)):
    k.append(b[i]/max(b)*100)

print(sum(k)/a)