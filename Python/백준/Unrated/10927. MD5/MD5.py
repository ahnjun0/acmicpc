import sys
import hashlib
input = lambda: sys.stdin.readline().rstrip()

print(hashlib.md5(input().encode('utf-8')).hexdigest())