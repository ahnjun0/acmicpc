import sys
input = lambda: int(sys.stdin.readline())

for _ in range(input()):
    inp = input()
    print("Good" if (inp+1)%(inp%100) == 0 else "Bye") 