word = input()
word = list(word.upper())
unique = list(set(word))
p = 0
t = 1

for i in range(len(unique)):
    k = word.count(unique[i])
    if k > p:
        p = k
        q = unique[i]
        t = 0

    elif k == p:
        t += 1

    
if t != 0:
    print("?")

else:
    print(q)
