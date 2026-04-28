import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
card = []

for _ in range(R):
    inp = input()
    card.append(inp + inp[::-1])

card += card[::-1]
A, B = map(int, input().split())

tmp = [*card[A-1]]
tmp[B-1] = "." if tmp[B-1] == "#" else "#"
card[A-1] = "".join(tmp)

print("\n".join(card))