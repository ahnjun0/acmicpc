import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    arr = [1, 2, 4] + [0] * 8
    match n := (int(input())):
        case 1 | 2 | 3:
            pass
        case _:
            for i in range(2, n):
                arr[i+1] = arr[i] + arr[i-1] + arr[i-2]
    print(arr[n-1])