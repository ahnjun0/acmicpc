import sys
input = lambda: sys.stdin.readline()

jaehwan = input()
doctor = input()

print("go" if doctor in jaehwan else "no")