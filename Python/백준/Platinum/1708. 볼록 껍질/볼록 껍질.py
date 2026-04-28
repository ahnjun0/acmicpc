import sys
input = lambda: sys.stdin.readline()

def ccw(a,b,c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def convex_hull(points):
    lower = [] # left -> right
    for p in points:
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = [] # right -> left
    for p in reversed(points):
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    full_hull = lower[:-1] + upper[:-1]
    
    return len(set(full_hull))
    

points = sorted([tuple(map(int, input().split())) for _ in range(int(input()))], key=lambda x: (x[0], x[1]))
print(convex_hull(points))