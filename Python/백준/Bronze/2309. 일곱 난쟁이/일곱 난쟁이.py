import sys
input = sys.stdin.readline

dwarf = []

for _ in range(9):
    dwarf.append(int(input()))

for i in range(9):
    for j in range(i+1, 9):
        if sum(dwarf) - dwarf[i] - dwarf[j] == 100:
            tmp1, tmp2 = dwarf[i], dwarf[j]

dwarf.remove(tmp1)
dwarf.remove(tmp2)
dwarf.sort()
print(*dwarf, sep='\n')