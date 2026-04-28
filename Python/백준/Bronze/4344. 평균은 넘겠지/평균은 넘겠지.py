a = int(input())
for _ in range(a):
    p = 0
    b = list(map(int, input().split(" ")))
    m = (sum((b[1:]))/b[0])
    for k in range(1, len(b)):
        if b[k] > m:
            p += 1
    print('{:.3f}%'.format(p/b[0]*100))