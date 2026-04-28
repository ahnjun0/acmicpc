import sys
input = lambda: int(sys.stdin.readline())

cnt = 0
while True:
    try:
        cnt += input()
    except:
        break

print(cnt)