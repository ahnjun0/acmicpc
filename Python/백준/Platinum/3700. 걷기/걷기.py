import sys
input = lambda: sys.stdin.readline()

class Object:
    def __init__(self, h, point, polygon):
        self.h = h
        self.point = point
        self.polygon = polygon

    def __lt__(self, other):
        return point_in_polygon(other.polygon, self.point) == 1
    
    def __repr__(self):
        return str(self.h)

def point_in_polygon(polygon, point):
    N = len(polygon)-1
    cnt = 0
    p1 = polygon[0]
    
    for i in range(1, N+1):
        p2 = polygon[i]
        
        if min(p1[1], p2[1]) < point[1] <= max(p1[1], p2[1]) and point[0] <= max(p1[0], p2[0]) and p1[1] != p2[1]:
            on_line = ((p2[0]-p1[0]) / (p2[1]-p1[1])) * (point[1]-p1[1]) + p1[0]
            if p1[0] == p2[0] or point[0] <= on_line:
                cnt += 1
        
        p1 = p2
    return cnt & 1


for _ in range(int(input())):
    seonyeong = []
    sanggeun = []

    for _ in range(int(input())):
        H, P, *xy = input().split()
        polygon = [(int(xy[i]), int(xy[i+1])) for i in range(0, int(P)*2, 2)]
        polygon.append(polygon[0])
        H = int(H)
        
        seonyeong_on = point_in_polygon(polygon, (0,0))
        sanggeun_on = point_in_polygon(polygon, (100000, 0))
        
        match (seonyeong_on, sanggeun_on):
            case (1, 0):
                seonyeong.append(Object(H, polygon[0], polygon))
            case (0, 1):
                sanggeun.append(Object(H, polygon[0], polygon))
    
    seonyeong.sort()
    sanggeun.sort()
    
    arr = seonyeong + sanggeun[::-1]

    increase_sum = 0
    decrease_sum = 0

    for i in range(1, len(arr)):
        if arr[i-1].h < arr[i].h:
            increase_sum += arr[i].h - arr[i-1].h
        elif arr[i-1].h > arr[i].h:
            decrease_sum += arr[i-1].h - arr[i].h
    
    print(increase_sum, decrease_sum)
