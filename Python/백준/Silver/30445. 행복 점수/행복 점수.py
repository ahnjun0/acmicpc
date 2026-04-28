import sys
from collections import defaultdict
input = lambda: list(sys.stdin.readline().rstrip())

def round(n):
    scaled_n = n * 10000
    rounded_scaled_n = int(scaled_n) + 1 if (scaled_n - int(scaled_n)) >= 0.5 else int(scaled_n)
    return rounded_scaled_n / 100

a = defaultdict(int)

for i in input():
    if i in "HAPYSD":
        a[i] += 1

happy = (a["H"]+a["A"]+a["P"]+a["Y"])
sad = (a["S"]+a["A"]+a["D"])

if happy == sad == 0:
    print("50.00")
    sys.exit(0)

print(f"{round(happy / (happy + sad)):.2f}")