N = int(input())

arr = list(range(1, 2*N, 2))
arr.extend(arr[-2::-1])

for i in arr:
    for _ in range((arr[N-1]-i)//2):
        print(" ", end='')
    for _ in range(i):
        print("*", end='')
    print()