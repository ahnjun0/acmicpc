import sys
input = lambda: sys.stdin.readline()

for i in range(1, int(input())+1):
    arr = [*map(int, input().split())]
    arr.sort(reverse=True)
    
    print(f"Scenario #{i}:")
    if arr[0] ** 2 == arr[1] ** 2 + arr[2] ** 2:
        print("yes\n")
    else:
        print("no\n")