num = set(range(1,10001))
m_num = set()

for i in range(1,10001):
    li = list(map(int, list(str(i))))
    m_num.add(sum(li)+i)

k = list(num-m_num)
k.sort()

for q in k:
    print(q)