N = 1000 - int(input())
cnt = 0
t = [100,10,1]
r = [5,1]

for i in t:
    for j in r:
        cnt += N//(i*j)
        N %= i*j
print(cnt)