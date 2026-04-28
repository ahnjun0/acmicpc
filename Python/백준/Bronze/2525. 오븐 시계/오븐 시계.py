h, m = map(int, input().split(" "))
t = int(input())
m += t
H = m//60
m -= 60*H
h += H
while h >=24:
    h -=24
print (h,m)