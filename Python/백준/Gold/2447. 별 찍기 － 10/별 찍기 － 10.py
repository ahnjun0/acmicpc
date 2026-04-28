import sys
sys.setrecursionlimit(10**6 )

def star_append(x):
    if x == 1:
        return ['*']

    stars = star_append(x//3)
    L=[]

    for star in stars:
        L.append(star*3)
    for star in stars:
        L.append(star+' '*(x//3)+star)
    for star in stars:
        L.append(star*3)
    return L

N = int(sys.stdin.readline().rstrip())
print('\n'.join(star_append(N)))