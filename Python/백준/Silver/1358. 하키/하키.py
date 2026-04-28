import sys
input = lambda: map(int, sys.stdin.readline().split())

W, H, X, Y, P = input()
cnt = 0
R = H/2

for i in range(P):
    px, py = input()
    
    if X <= px <= X+W and Y <= py <= Y + H:
        cnt += 1
    
    else:
        if (px-X)**2 + (py-Y-R)**2 <= R**2 or (px-X-W)**2 + (py-Y-R)**2 <= R**2:
            cnt += 1

print(cnt)