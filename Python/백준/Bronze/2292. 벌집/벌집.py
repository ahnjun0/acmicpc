import sys
n = int(sys.stdin.readline().rstrip())
nums = 1
k=1
while n>nums:
    nums += 6*k
    k += 1
print(k)