i = int(input())
t = 0

for j in range(i):
    k = list(input())
    set_k = list(set(k))
    if len(k) == len(set_k):
        t += 1
    else:
        list_k = []
        while len(k) != 0:
            if k[0] not in list_k:
                list_k.append(k[0])
                choice = k[0]
                del k[0]

            elif k[0] == choice:
                del k[0]
            
            else:
                t -= 1
                break
        t += 1
print(t)