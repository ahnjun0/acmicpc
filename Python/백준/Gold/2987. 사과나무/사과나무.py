import sys
input = lambda: sys.stdin.readline()

def ccw(p1, p2, p3):
    return p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])

tri = [[*map(int, input().split())] for _ in range(3)]
print(f"{abs(ccw(*tri))/2:.1f}")

if ccw(tri[2], tri[1], tri[0]) > 0:
    tri.reverse()

ret = 0
for _ in range(int(input())):
    tmp = [*map(int, input().split())]
    if ccw(tmp, tri[1], tri[0]) > 0: continue
    if ccw(tmp, tri[0], tri[2]) > 0: continue
    if ccw(tmp, tri[2], tri[1]) > 0: continue
    ret += 1

print(ret)