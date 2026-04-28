a = list(input())
a = list(map(ord, a))
t = 0
for i in a:
    if i >= 65 and i<= 67:
        t += 3
    if i >= 68 and i<= 70:
        t += 4
    if i >= 71 and i<= 73:
        t += 5
    if i >= 74 and i<= 76:
        t += 6
    if i >= 77 and i<= 79:
        t += 7
    if i >= 80 and i<= 83:
        t += 8
    if i >= 84 and i<= 86:
        t += 9
    if i >= 87 and i<= 90:
        t += 10
print(t)