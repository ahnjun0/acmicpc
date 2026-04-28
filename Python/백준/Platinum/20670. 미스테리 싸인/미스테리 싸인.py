import sys
input = lambda: map(int, sys.stdin.readline().split())

def vector(a, b): return (b[0]-a[0], b[1]-a[1])

def ccw(v1, v2):
    cross_product = v1[0]*v2[1] - v1[1]*v2[0]
    if cross_product > 0: return 1
    elif cross_product < 0: return -1
    else: return 0

def point_in_convex_polygon(polygon, point):
    n = len(polygon)
    vec_l = vector(polygon[0], polygon[n-1])
    vec_r = vector(polygon[0], polygon[1])
    vec_c = vector(polygon[0], point)

    if ccw(vec_l, vec_c) > 0 or ccw(vec_r, vec_c) < 0:
        return False

    # Binary Search
    l, r = 1, n-1
    while l+1 < r:
        m = (l + r) // 2
        vec_m = vector(polygon[0], polygon[m])
        if ccw(vec_m, vec_c) > 0:
            l = m
        else:
            r = m

    v1 = vector(polygon[l], point)
    v2 = vector(point, polygon[l+1])
    return ccw(v1, v2) < 0

N, M, K = input()
A = [(x, y) for x, y in zip(*[iter(input())]*2)]
B = [(x, y) for x, y in zip(*[iter(input())]*2)]
sign = [(x, y) for x, y in zip(*[iter(input())]*2)]

violation = 0
for point in sign:
    if not point_in_convex_polygon(A, point) or point_in_convex_polygon(B, point):
        violation += 1

print(violation if violation > 0 else "YES")