a = [int(input()) for _ in range(10)]
b = set()
for i in range(10):
    b.add(a[i]%42)
print(len(b))