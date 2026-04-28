import sys
input = lambda: sys.stdin.readline()

for i in range(1, int(input())+1):
    A, B, C = sorted(map(int, input().split()))
    
    if A == B and B == C:
        print(f"Case #{i}: equilateral")
    elif A + B > C:
        if A == B or B == C:
            print(f"Case #{i}: isosceles")
        else:
            print(f"Case #{i}: scalene")
    else:
        print(f"Case #{i}: invalid!")