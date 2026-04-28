import sys
input = lambda: sys.stdin.readline().split()

n, name = input()
n = int(n)

unique_chars = []
seen = set()
discarded_count = 0

for char in name:
    if char not in seen:
        unique_chars.append(char)
        seen.add(char)
    else:
        discarded_count += 1

result = ''.join(unique_chars) + str(discarded_count + 4)
result = str(n + 1906) + result
result = result[::-1]
result = "smupc_" + result

print(result)