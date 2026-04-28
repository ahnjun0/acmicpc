import sys
input = lambda: map(int, sys.stdin.readline().split())

while True:
    inp = [*input()]
    if inp == [0, 0, 0]:
        sys.exit(0)
    inp.sort(reverse=True)
    
    if inp[0] >= inp[1] + inp[2]:
        print("Invalid")
    
    elif inp[0] == inp[1] == inp[2]:
        print("Equilateral")

    elif inp[0] == inp[1] or inp[1] == inp[2]:
        print("Isosceles")
    
    else:
        print("Scalene")