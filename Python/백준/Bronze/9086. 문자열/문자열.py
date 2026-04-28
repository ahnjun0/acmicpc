import sys
input = sys.stdin.readline

for _ in range(int(input())):
    test_case = input().rstrip()
    li_test = list(test_case)
    print(li_test[0],li_test[-1], sep='')