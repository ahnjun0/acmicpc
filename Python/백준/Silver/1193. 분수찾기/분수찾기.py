import sys
n = int(sys.stdin.readline().rstrip())
line = 0
end = 0
while n>end:
    line += 1
    end += line

h = end - n
if line%2==0:
    print('{}/{}'.format(line-h, h+1))
else:
    print('{}/{}'.format(h+1, line-h))