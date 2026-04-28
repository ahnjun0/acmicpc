import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline()


tree = defaultdict(list)

N, R, Q = map(int, input().split())
for _ in range(N-1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

cnt = [0] * (N+1)

def count(node):
    cnt[node] = 1
    for i in tree[node]:
        if not cnt[i]:
            count(i)
            cnt[node] += cnt[i]

count(R)

for _ in range(Q):
    print(cnt[int(input())])
    