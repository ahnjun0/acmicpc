import sys
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    k = int(sys.stdin.readline().rstrip()) #층
    n = int(sys.stdin.readline().rstrip()) #호수
    n_li = list(range(1,n+1,1))
    for _ in range(k):
        pp = []
        for i in range(n):
            li = sum(n_li[0:i+1])
            pp.append(li)
        n_li = pp
    print(pp[-1])