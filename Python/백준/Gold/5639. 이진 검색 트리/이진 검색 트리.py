import sys
input = lambda: int(sys.stdin.readline())
sys.setrecursionlimit(10**6)

tree = []
while True:
    try: tree.append(int(input()))
    except: break

if not tree: sys.exit(0)

def recursion(start, end):
    if start > end: return
    
    for i in range(start+1, end+1):
        if tree[start] < tree[i]:
            center_point = i
            break
    else:
        center_point = end + 1
    
    recursion(start+1, center_point-1)
    recursion(center_point, end)
    print(tree[start])

recursion(0, len(tree)-1)