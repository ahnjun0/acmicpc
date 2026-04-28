import sys
input = lambda: map(int, sys.stdin.readline().rstrip().split())

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
date = 0

x, y = input()
date += sum(day[:x-1])
date = (date + y) % 7
print(week[date])