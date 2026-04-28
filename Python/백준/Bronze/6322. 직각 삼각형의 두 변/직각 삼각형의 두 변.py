import sys
input = lambda: map(int, sys.stdin.readline().split())

idx = 1
while True:
    a, b, c = input()
    if (a, b, c) == (0, 0, 0): sys.exit(0)
    
    print(f"Triangle #{idx}")
    if c == -1:
        print(f"c = {(a**2 + b**2)**.5:.3f}")
    elif c > a and c > b:
        print(f"{'a' if a==-1 else 'b'} = {(c**2 - max(a, b)**2)**.5:.3f}")
    else:
        print("Impossible.")
    
    print()
    
    idx += 1