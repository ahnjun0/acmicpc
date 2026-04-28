a = list(input())
a.append(0)
t=0
if len(a)>=3:
    for i in range(len(a)-2):
        if str(a[i])+str(a[i+1])+str(a[i+2]) == 'dz=':
            del a[i:i+3]
            a.insert(i,0)
            a.insert(i,0)
            a.insert(i,i+101)

if len(a)>=2:
    for i in range(len(a)-1):
        k = str(a[i])+str(a[i+1])
        if (k == 'c=' or k == 'c-' or k == 'd-' or k == 'lj' or k == 'nj' or k == 's=' or k == 'z='):
            del a[i:i+2]
            a.insert(i,0)
            a.insert(i,i+202)


while 0 in a:
    a.remove(0)

print(len(a))