import sys
input = lambda: sys.stdin.readline().rstrip()

W, N = input().split()
arr = []

for _ in range(int(N)):
    arr.append(input().translate(str.maketrans("123456789", "15??2??8?")))

match W:
    case "L" | "R":
        for s in arr:
            print(s[::-1])
    case "U" | "D":
        for s in arr[::-1]:
            print(s)