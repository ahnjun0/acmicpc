import sys
input = lambda: int(sys.stdin.readline())

cnt = 1
while ((val := input()) != 0):
    print(f'{cnt}. {"odd" if val & 1 else "even"} {val//2}')
    cnt += 1