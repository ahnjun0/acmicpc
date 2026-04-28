c = n = int(input())
nn = 0
t = 0
co = 0
while 1:
    t = n//10 + n%10
    nn = (n%10)*10 + t%10
    co += 1
    n = nn
    if nn == c:
        break
print(co)