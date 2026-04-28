import sys
input = sys.stdin.readline

def GCD(a, b):
    while b!=0:
        r = a%b
        a = b
        b = r
    return a

a, b = input().rstrip().split()
a, b = int(a), int(b)
result = GCD(a,b)
print(result, int(a*b/result), sep='\n')