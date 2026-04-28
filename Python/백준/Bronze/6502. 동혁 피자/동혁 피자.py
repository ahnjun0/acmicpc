import sys
input = lambda: sys.stdin.readline()

i = 1
while True:
    if (inp := input()) == '0\n':break
    
    r, w, l = map(int, inp.split())
    if w**2 + l**2 <= 4 * r**2:
        print(f"Pizza {i} fits on the table.")
    else:
        print(f"Pizza {i} does not fit on the table.")
    i += 1