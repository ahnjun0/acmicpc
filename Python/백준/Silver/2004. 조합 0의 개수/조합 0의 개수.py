def two(n):
    cnt = 0
    while n := n // 2:
        cnt += n
    return cnt

def five(n):
    cnt = 0
    while n := n // 5:
        cnt += n
    return cnt

n, m = map(int, input().split())
print(min(two(n)-two(n-m)-two(m), five(n)-five(n-m)-five(m)))