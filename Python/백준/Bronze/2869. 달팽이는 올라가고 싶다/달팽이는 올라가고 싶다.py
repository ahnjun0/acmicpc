import sys
a,b,v = map(int, sys.stdin.readline().rstrip().split(" "))

print(int(((v-b-1)/((a-b))+1)))