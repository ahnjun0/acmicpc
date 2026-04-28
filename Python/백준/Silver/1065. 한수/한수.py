k = int(input())
r = []

han = list(range(100,k+1))

if k<100:
    print(k)

if k>=100 and k<1000:
    for i in range(len(han)):
        s = list(str(han[i]))
        if (int(s[1]) - int(s[0])) == (int(s[2]) - int(s[1])):
            r.append(han[i])
    print(len(r)+99)

if k==1000:
    print(144)
