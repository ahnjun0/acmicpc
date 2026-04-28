import re

def is_slump(string):
    return re.fullmatch(r'((D|E)F+)+G', string) is not None

def is_slimp(string):
    if string == 'AH':
        return True
    elif string.startswith('AB') and string.endswith('C'):
        return is_slimp(string[2:-1])
    elif string.startswith('A') and string.endswith('C'):
        return is_slump(string[1:-1])
    return False

def is_slurpy(string):
    for i in range(2, len(string)):
        if is_slimp(string[:i]) and is_slump(string[i:]):
            return True
    return False

print("SLURPYS OUTPUT")
for _ in range(int(input())):
    inp = input()
    print("YES" if is_slurpy(inp) else "NO")
print('END OF OUTPUT')