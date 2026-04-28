a, b = input().split(" ")
a, b = list(str(a)), list(str(b))
a.reverse(), b.reverse()
a,b = int(''.join(a)), int(''.join(b))
if a>b:
    print(a)
else:
    print(b)