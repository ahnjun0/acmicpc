d = [1,3,5]
for i in range(3, n := int(input())):
    d.append(d[-1] + 2 *d[-2])
    
print(d[n-1] % 10007)