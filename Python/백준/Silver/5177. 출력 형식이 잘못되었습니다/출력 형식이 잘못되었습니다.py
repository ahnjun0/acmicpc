import sys, re
input = lambda: sys.stdin.readline()

def normalize(s):
    s = s.lower().strip()
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'\s*([()\[\]{}.,;:])\s*', r'\1', s) 
    s = s.replace('[', '(').replace('{', '(').replace(']', ')').replace('}', ')')
    s = s.replace(';', ',')

    return s

for i in range(1, int(input())+1):
    inp1 = normalize(input())
    inp2 = normalize(input())
    if inp1 == inp2:
        print(f"Data Set {i}: equal")
    else:
        print(f"Data Set {i}: not equal")
    print()