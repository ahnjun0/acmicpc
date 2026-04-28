import sys
input = lambda: sys.stdin.readline().rstrip()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def add_fractions(frac1, frac2):
    # (numerator, denominator)
    num1, den1 = frac1
    num2, den2 = frac2
    common_denominator = den1 * den2
    num = num1 * den2 + num2 * den1
    common_gcd = gcd(num, common_denominator)
    return (num // common_gcd, common_denominator // common_gcd)

# (n: numerator, d: denominator)
def compound_fraction(n, d):
    return (n[0]*d[1], n[1]*d[0])

def inFraction():
    ret = []
    
    while True:
        val = stack.pop()
        if val == ")":
            ret.append(inFraction())

        elif val == "(":
            if len(ret) != 3:
                print(-1)
                sys.exit(0)
            
            return add_fractions(compound_fraction(ret[1], ret[0]), ret[2])

        else:
            ret.append((int(val), 1))

N = int(input())
stack = [*input().split()]

if N != len(stack) or stack[-1] != ")":
    print(-1)
    sys.exit(0)

stack.pop()
frac = inFraction()

if len(stack) != 0:
    print(-1)
    sys.exit(0)
    
print(f"{frac[0]} {frac[1]}")