a = list(map(int, input().split(" ")))
a.sort()

if len(set(a)) == 1:
    print(10000+a[0]*1000)

elif len(set(a)) == 2:
    if a[0] == a[1]:
        print(1000+a[0]*100)
    else:
        print(1000+a[1]*100)
    
elif len(set(a)) == 3:
    print(a[2]*100)