import sys
input = lambda: sys.stdin.readline().rstrip()

mirco = [*map(int, [*input()])]

if 0 in mirco:
    mirco.remove(0)
    
    if sum(mirco) % 3 == 0:
        print(''.join(map(str, sorted(mirco, reverse=True))) + '0')
        sys.exit(0)

print(-1)
