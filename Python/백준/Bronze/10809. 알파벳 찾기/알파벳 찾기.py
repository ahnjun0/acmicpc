a = list(input())
for i in range(97, 123):
    k = chr(i)
    try:
        print(a.index(k),end=' ')
    except ValueError:
        print(-1,end=' ')