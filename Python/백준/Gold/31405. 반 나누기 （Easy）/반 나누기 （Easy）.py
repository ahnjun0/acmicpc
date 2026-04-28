import sys
input = lambda: map(int, sys.stdin.readline().split())

def area(arr):
    plus = minus = 0
    for i in range(len(arr)-1):
        plus += arr[i][0] * arr[i+1][1]
        minus += arr[i][1] * arr[i+1][0]
    
    return .5 * abs(plus - minus)

shape = [[*input()] for _ in range(*input())]
shape.append(shape[0])

half_area = area(shape) / 2
cumulate = 0

print("YES")
print("1 0")

for i in range(1, len(shape)-2):
    tmp = area([shape[0], shape[i], shape[i+1], shape[0]])
    
    if cumulate + tmp > half_area:
        print(i+1, (half_area-cumulate) / tmp)
        break
    
    cumulate += tmp