h, m = input().split(" ")
h, m = int(h), int(m)

if m >= 45:
    m -= 45
    print(h, m)
    
else:
    if h == 0:
        print(23, m+15)
        
    else:
        m += 15
        h -= 1
        print(h, m)        