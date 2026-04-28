def repeat_list(original_list, rows, cols):
    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(original_list[(i % 5)][(j % 5)])
        result.append(row)
    
    return result

original_list = [[1,2,3,4,5],
                 [3,4,5,1,2],
                 [5,1,2,3,4],
                 [2,3,4,5,1],
                 [4,5,1,2,3]]
                 
arr = repeat_list(original_list, *map(int, input().split()))

for i in arr:
    print(*i)