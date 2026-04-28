import sys
input = lambda: map(int, sys.stdin.readline().split())
idx = 1
while True:
    L, P, V = input()
    if (L, P, V) == (0, 0, 0): break
    print(f"Case {idx}: {(V//P) * L + min(V%P, L)}")
    idx += 1