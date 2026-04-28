import sys
t = int(sys.stdin.readline().rstrip())

five = int(t//5)
remain = int(t%5)
if remain == 0 and t>=5:
    print(five)
elif remain == 1 and t>5:
    print(five+1)
elif remain == 3:
    print(five+1)
elif (remain == 2 or remain==4) and t>5 and t!=7:
    print(five+2)
elif t == 7:
    print(-1)
else:
    print(-1)