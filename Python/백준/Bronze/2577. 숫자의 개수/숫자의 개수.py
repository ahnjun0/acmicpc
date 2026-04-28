A = int(input())
B = int(input())
C = int(input())
l = list(str(A*B*C))
for i in range(10):
    print(l.count(str(i)))