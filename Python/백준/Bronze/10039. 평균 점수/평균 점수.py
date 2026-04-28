import sys
input = lambda: int(sys.stdin.readline())

score = 0
for _ in range(5):
    inp = input()
    score += inp if inp > 40 else 40

print(score//5)