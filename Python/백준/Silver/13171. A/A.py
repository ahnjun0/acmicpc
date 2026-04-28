import sys
input = lambda: int(sys.stdin.readline())


def power(A, B):
	if B == 1:
		if A >= 1000000007: A %= 1000000007
		return A


	power_val = (power(A, B//2))
	if power_val >= 1000000007: power_val %= 1000000007

	if B & 1 == 0:
		return power_val ** 2 % 1000000007
	else:
		return ((power_val ** 2) * A) % 1000000007


A = input()
X = input()
print(power(A, X))