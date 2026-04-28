a = int(input())
for _ in range(a):
    k = input().split(" ")
    for _ in range(int(k[0])):
        j = list(k[1])
    for i in j:
        print(i*int(k[0]),end="")
    print()