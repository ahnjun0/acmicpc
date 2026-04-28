arr = [0] * (N := (int(input()) + 1))
for i in range(2, N):
    arr[i] = arr[i-1]+1
    for j in [2, 3]:
        if i % j == 0:
            arr[i] = min(arr[i], arr[i//j] + 1)
print(arr[-1])