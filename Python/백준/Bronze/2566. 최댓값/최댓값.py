import sys
input = sys.stdin.readline

arr = []
row = column = maxi = 0
for i in range(9):
    input_arr = list(map(int, input().split()))
    arr.append(input_arr)
    if max(input_arr) > maxi:
        row = i
        maxi = max(input_arr)
    
column = arr[row].index(maxi)

print(maxi)
print(row+1, column+1)