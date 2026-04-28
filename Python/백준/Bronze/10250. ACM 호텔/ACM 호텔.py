import sys
t = int(input())
for _ in range(t):
    h,w,n = map(int, sys.stdin.readline().rstrip().split(" "))
    p = str(int(n%h))
    q = str(int(n//h))
    if p == '0':
        p = str(h)
    else:
        q = str(int(q)+1)
    if len(q) == 1:
        q = '0'+q
    print(int(p+q))