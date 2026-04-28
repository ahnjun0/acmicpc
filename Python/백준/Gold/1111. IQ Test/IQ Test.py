import sys
input = lambda: sys.stdin.readline()

N = int(input())
arr = [*map(int, input().split())]

if N == 1: print('A')
elif N == 2:
    if arr[0] != arr[1]: print('A')
    else: print(arr[0])

else:
    if arr[0] == arr[1]:
        if len(set(arr)) == 1:
            print(arr[0])
        else:
            print('B')
    else:
        a = (arr[1] - arr[2]) // (arr[0] - arr[1])
        b = arr[1] - (arr[0] * a)
        
        for i in range(N-1):
            test = arr[i] * a + b
            if test != arr[i+1]:
                print('B')
                break
        else:
            print(arr[-1]*a + b)