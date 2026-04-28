import sys
input = lambda: sys.stdin.readline()

def point_on_line(p1, p2, point):
    if min(p1[0], p2[0]) <= point[0] <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= point[1] <= max(p1[1], p2[1]):
        cross_product = (point[1] - p1[1]) * (p2[0] - p1[0]) - (point[0] - p1[0]) * (p2[1] - p1[1])
        if cross_product == 0:
            return True
    return False

def point_in_polygon(polygon, point):
    N = len(polygon)-1
    cnt = 0
    p1 = polygon[0]
    
    for i in range(1, N+1):
        p2 = polygon[i]
        
        if point_on_line(p1, p2, point):
            return 1
        
        if min(p1[1], p2[1]) < point[1] <= max(p1[1], p2[1]) and point[0] <= max(p1[0], p2[0]) and p1[1] != p2[1]:
            on_line = ((p2[0]-p1[0]) / (p2[1]-p1[1])) * (point[1]-p1[1]) + p1[0]
            if p1[0] == p2[0] or point[0] <= on_line:
                cnt += 1
        
        p1 = p2
    
    return cnt & 1


polygon = []

for _ in range(int(input())):
    polygon.append(tuple(map(int, input().split())))

polygon.append(polygon[0])

print(point_in_polygon(polygon, tuple(map(int, input().split()))))
print(point_in_polygon(polygon, tuple(map(int, input().split()))))
print(point_in_polygon(polygon, tuple(map(int, input().split()))))