import sys
input = lambda: sys.stdin.readline()

minX, minY, maxX, maxY = 10000, 10000, -10000, -10000

for i in range(int(input())):
    x, y = map(int, input().split())
    
    if x < minX: minX = x
    if y < minY: minY = y
    if x > maxX: maxX = x
    if y > maxY: maxY = y

print((maxX - minX) * (maxY - minY))