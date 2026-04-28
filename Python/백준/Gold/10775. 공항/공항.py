import sys
input = lambda: int(sys.stdin.readline())

def unionFind(x):
    global gates
    if gates[x] == x: return x
    
    gates[x] = unionFind(gates[x])
    return gates[x]

G = input()
P = input()
airplanes = [input() for _ in range(P)]
gates = [i for i in range(G+1)]

cnt = 0
for plane in airplanes:
    if (now := unionFind(plane)) == 0:
        break
    gates[now] = gates[now-1]
    cnt += 1
print(cnt)