A, B = input().split()
print(sum(map(int, [A.replace("6","5"), B.replace("6","5")])), sum(map(int, [A.replace("5","6"), B.replace("5","6")])))