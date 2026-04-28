import math, sys

n = int(input())

if int(math.sqrt(n)) == math.sqrt(n): print(1)
else:
    for i in range(1, int(math.sqrt(n))+1):
        if int(math.sqrt(n - i**2)) == math.sqrt(n - i**2):
            print(2)
            sys.exit(0)
            
    for i in range(1, int(math.sqrt(n))+1):
        for j in range(int(math.sqrt(n - i**2)) + 1):
            if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
                print(3)
                sys.exit(0)
    
    print(4)
